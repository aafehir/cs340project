from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:54338' % ("aacuser", "1234"))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self,criteria):
        if criteria is not None:
            # {'_id':False} omits the unique ID of each row
            data = self.database.animals.find(criteria,{"_id":False})

        else:
            #if there is no search criteria then all the rows will be returned
            data = self.database.animals.find( {} , {"_id":False})
        return data
# Create method to implement the U in CRUD.
    def update(self, query, update):
        if query is not None:
            result = self.database.animals.update(query, update)
            return result
        else:
            raise Exception("Nothing to update, because query parameter is empty")
# Create method to implement the D in CRUD.
    def delete(self, criteria):
        if criteria is not None:
             result = self.database.animals.delete_many(criteria)
             return result
        else:
            raise Exception("Nothing to delete, decause criteria parameter is empty")