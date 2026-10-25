import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")
debug = os.getenv("DEBUG", "False").lower() == "true"

print("Application:", app_name)
print("API key configured:", bool(api_key))
print("Debug mode:", debug)
