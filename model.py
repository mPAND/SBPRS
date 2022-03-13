import pandas as pd
import numpy as np
import pickle
import os
import gzip

dirname = os.path.dirname(__file__)

final_user_df_path = os.path.join(dirname, 'notebooks', 'final_user_df.pkl')
final_user_df =  pickle.load(file = open(final_user_df_path, 'rb'))

full_user_final_rating_path = os.path.join(dirname, 'models', 'full_user_final_rating.data')


# read the file
fp = gzip.open(full_user_final_rating_path,'rb') #This assumes that full_user_final_rating.data is already packed with gzip
full_user_final_rating = pickle.load(fp)
fp.close()

#full_user_final_rating= pickle.load(file = open(full_user_final_rating_path, 'rb'))

def getRecommendations(ip_username):

    _df=final_user_df[final_user_df.username==ip_username][["product_name","pct_positive_review"]]
    list_productName=_df['product_name'].tolist()
    list_productPosReviewRate=_df['pct_positive_review'].round(2).tolist()

    if (ip_username not in full_user_final_rating.index):
        errorMessage= f' Unknown User "{ip_username}" . Kindly Check user name !!'
        return errorMessage,None
    elif (len(_df)==0):
        errorMessage= f' No Positive Recommended Products for User "{ip_username}" . Kindly try for another User !!'
        return errorMessage,None
    else:
        return list_productName,list_productPosReviewRate