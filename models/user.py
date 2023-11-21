#!venv/bin/python3
""" This is a user class definition """
from models.base_model import BaseModel


class User(BaseModel):
    """ user class definition with the needed attribute
     empty string for email
     empty string for password
     empty string for first_name
     empty string for last_name
     empty string for cohort """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    cohort = None
