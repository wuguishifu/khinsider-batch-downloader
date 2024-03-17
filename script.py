import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

url_header = 'https://downloads.khinsider.com'


def fetch_and_parse_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        return soup

    except requests.exceptions.RequestException as e:
        print("Error fetching/parsing HTML:", e)
        return None


def download_mp3(url, directory):
    filename = urllib.parse.unquote(url.split('/')[-1].replace('%2520', ' '))
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(directory, filename), 'wb') as f:
            f.write(response.content)
        print('downloaded', filename)
    else:
        print('failed to download', filename)


directory = input("Enter the directory to save the files: ")
url = input("Enter the URL of the soundtrack: ")

parsed = fetch_and_parse_html(url)

table = parsed.find(name='table', attrs={"id": "songlist"})
rows = table.find_all(name='tr')
for row in rows:
    td = row.find(name='td', attrs={"class": "clickable-row"})
    if not td:
        continue
    a = td.find(name='a')
    if not a:
        continue
    href = a['href']
    download_page = fetch_and_parse_html(url_header + href)
    audio = download_page.find(name='audio', attrs={"id": "audio"})
    if not audio:
        continue
    download_mp3(audio['src'], directory)
