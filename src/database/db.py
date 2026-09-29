from src.database.config import supabase
import bcrypt

def _hash_password(psw):
    return bcrypt.hashpw(psw.encode(), bcrypt.gensalt()).decode()

def _check_password(hashed, password):
    return bcrypt.checkpw(password.encode(), hashed_password=hashed.encode())

def check_teacher_exists(username):
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0

def create_teacher(name, username, password):
    data = {
        "username":username,
        "password": _hash_password(password),
        "name":name
    }
    response = supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data[0]
        if _check_password(teacher["password"], password):
            return teacher
    return None
