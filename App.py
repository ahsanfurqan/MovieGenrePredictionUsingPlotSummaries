from flask import Flask,render_template,request,jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import numpy as np

app = Flask(__name__)
#Bootstrap(app)
path='D:/MovieGenrePredictor/fypmodel73.35%.h5'
mymodel=load_model(path)   
mainGenres={0:'Drama',1:'Comedy',2:'Action',3:'Horror'}
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
    return pad_sequences(sequence,maxlen=1488)
@app.route('/')
def index():
    return render_template("Home.html")
@app.route('/prediction',methods=['POST'])
def prediction():
    #text=request.get_json()
    text=request.form['text'] 
    text=clean_text(text)
    # return jsonify({'prediction':text})
    data=tokenizing(text)
    pred=mymodel.predict(data)  
    pred = np.around(pred)
    pred=np.argmax(pred)
    predict_classes=mainGenres[pred]
    #return jsonify({'text':pred})
    return jsonify({'prediction':predict_classes})
    #return render_template('prediction.html',data=predict_classes)

if __name__=="__main__":
    app.run(host="127.0.0.1",port="5000", debug=True)