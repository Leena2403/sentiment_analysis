import streamlit as st
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem.porter import PorterStemmer
import re

def preprocessing(file):
    # text = open(file,encoding='utf-8').read()
    lower_case = file.lower()
    cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation)) # removing special characters
    return cleaned_text

def tokenise(cleaned_text):
    # Tokenization
    tokenize_words = word_tokenize(cleaned_text, "english")  # works efficiently
    return tokenize_words

# print(lower_case)
# print(cleaned_text)
# print(tokenize_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


def extraction(tokenize_words):
    final_words = []
    for word in tokenize_words:
        if word not in stopwords.words('english'):
            final_words.append(word) # extracting meangingful words.
    return final_words

ps = PorterStemmer()
def stemming(content):

  stemmed_content = re.sub('[^a-zA-Z]',' ',content) # checking for special characters
  stemmed_content = stemmed_content.lower() # lower case
  stemmed_content = stemmed_content.split() # list
  stemmed_content = [ps.stem(word) for word in stemmed_content if word not in stopwords.words('english')] # stemming meangingful words
  stemmed_content = ' '.join(stemmed_content) # string them up again

  return stemmed_content

# Emotion Algorithm

def emotion_algo(final_words):
    emotion_list = []
    with open('emotions.txt', 'r') as file:
        for line in file:
            # clearing space, commas and line
            clear_line = line.replace('\n','').replace(',', '').replace("'",'').strip()
            word, emotion = clear_line.split(':')

            if word in final_words:
                emotion_list.append(emotion)
        w = Counter(emotion_list)
    return w

def sentiment_analyse(cleaned_file):
    score = SentimentIntensityAnalyzer().polarity_scores(cleaned_file)
    neg = score['neg']
    pos = score['pos']
    neu = score['neu']

    if neu > pos and neu > neg:
        print("Neutral Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Negative Sentiment")
    return score

# w = Counter(emotion_list)
# print(w)

def bar_plot(w):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    ax.set_ylabel('Word Count')
    ax.set_xlabel('Emotions')
    ax.set_title(f'Sentiment Analysis Bargraph')
    ax.grid(True)
    st.pyplot(fig)

st.title("Sentiment Analysis")

user_text = st.text_area(
"Add your text, we'll do a sentiment analysis"
)

if st.button("Apply"):
    preprocess = preprocessing(user_text)
    tokenize_words = tokenise(preprocess)
    final_words = extraction(tokenize_words)
    stem = stemming(user_text)
    w = emotion_algo(final_words)
    bar_plot(w)
    sentiment = sentiment_analyse(preprocess)





