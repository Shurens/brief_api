#connexion_API.py
from pymongo import MongoClient
from bson import ObjectId

class MongoAccess:
    __USER = "root"
    __PW = "example"
    __DB_NAME = "webapi"

    def __init__(self):
        self.client = MongoClient(f"mongodb://{self.__USER}:{self.__PW}@mongo:27017")
        self.db = self.client[self.__DB_NAME]

    def get_all_mammals(self):
        mammals = self.db.mammals.find({})
        return list(mammals)

    def get_mammals(self, skip: int = 0, limit: int = 10):
        mammals = self.db.mammals.find({}).skip(skip).limit(limit)
        return list(mammals)

    def get_mammal(self, id):
        id = ObjectId(id)
        mammal = self.db.mammals.find_one({"_id": id})
        return mammal

    def del_mammal(self, id):
        id = ObjectId(id)
        self.db.mammals.delete_one({'_id': id})

    def validate_species_data(self, species_data):
        required_fields = [
            "Scientific_name",
            "Common_name",
            "Species_ID",
            "Start_date",
            "Latitude",
            "Longitude",
            "Basis_of_record",
            "Country",
            "State/Province"
        ]
        for field in required_fields:
            if field not in species_data or not species_data[field]:
                raise ValueError(f"Field '{field}' is required and cannot be empty.")

    def set_mammal(self, **species_data):
        self.validate_species_data(species_data)
        result = self.db.mammals.insert_one(species_data)
        inserted_id = result.inserted_id
        return self.get_mammal(str(inserted_id))

    def update_mammal(self, id, Scientific_name, Common_name, Species_ID, Start_date, Latitude, Longitude, Basis_of_record, Order, Family, Genus, Country, State_Province):
        id = ObjectId(id)
        mammal = {
            "Scientific_name": Scientific_name,
            "Common_name": Common_name,
            "Species_ID": Species_ID,
            "Start_date": Start_date,
            "Latitude": Latitude,
            "Longitude": Longitude,
            "Basis_of_record": Basis_of_record,
            "Order": Order,
            "Family": Family,
            "Genus": Genus,
            "Country": Country,
            "State/Province": State_Province
        }
        self.db.mammals.update_one({"_id": id}, {'$set': mammal})
