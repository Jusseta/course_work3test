import json


def get_data():
    with open('operations.json', encoding='utf-8') as file:
        all_data = json.loads(file.read())
        return all_data


def sort_data(data):
    full_data = []
    for i in data:
        if 'state' in i:
            if i['state'] == "EXECUTED":
                full_data.append(i)
    return sorted(full_data, key=lambda k: k['date'].split('.'), reverse=True)
