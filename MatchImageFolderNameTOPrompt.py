import pandas as pd
import os

# Paths
excel_path = "C:\\Users\\kerem\\PokemonDatabase\\Code\\Clean Images and make cvs\\Test.xlsx"
image_dir = "C:\\Users\\kerem\\PokemonDatabase\\Code\\Clean Images and make cvs\\Test"

# Read the Excel file from 'Sheet1', starting from Row 3, Columns B and C
df = pd.read_excel(excel_path, sheet_name='Sheet', usecols="B:C", header=1, skiprows=1)

# Dictionary to hold the prompt and corresponding image paths
prompt_image_mapping = {}

# Iterate through each row in the DataFrame
for _, row in df.iterrows():
    folder_name, prompt = row.iloc[0], row.iloc[1]  # Use .iloc for positional indexing
    folder_path = os.path.join(image_dir, folder_name)

    # Check if the folder exists
    if os.path.isdir(folder_path):
        image_files = ["Test/" + f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        prompt_image_mapping[prompt] = image_files
    else:
        print(f"Folder not found: {folder_name}")

# Convert the dictionary into a list of tuples (prompt, image_path)
data = []
for prompt, image_paths in prompt_image_mapping.items():
    for path in image_paths:
        data.append((prompt, path))

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['prompt', 'image_path'])

# Save the DataFrame to a CSV file
csv_path = "C:\\Users\\kerem\\PokemonDatabase\\Code\\Clean Images and make cvs\\TestData.csv"
df.to_csv(csv_path, index=False)

print("CSV file created successfully.")
