# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 23:14:59 2023

@author: Shreyas
"""
# from Items_based_recommendation.ipynb notebook
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


movies_df = pd.read_csv("movies.csv")
movies_df.drop("genres", axis=1, inplace = True)
ratings_df = pd.read_csv("ratings.csv")
ratings_df.drop("timestamp", axis=1, inplace = True)

ratings_dff = ratings_df.sample(100000, random_state = 10).reset_index(drop = True)
final_dataset = ratings_dff.pivot_table(index='movieId',columns='userId',values='rating')
final_dataset.fillna(0,inplace=True)
final_dataset.reset_index(inplace=True)

no_user_voted = ratings_dff.groupby('movieId')['rating'].agg('count')
print(final_dataset.head())

csr_data = csr_matrix(final_dataset.values)
knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
knn.fit(csr_data)

def get_movie_recommendation(movie_name):
    n_movies_to_reccomend = 10
    movie_list = movies_df[movies_df['title'] == movie_name]  
    if len(movie_list):        
        movie_idx = movie_list.iloc[0]['movieId']
        movie_idx = final_dataset[final_dataset['movieId'] == movie_idx].index[0]
        distances , indices = knn.kneighbors(csr_data[movie_idx],n_neighbors=n_movies_to_reccomend+1)    
        rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
        recommend_frame = []
        for val in rec_movie_indices:
            movie_idx = final_dataset.iloc[val[0]]['movieId']
            idx = movies_df[movies_df['movieId'] == movie_idx].index
            recommend_frame.append({'Title':movies_df.iloc[idx]['title'].values[0],'Distance':val[1]})
        df = pd.DataFrame(recommend_frame,index=range(1,n_movies_to_reccomend+1))
        return df
    else:
        return "No movies found. Please check your input"
    
    
get_movie_recommendation('Jumanji (1995)')  



