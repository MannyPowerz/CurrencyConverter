from requests import get
from dotenv import load_dotenv
from flask import Flask, jsonify, request, current_app
from flask_cors import CORS
import os



load_dotenv()

app = Flask(__name__)
CORS(app)


API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

print("API_KEY:", API_KEY)  # Make sure it's not None
print("BASE_URL:", BASE_URL)  # Make sure it's correct


# 1.) Dropdown menu for Currency selection currency 1 & currency 2 with currency abreviation hyphen name of currecy hyphen Symbol if possible, Start with using endpoint of url h then convert JSON dictionary into tuple and using json() method and convert currencies to a list and sort it 

# def generate_Currency_List():
#     endpoint = f"api/v7/currencies?apiKey={API_KEY}"
#     url = BASE_URL + endpoint
#     response = get(url)
#     data = response.json()
#     currencies = data.get("results", {}) 
    
#     currency_list = sorted(
#         [(info["id"], info.get("currencyName", ""), info.get("currencySymbol", "")) for info in currencies.values()]
#     )
#     return currency_list

from flask import current_app

def generate_Currency_List():
    try:
        endpoint = f"api/v7/currencies?apiKey={API_KEY}"
        url = BASE_URL + endpoint
        response = get(url)
        response.raise_for_status()  # Raises an error for bad status codes
        
        data = response.json()
        if not data:
            print("No data received from API")
            return []
            
        currencies = data.get("results", {})
        if not currencies:
            print("No currencies found in data")
            return []
            
        currency_list = sorted(
            [(info["id"], info.get("currencyName", ""), info.get("currencySymbol", "")) 
            for info in currencies.values()]
        )
        return currency_list
        
    except Exception as e:
        print(f"Error in generate_Currency_List: {str(e)}")
        return []


# @app.route('/api/currencies', methods=['GET'])
# def currencies():
#     currency_list = generate_Currency_List()
#     return jsonify(currency_list)

@app.route('/api/currencies', methods=['GET'])
def currencies():
    print("Currencies endpoint hit")  # Debug print
    currency_list = generate_Currency_List()
    print("Currency list:", currency_list[:5])  # Print first 5 currencies
    return jsonify(currency_list)



#______________________________________________________________

# 2.) Exchange rate from currecy 1 converted to currency 2 is at a specific rate, test if example currecy 2 to currecy 1 rate is possible when flipped over positions providing different rate ,
# - endpoint for echnage rate w/ "{currency1}_{currency2}""
# - url assignemnt
# - error handling if data is 0 print(" ") & return keyword
# - use list of values method for the first that comes up in list 

def get_exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()
    
    if len(data) == 0:
        print(f"Invalid Entry")
        return
    
    return list(data.values())[0]





@app.route('/api/exchange-rate', methods =['GET'])
def exchange_rate():
    currency1 = request.args.get('currency1')
    currency2 = request.args.get('currency2')
    if not currency1 or not currency2:
        return jsonify({"error": "Currency parameters are required"}), 400
    rate = get_exchange_rate(currency1,currency2)
    if rate is None:
        return jsonify({"error": "Invalid currencies or data unavailable"}), 404
    return jsonify({"rate": rate})


#______________________________________________________________

# 3.) Option after Exchange Rate recieved for Conversion of Amount inputed of currency 1 output Amount that will be recived of currecny 2 , rate times amount of currency 1


def convert_Amount(currency1, currency2, amount):
    
    rate = get_exchange_rate(currency1, currency2)
    if rate is None:
        return None

    # try:
    #     amount = float(amount)
    # except ValueError:
    #     print(f"Invalid Amount")
    #     return
    
    newAmount = rate * amount
    return newAmount

@app.route('/api/convert', methods=['GET'])
def convert():
    currency1 = request.args.get('currency1')
    currency2 = request.args.get('currency2')
    amount = request.args.get('amount')
    
    if not (currency1 and currency2 and amount):
        return jsonify({"error": "All parameters (currency1, currency2, amount) are required"}), 400
    try:
        amount = float(amount)
    except ValueError:
        return jsonify({"error":"Invalid amount"}),400
    
    converted_Amount = convert_Amount(currency1, currency2, amount)
    
    if converted_Amount is None:
        return jsonify({"error": "Conversion failed"}), 500
    return jsonify({"converted_amount": converted_Amount})
    
#If needed how to convert amount the other way around using currency2 amount as base currency to currecy 1 as mentioned getting a new rate going the opposite direction possibly


# FETCH data in python and set through web framework 

# Run the Flask app
    
# if __name__ == "__main__":
#     app.run(debug=True)

def test_api_connection():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    try:
        response = get(url)
        print("Status Code:", response.status_code)
        print("Response:", response.json())
    except Exception as e:
        print("API Error:", str(e))

# Add this to your main
if __name__ == "__main__":
    print("Testing API connection...")
    test_api_connection()
    app.run(debug=True)

#______________________________________________________________


# The backend and frontend will communicate via API calls

# Frontend sends requests to the backend with currency pairs and amounts

# Backend processes the request, performs the conversion, and sends the result (converted amount) back to the frontend

#******************************************************************************

# Receive currency pairs and amounts from the frontend.

# Plan API Endpoints  (e.g., /convert, /get_rates). Determine data structures and formats for requests and responses.

# Perform the necessary calculations to convert currencies based on the retrieved exchange rates

# Validate user input (e.g., currency codes, amounts) to prevent errors and ensure data integrity , Imnplement error handling for invalid user input


# Format the calculated results (converted amounts) in a suitable format for the frontend to easily consume (e.g., JSON)

# Handle potential API errors or rate limit issues gracefully


