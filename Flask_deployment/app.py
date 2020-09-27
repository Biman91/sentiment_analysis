from flask import Flask,render_template,url_for,request
import pickle
import numpy as np
from nltk.tokenize import word_tokenize
from preprocessing import to_lower, clean, remove_puntuation, remove_stopwords, convert_number, stem_txt
import nltk
nltk.download('punkt')


# load model
model = pickle.load(open('model.pkl', 'rb'))
word_dict = pickle.load(open('bow.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = str(message)
        i1 = to_lower(data)
        i2 = clean(i1)
        i3 = remove_puntuation(i2)
        i4 = remove_stopwords(i3)
        i5 = convert_number(i4)
        i6 = stem_txt(i5)
        bow = []
        for word in word_tokenize(i6):
            bow.append(word_tokenize(i6).count(word))
        cleaned_inp = []
        for i in word_dict:
            cleaned_inp.append(i6.count(i[0]))
        pred = np.array(cleaned_inp).reshape(1, 1000)
        my_prediction = model.predict(pred)
    return render_template('output.html', prediction=my_prediction)


if __name__ == '__main__':
	app.run(debug=True)