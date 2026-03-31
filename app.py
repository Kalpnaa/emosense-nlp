from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict' ,methods=['POST'])
def p():
    text = request.form['text']
    return render_template('index.html', prediction=text)



if __name__ == "__main__":
    app.run(debug=True)