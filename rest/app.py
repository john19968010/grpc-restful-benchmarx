from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import os
import uvicorn


# Create an instance of the FastAPI class
load_dotenv()
app = FastAPI()

# Define a route and its corresponding function
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


# @app.get("/from_previous")
# async def read_root():
#     pod_num = int(os.getenv('pod_num')) - 1
#     if pod_num == 0:
#         return {"message": "Hello, World!"}
#     ret = requests.get(f"http://hello-world-rest{pod_num}:10009")
#     return {"message": ret.json()["message"]}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10009)