# test_dict = {"a": 43, "b": 1233, "c": 8}

max_key = max(test_dict, key=test_dict.get)
min_key = min(test_dict, key=test_dict.get)
print(f"min: {min_key}")
print(f"max: {max_key}")
