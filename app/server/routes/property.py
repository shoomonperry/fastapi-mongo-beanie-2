from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from app.server.models.property import Property, UpdateProperty


router = APIRouter()

@router.post("/", response_description="Property added to the database")
async def add_property(property: Property) -> dict:
    await property.create()
    return {"message": "Property added successfully"}

@router.get("/{id}", response_description="Property record retrieved")
async def get_property_record(id: PydanticObjectId) -> Property:
    property = await Property.get(id)
    return property


@router.get("/", response_description="Property records retrieved")
async def get_properties() -> List[Property]:
    properties = await Property.find_all().to_list()
    return properties

@router.put("/{id}", response_description="Property record updated")
async def update_property_data(id: PydanticObjectId, req: UpdateProperty) -> Property:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    review = await Property.get(id)
    if not review:
        raise HTTPException(
            status_code=404,
            detail="Property record not found!"
        )

    await property.update(update_query)
    return property


@router.delete("/{id}", response_description="Property record deleted from the database")
async def delete_property_data(id: PydanticObjectId) -> dict:
    record = await Property.get(id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Property record not found!"
        )

    await record.delete()
    return {
        "message": "Record deleted successfully"
    }
