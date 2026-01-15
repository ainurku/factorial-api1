from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math

app = FastAPI()

class FactorialRequest(BaseModel):
    n: int

@app.post("/factorial")
def calculate_factorial(request: FactorialRequest):
    if request.n < 0:
        raise HTTPException(400, "n must be >= 0")

    return {
        "n": request.n,
        "factorial": math.factorial(request.n)
    }
