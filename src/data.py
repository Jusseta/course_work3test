import json


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    return data[-1:-5:-1]
