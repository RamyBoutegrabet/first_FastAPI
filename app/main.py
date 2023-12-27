from typing import Optional, List
from fastapi import Body, FastAPI, status, HTTPException, Response, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


while True :
    try:
        conn = psycopg2.connect(host = 'localhost',database = 'fastapi', 
                                user = 'postgres', password = 'admin',
                                cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to DataBase Failed")
        print("Error :", error)
        time.sleep(2)

my_posts = [{"title" : "title of post 1" , "content" : "content of post 1", "id" : 1},
            {"title" : "favorite foods", "content" : "I like pizza", "id" : 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id :
            return p

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i
@app.get("/")
def root():
    return{"message": "Welcome To My API"}
    
    