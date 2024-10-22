from bs4 import BeautifulSoup
import requests
import pandas as pd

# Fetch the webpage
response = requests.get("https://minecraft.fandom.com/wiki/Enchanting")
soup = BeautifulSoup(response.text, "html.parser")

# Find all tables
tables = soup.find_all('table')

# Initialize a variable to hold the enchantment table
enchantment_table = None

# Look for the table that contains the summary of enchantments
for table in tables:
    if 'Summary of enchantments' in table.get('data-description', ''):
        enchantment_table = table
        break

# Lists to store enchantment data
names = []
summaries = []
treasures = []
incompatible_with = []
max_levels = []
primary_items = []
secondary_items = []
weights = []

# Check if the enchantment table is found
if enchantment_table:
    # Iterate through each row in the table
    for row in enchantment_table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        if len(columns) >= 8:  # Ensure there are enough columns
            # Extract enchantment data
            name = columns[0].text.strip()  # First column for Name
            summary = columns[1].text.strip()
            treasure = columns[2].text.strip()
            incompatible_item = columns[3].text.strip()
            max_level = columns[4].text.strip()
            primary_item = columns[5].text.strip()
            secondary_item = columns[6].text.strip()
            weight = columns[7].text.strip()

            # Append the data to lists
            names.append(name)
            summaries.append(summary)
            treasures.append(treasure)
            incompatible_with.append(incompatible_item)
            max_levels.append(max_level)
            primary_items.append(primary_item)
            secondary_items.append(secondary_item)
            weights.append(weight)

    # Check if any data was collected
    if names:
        # Create a DataFrame to organize the data
        df = pd.DataFrame({
            'Name': names,
            'Summary': summaries,
            'Treasure': treasures,
            'Incompatible With': incompatible_with,
            'Max Level': max_levels,
            'Primary Items': primary_items,
            'Secondary Items': secondary_items,
            'Weight': weights
        })

        # Remove duplicates if any
        df.drop_duplicates(inplace=True)

        # Save to CSV file
        df.to_csv("minecraft_enchantments.csv", index=False)
        print("Data scraping complete. Check 'minecraft_enchantments.csv' for results.")
    else:
        print("No enchantment data found. Please check the table structure on the wiki page.")
else:
    print("Enchantment table not found. Please verify the HTML structure.")
