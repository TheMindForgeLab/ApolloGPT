from __future__ import annotations

from fastapi import APIRouter, HTTPException

from apollo.businesses.business_manager import BusinessManager

router = APIRouter(prefix="/api/businesses", tags=["businesses"])
manager = BusinessManager()


@router.get("")
def list_businesses():
    return {"items": manager.list_businesses()}


@router.post("")
def create_business(payload: dict):
    if not payload.get("name"):
        raise HTTPException(status_code=400, detail="Business name is required.")
    return manager.create_business(payload)


@router.get("/{business_id}")
def get_business(business_id: str):
    dashboard = manager.get_business_dashboard(business_id)
    if not dashboard:
        raise HTTPException(status_code=404, detail="Business not found.")
    return dashboard
