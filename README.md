## Movie Recommendation 
This project deals with recommending movies based on the ratings ---Item based movie recommendation <br> 
Movie recommendation can be done in multiple ways, some are: <br>
1. Content Based Movie recommendation - Recommednaing movies based on the features(Genre, Male/Female lead, director etc) of the movie / Similar movies(based on its features) are recommended.
2. Collaborative Movie recommendation - Collaborative filtering is a recommendation strategy that considers the user’s behavior and compares it with other users in the database. It uses the history of all users to influence the recommendation algorithm. Unlike content-based filtering, collaborative filtering relies on the interactions of multiple users with items to generate suggestions.
3. Item based Movie Recommendation - Item-based Collaborative Filtering focuses on finding similar movies instead of similar users to recommend to user ‘A’ based on their past preferences. It identifies pairs of movies rated/liked by the same users, measures their similarity across all users who rated both, and then suggests similar movies based on the similarity scores.
<br>
__Dataset__  
This dataset (ml-25m) describes 5-star rating and free-text tagging activity from [MovieLens](http://movielens.org), a movie recommendation service. It contains 25000095 ratings and 1093360 tag applications across 62423 movies. These data were created by 162541 users between January 09, 1995 and November 21, 2019. This dataset was generated on November 21, 2019. <br>
Users were selected at random for inclusion. All selected users had rated at least 20 movies. No demographic information is included. Each user is represented by an id, and no other information is provided.
The data are contained in the files `genome-scores.csv`, `genome-tags.csv`, `links.csv`, `movies.csv`, `ratings.csv` and `tags.csv`. More details about the contents and use of all these files follows.
This and other GroupLens data sets are publicly available for download [here](http://grouplens.org/datasets/). <br>
We shall use movies and ratings csv files for our project. <br>
__RatingCsv__ : All ratings are contained in the file `ratings.csv`. Each line of this file after the header row represents one rating of one movie by one user, and has the following format:

    userId,movieId,rating,timestamp

The lines within this file are ordered first by userId, then, within user, by movieId.Ratings are made on a 5-star scale, with half-star increments (0.5 stars - 5.0 stars).Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970. <br>
__MoviesCsv__ : Movie information is contained in the file `movies.csv`. Each line of this file after the header row represents one movie, and has the following format:

    movieId,title,genres
__Model__ : Firstly cosine similarity is used to get similar movies based on ratings. Then NearestNeighbors ML model is used to get similar movies. <br>
FastAPI web framework is used to build an API for NearestNeighbors model which can be further deployed in a cloud platform.
