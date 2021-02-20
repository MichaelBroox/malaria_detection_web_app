from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import tensorflow as tf


app = Flask(__name__)

app.config['SECRET_KEY'] = '411db000c91fe7ff8821927d6047426f'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
	return render_template('test.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    '''
    For predicting and rendering results on index.html
    '''

    model = tf.keras.models.load_model('saved_model/MalariaPrediction.h5')

    values = [int(x) for x in request.form.values()]
    
    features = np.array([values])
    
    features = np.reshape(features, (features.shape[0], 1 , features.shape[1]))
    
    prediction = model.predict(features)

    if prediction < 0.5:
        result = 'No suspicion'
    elif prediction >= 0.5:
        result = 'Malaria Suspected'

    flash(message=f'{result} at {np.round(prediction[0][0] * 100, 3)}% chance.')
    
    return render_template('test.html')



if __name__ == "__main__":
    app.run(debug=True)