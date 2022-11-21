from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')




@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/noche_1')
def noche_1():
    return render_template('noche1.html')


if __name__== '__main__':
    app.run(debug=True)    