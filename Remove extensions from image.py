import csv

# Path to the CSV file
file_path = "C:\\Users\\kerem\\PokemonDatabase\\Code\\Edit Datasheet Exel\\ValData.csv"

# Temporary list to store the modified rows
modified_rows = []

with open(file_path, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) > 1:  # Check if the row has at least 2 columns
            path = row[1]  # Assuming the path is in the second column (Column B)
            parts = path.split('/')
            if len(parts) > 1:
                parts[1] = "Validation"
                row[1] = '/'.join(parts)
        modified_rows.append(row)

# Write the modified rows back to the CSV file
with open(file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(modified_rows)

print("CSV file updated successfully.")
