from flask import Flask, render_template, request

app = Flask(__name__)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Form Submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Data save karne ke liye (abhi file me save karte hain)
    with open("data.txt", "a") as f:
        f.write(f"{name}, {email}\n")

    return f"Thanks {name}, we got your data!"

if __name__ == '__main__':
    app.run(debug=True)
