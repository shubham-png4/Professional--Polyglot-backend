
from fastapi import FastAPI
app=FastAPI(title="Professional Polyglot Backend")
@app.get("/health")
def health():
    return {"status":"ok"}
