from fastapi import FastAPI, status, Body
from fastapi.responses import JSONResponse

app = FastAPI()


# Root
@app.get("/")
def root():
    content = {"message" : "Cost Manager"}
    return JSONResponse(content=content, status_code=status.HTTP_202_ACCEPTED)

Cost = {
    1 : {
        "id": 1,
        "description":"Buy Laptop",
        "amount": 250000.0
        },

    2 : {
        "id": 2,
        "description":"Buy mouse",
        "amount": 50000.0
    }
        }


# Add Cost
@app.post("/add_cost", status_code=status.HTTP_201_CREATED)
async def add_cost(id:int = Body(), 
                   description:str = Body(), 
                   amount:float = Body()):

    cost_info = {
        "id": id,
        "description": description,
        "amount": amount
                }
    
    Cost[id] = cost_info
    return JSONResponse({"message": f"{cost_info} add successful."}, 
                        status_code=status.HTTP_201_CREATED)

# costs
@app.get("/Costs")
def Costs():
    return Cost


# Optional cost
@app.get("/cost/{id}")
def optional_cost(id:int):

    if id not in Cost:
        return JSONResponse({"message": "Cost not found"}, 
                            status_code=status.HTTP_404_NOT_FOUND)
    
    return Cost.get(id)


# replace cost
@app.put("/replace_cost/{id}", status_code=status.HTTP_200_OK)
def replace_cost(id:int, description:str, amount:float):

    if id not in Cost:
        return {"message": "Cost not found"}
    
    Cost[id] = {
        "id" : id,
        "description" : description,
        "amount" : amount
    }

    return Cost[id]
    
# Delete cost
@app.delete("/delete_cost/{id}")
def delete_cost(id: int):

    if id not in Cost:
        return JSONResponse({"message": "Cost not found"}, 
                            status_code=status.HTTP_404_NOT_FOUND)
    
    del Cost[id]

    return JSONResponse({"message": f"id : {id} removed successful from Cost"}, 
                        status_code=status.HTTP_200_OK)