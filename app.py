#from sklearn.externals import joblib

#clf = joblib.load('classifier.pkl')
#def predict(a):
#    predicted = clf.predict(a)    # predicted is 1x1 numpy array
#    return int(predicted[0])
from flask import Flask,render_template,url_for,request
import pickle
from sklearn.externals import joblib

app = Flask(__name__) #initialize a new Flask instance，
#to let Flask know that it can find the HTML template folder (templates)
#in the same directory where it is located.

#the route decorator (@app.route('/')) specifies the URL that
#should trigger the execution of the home function.
@app.route('/')
#home function simply render the home.html HTML file,
#which is located in the templates folder.
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
#predict function access the new message entered by the user and
#use our model to make a prediction for its label.
def predict():
	model = open('classifier.pkl','rb')
	clf = joblib.load(model)
# the POST method transports the form data to the server in the message body.
	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		my_prediction = clf.predict(data)[0]
	return render_template('result.html', prediction = my_prediction)


if __name__ == '__main__':
	app.run(debug=True)#activate Flask's debugger avoide relaunch the server in case of
	#modification de contenu ,and run the application
	#on the server when this script is directly executed by the Python interpreter
