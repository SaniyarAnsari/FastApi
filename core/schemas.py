from pydantic import BaseModel

class BasePersonSchema(BaseModel):
    name : str
    
class PersonCreateSchema(BasePersonSchema):...

class PersonResponseSchema(BasePersonSchema):
    id : int

class PersonUpdateSchema(BasePersonSchema):...
