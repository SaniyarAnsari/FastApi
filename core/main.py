from fastapi import FastAPI, Query, status, HTTPException, Path, Form, Body, File, UploadFile
from typing import Optional, Annotated
from fastapi.responses import JSONResponse
import random 


app = FastAPI()

names_list = [
    {"id" : 1, "name":"Ali"},
    {"id" : 2, "name":"saniyar"},
    {"id" : 3, "name":"mohammad"},
    {"id" : 4, "name":"amir"},
]


# ====================================================================================================================

@app.get("/")
def root():
    content = {"message" : "Hello world!"}
    return JSONResponse(content=content, status_code=status.HTTP_202_ACCEPTED)

# ====================================================================================================================

@app.get("/names")
def retrieve_names_list():
    return names_list


# ====================================================================================================================

@app.get("/names/{name_id}")
def retrieve_names_detail(name_id:int = Path(alias="object id", title="Object id", description="the id of the name in names")):
    for name in names_list:
        if name["id"] == name_id:
            return name

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "object not found")

# ====================================================================================================================

# @app.get("/search_by_id")
# def retrieve_names_list(q : Annotated[str | None, Query(max_length=10, description="search by name")]):
#     if q:
#         for item in names_list:
#             if item["name"] == q:
#                 return item
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "object not found")

# ====================================================================================================================

@app.get("/search")
def retrieve_names_list(
    q : Annotated[str | None, Query(alias="search",description="it will be search users from name", max_length=10)] = None,
    id: Annotated[int | None, Query(ge=1, le=500, description="search by id")] = None
    ):
    
    searchs = []
    
    if id is not None:
        for item in names_list:
            if item["id"] == id:
                searchs.append(item)
    if q:
        for item in names_list:
            if item["name"] == q:
                searchs.append(item)

    return searchs

# ====================================================================================================================

@app.post("/upload_files/v2")
def upload(file:UploadFile = File(...)):
    content = await file.read()
    print(file.__dict__)
    return {"file_name" : file.filename, "content_type" : file.content_type, "full_size" : len(file)}

# ====================================================================================================================
@app.post("/crate_users", status_code=status.HTTP_201_CREATED) # status_code=201 --> status_code=status.HTTP_201_CREATED
def create_name(name:str = Body(), age :int = Body(), id :int = Body()):
    object_info = {"id" : id, "age" : age,
      "name" : name}
    names_list.append(object_info)
    return {"result" : object_info}

# ====================================================================================================================
 
@app.post("/upload_files")
def upload(file: bytes = File(...)):
    print(file)
    return {"full_size" : len(file)}

# ====================================================================================================================

@app.put("/name/{name_id}", status_code=status.HTTP_200_OK)
def update_names_detail(name_id : int = Path(), name : str = Form()):
    for item in names_list:
        if item["id"] == name_id:
            item["name"] = name
            return item
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "object not found")

# ====================================================================================================================

@app.delete("/name/{name_id}")
def delete_names_detail(name_id:int):
    for item in names_list:
        if item["id"] == name_id:
            names_list.remove(item)
            return JSONResponse({"detail" : "Object removed "},status_code=status.HTTP_200_OK)
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "object not found")
