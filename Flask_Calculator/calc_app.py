from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# To renderHomepage
@app.route('/', methods=['POST', 'GET'])
def home_page():
    return render_template('calc.html')


# This will be called from UI
@app.route('/math', methods=['POST'])
def math_operation():
    if request.method == 'POST':
        operation = request.form['operation']
        num1 = request.form['num1']
        num2 = request.form['num2']

        if operation == 'add':
            r = float(num1) + float(num2)
            result = 'the' + ' sum' + ' of' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'subtract':
            r = float(num1) - float(num2)
            result = 'the' + ' difference' + ' of' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':
            r = float(num1) * float(num2)
            result = 'the' + ' product' + ' of' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':
            quotient = float(num1) // float(num2)
            remainder = float(num1) % float(num2)
            result = 'the' + ' quotient' + ' of dividing ' + str(num1) + ' and ' + str(num2) + ' is ' + str(quotient) + ' and the remainder' + ' is ' + str(remainder)
        return render_template('results.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
