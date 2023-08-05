import numpy as np
from flask import Flask,render_template,request
import pickle

# create flask app
app=Flask(__name__)

# load the pickle model
model=pickle.load(open('model.pkl','rb'))


# defining homepage

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    prediction=model.predict(features)
    
    return render_template("index.html",prediction_text="The flower species is {}".format(prediction))


if __name__=="__main__":
    app.run(debug=True)