from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dispatcher import dispatch
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/makeup-check")
async def makeup_check(
    noMakeupPhoto: UploadFile = File(...),
    makeupPhoto: UploadFile = File(...),
    makeupStyle: str = Form(...)
):

    try:
        result = await dispatch(noMakeupPhoto, makeupPhoto, makeupStyle)
        print("Dispatch Result:", result)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
