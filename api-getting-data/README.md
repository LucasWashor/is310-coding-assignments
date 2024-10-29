# API Data Fetcher

## Description
This project utilizes the **Star Wars API (SWAPI)** and the **Europeana API** to fetch and combine data about a specified Star Wars character and a related cultural artifact. 

- **SWAPI**: A RESTful API that provides a wealth of information about the Star Wars universe, including characters, films, starships, vehicles, and planets.
- **Europeana API**: A digital platform that provides access to millions of digitized items from European museums, galleries, and archives, showcasing art, culture, and history.

## Purpose
The purpose of this project is to demonstrate how to integrate data from two different APIs. By combining character data from SWAPI with related artwork or objects from Europeana, we aim to enrich our understanding of cultural artifacts associated with popular media.

## Script Functionality
The script performs the following tasks:

1. **Input Required**: 
   - The script requires the name of a Star Wars character as input (e.g., "Luke Skywalker").

2. **Data Fetching**:
   - The script sends a request to SWAPI to retrieve data related to the specified character.
   - It then sends a request to the Europeana API to fetch data related to an object that connects to the character.

3. **Output Format**:
   - The fetched data is compiled into a single JSON file, structured as follows:

```json
{
  "swapi_data": {
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    ...
  },
  "europeana_data": {
    "completeness": 0,
    "country": ["Germany"],
    ...
  }
}

