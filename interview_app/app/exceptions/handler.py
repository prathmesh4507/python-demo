from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.custoum_exceptions import InterviewNotFoundError 

def global_exception_handler(app):

    @app.exception_handler(InterviewNotFoundError)
    def handle_interview_not_found_exceptipn(request: Request, ex: InterviewNotFoundError):
        return JSONResponse(
            status_code= 400,
            content={
                "message" : ex.msg
            }
        )
    
    # @app.exception_handler(NameError)
    # def handle_name_error(request: Request, ex:NameError ){

    # }

    @app.exception_handler(Exception)
    def handling_generic_exception(ex: Exception, request: Request):
        return JSONResponse(
            status_code= 401,
            content={
                "status":"hey there"
            }
        )