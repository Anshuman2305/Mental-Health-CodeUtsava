from unittest import result
import flask
import pickle
import pandas as pd



# Use pickle to load in the pre-trained model.
with open(f'model/model_pkl.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
       return(flask.render_template('main.html')) #homepage is loaded

    if flask.request.method == 'POST':  #when we will click the submit button
        q1 = flask.request.form['q1']
        q2 = flask.request.form['q2']
        q3 = flask.request.form['q3']
        q4 = flask.request.form['q4']
        q5 = flask.request.form['q5']
        q6 = flask.request.form['q6']
        q7 = flask.request.form['q7']
        q8 = flask.request.form['q8']
        q9 = flask.request.form['q9']
        q10 = flask.request.form['q10']

        # Make DataFrame for model
        input_variables = pd.DataFrame([[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]],
                                      columns=['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10'],
                                      dtype=float,
                                      index=['input'])
                
        
        # Get the model's prediction
        prediction = model.predict(input_variables)[0]

        if prediction == 0: 
            guess = "Not Depressed"
        if prediction == 1: 
            guess = "Mildly Depressed"
        if prediction == 2: 
            guess = "Moderately Depressed"
        if prediction == 3: 
            guess = "Severely Depressed"
        if prediction == 4: 
            guess = "Critically Depressed"

    


        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html',
                                     original_input={},
                                     result=guess,
                                     )

if __name__ == '__main__':
    app.run()