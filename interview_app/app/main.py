from fastapi import FastAPI
from app.routes.routes import router as Intrview_router


app=FastAPI(
    title="Interview-app",
    docs_url="/docs",
    version="1.0.0",
    description="create simple Interview-app using fastAPI"
)

app.include_router(Intrview_router)
        

@app.get("/health")
def get_health():
    return {
        "Msg" : "server is ok and running"
    }
    