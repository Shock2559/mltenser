import pickle
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from flask import Flask, render_template, url_for, request, jsonify
import numpy as np

import telebot

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


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response


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

with open('net_topic', 'rb') as pkl:
    model2 = pickle.load(pkl)

@app.route('/topic', methods=['post'])
def get_sort():

    request_data = request.get_json()
    q1 = float(request_data['q1'])
    q2 = float(request_data['q2'])
    q3 = float(request_data['q3'])
    q4 = float(request_data['q4'])

    pred = model2.predict([[q1, q2, q3, q4]])
    label = ['1', '2', '3']
    return jsonify(topic=label[pred[0]])

bot = telebot.TeleBot("6444671565:AAFtC4IopclJPSBPPKabnBDgcdigc9wRyuo")

@app.route('/send_message_bot', methods=['GET'])
def get_send():

    print(request.headers['message'])
    request_data = request.headers['message']

    users = bot.get_updates()

    for user in users:
        if user.message.chat.id:
            bot.send_message(user.message.chat.id, request_data)


    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8098)
