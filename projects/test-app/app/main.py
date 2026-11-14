from fastapi import FastAPI

app = FastAPI(title="test-app")

@app.get("/")
def read_root():
    return {"message": "Hello from test-app"}
