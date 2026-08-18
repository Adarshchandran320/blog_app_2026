def validate_user_id(user_id):
    user_id = user_id.strip()

    if not user_id:
        return False, "User ID cannot be blank"
    if " " in user_id:
        return False, "User ID cannot contain spaces"
    return True, ""


def validate_required(value, field_name):
    if not value or not value.strip():
        return False, f"{field_name} cannot be blank"
    return True, ""