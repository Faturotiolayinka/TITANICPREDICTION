from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import numpy as np
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session management

# Load the trained model
def load_model():
    with open('titanidatae.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

# Helper functions for file-based user storage
def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            return json.load(f)
    return {"admin": "admin"}

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f)

users = load_users()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users:
            error = 'Username already exists.'
        else:
            users[username] = password
            save_users(users)
            message = 'Signup successful! Please log in.'
            return render_template('signup.html', message=message)
    return render_template('signup.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users and users[username] == password:
            session['logged_in'] = True
            return redirect(url_for('predict'))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', error=error)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return redirect(url_for('predict'))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    prediction = None
    if request.method == 'POST':
        features = [
            float(request.form['pclass']),
            float(request.form['sex']),
            float(request.form['age']),
            float(request.form['sibsp']),
            float(request.form['parch']),
            float(request.form['fare']),
            float(request.form['embarked'])
        ]
        pred = model.predict([features])[0]
        print("Model prediction raw value:", pred)
        # If the model returns a string, use it directly
        if isinstance(pred, str):
            prediction = pred
        else:
            try:
                pred = int(round(float(pred)))
                if pred == 1:
                    prediction = "Survived"
                elif pred == 0:
                    prediction = "Died"
                else:
                    prediction = f"Unknown result (raw: {pred})"
            except Exception as e:
                print("Prediction conversion error:", e)
                prediction = f"Unknown result (raw: {pred})"
    return render_template('index.html', prediction=prediction)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
