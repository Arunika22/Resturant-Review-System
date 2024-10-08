import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Zomato Review Kaggle.tsv',delimiter ='\t',quoting = 3)
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
  zomato_ratings = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
  zomato_ratings = zomato_ratings.lower()
  zomato_ratings = zomato_ratings.split()
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  zomato_ratings = [ps.stem(word) for word in zomato_ratings if not word in set(all_stopwords)]
  zomato_ratings = ' '.join(zomato_ratings)
  corpus.append(zomato_ratings)
  import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
corpus =[]
from nltk.stem.porter import PorterStemmer
for i in range(0,1000) :
  zomato_ratings = re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
  zomato_ratings = zomato_ratings.lower()
  zomato_ratings = zomato_ratings.split()
  ps =PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  zomato_ratings =[ps.stem(word) for word in zomato_ratings if not word in set(all_stopwords)]
  zomato_ratings =' '.join(zomato_ratings)
  corpus.append(zomato_ratings)
  print(corpus)
  from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 21)
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

st.title("FoodMood")
st.image("FoodImage.jpg")
st.title("Enter your review")

text = st.text_area("Enter a text here")
if st.button("Predict Sentiment") and text:
    # Use the previously trained CountVectorizer to transform the input text
    y = cv.transform([text]).toarray()
    
    # Reshape the input data
    y_reshaped = y.reshape(1, -1)

    # Make the prediction
    y_pred = classifier.predict(y_reshaped)
    
    # Map the predicted class to a meaningful label
    sentiment = "Positive" if y_pred[0] == 1 else "Negative"
    
    # Display the corresponding message
    if sentiment == "Positive":
        st.write("Great! Your review has a positive sentiment.")
    else:
        st.write("We appreciate your feedback. If there are any issues, please let us know.")

    # You can also display the raw prediction if needed
    st.write(f"Raw prediction: {y_pred[0]}")