from constants import MAX_ADMINS, ADMIN_NAME_FORMAT

def is_admin_existing(admins, admin_id, admin_email):
    """
    Check if an admin with the given ID or email already exists.
    """
    return any(admin.id == admin_id or admin.email == admin_email for admin in admins)

def format_admin_name(name):
    """
    Format the admin's name based on the ADMIN_NAME_FORMAT constant.
    """
    if ADMIN_NAME_FORMAT == "capitalize":
        return " ".join(word.capitalize() for word in name.split())
    elif ADMIN_NAME_FORMAT == "uppercase":
        return name.upper()
    return name  # Default to no formatting

def can_add_more_admins(current_count):
    """
    Check if more admins can be added based on MAX_ADMINS.
    """
    return current_count < MAX_ADMINS
