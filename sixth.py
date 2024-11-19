import sys
import requests
from bs4 import BeautifulSoup

def download_url_and_get_all_hrefs(url):
    hrefs = []

    try: 
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            for a_tag in soup.find_all('a', href=True):
                hrefs.append(a_tag['href'])
        else:
            print(f"Chyba: Neplatná odpověď (Status code: {response.status_code})")

    except requests.RequestException as e:
        print(f"Chyba při stahování URL: {e}")

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]

        hrefs = download_url_and_get_all_hrefs(url)

        if hrefs: 
            for href in hrefs:
                print(href)
        else:
            print("Nebyly nalezeny žádné odkazy.")

    except IndexError:
        print("Chyba: Nebyla zadána žádná URL.")
    except Exception as e:
        print(f"Program skončil chybou: {e}")

        
