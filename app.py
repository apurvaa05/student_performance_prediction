from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        gender = int(request.form['gender'])
        previous_grade = float(request.form['previous_grade'])
        extracurricular = int(request.form['extracurricular'])
        parental_support = int(request.form['parental_support'])
        online_classes = int(request.form['online_classes'])
        avg_study_hours = float(request.form['avg_study_hours'])
        avg_attendance = float(request.form['avg_attendance'])

        # Arrange in correct order
        features = np.array([[gender, previous_grade, extracurricular,
                              parental_support, online_classes,
                              avg_study_hours, avg_attendance]])

        prediction = model.predict(features)[0]

        return render_template('index.html',
                               prediction_text=f"Predicted Final Grade: {round(prediction,2)}")

    except Exception as e:
        return render_template('index.html',
                               prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)