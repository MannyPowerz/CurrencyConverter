from requests import get
from pprint import PrettyPrinter

printer = PrettyPrinter()

# 1.) Dropdown menu for Currency selection currency 1 t& currency 2 with currency abreviation hyphen name of currecy hyphen Symbol if possible, Start with using endpoint of url and using json() method and convert currencies to a list and sort it


# 2.) Exchange rate from currecy 1 converted to currency 2 is at a specific rate, test if example currecy 2 to currecy 1 rate is possible when flipped over positions providing different rate ,


# 3.) Option after Exchange Rate recieved for Conversion of Amount inputed of currency 1 output Amount that will be recived of currecny 2 , rate times amount of currency 1






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


