# Libraries
from flask import Flask, render_template, request, url_for
import pickle
import pandas as pd
import my_module

app= Flask(__name__) # flask object creation

dict_needed= dict(pickle.load(open('dict_required.pkl','rb')))
dict_needed= pd.DataFrame(dict_needed)

# Function for index page
@app.route("/")
def index():
    return render_template('index.html',
                           titles=dict_needed['Book-Title'])

# Function for recommendation page rendering
@app.route('/recommendation',methods=['post'])
def recommendation():
    user_input= request.form.get('user_input')
    results= my_module.recommend(user_input)
    return render_template('recommend.html',
                           titles= results['Book-Title'].values,
                           image= results['Image-URL-M'].values,
                           publisher = results['Publisher'].values,
                           yop = results['Year-Of-Publication'].values,
                           author = results['Book-Author'].values
                           )


if __name__ == '__main__':
    app.run(debug=True)