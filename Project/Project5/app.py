from flask import Flask, jsonify, request, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



app = Flask(__name__)


## import ridge and scalar pickle
ridge = pickle.load(open('models/ridge.pkl','rb'))
sc = pickle.load(open('models/sc.pkl','rb'))


## 




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def pred():
    if request.method=="POST":
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data = sc.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge.predict(new_data)
        return render_template('home.html',result=result[0])
    else:
        return render_template('home.html')


if __name__ =="__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)