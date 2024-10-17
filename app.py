from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Flask!</h1>"

@app.route('/index')
def index():
    return "Welcome, Flask!"

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Get the form data
        math = int(request.form['math'])
        science = int(request.form['science'])
        history = int(request.form['history'])

        # Calculate the average score
        average = (math + science + history) / 3

        # Determine if the person passed or failed
        result = "pass" if average >= 50 else "fail"

        # Render the same form with the result and score
        return render_template('form.html', result=result, score=average)

    # Render the form for GET requests without result
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
