#!/usr/bin/env python3

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):

    """Loads JSON data from a file and
    deserializes it into a Python dictionary."""

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == '__main__':
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')

# Output: The data has been serialized and saved to 'data.json'
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')

# Output: The deserialized data
print("Deserialized Data:")
print(deserialized_data)
