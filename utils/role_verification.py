from fastapi import HTTPException


def role_verification(user, function):
    allowed_functions_for_users = ["get_own"]

    if user.role == "admin":
        return True

    elif user.role == "user" and function in allowed_functions_for_users:
        return True

    else:
        raise HTTPException(status_code=401, detail='Sizga ruhsat berilmagan!')

