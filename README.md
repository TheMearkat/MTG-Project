# MTG Card Randomizer

This project is a Python script that retrieves random Magic: The Gathering cards using the Scryfall API and matches them with data from a CSV file. The CSV file contains card information such as game statistics and win rates.

## Requirements

- Python 3.x
- Requests library (Install using `pip install requests`)
- IPython library (Install using `pip install ipython`)

## Installation

1. Clone this repository to your local machine.
2. Install the required Python libraries by running:
   pip install -r requirements.txt
   

## Usage

1. Run the `mtg_card_randomizer.py` script using the following command:
  python mtg_card_randomizer.py


2. The script will retrieve random Magic: The Gathering cards from the Scryfall API and match them with the data from the CSV file (`card_info.csv`).

3. The script will display the card's name, image URL, and other information such as "Game in Hand Win Rate" and "Average Last Seen At." It will also determine if the card is considered good or bad based on the "Game in Hand Win Rate."

4. The script will display the image of the randomly selected card.

## CSV Data Format

The CSV file (`card_info.csv`) should have the following columns:

- Name
- Color
- Rarity
- Seen
- ALSA
- Picked
- ATA
- GP
- GP WR
- OH
- OH WR
- GD
- GD WR
- GIH
- GIH WR
- # GNS
- GNS WR
- IWD

Please ensure that the column names match exactly as listed above. The script will read and match the card data based on the "Name" column.
All information was sourced from the 17lands.com public data sets. You can read more about what each field means here https://www.17lands.com/metrics_definitions

## Atribution

The data used in this project includes statistics from 17lands, which falls under the Creative Commons Attribution 4.0 International License. The CSV data (`card_info.csv`) is derived from 17lands data, and appropriate attribution goes to 17lands.

## Note

- This project is intended for educational and personal use and is not affiliated with Wizards of the Coast or Scryfall.
- The Scryfall API provides random cards, and the data from the CSV file is for illustration purposes only.

