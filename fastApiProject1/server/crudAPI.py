#crudAPI.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import List, Optional
from connectorBDD import MongoAccess

app = FastAPI()
mongo_access = MongoAccess()


class Species(BaseModel):
    Scientific_name: str
    Common_name: str
    Species_ID: str
    Start_Year: int
    Latitude: float
    Longitude: float
    Basis_of_record: str
    Order: str
    Family: str
    Genus: str
    Country: str
    State: str


class SpeciesCreateParams(Species):
    Scientific_name: str
    Common_name: str
    Species_ID: str
    Start_Year: int
    Latitude: float
    Longitude: float
    Basis_of_record: str
    Order: str
    Family: str
    Genus: str
    Country: str
    State: str


class SpeciesUpdateParams(Species):
    Scientific_name: Optional[str]
    Common_name: Optional[str]
    Species_ID: Optional[str]
    Start_Year: Optional[int]
    Latitude: Optional[float]
    Longitude: Optional[float]
    Basis_of_record: Optional[str]
    Order: Optional[str]
    Family: Optional[str]
    Genus: Optional[str]
    Country: Optional[str]
    State: Optional[str]


    class Config:
        json_encoders = {ObjectId: lambda x: str(x)}
        arbitrary_types_allowed = True

def serialize_objectid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(repr(obj) + " is not JSON serializable")

def get_paginated_species(skip: int = 0, limit: int = 10):
    species = mongo_access.get_mammals(skip, limit)
    return species 

@app.get("/")
async def root():
    return {"message": "Welcome to the mammals API service"}

@app.post("/species/", response_model=Species)
async def create_species(params: SpeciesCreateParams):

    species_data = {
        "Scientific_name": params.Scientific_name,
        "Common_name": params.Common_name,
        "Species_ID": params.Species_ID,
        "Start_Year": params.Start_Year,
        "Latitude": params.Latitude,
        "Longitude": params.Longitude,
        "Basis_of_record": params.Basis_of_record,
        "Order": params.Order,
        "Family": params.Family,
        "Genus": params.Genus,
        "Country": params.Country,
        "State": params.State
    }
    created_species = mongo_access.set_mammal(**species_data)
    return created_species

@app.get("/all_species/")
async def read_all_species():
    species = get_paginated_species(0, 221386)
    # Sérialiser l'ObjectId en utilisant la fonction personnalisée
    species_serialized = json.loads(json.dumps(species, default=serialize_objectid))
    return JSONResponse(content=species_serialized)

@app.get("/species/{species_id}", response_model=Species)
async def read_species(species_id: str):
    species = mongo_access.get_mammal(species_id)
    if species is None:
        raise HTTPException(status_code=404, detail="Species not found")
    return species

@app.get("/species/", response_model=List[Species])
async def read_species_list(skip: int = 0, limit: int = 10):
    species_list = mongo_access.get_mammals(skip, limit)
    return species_list

@app.put("/species/{species_id}", response_model=Species)
async def update_species(species_id: str, params: SpeciesUpdateParams):
    species_data = params.dict()
    updated_species = await mongo_access.update_mammal(species_id, **species_data)
    return updated_species

@app.delete("/species/{species_id}", response_model=dict)
async def delete_species(species_id: str):
    mongo_access.del_mammal(species_id)
    return {"message": "Species deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)