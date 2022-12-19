from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html') #to render html site in templates folder
    # return 'hello world'

@app.route('/pro')
def products():
    return 'this is a product'

if __name__ == "__main__":
    app.run(debug=True)

    # REFERENCE https://youtu.be/oA8brF3w5XQ?t=1558 ==================================================================