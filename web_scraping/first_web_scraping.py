# import requests
# from bs4 import BeautifulSoup

# # URL to scrape from Project Gutenberg
# url = 'https://www.gutenberg.org/browse/scores/top'

# # Fetch the webpage
# response = requests.get(url)

# # Ensure the request was successful
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Prettify the parsed HTML (optional, for debugging)
#     print(soup.prettify())

#     # Find and print all the links (anchor tags)
#     links = soup.find_all('a')
#     for link in links:
#         print(link.get('href'))  # Prints the href (URL)
#         print(link.get_text())   # Prints the text (the link text)
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

from bs4 import BeautifulSoup

# Load the HTML file
with open("top_100_ebooks.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Find the 'Top 100 EBooks yesterday' section
h2_tag = soup.find('h2', string="Top 100 EBooks yesterday")

# Find the next 'ol' tag after the h2 tag
ol_tag = h2_tag.find_next('ol')

# Get all 'li' tags inside the 'ol' tag
titles = ol_tag.find_all('li')

# Print each title
for title in titles:
    print(title.get_text())

