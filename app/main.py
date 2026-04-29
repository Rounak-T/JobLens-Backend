from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def test():
    return {"message": "The app is running"}
