import requests
# method used in Jupyter notebook to display images 
from IPython.display import display, Image
import json
import random
import csv

#read csv file
def read_csv_file(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
        
#convert string percentages into float for comparison
def percentage_to_float(percentage_str):
    return float(percentage_str.rstrip('%'))

#make request to scryfall api
res = requests.get("https://api.scryfall.com/sets/ltr")
set_info = res.json()
search_info = set_info.get("search_uri")

search_result = requests.get(search_info)
data = json.loads(search_result.text)

# Randomly select an entry from the data
random_entry = random.choice(data['data'])

# Extract the name and image_uris for the randomly selected card
name = random_entry['name']
image_uris = random_entry['image_uris']
small_image_url = image_uris.get('small', '')

#use whatever your file path is 
file_path = 'YOUR-FILE-PATH'
csv_data = read_csv_file(file_path)

# Find the matching row in the CSV data based on the card's name. I used '\ufeffName' because, for whatever reason, thats what the source csv had.
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

#Method to display image in jupyter notebook
display(Image(url=small_image_url))
