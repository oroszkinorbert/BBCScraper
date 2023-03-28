import requests
from bs4 import BeautifulSoup
import pandas as pd

urls=[]
query='nuclear'
# List of URLs to scrape
for i in range(1):
    urls.append(f"https://www.bbc.co.uk/search?q=nuclear&d=news_gnl&page={i}")

# Create empty lists to store the titles, texts, and dates of articles containing the word "nuclear"
nuclear_titles = []
nuclear_texts = []
nuclear_dates = []


# Loop through all the URLs in the list
for url in urls:
    # Send an HTTP GET request to the URL and get the HTML response
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')


    # Find all the articles on the page
    articles = soup.find_all("div", class_="ssrcss-53phst-Promo ett16tt0")
    articles2 = soup.find_all("a", class_="ssrcss-rl2iw9-PromoLink e1f5wbog1")
    links = [l.get("href") for l in articles2]
    print(links)

    # Loop through all the articles and check if they contain the word "nuclear"
    for article in articles:
            # If the article contains the word "nuclear", extract its title, text, and date
        title = article.find("p")
        nuclear_titles.append(title.text)
        

    for link in links:
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        arttext = soup.find_all("p", string=True)
        date = article.find("datetime=""")
        nuclear_dates.append(date)
        Con = "".join([p.text for p in arttext])
        nuclear_texts.append(Con)


# Create a pandas dataframe from the lists of titles, texts, and dates
df = pd.DataFrame({'Title': nuclear_titles, 'Text': nuclear_texts, 'Date': nuclear_dates})

# Print the dataframe
print(df)
#df.to_excel(f'C:/Users/Norbi/Desktop/Konyvek/ProjectLab/{query}bbcnews3.xlsx',"Munka1")
