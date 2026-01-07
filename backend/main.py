from fastapi import FastAPI, UploadFile, File
import pandas as pd
import traceback
from backend.nlp.intent import detect_intent
from backend.insights.generator import generate_insight

DATAFRAME_STORE = {}

app = FastAPI(title="AI Autonomous Data Analyst")

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    try:
        file.file.seek(0)
        df = pd.read_csv(file.file)

        DATAFRAME_STORE["df"] = df

        return {
            "message": "File uploaded successfully",
            "rows": df.shape[0],
            "columns": list(df.columns)
        }

    except Exception as e:
        return {"error": str(e)}

@app.post("/question")
async def ask_question(payload: dict):
    question = payload.get("question", "")
    intent = detect_intent(question)

    df = DATAFRAME_STORE.get("df")

    if df is None:
        return {"error": "No dataset uploaded yet"}

    insight = generate_insight(df, intent)

    return {
        "question": question,
        "detected_intent": intent,
        "insight": insight
    }

