import requests
from todo import TODOClass
import json

def getAllTODOs():
    response = requests.get('https://dummyjson.com/todos')
    data = response.json()
    for item in data["todos"]:
        print(f'id: {item["id"]}, tarea: {item["todo"]}, terminado: {item["completed"]}')

def searchTODOById():
    id = input('Ingrese el ID: ')
    response = requests.get(f'https://dummyjson.com/todos/{id}')
    data = response.json() # decodifica respuesta a json
    todo = TODOClass(data["id"], data["todo"], data["completed"])
    print(f'id: {todo.getId()}')
    print(f'tarea: {todo.getTodo()}')
    print(f'terminado: {todo.getCompleted()}')

def addTODO(): # metodo para publicar un registro por metodo POST
    todo = TODOClass()
    todo.setTodo(input('Ingresar todo: '))
    todo.setCompleted(input('Ingresar estado (completado): '))
    response = requests.post('https://dummyjson.com/todos/add', json={
        "todo": todo.getTodo(),
        "completed": todo.getCompleted(),
        "userId": '5'
    })
    print('Tarea publicada')
    print(response.json())
    
def deleteTODO(): # metodo para eliminar un registro por metodo DELETE
    id = input('Ingresar id: ')
    response = requests.delete(f'https://dummyjson.com/todos/{id}')
    print('Tarea eliminada')
    print(response.json())

def updateTODO(): # metodo para actualizar un registro por metodo PUT
    todo = TODOClass()
    todo.setId(input('Ingresar id: '))
    todo.setCompleted(input('Ingresar estado (completado): '))
    response = requests.put(f'https://dummyjson.com/todos/{todo.getId()}', json={
        "completed": todo.getCompleted()
    })
    print('Tarea actual')
    print(response.json())


option = 0

while option != 6:
    print('---------- Menu ----------')
    print('1.- obtener tarea')
    print('2.- buscar tarea')
    print('3.- agregar tarea')
    print('4.- eliminar tarea')
    print('5.- actualizar tarea')
    print('6.- salir')
    option = int(input('Ingrese su opcion: '))
    if option == 1:
        getAllTODOs()
    elif option == 2:
        searchTODOById()
    elif option == 3:
        addTODO()
    elif option == 4:
        deleteTODO()
    elif option == 5:
        updateTODO()