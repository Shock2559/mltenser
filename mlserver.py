import pickle
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from flask import Flask, render_template, url_for, request, jsonify
import numpy as np

app = Flask(__name__)

classes = ['correct', 'incorrect']
model = load_model('IB_LSTM.h5')
with open('data.pickle', 'rb') as file:
    tokenizer = pickle.load(file)
reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))
max_text_len = 19


def sequence_to_text(list_of_indices):
    words = [reverse_word_map.get(letter) for letter in list_of_indices]
    return (words)


@app.route('/api', methods=['post'])
def get_answer():
    request_data = request.get_json()
    t = request_data['text'].lower()

    data = tokenizer.texts_to_sequences([t])
    data_pad = pad_sequences(data, maxlen=max_text_len)
    print(sequence_to_text(data[0]))

    res = model.predict(data_pad)
    res = np.argmax(res)

    return jsonify(answer=classes[res])

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8098)
