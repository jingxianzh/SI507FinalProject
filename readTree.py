import json

from bst_python import BinarySearchTree


def load_cache(CACHE_FILE_NAME):
    try:
        cache_file = open(CACHE_FILE_NAME, 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache


cache_json = 'cacheIMDB_TOP750.json'
cache_dict = load_cache(cache_json)

bst = BinarySearchTree()

for movie in cache_dict.values():
    if 'imdbRating' in movie:
        rating = movie['imdbRating']
        if rating != 'N/A':
            bst.put(key=rating, val=movie['Title'])

bst.saveTree("imdbRating.json")
