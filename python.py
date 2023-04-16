from fastapi import FastAPI

app = FastAPI()

my_array = [
    {
        "name": "Emmanuel",
        "idade": 19,
        "id": 1
    },
    {
        "name": "João",
        "idade": "gay",
        "id": 2
    }
]

@app.get("/")
async def teste():
    return my_array


@app.get("/home")
async def teste():
    return "home"

@app.get("/{id}")
async def getById(id):

    my_user = [
        element for element in my_array if element["id"] == int(id)
    ]

    print(my_user)

    return my_user

if __name__ == '__main__':
    import uvicorn 

    uvicorn.run("python:app", host="127.0.0.1", port=8000, log_level="info", reload=True)