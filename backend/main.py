from fastapi import FastAPI, UploadFile, File
import pandas as pd
import traceback

app = FastAPI(title="AI Autonomous Data Analyst")

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    try:
        file.file.seek(0)
        raw = file.file.read()

        print("---- RAW FILE CONTENT (first 500 chars) ----")
        print(raw[:500])

        file.file.seek(0)
        df = pd.read_csv(file.file)

        print("---- DATAFRAME HEAD ----")
        print(df.head())

        return {
            "rows": df.shape[0],
            "columns": list(df.columns)
        }

    except Exception as e:
        print("---- ERROR TRACEBACK ----")
        traceback.print_exc()
        return {"error": str(e)}
