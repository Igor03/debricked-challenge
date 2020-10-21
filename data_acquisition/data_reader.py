import os
import json


def read_json_file(filepath:str, filename:str) -> list:
    json_file = open(os.path.join(filepath, filename))
    data = json.load(json_file)
    return data


