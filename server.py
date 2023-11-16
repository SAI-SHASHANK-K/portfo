from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("databse.txt", mode="a") as database:
        email = data["email"]
        phone = data["phone"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email},{phone}, {subject}, {message}')
        
def write_to_csv(data):
    with open("database.csv", mode="a", newline='\n') as database2:
        email = data["email"]
        mobile_no = data["mobile_no"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,mobile_no,subject,message])
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something Went Wrong. Try Again'
    
    
