from fastapi import FastAPI, Request, Response

app = FastAPI()

# Middleware example
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response: Response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.process_time())
    return response

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Startup event
@app.on_event("startup")
def startup_event():
    print("Application startup")

# Shutdown event
@app.on_event("shutdown")
def shutdown_event():
    print("Application shutdown")

# Main route example
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Additional routes can be defined here...