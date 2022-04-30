from bs4 import BeautifulSoup
import requests
import time
import json


def get_omdbapi_info(title):
    OMDBAPI_KEY = "2d84c686"
    base_url = "http://www.omdbapi.com"
    params = {
        "t": title,
        "apikey": OMDBAPI_KEY
    }
    response = requests.get(base_url, params)
    results = response.json()
    return results


def load_cache(cache_json):
    try:
        cache_file = open(cache_json, 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache


def save_cache(cache_dict, cache_json):
    cache_file = open(cache_json, 'w')
    contents_to_write = json.dumps(cache_dict)
    cache_file.write(contents_to_write)
    cache_file.close()


def request_cache(movie_title, cache_dict):
    if (movie_title in cache_dict.keys()):  # the movie_title is our unique key
        print("Using cache")
        return cache_dict[movie_title]
    else:
        print("Fetching")
        time.sleep(1)
        movie_info = get_omdbapi_info(movie_title)
        cache_dict[movie_title] = movie_info
        save_cache(cache_dict, cache_json)
        return cache_dict[movie_title]


# url = 'https://www.imdb.com/feature/genre/?ref_=nv_ch_gr'
cache_json = 'cacheIMDB_TOP750.json'
cache_dict = {}
cache_dict = load_cache(cache_json)


BASE_URL = 'https://www.imdb.com'
GENRE_PATH = '/feature/genre/?ref_=nv_ch_gr'
# Make the soup for the genres page
popular_genres_url = BASE_URL + GENRE_PATH
response = requests.get(popular_genres_url)
soup = BeautifulSoup(response.text, 'html.parser')

# For each genres listed
genres_listing_parent = soup.find('div', id='main')
genres_listing_divs = genres_listing_parent.find_all(
    'div', class_='image')
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(genres_listing_divs)

# extract the genre details URL
for div in genres_listing_divs:
    genre_details_url = div.find('a')['href']
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print(genre_url)

    # Make the soup for genre details
    response = requests.get(genre_details_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # extract top50 title
    top50_list = soup.find('div', class_='lister-list')
    top50_item_divs = top50_list.find_all('div', class_='lister-item')

    for top50_item in top50_item_divs:
        movie_header = top50_item.find('h3', class_='lister-item-header').text
        movie_title = movie_header.split('\n')[2]
        request_cache(movie_title, cache_dict)

# print('length', len(cache_dict))
