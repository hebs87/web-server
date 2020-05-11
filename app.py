from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# This enables us to dynamically render our routes - it is the equivalent of having a separate view for each route
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name + '.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """
    A view to handle the contact form submission
    """
    return 'Form successfully submitted!'


if __name__ == '__main__':
    app.run()
