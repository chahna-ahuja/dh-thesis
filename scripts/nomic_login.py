# scripts/nomic_login.py
#to make nomic login script for all notebooks or scripts hereafter 

import os
from nomic import cli
from dotenv import load_dotenv

# Load .env from project root
load_dotenv()

# Get the API key
api_key = os.getenv("NOMIC_API_KEY")

def login_nomic():
    """
    Log in to Nomic Atlas using API key from .env.
    (Ask developer for .env key if you are an external user)
    Returns True if login is successful, False otherwise.
    """
    if not api_key:
        print("Error: No NOMIC_API_KEY found. Check your .env file.")
        return False

    try:
        cli.login(api_key)
        print("Login Successful!")
        return True
    except Exception as e:
        print("Login Failed:", e)
        return False