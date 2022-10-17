from datetime import datetime

from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional


class Property(Document):
    name: str = Field(...)
    address: str = Field(...)
    lat: float = Field(...)
    long: float = Field(...)
    type: str = Field(...)
    bedrooms: int = Field(...)
    bathrooms: int = Field(...)
    sizeSqFt: int
    sizeSqM: int
    tenure: str = Field(...)
    description: str = Field(...)
    price: int = Field(...)
    priceDescriptor: str = Field(...)
    photos: list
    epc: str
    dateAmended: datetime = datetime.now()



    class Settings:
        name = "property"

    class Config:
        schema_extra = {
            "example": {
                "name": "Savannah Heights",
                "address": "Old Leigh Road, Leigh-on-sea, SS9",
                "lat": 51.54351610190346,
                "long": 0.6741379268571732,
                "type": "Flat",
                "bedrooms": 1,
                "bathrooms":1,
                "sizeSqFt":560,
                "sizeSqM":52,
                "tenure":"Leasehold",
                "description":"Retire in style, this over 60's apartment is located in a sought after development just off Leigh-on-Sea Broadway. Located near Chalkwell park which is ideal for spending time with the family through the summer. The property itself benefits from a 24 hour careline, a house manager, a well maintained communal garden and communal facilities. With a community feel and a modern interior this property will make you feel right at home as soon as you put your bags down.",
                "price": 150000,
                "priceDescriptor": "Offers Over",
                "photos": ["url_for_photo_1", "url_for_photo_2", "url_for_photo_3"],
                "epc":"url_for_epc_image",
                "dateAmended": datetime.now()
            }
        }

class UpdateProperty(BaseModel):
    name: Optional[str]
    address: Optional[str]
    lat: Optional[float]
    long: Optional[float]
    type: Optional[str]
    bedrooms: Optional[int]
    bathrooms: Optional[int]
    sizeSqFt: Optional[int]
    sizeSqM: Optional[int]
    tenure: Optional[str]
    description: Optional[str]
    price: Optional[int]
    priceDescriptor: Optional[str]
    photos: Optional[list]
    epc: Optional[str]
    dateAmended: Optional[datetime]


    class Config:
        schema_extra = {
            "example": {
                "name": "Savannah Heights",
                "address": "Old Leigh Road, Leigh-on-sea, SS9",
                "lat": 51.54351610190346,
                "long": 0.6741379268571732,
                "type": "Flat",
                "bedrooms": 1,
                "bathrooms":1,
                "sizeSqFt":560,
                "sizeSqM":52,
                "tenure":"Leasehold",
                "description":"Retire in style, this over 60's apartment is located in a sought after development just off Leigh-on-Sea Broadway. Located near Chalkwell park which is ideal for spending time with the family through the summer. The property itself benefits from a 24 hour careline, a house manager, a well maintained communal garden and communal facilities. With a community feel and a modern interior this property will make you feel right at home as soon as you put your bags down.",
                "price": 150000,
                "priceDescriptor": "Offers Over",
                "photos": ["url_for_photo_1", "url_for_photo_2", "url_for_photo_3"],
                "epc":"url_for_epc_image",
                "dateAmended": datetime.now()
            }

        }