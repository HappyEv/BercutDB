import json


class FileManager:
    @staticmethod
    def get_data(key, filename):
        """Returns value from given JSON file with given key.
        """
        file = open(filename)
        json_data = json.load(file)
        return json_data[key]