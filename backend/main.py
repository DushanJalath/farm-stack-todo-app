from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import (
    fetch_all_todos,
    fetch_one_todo,
    create_todo,
    update_todo,
    remove_todo
    )
from model import ToDo

app=FastAPI()

origins=['http://localhost:3000'] #react port (front end port)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def read_root():
    return {"Ping":"Pong"}

@app.get('/api/todo',response_model=list[ToDo])
async def get_todo():
    response=await fetch_all_todos()
    return response

@app.get('/api/get_todo_by_id{title}',response_model=ToDo)
async def get_todo_by_id(title):
    response=await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f'there is no todo item with this title {title}')
    

@app.post('/api/todo',response_model=ToDo)
async def save_todo(todo:ToDo):
    response =await create_todo(todo)
    if response :
        return response
    raise HTTPException(400,'something went wrong / Bad request')

@app.put('/api/todo/{title}/',response_model=ToDo)
async def put_todo(title:str,desc:str):
    response=await update_todo(title,desc)
    if response:
        return response
    raise HTTPException(404, f'there is no todo item with this title {title}')

@app.delete('/api/todo/{title}')
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Succesfullu deleted todo item"
    raise HTTPException(404, f'there is no todo item with this title {title}')    



