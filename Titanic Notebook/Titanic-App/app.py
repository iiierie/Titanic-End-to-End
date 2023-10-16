from flask import Flask, render_template
from flask import request
import pickle
import numpy as np

# import the trained machine learning model
with open('titanic_model.pkl','rb') as file:
    model = pickle.load(file)

# app
app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        try:
            Pclass = int(request.form.get('Pclass'))
            Sex = (request.form.get('Sex'))
            Age = (request.form.get('Age'))
            Embarked = (request.form.get('Embarked'))
            Fare = int(request.form.get('Fare'))
            SibSp = int(request.form.get('SibSp'))
            Parch = int(request.form.get('Parch'))



            # preprocessing the data

            #sex
            if Sex == 'male':
                Sex = 1
            else:
                Sex = 0

            #embarked
            if Embarked == 'S':
                Embarked = 2
            elif Embarked =='C':
                Embarked = 0
            else:
                Embarked = 1

            # age bin
            # Define the encoded age dictionary
            encoded_age = {
                "teenager": 5,
                "adult": 0,
                "elderly adult": 2,
                "child": 1,
                "young": 6,
                "old": 4,
                "infant": 3
            }
            # Input age category from the user
            input_category = Age

            # Check if the input category exists in the encoded age dictionary
            if input_category in encoded_age:
                # Change the age value to the encoded number
                age_value = encoded_age[input_category]
                Age = age_value


            # prediction time

                # Prepare the input data for prediction as a NumPy array
                input_data = np.array([[Pclass, Sex, Age, Embarked, Fare, SibSp, Parch]])

                # Make predictions using the loaded model
                prediction = model.predict(input_data)

                # The 'prediction' variable now holds the model's prediction (0 or 1, for survival)


                if prediction[0] == 1:
                    result = 'Survive :)'
                else:
                    result = 'not Survive T_T'

                return render_template('index.html', result = result)
        except Exception as e:
            result = 'not Survive T_T'
            return render_template('index.html', result=result)
    # else:
    #     return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
