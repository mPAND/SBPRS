# Sentiment Based Product Recommendation System

EBuss e-commerce company has huge market share in many fields, and it sells the products in various categories such as household essentials, books, personal care products, medicines, cosmetic items, beauty products, electrical appliances, kitchen and dining products and health care product

Company wants to expand its market and become a major leader by competing with market leaders like Amazon, Flipkart. Hence Ebuss wants to implemenent Machine learning concepts to build a sentiment based product recommentation system to offer service to customers.

As part of CAPSTONE project, following tasks are implemented in this repo

1. Data sourcing and sentiment analysis
2. Building a recommendation system
3. Improving the recommendations using the sentiment analysis model
4. Deploying the end-to-end project with a user interface

This project is deployed on https://sbprs-product-reco-manuel.herokuapp.com/


## High level Steps
1. Exploratory data analysis
2. Data cleaning
3. Feature extraction
4. Building a Recommendation System
    
    Build below recommendation system and choose the best one 
    1. User-based recommendation system
    2. Item-based recommendation system

5. Build a text classification model

    Build a sentiment Classification model using on of below

    1. Logistic Regression
    2. Decision Tree ( with Hyper Parameter Tuning)
    3. Random Forest ( with Hyper Parameter Tuning)

6. Improve the recommendation system output using classifier model
    1. Pick Top 20 Recommended products for a user
    2. Calculate Postive Sentiment Review for each product
    3. Pick Top 5 products which has highest positive review

* Recommendation and Classification models are precalculated in advance since input data is static,
* Identifing top 5 products are calculated in advance so that deployed app is fast and consumes less memory.

## Flask UI
Deployed Flask UI offers following functionality
1) Accepts username as input
2) Recommends 5 products for entered username
3) If username is unknown, proper message is displayed to user
4) If entered user has no common products with other users, model does not have any  recommended products for user ( eg. repster1988 ) . Appropriate message is shown to user