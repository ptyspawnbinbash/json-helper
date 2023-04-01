#!/usr/bin/env python3

import json
import sys

def rename_keys(data, mappings):
    if isinstance(data, list):
        for item in data:
            rename_keys(item, mappings)
    elif isinstance(data, dict):
        for k, v in list(data.items()):
            if k in mappings:
                data[mappings[k]] = data.pop(k)
            rename_keys(v, mappings)

def update_values(json_obj, key, new_value):
    if isinstance(json_obj, dict):
        for k, v in json_obj.items():
            if k == key:
                json_obj[k] = new_value
            else:
                update_values(v, key, new_value)
    elif isinstance(json_obj, list):
        for item in json_obj:
            update_values(item, key, new_value)

def main():
    if len(sys.argv) < 4:
        print("Usage: ./json-helper.py <action> <input_file> <key>:<new_value>")
        print("Usage: python3 json-helper.py <action> <input_file> <key>:<new_value>")
        sys.exit(1)

    action = sys.argv[1]
    input_file = sys.argv[2]
    key, new_value = sys.argv[3].split(":")

    with open(input_file, 'r') as f:
        json_obj = json.load(f)

    if action == "update-key":
        rename_keys(json_obj, {key: new_value})
    elif action == "update-value":
        update_values(json_obj, key, new_value)
    else:
        print("Invalid action. Use 'update-key' or 'update-value'")
        sys.exit(1)

    with open(input_file, 'w') as f:
        json.dump(json_obj, f, indent=2)

if __name__ == "__main__":
    main()
