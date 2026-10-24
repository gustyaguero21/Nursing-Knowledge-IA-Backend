import os
from dotenv import load_dotenv

def LoadEnv():
    if os.path.exists('../.env'):
        load_dotenv()
    else:
        raise FileNotFoundError("error loading .env file")


def GetDBConnection()->str:
    db_host=os.getenv('DB_CONNECTION')

    return str(db_host)


def GetDBName()->str:
    db_name=os.getenv('DB_NAME')

    return str(db_name)


def GetDBUser():
    db_user=os.getenv('DB_USER')

    return db_user


def GetDBPassword():
    db_password=os.getenv('DB_PASSWORD')

    return db_password
