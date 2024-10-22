import requests
from bs4 import BeautifulSoup
import csv

# URL of the Marvel Cinematic Universe Wiki movies page
url = 'https://marvelcinematicuniverse.fandom.com/wiki/Marvel_Cinematic_Universe'

# Send a GET request to the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Create a list to hold the movie data
movies_data = []

# Find all movie entries
movies = soup.find_all('div', class_='movie')  # Adjust this based on the actual HTML structure

for movie in movies:
    title = movie.find('h2', class_='title').get_text(strip=True)
    release_date = movie.find('p', class_='release-date').get_text(strip=True)
    box_office = movie.find('p', class_='box-office').get_text(strip=True)
    genre = movie.find('p', class_='genre').get_text(strip=True)
    director = movie.find('p', class_='director').get_text(strip=True)
    cast = movie.find('p', class_='cast').get_text(strip=True)
    summary = movie.find('p', class_='summary').get_text(strip=True)

    # Append data to the list
    movies_data.append({
        'Title': title,
        'Release Date': release_date,
        'Box Office': box_office,
        'Genre': genre,
        'Director': director,
        'Cast': cast,
        'Summary': summary
    })

# Save data to CSV
with open('mcu_movies.csv', 'w', newline='') as csvfile:
    fieldnames = ['Title', 'Release Date', 'Box Office', 'Genre', 'Director', 'Cast', 'Summary']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for movie in movies_data:
        writer.writerow(movie)


print("Data scraping complete. Check 'mcu_movies.csv' for results.")
