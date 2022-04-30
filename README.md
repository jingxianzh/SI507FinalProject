# Instructions

This program is a mini-movie recommendation project.  
There are two major functions. One is four pictures of the graph based on the database.  
The other is to provide movie recommendations based on users' preferences.  
Download the code and run the user_command_final.py file.  
Follow the routes and hints to make your choices and explore the graphs created.

# Required Packages

bs4, requests, numpy, seaborn, pandas

# Data Structure

I built a binary search tree based on the imdbRating from the cacheIMDB_TOP750.json. The rating scale is float number from 0 to 10. It is a tuple containing the movie's imdbRating and the movie titles. They are used as the last filter option for users to find recommended movies. The root is the first movie from the json.file, then based on the class created from bst_python.py and the format function to create a tuple which contains leftChild and rightChild if applicable.
