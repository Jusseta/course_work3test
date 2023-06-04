from data import get_data
from data import sort_data
from utils import get_operations
from utils import encode_numbers


data = sort_data(get_data())
encode_operations = encode_numbers(get_operations(data))


def print_operation(encode_operation):
    for i in encode_operation:
        print(f"{i['date']} {i['description']}\n"
              f"{i['from_whom']} --> {i['to_whom']}\n"
              f"{i['amount']} {i['name']}\n")


print_operation(encode_operations)
