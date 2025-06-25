import joblib
from pathlib import Path

# existing functions...
from .extract_features import extract_features_from_code
from .code_t5_summary import get_code_explanation, get_pylint_feedback 

# Load model once
model_path = Path(__file__).resolve().parent / "code_quality_model.pkl"
ml_model = joblib.load(model_path)


def analyze_code(code, language="python"):
    explanation = get_code_explanation(code) if language == "python" else "Explanation not available"
    bugs, suggestions = get_pylint_feedback(code) if language == "python" else ([], [])
    

    features = extract_features_from_code(code)
    feature_vector = [[
        features["loc"],
        features["docstring_present"],
        features["indent_issues"],
        features["total_pylint_warnings"]
    ]]

    score = ml_model.predict(feature_vector)[0]

    return {
        "explanation": explanation,
        "bugs": bugs,
        "suggestions": suggestions,
        "score": round(score, 2)
    }
