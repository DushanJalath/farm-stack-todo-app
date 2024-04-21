from pymongo import MongoClient
from model import ToDo

client = MongoClient('mongodb://localhost:27017/')

db = client["TodoList"]  # Replace with your database name
collection = db["todo"] 


async def fetch_one_todo(title):
    document =collection.find_one({"title": title})
    return document

async def fetch_all_todos():
  todos = []
  cursor = collection.find({})  # Find all documents
  for doc in cursor:
    todo_object = ToDo(**doc)  # Convert each document to a Todo object
    todos.append(todo_object)  # Add the converted object to the todos list
  return todos


async def create_todo(todo):
    result = collection.insert_one(todo.dict())
    return todo.dict()


async def update_todo(title, desc):
    update_result = collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = collection.find_one({"title": title})
    return document


async def remove_todo(title):
    collection.delete_one({"title": title})
    return True