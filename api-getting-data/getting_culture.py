import os
import requests
import json

def fetch_swapi_data(character_name):
    url = f'https://swapi.dev/api/people/?search={character_name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]  # Return first match
        else:
            print("Character not found in SWAPI.")
            return None
    else:
        print(f"Error fetching data from SWAPI: {response.status_code}")
        return None

def fetch_europeana_data(query):
    api_key = os.getenv("EUROPEANA_API_KEY")
    url = f'https://api.europeana.eu/record/v2/search.json?wskey={api_key}&query={query}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['items']:
            return data['items'][0]  # Return first match
        else:
            print("No related cultural data found.")
            return None
    else:
        print(f"Error fetching data from Europeana: {response.status_code}")
        return None

def main():
    character_name = input("Enter the name of a Star Wars character: ")
    swapi_data = fetch_swapi_data(character_name)
    
    if swapi_data:
        print("SWAPI Data:")
        print(json.dumps(swapi_data, indent=2))  # Pretty print SWAPI data
        
        # Use character's name to fetch related data from Europeana
        europeana_data = fetch_europeana_data(character_name)
        if europeana_data:
            print("Europeana Data:")
            print(json.dumps(europeana_data, indent=2))  # Pretty print Europeana data

        # Save combined data to a JSON file
        combined_data = {
            "swapi_data": swapi_data,
            "europeana_data": europeana_data
        }
        with open(f"{character_name}_data.json", "w") as outfile:
            json.dump(combined_data, outfile, indent=2)
            print(f"Data saved to {character_name}_data.json")

if __name__ == "__main__":
    main()
