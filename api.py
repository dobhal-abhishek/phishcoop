import flask
from flask import Flask, render_template, request
from sklearn.externals import joblib
import inputScript
import regex


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('home.html')

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route('/predict', methods = ['POST'])
def make_prediction():
    if request.method=='POST':
        url = request.form['url']
        if not url:
            return render_template('home.html', label = 'Please input url')
        elif(not(regex.search(r'^(http|ftp)s?://', url))):
            return render_template('home.html', label = 'Please input full url, for exp- https://facebook.com')
        
        
        checkprediction = inputScript.main(url)
        prediction = classifier.predict(checkprediction)

        if prediction[0]==1 :
            label = 'website is not legitimate'
        elif prediction[0]==-1:
            label ='website is legitimate'
        
        return render_template('home.html', label=label)
        
        
if __name__ == '__main__':
    classifier = joblib.load('rf_final.pkl')
    app.run(host='0.0.0.0', port=8000, debug=True)