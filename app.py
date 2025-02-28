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

