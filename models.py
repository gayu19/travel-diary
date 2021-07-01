import harperdb
import os

db = harperdb.HarperDB(
    url=os.environ["DB_URL"],
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"])

schema = "travel_diary"
    
class DiaryModel:
    table = "diary"
    def create(self, place_list):
        return db.insert(schema, self.table, place_list)  
        
    def get(self, search_attribute, search_value):
        return db.search_by_value(schema, self.table, search_attribute, search_value, get_attributes=['name','description','type','expenditure','location'])

    def get_all(self):
        return db.sql(f"select expenditure, description, location, name, type from {schema}.{self.table}")