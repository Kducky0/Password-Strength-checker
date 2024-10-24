from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    strength = 'Weak'
    color_class = 'weak'  # Default to weak

    if len(password) >= 8:
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_number = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

        if has_upper and has_lower and has_number and has_special:
            strength = 'Strong'
            color_class = 'strong'
        elif (has_upper and has_lower) or (has_upper and has_number) or (has_lower and has_number):
            strength = 'Moderate'
            color_class = 'moderate'

    return strength, color_class

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = ''
    color_class = ''
    if request.method == 'POST':
        password = request.form['password']
        strength, color_class = check_password_strength(password)
    return render_template('index.html', strength=strength, color_class=color_class)

if __name__ == '__main__':
    app.run(debug=True)
