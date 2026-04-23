import datetime
from app.db.db import interviews
from app.exceptions.custoum_exceptions import InterviewNotFoundError
from app.schemas.request import InterviewCreateRequest,InterviewUpdateRequest

#create Interviews
def create_interview(request:InterviewCreateRequest):
    new_interviews={
        "id":len(interviews)+1,
        "candidate_name":request.candidate_name,
        "interviwer_name":request.interviwer_name,
        "time":request.time            
    }
    interviews.append(new_interviews)
    return new_interviews

#get interviews
def get_all_interviews():
    return interviews
        
    

#create interview by id
def get_interview_by_id(interview_id:int):
    for each_interview in interviews:
        if each_interview["id"]==interview_id:
            return each_interview
    raise InterviewNotFoundError(interview_id)

#put interview by id
def update_interview_by_id(interview_id:int,request:InterviewUpdateRequest):
    for each_interview in interviews:
        if each_interview["id"]==interview_id:
            each_interview.update({
                "candidate_name":request.candidate_name,
                "interviwer_name":request.interviwer_name,
                "time":request.time
            })
            return each_interview
    raise InterviewNotFoundError(interview_id)

#delete interview by id
def delete_interview_by_id(interview_id:int):
    for each_interview in interviews:
        if each_interview["id"]==interview_id:
            interviews.remove(each_interview)
            return True
        return False

#get interview by date & time
def get_time(start_time:datetime.datetime,end_time:datetime.datetime):
    output_list=[]
    for each_interview_time in interviews:
        interview_actual_time=each_interview_time["time"]
        if start_time<interview_actual_time<end_time:
            output_list.append(each_interview_time)
        return output_list    
        
