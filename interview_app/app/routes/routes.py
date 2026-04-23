from fastapi import APIRouter
import datetime
from app.services import interview_services
from app.schemas.request import InterviewCreateRequest,InterviewUpdateRequest
from app.schemas.response import InterviewResponse
router=APIRouter(prefix="/interviews")

#create Interviews
@router.post("/")
def create_interview(request:InterviewCreateRequest):
    # request is pJSON which deserializaed to python object
    # python object send to service
    # service returns python dict
    data=interview_services.create_interview(request)
    # need to convert python dict to pydantic object of InterviewResponse
    response = InterviewResponse(**data)
    return response

#get interviews
@router.get("/")
def get_all_interviews():
    interview_list= interview_services.get_all_interviews() 
    output_list=[]
    for python_dict in interview_list:
        pydantic_obj=InterviewResponse(**python_dict)
        output_list.append(pydantic_obj)
    return interview_list
    
    
#create interview by id
@router.get("/{interview_id}")
def get_interview_by_id(interview_id:int):
    ret_interview=interview_services.get_interview_by_id(interview_id)
    response_obj=InterviewResponse(**ret_interview)
    return response_obj

#put interview by id
@router.put("/{interview_id}")
def update_interview_by_id(interview_id:int,request:InterviewResponse):
    update_interview=interview_services.update_interview_by_id(interview_id,request)
    response_obj=InterviewResponse(**update_interview)
    return response_obj

#delete interview by id
@router.delete("/{interview_id}")
def delete_interview_by_id(interview_id:int):
   is_interview_delete= interview_services.delete_interview_by_id(interview_id)
   return {
       "msg" : f"Interview delete response: {is_interview_delete}"
   }
    
#get interview by date & time
@router.get("/{get_time}")
def get_time(start_time:datetime.datetime,end_time:datetime.datetime):
    output_list=interview_services.get_time(start_time,end_time)
    response_list=[]
    for each_interviwe in output_list:
        py_obj=InterviewResponse(**each_interviwe)
        response_list.append(py_obj)
    return response_list
    
