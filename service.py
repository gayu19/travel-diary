from models import DiaryModel


class DiaryService:
    def __init__(self):
        self.model = DiaryModel()

    def create(self, params):
        return self.model.create(params)

    def get_all(self):
        response = self.model.get_all()
        return response
    
    def get(self, search_attribute, search_value):
        response = self.model.get(search_attribute, search_value)
        return response

    