from flask import Flask, render_template, request, jsonify
import random
import os

app = Flask(__name__)

# Initialize rocket position

rocket_position = 650

# Path to the file where messages will be stored
messages_file = 'messages.txt'

# Path to the file where chat messages are stored
chat_file = 'chat.txt'

@app.route('/')
def index():
    global rocket_position
    # Read messages from the file
    if os.path.exists(messages_file):
        with open(messages_file, 'r') as file:
            messages = file.readlines()
    else:
        messages = []

    return render_template('index.html', messages=messages, rocket_position=rocket_position)

@app.route('/message', methods=['POST'])
def message():
    global rocket_position
    message = request.form['message']
    
    # Update rocket position
    rocket_position -= random.randint(10, 50)
    if rocket_position < 50:  # Assume 50px is the position of Mars
        rocket_position = 50

    # Save message to file
    with open(messages_file, 'a') as file:
        file.write(message + '\n')

    return jsonify({'rocket_position': rocket_position, 'message': message})

@app.route('/random_chat')
def random_chat():
    # Read random line from chat file
    with open(chat_file, 'r') as file:
        chats = file.readlines()
    random_chat = random.choice(chats).strip()
    return random_chat

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
