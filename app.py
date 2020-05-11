from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# This enables us to dynamically render our routes - it is the equivalent of having a separate view for each route
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name + '.html')


if __name__ == '__main__':
    app.run()
