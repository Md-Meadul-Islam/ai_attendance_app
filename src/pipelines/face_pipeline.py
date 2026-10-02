import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st
from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(face_recognition_models.pose_predictor_model_location())

    facerec = dlib.face_recognition_model_v1(face_recognition_models.face_recognition_model_location())#face recognition_model_location()

    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()

    # Detect faces in the image
    faces = detector(image_np, 1)

    encodings = []

    for face in faces:
        # Get the landmarks/parts for the face in box d.
        shape = sp(image_np, face)

        # Compute the 128D vector that describes the face in img identified by shape
        face_descriptor = facerec.compute_face_descriptor(image_np, shape)

        encodings.append(np.array(face_descriptor))

    return encodings

def get_trained_model():
    X = []
    y = []

    students = get_all_students()

    for student in students:
        if student['face_embedding'] is not None:
            X.append(np.array(student['face_embedding']))
            y.append(student['student_id'])
    if len(X) == 0:
        return 0

    clf  = SVC(kernel='linear', probability=True, class_weight='balanced')
    try:
        clf.fit(X, y)
    except Exception as e:
        st.error(f"Error training the model: {e}")
        pass
    return {"clf": clf, "X": X, "y": y}

def train_classifier():
    st.cache_resource.clear()
    model = get_trained_model()
    return bool(model)

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)
    detected_students = {}
    model_data = get_trained_model()
    if not model_data:
        return detected_students, [], len(encodings)

    clf = model_data["clf"]
    X_train = model_data["X"]
    y_train = model_data["y"]

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        if len(all_students) >= 2:
            predicted_id = int(clf.predict([encoding])[0])
        else:
            predicted_id = int(all_students[0])  # If only one student, assign that ID

        student_embedding = X_train[y_train.index(predicted_id)]
        distance = np.linalg.norm(encoding - student_embedding)
        resamblance_threshold = 0.6  # Adjust this threshold based on your requirements
        if distance <= resamblance_threshold:
            detected_students[predicted_id] = True
    return detected_students, all_students, len(encodings)