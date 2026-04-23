from pydantic import BaseModel,Field
from datetime import datetime

class InterviewCreateRequest(BaseModel):
    candidate_name:str=Field(max_length=100,min_length=3,example="username surname")
    interviwer_name:str
    time:datetime
    
class InterviewUpdateRequest(BaseModel):
    candidate_name:str=Field(max_length=100,min_length=3,example="username surname")
    interviwer_name:str
    time:datetime