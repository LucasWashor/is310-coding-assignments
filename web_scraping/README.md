# Minecraft Enchantment Scraper

For this assignment, I chose to scrape the Minecraft fandom page to gather information about various enchantments in the game. The specific page I am scraping is [Minecraft Enchanting](https://minecraft.fandom.com/wiki/Enchanting).

## Why Minecraft Enchantments?

I have always loved playing minecraft with my brothers as a kid and I thought it would be an awesome page to scrape! To kind of explain what enchantments are if you aren't familiar: Enchantments play a crucial role in enhancing the gameplay experience by providing players with various advantages, such as improved weapon damage, better armor protection, and special abilities. By collecting data on enchantments, researchers and players can gain insights into how different enchantments can be strategically used in gameplay.

## Data to be Scraped

The data extracted includes:
- Enchantment Name
- Effect
- Applicable Items
- Max Level
- Enchantment Type

## Robots.txt File

I checked the robots.txt file for the Minecraft fandom to ensure compliance with their scraping policies. You can view the file [here](https://minecraft.fandom.com/robots.txt). The relevant pages for this project are allowed for scraping.

## Requirements

To run the `fandom_wiki_scraping.py` file, you will need:
- Python installed on your system.
- The following libraries: `requests`, `beautifulsoup4`, and `csv`.

## Usage

1. Clone the repository or download the files.
2. Run the script using:
   ```bash
   python fandom_wiki_scraping.py
