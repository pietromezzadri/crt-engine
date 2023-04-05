import json


def json_to_dict(json_file):
    file_content = open(json_file, 'r', encoding='utf-8')
    json_data = json.loads(file_content.read())
    return json_data
