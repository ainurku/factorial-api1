from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math

from logarithm import calculate_log

app = FastAPI()

# JSON request model
class FactorialRequest(BaseModel):
    n: int

# JSON response model
class FactorialResponse(BaseModel):
    n: int
    factorial: int

class LogRequest(BaseModel):
    n: float
    base: float = 10

class LogResponse(BaseModel):
    n: float
    base: float
    result: float


@app.post("/factorial", response_model=FactorialResponse)
def calculate_factorial(request: FactorialRequest):

    if request.n < 0:
        raise HTTPException(
            status_code=400,
            detail="n must be a non-negative integer"
        )

    result = math.factorial(request.n)

    return {
        "n": request.n,
        "factorial": result
    }

@app.post("/logarithm", response_model= LogResponse)
def logarithm(req: LogRequest):
    try:
        return {
            "n": req.n,
            "base": req.base,
            "result": calculate_log(req.n, req.base)
        }
    except ValueError as e:
        raise HTTPException(400, str(e))
