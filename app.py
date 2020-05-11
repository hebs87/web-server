from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    """
    This enables us to dynamically render our routes - it is the equivalent of having a separate view for each route
    """
    return render_template(page_name + '.html')


# def write_to_file(data):
#     """
#     A utility function to write the form data to a database.txt file
#     """
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    """
    A utility function to write the form data to a database.csv file using the csv module
    """
    with open('database.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """
    A view to handle the contact form submission
    """
    if request.method == 'POST':
        try:
            # Convert all form data into a dictionary
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou')
        except:
            return 'Couldn\'t submit your details, please try again!'
    else:
        return 'Something went wrong, please try again!'


if __name__ == '__main__':
    app.run()
