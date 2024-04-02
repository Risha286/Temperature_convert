# backend.py
from flask import Flask, request, jsonify

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    temperature = data['temperature']
    unit = data['unit']
    result = {}

    if unit == 'Celsius':
        result['fahrenheit'] = celsius_to_fahrenheit(temperature)
        result['celsius'] = temperature
        result['kelvin'] = celsius_to_kelvin(temperature)
    elif unit == 'Fahrenheit':
        result['celsius'] = (temperature - 32) * 5/9
        result['fahrenheit'] = temperature
        result['kelvin'] = (temperature - 32) * 5/9 + 273.15
    elif unit == 'Kelvin':
        result['celsius'] = temperature - 273.15
        result['fahrenheit'] = (temperature - 273.15) * 9/5 + 32
        result['kelvin'] = temperature
    else:
        return jsonify({'error': 'Invalid unit.'}), 400

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
