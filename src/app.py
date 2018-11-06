from flask import Flask
from src.cli.roman import roman_to_int, int_to_roman

app = Flask(__name__)


@app.route('/<x>')
def convert_to_int(x):
    return "Number: " + str(roman_to_int(x.upper()))


@app.route('/<int:x>')
def convert_to_roman(x):
    return "Roman number: " + int_to_roman(x)


if __name__ == '__main__':
    app.run(port=9000, debug=True)
