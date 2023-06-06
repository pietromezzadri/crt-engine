import json


def json_to_dict(json_file):
    with open(json_file, 'r', encoding='utf-8') as file_content:
        json_data = json.loads(file_content.read())
        return json_data
