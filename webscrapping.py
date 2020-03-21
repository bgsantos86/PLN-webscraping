from bs4 import BeautifulSoup
import urllib.request

def get_links_from(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/'
    page = urllib.request.urlopen(url)
    links = []

    page = urllib.request.urlopen(url)
    if page.getcode() == 200:
        soup = BeautifulSoup(page, 'html.parser')

        for a in soup.find_all('a', attrs={'class': 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE'}):
            links.append((a.text, 'https://www.reddit.com' + a.get('href')))
        return links


for link_name, link_url in get_links_from('programming'):
    print(f'{link_name} - {link_url}')