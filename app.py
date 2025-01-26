import streamlit as st
import pickle
import numpy as np

movie_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movie_list['title'].values
st.title('Movie Recommender System')
movie_name = st.selectbox('Write Movie Name',movie_list)

def recommend(movie_name):
    # movie_index = movie_list[movie_list['title'] == movie_name].index[0]
    movie_index = np.where(movie_list == movie_name)[0][0]
    
    distances = similarity[movie_index]
    # movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x : x[1])[1:6]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    for i in movies_list:
        movie_id = i[0]

        # name = movie_name.iloc[i[0]].title
        recommend_movies.append(movie_list[i[0]])
        # recommend_movies.append(name)
    return recommend_movies
  
if st.button('Recommend'):
    res = recommend(movie_name)
    for i in res:
        st.write(i)