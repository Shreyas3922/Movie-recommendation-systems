# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Library imports
from fastapi import FastAPI
from pydantic import BaseModel
#import uvicorn
#import pickle
from spy_copy import get_movie_recommendation
# Create the app object
app = FastAPI()

class MovieName(BaseModel):
    title: str

# route index
@app.get('/')
def index():
    return{'message':'Hello, World'}

# get the movie recommendations based on the movie name passed

@app.post('/predict')
async def predict_movie(data:MovieName):
    data = data.dict()
    title=data['title']
    results = get_movie_recommendation(title)
    if type(results) == str:
        ll = results
    else:
        ll = list(results['Title'])
    print(ll) 
    return {'movie': results}

#if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1', port=8000)
   

# Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
#    uvicorn server:app --reload    #on cmd
#if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1', port=8000)