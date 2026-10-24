from dotenv import load_dotenv
import os

def LoadEnv():
    if os.path.exists('../.env'):
        load_dotenv()
    else:
        raise FileNotFoundError("error loading .env file")
