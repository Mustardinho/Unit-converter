from flask import Flask, render_template, request

app = Flask(__name__)

def convert_temperature(value, unit_from, unit_to):
    # Step 1: Normalize everything to a base unit (Celsius)
    if unit_from == 'celsius':
        celsius = value
    elif unit_from == 'fahrenheit':
        celsius = (value - 32) * 5/9
    elif unit_from == 'kelvin':
        celsius = value - 273.15
    else:
        return None

    # Step 2: Convert from Celsius to the target unit
    if unit_to == 'celsius':
        return celsius
    elif unit_to == 'fahrenheit':
        return (celsius * 9/5) + 32
    elif unit_to == 'kelvin':
        return celsius + 273.15
    else:
        return None

@app.route('/length.html', methods=['GET', 'POST'])
def home():
    result = None
    length_value = ""
    unit_from = ""
    unit_to = ""
    
    if request.method == 'POST':
        try:
            length_value = request.form.get('length_value', '')
            value = float(length_value)
            unit_from = request.form.get('unit_from', '')
            unit_to = request.form.get('unit_to', '')
            
            factors = {
                'meters': 1.0,
                'centimeter': 0.01,
                'kilometer': 1000.0,
                'inch': 0.0254,
                'foot': 0.3048,
                'yard': 0.9144,
                'mile': 1609.344
            }
            
            if unit_from in factors and unit_to in factors:
                value_in_meters = value * factors[unit_from]
                converted_value = value_in_meters / factors[unit_to]
                
                result = f"{value} {unit_from} = {converted_value:.4f} {unit_to}"
            else:
                result = "Error: Invalid unit selection."
            
        except ValueError:
            result = "Error: Please enter a valid number"

    return render_template(
        'length.html',
        result = result,
        length_value = length_value,
        unit_from = unit_from,
        unit_to = unit_to
    )

@app.route('/temp.html', methods=['GET', 'POST'])
def temp():
    result = None
    temp_value = ""
    unit_from = ""
    unit_to = ""
    
    if request.method == 'POST':
        try:
            temp_value = request.form.get('temp_value', '')
            value = float(temp_value)
            unit_from = request.form.get('unit_from', '')
            unit_to = request.form.get('unit_to', '')
            
            converted = convert_temperature(value, unit_from, unit_to)
    
            if converted is not None:
                symbols = {'celsius': '°C', 'fahrenheit': '°F', 'kelvin': 'K'}
                from_sym = symbols.get(unit_from, '')
                to_sym = symbols.get(unit_to, '')
                result = f"{value}{from_sym} = {converted:.2f}{to_sym}"
            else:
                result = "Error: Invalid unit selection."

        except ValueError:
            result = "Error: Please enter a valid number."
    
    return render_template(
        "temp.html",
        result = result,
        temp_value = temp_value,
        unit_from = unit_from,
        unit_to = unit_to
    )
    
    # --- WEIGHT ROUTE ---
@app.route('/weight.html', methods=['GET', 'POST'])
def weight():
    result = None
    weight_value = ""
    unit_from = ""
    unit_to = ""
    
    if request.method == 'POST':
        try:
            weight_value = request.form.get('weight_value', '')
            value = float(weight_value)
            unit_from = request.form.get('unit_from', '')
            unit_to = request.form.get('unit_to', '')
            
            factors = {
                'milligram': 0.001,
                'gram': 1.0,
                'kilogram': 1000.0,
                'ounce': 28.349523125,
                'pound': 453.59237
            }
            
            if unit_from in factors and unit_to in factors:
                # Step 1: Convert input to grams
                value_in_grams = value * factors[unit_from]
                # Step 2: Convert grams to target unit
                converted_value = value_in_grams / factors[unit_to]
                
                result = f"{value} {unit_from} = {converted_value:.4f} {unit_to}"
            else:
                result = "Error: Invalid unit selection."
            
        except ValueError:
            result = "Error: Please enter a valid number"

    return render_template(
        'weight.html',
        result = result,
        weight_value = weight_value,
        unit_from = unit_from,
        unit_to = unit_to
    )
    
if __name__ == '__main__':
    app.run(debug=True)