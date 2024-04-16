from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def alive():
	'This resturns wheter the api is alive'
	return({"status":"alive"})

@app.get("/power/{n}")	
def power(n: int ):
	'This function computes the power 2 of n'
	return({"number":n, "power":n**2})
	
class Operand(BaseModel):
	a: int
	b: int	

@app.post("/adder/")
def adder( ops : Operand): #Depend on the class Operad variables. It's like create a new type
	return({"return": ops.a + ops.b })
	
