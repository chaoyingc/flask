import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import nltk
from nltk.tokenize import word_tokenize
from nltk import corpus
from nltk.corpus import stopwords
import re
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
from sklearn.externals import joblib
from sklearn.linear_model import SGDClassifier

df = pd.read_csv('tweet_data.csv')
def _processTweet(tweet):
    tweet = tweet.str.lower() # convert text to lower-case
    tweet = tweet.apply(lambda elem: re.sub(r"\srt\s|&.*;|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", elem))# regex for removing unuseful elements
    tweet = tweet.apply(lambda x: word_tokenize(x))#split sentences into words
    return tweet
tweets=_processTweet(df['tweet'])
stop_words = set(stopwords.words('english'))#get a set of words to delete
tweets=tweets.apply(lambda x: [item for item in x if item not in stop_words])#iterate in tweets to delete the words in the set stopwords
tweets=tweets.apply(lambda x: ' '.join(x))# remove the bracket and comma
y=df['class']
X=tweets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
# pipeline transform esmators to one final esmator pipeline_clf_svm
pipeline_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf',  TfidfTransformer()),
    ('sgd', SGDClassifier()),
])
pipeline_clf.fit(X_train,y_train)
predictions = pipeline_clf.predict(X_test)
# save the model to a file "tweets.plk" for the classification
#clf = joblib.dump(model,"classifier.pkl")
#from sklearn import externals
#model_filename = 'tweet.joblib.z'
#externals.joblib.dump(pipeline_clf_svm, model_filename)
from sklearn.externals import joblib
joblib.dump(pipeline_clf, 'classifier.pkl')
