from flask import Flask,render_template,request,jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import numpy as np

app = Flask(__name__)
#Bootstrap(app)
path='D:/MovieGenrePredictor/fypmodel64.08%.h5'
mymodel=load_model(path)   
mainGenres={0:'Drama',1:'Comedy',2:'Action',3:'Horror'}
max_num_words=5000
max_seq_len=600
nltk.download('stopwords')
nltk.download('punkt')
stop = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
def lemmatize_text(text):
    return " ".join([lemmatizer.lemmatize(w) for w in text.split()])
def removingStopWords(text):
    text=' '.join(word for word in text.split() if word not in (stop))
    return text
def  clean_text(cleanText):
    cleanText = cleanText.lower()
    cleanText =re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "",cleanText)  
    # remove numbers
    cleanText= re.sub(r"\d+", "",cleanText)
    
    return cleanText
def tokenizing(text):
    tokenizer=Tokenizer(num_words=max_num_words,filters='!"#$&%()*+-./:;<=>?@[\]^_`{|}~',lower=True)
    tokenizer.fit_on_texts(text)
    sequence=tokenizer.texts_to_sequences(text)
    return pad_sequences(sequence,maxlen=max_seq_len)
@app.route('/')
def index():
    return render_template("Home.html")
@app.route('/prediction',methods=['POST'])
def prediction():
    #text=request.get_json()
    text=request.form['text'] 
    text=clean_text(text)
    text=removingStopWords(text)
    text=lemmatize_text(text)
    # return jsonify({'prediction':text})
    data=tokenizing(text)
    pred=mymodel.predict(data)  
    pred=np.argmax(pred[0])
    predict_classes=mainGenres[pred]
    #return jsonify({'text':pred})
    return jsonify({'prediction':predict_classes})
    #return render_template('prediction.html',data=predict_classes)

if __name__=="__main__":
    app.run(host="127.0.0.1",port="5000", debug=True)