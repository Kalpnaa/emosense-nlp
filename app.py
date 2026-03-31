from flask import Flask,render_template,request
from utils.predictor import predict_emotion
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def p():
    text = request.form['text']

    result = predict_emotion(text)

    return render_template(
        'index.html',
        prediction=result["emotion"],
        top_words=result["keywords"]
    )


if __name__ == "__main__":
    app.run(debug=True)