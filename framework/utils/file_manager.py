import json


class FileManager:
    def __new__(cls, file):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FileManager, cls).__new__(cls)
        return cls.instance

    def __init__(self, file):
        file = open(file)
        self.data = json.load(file)

    def get_data(self, key):
        return self.data[key]
