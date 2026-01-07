import pandas as pd

def generate_insight(df: pd.DataFrame, intent: str) -> dict:
    if intent == "aggregation":
        # Example: sales by region
        if "region" in df.columns and "sales" in df.columns:
            result = df.groupby("region")["sales"].sum().to_dict()
            return {
                "type": "aggregation",
                "description": "Total sales by region",
                "result": result
            }

    if intent == "summary":
        numeric_cols = df.select_dtypes(include="number")
        return {
            "type": "summary",
            "description": "Summary statistics",
            "result": numeric_cols.mean().to_dict()
        }

    if intent == "comparison":
        if "category" in df.columns and "sales" in df.columns:
            result = df.groupby("category")["sales"].mean().to_dict()
            return {
                "type": "comparison",
                "description": "Average sales by category",
                "result": result
            }

    if intent == "trend":
        if "date" in df.columns and "sales" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
            trend = df.groupby("date")["sales"].sum().to_dict()
            return {
                "type": "trend",
                "description": "Sales trend over time",
                "result": trend
            }

    return {
        "type": "unknown",
        "description": "Could not generate insight for this question",
        "result": {}
    }
