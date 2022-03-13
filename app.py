from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import pandas as pd
import pickle
#import nltk
import model
import os


#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
# nltk.download('all')

app = Flask(__name__)


@app.route('/')
def index():
    # fetching all username list
    allUsername = model.full_user_final_rating.index.tolist()
    return render_template('index.html', usernameList = allUsername)


@app.route('/recommend', methods = ['POST'])
def recommend():
    username = str(request.form.get('username'))
    
    print('username :', username)
    if not username:
        return redirect(url_for('index'))

    productNameList, posSentimentRateList = model.getRecommendations(username)

    if  posSentimentRateList == None or type(productNameList) == 'str':
        allUsername = model.full_user_final_rating.index
        return render_template('index.html', usernameList = allUsername, error = productNameList)

    productList = zip(productNameList, posSentimentRateList)

    return render_template('recommendations.html', username = username, productList = productList)


if __name__ == '__main__':
    print('===============Flask App Started=============')
    print('Sentiment Based Product Recommendation System')
    app.run(debug = True)