import json


class FileManager:
    __instance = None

    def __init__(self, file):
        if FileManager.__instance is not None:
            raise Exception("More than one instance in Singleton")
        else:
            file = open(file)
            self.data = json.load(file)

    def get_data(self, key):
        return self.data[key]

    def clear(self):
        FileManager.__instance = None