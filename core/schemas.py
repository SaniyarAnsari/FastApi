from pydantic import BaseModel, Field

class CostModel(BaseModel):
    title: str = Field(description="Enter title of cost", min_length=2, max_length=20, pattern=r"^[a-zA-Z0-9 ]+$")
    id : int
    description : str = Field(min_length=3, max_length=100)
    amount: float= Field(gt=0)

class CostUpdate(BaseModel):
    title: str = Field(description="add title of cost", min_length=2, max_length=20)
    description: str = Field(min_length=3, max_length=100)
    amount: float = Field(gt=0)