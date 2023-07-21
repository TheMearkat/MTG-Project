import requests
from IPython.display import display, Image
import json
import random
import csv

def read_csv_file(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def percentage_to_float(percentage_str):
    return float(percentage_str.rstrip('%'))

res = requests.get("https://api.scryfall.com/sets/ltr")
set_info = res.json()
search_info = set_info.get("search_uri")

something = requests.get(search_info)
data = json.loads(something.text)

# Randomly select an entry from the data
random_entry = random.choice(data['data'])

# Extract the name and image_uris for the randomly selected card
name = random_entry['name']
image_uris = random_entry['image_uris']
small_image_url = image_uris.get('small', '')

file_path = '/home/bb8c88b1-5886-4a0a-9b24-aefddc53f90c/MTG Project/card_info.csv'
csv_data = read_csv_file(file_path)

# Find the matching row in the CSV data based on the card's name
matching_row = None
for row in csv_data:
    if row.get('\ufeffName') and row['\ufeffName'].lower() == name.lower():
        matching_row = row
        break

if matching_row:
    # Extract the card information from the matching row
    gihwr = percentage_to_float(matching_row['GIH WR'])
    alsa = matching_row['ALSA']
    # Add more fields as needed

    # Print the results
    print(f"Random Card Name: {name}")
    print(f"Game in Hand Win Rate: {gihwr}")
    print(f"Average Last Seen At: {alsa}")
    
    if int(gihwr) > 55:
        print("This is a good card")
    else:
        print("This is a bad card")
    # Print more fields as needed
else:
    print("No matching card found in the CSV data.")

# Print the results
print(f"Random Card Name: {name}")
print(f"Random Small Image URL: {small_image_url}")

display(Image(url=small_image_url))
