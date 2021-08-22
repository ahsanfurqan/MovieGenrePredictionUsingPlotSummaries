from flask import Flask,render_template,request,jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import numpy as np

app = Flask(__name__)
path='D:/MovieGenrePredictor/fypmodel69.75%.h5'
mymodel=load_model(path)   
mainGenres=['drama','comedy','action','horror']
def  clean_text(cleanText):
    cleanText = cleanText.lower()
    cleanText =re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "",cleanText)  
    # remove numbers
    cleanText= re.sub(r"\d+", "",cleanText)
    
    return cleanText
def tokenizing(text):
    tokenizer=Tokenizer()
    tokenizer.fit_on_texts(text)
    sequence=tokenizer.texts_to_sequences(text)
    return pad_sequences(sequence,maxlen=2933)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/prediction',methods=['POST'])
def prediction():
    text=request.form['summary'] 
    text=clean_text(text)
    data=tokenizing(text)
    pred=mymodel.predict(data)
    pred=np.argmax(pred)
    return render_template('prediction.html',data=pred)

if __name__=="__main__":
    app.run(host='192.168.18.43', port=5000, debug=True)