def detect_intent(question: str) -> str:
    q = question.lower()

    if any(word in q for word in ["trend", "over time", "growth", "change"]):
        return "trend"

    if any(word in q for word in ["compare", "vs", "versus", "difference"]):
        return "comparison"

    if any(word in q for word in ["average", "mean", "total", "sum", "count"]):
        return "summary"

    if any(word in q for word in ["by", "group", "per"]):
        return "aggregation"

    return "unknown"
