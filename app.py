from fastapi import FastAPI, File, UploadFile
from predict import classify_paraphrase

app = FastAPI()

@app.post("/classify/")
async def create_upload_file(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    text1 = (await file1.read()).decode("utf-8")
    text2 = (await file2.read()).decode("utf-8")
    
    result, score = classify_paraphrase(text1, text2)
    
    return {"file1": file1.filename, "file2": file2.filename, "result": result, "score": score}