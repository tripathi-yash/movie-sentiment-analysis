from flask import Flask, render_template, request, jsonify
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load model
model = load_model('model-002.keras', compile=False)

# Load tokenizer
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

MAX_LEN = 300

# Store history
history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']

    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=MAX_LEN)

    prediction = float(model.predict(padded)[0][0])
    label = "Positive" if prediction > 0.5 else "Negative"

    # Save history
    history.append({
        "text": text,
        "score": prediction,
        "label": label
    })

    return jsonify({
        "label": label,
        "score": prediction
    })

@app.route('/history')
def get_history():
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)