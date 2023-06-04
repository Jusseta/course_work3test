from datetime import datetime


def get_operations(sorted_data):
    operations = []
    for i in sorted_data[:5]:
        date = datetime.fromisoformat(i['date']).strftime('%d.%m.%Y')
        description = i['description']
        if 'from' in i:
            from_whom = i['from']
        else:
            from_whom = ''
        to_whom = i['to']
        amount = i['operationAmount']['amount']
        name = i['operationAmount']['currency']['name']

        one_operation = {'date':date, 'description':description, 'from_whom':from_whom,
                         'to_whom':to_whom, 'amount':amount, 'name':name}
        operations.append(one_operation)

    return operations


def encode_numbers(operations):
    encode_operations = operations
    for i in encode_operations:
        from_whom_count = len(i['from_whom'].split(" ")[-1]) - 10
        from_whom_temp = i['from_whom'].split(" ")[-1][:6] + "*" * from_whom_count + i['from_whom'][-4:]
        i['from_whom'] = i['from_whom'].split(" ")[0] + ' ' + from_whom_temp

        to_whom_temp = "*" * 2 + i['to_whom'].split(" ")[1][-4:]
        i['to_whom'] = i['to_whom'].split(" ")[0] + ' ' + to_whom_temp

    return encode_operations
