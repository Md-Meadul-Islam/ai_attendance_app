import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav
import io
import librosa
import streamlit as st

@st.cache_resource
def load_voice_encoder():
    encoder = VoiceEncoder()
    return encoder

def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()
        audio_data, sr = librosa.load(io.BytesIO(audio_bytes), sr=None)
        print("audio_data", audio_data)
        print("sr", sr)
        wav = preprocess_wav(audio_data, sr)
        print("wav", wav)
        embedding = encoder.embed_utterance(wav)
        print("embedding", embedding)
        return embedding.tolist()

    except Exception as e:
        st.error(f"Error loading voice encoder: {e}")
        return None

def identify_speaker(new_embedding, candidates_dict, threshold=0.65):
    """
    Identify the speaker based on the new embedding and a dictionary of candidate embeddings.

    Args:
        new_embedding (list): The embedding of the new audio input.
        candidates_dict (dict): A dictionary where keys are candidate IDs and values are their embeddings.
        threshold (float): The similarity threshold for identification.

    Returns:
        tuple: A tuple containing the ID of the identified speaker and the similarity score, or (None, 0.0) if no match is found.
    """

    if new_embedding is None or not candidates_dict:
        return None, 0.0

    best_sid = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dict.items():
        # Calculate cosine similarity
        score = np.dot(new_embedding, stored_embedding) / (np.linalg.norm(new_embedding) * np.linalg.norm(stored_embedding))

        if score > best_score:
            best_score = score
            best_sid = sid
    if best_score >= threshold:
        return best_sid, best_score
    return None, best_score

def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.65):
    """

    """
    try:
        encoder = load_voice_encoder() #
        audio_data, sr = librosa.load(io.BytesIO(audio_bytes), sr=None) #
        wav = preprocess_wav(audio_data, sr) #
        segments = librosa.effects.split(wav, top_db=20) #

        identified_results = []

        for start, end in segments:
            if end-start<sr*0.5:
                continue
            segment_audio = wav[start:end]
            wav = preprocess_wav(segment_audio)
            embedding = encoder.embed_utterance(wav)

            sid, score = identify_speaker(embedding, candidates_dict, threshold)
            identified_results.append((sid, score))

            if sid:
                if sid not in identified_results or score > identified_results[sid]:
                    identified_results[sid] = score
        return identified_results

    except Exception as e:
        st.error(f"Error processing bulk audio: {e}")
        return None, 0.0