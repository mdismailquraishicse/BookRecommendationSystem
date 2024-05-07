# Libraries
from flask import Flask, render_template
import pickle
import pandas as pd

app= Flask(__name__) # flask object creation

# Loading pickle files
book_index = list(pickle.load(open('similarity_columns.pkl','rb')))
similarity_scores= dict(pickle.load(open('similarity_score.pkl','rb')))
dict_needed= dict(pickle.load(open('dict_required.pkl','rb')))
# Making dataframes
dict_needed= pd.DataFrame(dict_needed)
similarity_df = pd.DataFrame(similarity_scores,columns=book_index)
# Recommend function
def recommend(book_title):
    recommended_titles = similarity_df[book_title].sort_values(ascending=False).reset_index()
    recommended_titles = recommended_titles.rename(columns={book_title:'similarity_score'}).head(6)
    full_data = dict_needed[dict_needed['Book-Title'].isin(recommended_titles['Book-Title'])]
    full_data = full_data.merge(recommended_titles, on='Book-Title')
    recommendations = full_data.sort_values(by='similarity_score', ascending=False).iloc[1:6]
    return recommendations
# Function for index page
@app.route("/")
def index():
    return render_template('index.html')

# Function for recommendation page rendering
@app.route('/recommendation')
def recommendation():
    results = recommend("The Dead Zone")
    return render_template('recommend.html',
                           titles= results['Book-Title'],
                           image= results['Image-URL-M'],
                           publisher = results['Publisher'],
                           yop = results['Year-Of-Publication'],
                           author = results['Book-Author']
                           )


if __name__ == '__main__':
    app.run(debug=True)