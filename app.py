import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Main page

@app.route('/page2')
def page2():
    return render_template('index2.html')  # Second page

@app.route('/page3')
def page3():
    return render_template('index3.html')  # Third page

if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
