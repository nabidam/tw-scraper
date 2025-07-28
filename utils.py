import json

def save_dict_to_json(data, json_path):
    with open(json_path, "w") as f:
        f.write(json.dumps(data, indent=4))