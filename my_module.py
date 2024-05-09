from nltk.stem import SnowballStemmer
import string
import pickle
import pandas as pd
import numpy as np

# Loading pickle files
book_index = list(pickle.load(open('similarity_columns.pkl','rb')))
similarity_scores= dict(pickle.load(open('similarity_score.pkl','rb')))
dict_needed= dict(pickle.load(open('dict_required.pkl','rb')))
# Making dataframes
dict_needed= pd.DataFrame(dict_needed)
similarity_df = pd.DataFrame(similarity_scores,columns=book_index)

# This function displays basic details of the dataset
def knowYourData(df):
  ''' Enter a dataframe '''
  print('Shape: ', df.shape)
  print('Duplicates count: ', df.duplicated().sum())
  print('Columns:')
  print(list(df.columns))
# This function removes punctuations and integers from a given sentence.
def remove_punctuations(text):
    ''' Enter texts '''
    punc= list(string.punctuation)
    result = ''
    for i in text:
        if i not in punc:
            result += i
    return result.lower()
# This function removes integers
def removeIntegers(text):
    result= []
    text= text.split()
    for t in text:
        if t.isnumeric() == False:
            result.append(t)
    return ' '.join(result)
# This function is used for stemming
def stemming(text):
    ''' Enter texts '''
    result = []
    ss= SnowballStemmer(language='english')
    for t in text.split():
        result.append(ss.stem(t))
    return ' '.join(result)
# Recommend function
def recommend(book_title):
    recommended_titles = similarity_df[book_title].sort_values(ascending=False).reset_index()
    recommended_titles = recommended_titles.rename(columns={book_title:'similarity_score'}).head(6)
    full_data = dict_needed[dict_needed['Book-Title'].isin(recommended_titles['Book-Title'])]
    full_data = full_data.merge(recommended_titles, on='Book-Title')
    recommendations = full_data.sort_values(by='similarity_score', ascending=False).iloc[1:6]
    return recommendations