import csv
import json

# Path to the CSV file and the output JSONL file
csv_file_path = "C:\\Users\\kerem\\PokemonDatabase\\Fnals\\TestData.csv"
jsonl_file_path = "C:\\Users\\kerem\\PokemonDatabase\\Fnals\\test.jsonl"

# Open the CSV file and read its contents
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)

    # Open the JSONL file for writing
    with open(jsonl_file_path, 'w', newline='', encoding='utf-8') as jsonl_file:
        for row in reader:
            # Skip empty rows
            if len(row) < 2:
                continue

            # Create a dictionary for the current row and write it as a JSON object
            json_object = {"text": row[0], "image": row[1]}
            jsonl_file.write(json.dumps(json_object) + '\n')

print("JSONL file created successfully.")
