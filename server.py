

from flask import Flask, render_template, url_for, request, redirect
import csv 
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

#generate the pages with a single code instead of copying @app route
@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)


#data sent through contact form
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		data = request.form.to_dict()
		write_to_csv(data)
		#write_to_txt(data)
		return redirect('./thankyou.html')     #duplicate the contact.html and name it thankyou.html. change the sections for the 'form' to your thank you message

	else:
		return 'Something went wrong. Try again!'

    	

#save the data received from webpage to a file
#def write_to_txt(data):
#	email=data["email"]
#	subject=data["subject"]
#	message=data["message"]
#	with open("database.txt", mode='a') as database:	
#		file =database.write(f"\n{email}, {subject},{message}")


def write_to_csv(data):
	email=data["email"]
	subject=data["subject"]
	message=data["message"]
	with open("database.csv", newline='', mode='a') as database2:	
		csv_writer =csv.writer(database2, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

