import flask
import joblib
import numpy as np
from flask import render_template, request
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
 
@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('index.html')

@app.route('/output', methods = ['POST'])
def prediction():
	if request.method == 'POST':
		gender = request.form['gender']
		married = request.form['status']
		dependat =request.form['dependants']
		education = request.form['education']
		employ = request.form['employ']
		annual_income = request.form['aincome']
		co_income = request.form['coincome']
		Loan_amount = request.form['Lamount']
		Loan_amount_term = request.form['Lamount_term']
		credit = request.form['credit']
		proper = request.form['property_area']

	gender = gender.lower()
	married= married.lower()
	education = education.lower()
	employ = employ.lower()
	proper = proper.lower()
	if(employ=='yes'):
		employ = 1
	else:
		employ = 0
	if(gender=='male'):
		gender = 1
	else:
		gender = 0
	if (married=='married'):
		married=1
	else:
		married=0
	if (proper=='rural'):
		proper=0
	elif (proper=='semiurban'):
		proper=1
	else:
		proper=2
	if (education=='graduate'):
		education=0
	else:
		education=1
    
	dependat = int(dependat)
	annual_income = int(annual_income)
	co_income = int(co_income)
	Loan_amount = int(Loan_amount)
	Loan_amount_term = int(Loan_amount_term)
	credit = int(credit)
	x =np.array([[gender, married, dependat,education,employ,annual_income,co_income,Loan_amount,Loan_amount_term,credit,proper]])
	model = joblib.load('Forest.pkl')
	ans = int(model.predict(x)[0])
	if (ans==1):
		print("Congratulations your eligble for this Loan")
	else:
		print("We are sad to inform that your request has not been accepted")
	return render_template('output.html', output=ans)
	

if __name__ == '__main__':
	app.debug = True
	app.run()
 
 