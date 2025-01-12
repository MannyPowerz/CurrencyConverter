from requests import get
from pprint import PrettyPrinter

printer = PrettyPrinter() #Formatted Output for JSON

# 1.) Dropdown menu for Currency selection currency 1 & currency 2 with currency abreviation hyphen name of currecy hyphen Symbol if possible, Start with using endpoint of url h then convert JSON dictionary into tuple and using json() method and convert currencies to a list and sort it 

def generateCurrencyList():
    endpoint = 
    url = BASE_URL + endpoint
    data = get(url).json()
    dataList = list(data.items()).sort()
    
    return dataList
    
def printCurrencyList(currencies):
    for name, currency in currencies:
        name = currency["currencyName"]
        currencyId = currency["id"]
        symbol = currency.get("currencySymbol", "")
        
        print(f"{name} : {currencyId} - {symbol}")

dataList = generateCurrencyList()
printCurrencyList(dataList)
    
    
#______________________________________________________________

# 2.) Exchange rate from currecy 1 converted to currency 2 is at a specific rate, test if example currecy 2 to currecy 1 rate is possible when flipped over positions providing different rate ,
# - endpoint for echnage rate w/ "{currency1}_{currency2}""
# - url assignemnt
# - error handling if data is 0 print(" ") & return keyword
# - use list of values method for the first that comes up in list 

def exchangeRate(currecy1, currency2):
    endpoint = 
    url = BASE_URL + endpoint
    data = get(url).json()
    
    if len(data) == 0:
        print(f"Invalid Entry")
        return
    
    return list(data.values())[0]

rate = exchangeRate(inputId_1, inputId_2)


#______________________________________________________________

# 3.) Option after Exchange Rate recieved for Conversion of Amount inputed of currency 1 output Amount that will be recived of currecny 2 , rate times amount of currency 1


def conversionOfAmount(currency1, currency2, amount):
    rate = exchangeRate(inputId_1, inputId_2)
    
    try:
        amount = float(amount)
    except ValueError:
        print(f"Invalid Amount")
        return
    
    newAmount = rate * amount
    return newAmount

#If needed how to convert amount the other way around using currency2 amount as base currency to currecy 1 as mentioned getting a new rate going the opposite direction possibly

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


