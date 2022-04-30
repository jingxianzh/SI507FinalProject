import json
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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


imdb = cache_dict

df = pd.DataFrame(imdb.values())

df['Country'].fillna('Others', inplace=True)
df_country = df.drop(df[df['Country'] == 'Others'].index)
df_country['Country'] = df_country['Country'].str.split(', ')
df_country = df_country.explode('Country', ignore_index=True)
country_list = df_country['Country'].value_counts(
).rename_axis('Country').reset_index(name='counts')
country_list.plot.bar(x="Country", y="counts", figsize=(25, 8))


df['imdbRating'].fillna('Others', inplace=True)
df_imdbRating = df.drop(df[df['imdbRating'] == 'N/A'].index)
df_imdbRating2 = df_imdbRating.drop(df[df['imdbRating'] == 'Others'].index)
df_imdbRating2['imdbRating'].value_counts()
df_imdbRating2['imdbRating'] = pd.to_numeric(df_imdbRating2['imdbRating'])
bins = pd.IntervalIndex.from_tuples(
    [(0, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)])
df_imdbRating2['imdbRating'] = pd.cut(df_imdbRating2['imdbRating'], bins).astype(str).str.replace(
    '(', '', regex=True).str.replace(']', '', regex=True).str.replace(',', ' -', regex=True)
df_imdbRating2['imdbRating']
df_imdbRating2.groupby('imdbRating').size().plot(kind='pie', ylabel='')


df['imdbVotes'].fillna('Others', inplace=True)
df_rel_Votes_Rating = df.drop(df[df['imdbVotes'] == 'N/A'].index)
df_rel_Votes_Rating = df_rel_Votes_Rating.drop(
    (df[df['imdbVotes'] == 'Others'].index))
df_rel_Votes_Rating['imdbVotes'] = df_rel_Votes_Rating['imdbVotes'].str.replace(
    ',', '').astype(int)
df['imdbRating'].fillna('Others', inplace=True)
df_rel_Votes_Rating = df_rel_Votes_Rating.drop(
    df_rel_Votes_Rating[df_rel_Votes_Rating['imdbRating'] == 'N/A'].index)
df_rel_Votes_Rating = df_rel_Votes_Rating.drop(
    (df_rel_Votes_Rating[df_rel_Votes_Rating['imdbRating'] == 'Others'].index))
df_rel_Votes_Rating['imdbRating'] = df_rel_Votes_Rating['imdbRating'].astype(
    float)


sns.pairplot(data=df_rel_Votes_Rating, vars=['imdbVotes', 'imdbRating'])
sns.relplot(data=df_rel_Votes_Rating, x="Year", y="imdbRating")
plt.show()


Genre_list = ["comedy", "sci-fi", "horror", "romance", "action", "thriller", "drama",
              "mystery", "crime", "animation", "adventure", "fantasy", "romance", "action", "superhero"]
Country_list = ["united states", "italy", "united kingdom", "france",
                "japan", "germany", "spain", "russia", "india", "china", "others"]


while True:
    print("Welcome come to this mini-movie recommendation center!")
    choice = input(
        f"\nWould you like to explore 4 pictures or ask for movie recommendations (please enter 'picture' or 'movie'?")
    if choice.lower() == 'picture':
        png = input(
            f"\nWe have one(country bar chart), two(rating pie chart), three(pair chart for imdbVotes and imdbRating), four(relationship chart between year and imdbRating). \n\n[Please enter 'one', 'two', 'three', or 'four']")
        if png == 'one':
            country_list.plot.bar(x="Country", y="counts", figsize=(25, 8))
        if png == 'two':
            df_imdbRating2.groupby('imdbRating').size().plot(
                kind='pie', ylabel='')
        if png == 'three':
            sns.pairplot(data=df_rel_Votes_Rating, vars=[
                         'imdbVotes', 'imdbRating'])
        if png == 'four':
            sns.relplot(data=df_rel_Votes_Rating, x="Year", y="imdbRating")
        plt.show()

    if choice.lower() == 'movie':

        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(
                'Please enter your filter options from genre, country and rating range.')
            while True:
                genre_option = input(f"\nPlease enter your preferred genre: ")
                if genre_option.lower() not in Genre_list:
                    print(f"\nWe ONLY have 'comedy, sci-fi, horror, romance, action, thriller, drama, mystery, crime, animation, adventure, fantasy, romance, action, superhero' options!")
                    continue
                else:
                    break

            while True:
                country_option = input(f"\nPlease enter a movie's country: ")
                if country_option.lower() not in Country_list:
                    print(
                        f"\nWe ONLY have 'United States, Italy, United Kingdom, France, Japan, Germany, Spain, Russia, India, China, Others' options!")
                    continue
                else:
                    break

            while True:
                rating_option = input(
                    f"\nPlease enter your lowest rating request (an integer or float between 0 and 10)!")
                try:
                    rating_option = float(rating_option)
                    if float(rating_option) > 10 or float(rating_option) < 0:
                        print(f"\nPlease enter an integer or float between 0 and 10!")
                    else:
                        break
                except:
                    continue

                    # rating_option = float(rating_option)
                    # if float(rating_option) > 10 or float(rating_option) < 0:
                    #     print(f"\nPlease enter an integer or float between 0 and 10!")
                    # else:
                    #     break
        # {"Title": "Everything Everywhere All at Once", "Year": "2022", "Rated": "R",
        #  "Released": "25 Mar 2022", "Runtime": "139 min", "Genre": "Action, Adventure, Comedy", "Director": "Dan Kwan, Daniel Scheinert",
        #   "Writer": "Dan Kwan, Daniel Scheinert", "Actors": "Michelle Yeoh, Stephanie Hsu, Ke Huy Quan",
        #    "Plot": "An aging Chinese immigrant is swept up in an insane adventure, where she alone can save the world by exploring other
        #    universes connecting with the lives she could have led.", "Language": "English, Mandarin, Cantonese", "Country": "United States",
        #    "Awards": "1 win", "Poster": "https://m.media-amazon.com/images/M/MV5BYTdiOTIyZTQtNmQ1OS00NjZlLWIyMTgtYzk5Y2M3ZDVmMDk1XkEyXkFqcGdeQXVyMTAzMDg4NzU0._V1_SX300.jpg",
        #     "Ratings": [{"Source": "Internet Movie Database", "Value": "9.0/10"}, {"Source": "Rotten Tomatoes", "Value": "97%"}, {"Source": "Metacritic", "Value": "82/100"}],
        #     "Metascore": "82", "imdbRating": "9.0", "imdbVotes": "9,209", "imdbID": "tt6710474", "Type": "movie", "DVD": "N/A", "BoxOffice": "$8,428,962", "Production": "N/A",
        #     "Website": "N/A", "Response": "True"}

            movie_list = []
            for value in cache_dict.values():
                # print(value)
                if 'Genre' not in value:
                    continue
                genre = value['Genre']
                # print(genre)
                if 'Country' not in value:
                    continue
                country = value['Country']
                # print(country)
                if 'imdbRating' not in value:
                    continue
                if value['imdbRating'] == 'N/A':
                    rating = 0
                else:
                    rating = value['imdbRating']
                # print(rating)

                if country_option.lower() == country.lower() and genre_option.lower() in genre.lower() and float(rating) >= float(rating_option):
                    movie_list.append(value)

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            if movie_list == []:
                print(
                    f"\nSorry, we don't have any recommendation based on your option, please try another!")
            else:
                print(f"\nWe got these recommended movies for you!")
                for movie in movie_list:
                    print(movie['Title'])
            break
