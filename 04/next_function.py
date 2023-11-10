list_of_dicts = [{'x': 1}, {'x': 3}, {'x': 5}, {'y': 5}]

result_dict = next((item for item in list_of_dicts if item.get('x', None) == 5), {})
print(result_dict)
