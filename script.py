import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Read variables
name = os.getenv("NAME")
city = os.getenv("CITY")
debug = os.getenv("DEBUG")

print("Hello!")
print(f"Name: {name}")
print(f"City: {city}")
print(f"Debug: {debug}")
