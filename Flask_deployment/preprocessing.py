# Convert everything into lowercase
def to_lower(text):
    return text.lower()

# Remove HTML tags
import re
def clean(text):
    cleaned = re.compile(r'<.*?>')
    return re.sub(cleaned,'',text)

# Remove Punctuation
import string
def remove_puntuation(text):
    text_nopunct = ''.join([i for i in text if i not in string.punctuation])
    return text_nopunct

# Remove stopwords
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    return [w for w in words if w not in stop_words]

# convert number to digit
import inflect
q = inflect.engine()
def convert_number(text):
    new_str = []
    for word in text:
        if word.isdigit():
            temp = q.number_to_words(word)
            new_str.append(temp)
        else:
            new_str.append(word)
    return new_str

# Stemming
from nltk.stem import PorterStemmer
def stem_txt(text):
    ps = PorterStemmer()
    return " ".join([ps.stem(w) for w in text])