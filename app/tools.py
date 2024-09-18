import json
import os



def read_json_file(filepath: str):
    print(f'READ JSON FILE: {filepath}')
    with open(filepath, 'r') as file:
        content = json.load(file)
    return content