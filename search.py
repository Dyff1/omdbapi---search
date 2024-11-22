import requests
import json
import os

while True:

    api = "your_api_key"
    title = input("Movie you want to search: ")
    response = requests.get(f"https://www.omdbapi.com/?t={title}&apikey={api}")
    response.raise_for_status()

    json_data = json.loads(response.text)

    print(json_data)

    file_path = 'data.json'

# New data to add
    new_data = (json_data)

# Check if the file exists and has data
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    # Open the file in read mode and load its content
        with open(file_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    else:
    # If the file doesn't exist or is empty, start with an empty list or dict
        existing_data = []

# Ensure the file contains a list; if not, make it a list
    if not isinstance(existing_data, list):
        existing_data = [existing_data]

# Append the new data
    existing_data.append(new_data)

# Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)
