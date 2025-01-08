from fastapi import APIRouter, HTTPException, Body
from typing import List
from models.admin import Admin
from helpers.admin_common import is_admin_existing, format_admin_name, can_add_more_admins

router = APIRouter()

# Mock database
admins = []

@router.get("/admins", response_model=List[Admin])
def get_admins():
    """
    Fetch a list of all admins.
    """
    if not admins:
        raise HTTPException(status_code=404, detail="No admins found")
    return admins

@router.post("/admins", response_model=Admin)
def add_admin(admin: Admin = Body(...)):
    """
    Add a new admin to the system.
    """
    # Check if max admins limit is reached
    if not can_add_more_admins(len(admins)):
        raise HTTPException(status_code=400, detail="Maximum number of admins reached")

    # Check if admin ID or email already exists
    if is_admin_existing(admins, admin.id, admin.email):
        raise HTTPException(status_code=400, detail="Admin with this ID or email already exists")

    # Format admin name
    admin.name = format_admin_name(admin.name)

    admins.append(admin)
    return admin
