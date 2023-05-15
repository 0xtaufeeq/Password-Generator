from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]{}()*;/.,-_"

    length = int(request.form['length'])
    include_lowercase = request.form.get('include_lowercase')
    include_uppercase = request.form.get('include_uppercase')
    include_numbers = request.form.get('include_numbers')
    include_symbols = request.form.get('include_symbols')

    all = ""
    if include_lowercase:
        all += lowercase
    if include_uppercase:
        all += uppercase
    if include_numbers:
        all += numbers
    if include_symbols:
        all += symbols

    if not all:
        return render_template('index.html', error="You must select at least one character type.")

    num_passwords = int(request.form['num_passwords'])

    passwords = []
    for _ in range(num_passwords):
        password = "".join(random.sample(all, length))
        passwords.append(password)

    return render_template('index.html', passwords=passwords)

if __name__ == '__main__':
    app.run(debug=True)
