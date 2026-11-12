from fastapi import FastAPI, status, Body
from fastapi.responses import JSONResponse
from core.schemas import CostModel, CostUpdate

app = FastAPI()


# Root
@app.get("/")
def root():
    content = {"message" : "Cost Manager"}
    return JSONResponse(content=content, status_code=status.HTTP_202_ACCEPTED)

Cost = {
    1 : {
        "title": "shopping",
        "id": 1,
        "description":"Buy Laptop",
        "amount": 250000.0
        },

    2 : {
        "title": "buyying",
        "id": 2,
        "description":"Buy mouse",
        "amount": 50000.0
    }
        } 





# Add Cost
@app.post("/add_cost", status_code=status.HTTP_201_CREATED)
def add_cost(cost_info : CostModel):

    if cost_info.id not in Cost:
        Cost[cost_info.id] = cost_info.model_dump()

        return JSONResponse({"message": f"{cost_info.title} add successful."}, 
                            status_code=status.HTTP_201_CREATED)
    
    else : 
        return JSONResponse({"message": "Cost already exists"}, status_code=status.HTTP_409_CONFLICT)




# costs
@app.get("/costs")
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
def replace_cost(id: int, cost_info: CostUpdate):

    if id not in Cost:
        return JSONResponse( {"message": "Cost not found"}, 
                            status_code=status.HTTP_404_NOT_FOUND)
    
    Cost[id] = {
        "id" : id,
        **cost_info.model_dump()
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