import subprocess
import tempfile
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import os

# Load CodeT5 model once at module level
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-base-multi-sum")  # Better variant
model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-base-multi-sum")


def get_code_explanation(code: str) -> str:
    """
    Generate a natural language explanation of the provided code using CodeT5.
    """
    task_prefix = "summarize: "
    input_text = task_prefix + code.strip()

    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)

    with torch.no_grad():
        summary_ids = model.generate(
            inputs['input_ids'],
            num_beams=4,
            length_penalty=2.0,
            max_length=128,
            early_stopping=True
        )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True).strip()

    # Fallback if output is unclear or minimal
    if not summary or "def" in summary.lower() or len(summary.split()) < 3:
        return "The explanation could not be generated. Try providing a more complete code snippet."

    return summary


def get_pylint_feedback(code: str):
    """
    Run pylint on the code and extract bugs and suggestions.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    result = subprocess.run(
        ["pylint", tmp_path, "--disable=all", "--enable=E,W,C,R"],
        capture_output=True,
        text=True
    )

    # Clean up the temp file after running pylint
    os.remove(tmp_path)

    bugs = []
    suggestions = []

    for line in result.stdout.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue

        if "[E" in line or "error" in line.lower():
            bugs.append(line)
        elif "[W" in line or "[C" in line or "[R" in line:
            suggestions.append(line)

    return bugs, suggestions


def analyze_code(code: str, language: str = "python") -> dict:
    """
    Analyze code using CodeT5 (for explanation) and Pylint (for bugs/suggestions).
    """
    if language != "python":
        return {
            "explanation": "Only Python is supported right now.",
            "bugs": [],
            "suggestions": []
        }

    try:
        explanation = get_code_explanation(code)
        bugs, suggestions = get_pylint_feedback(code)

        return {
            "explanation": explanation,
            "bugs": bugs,
            "suggestions": suggestions
        }
    except Exception as e:
        return {
            "explanation": "An error occurred while analyzing the code.",
            "bugs": [],
            "suggestions": [str(e)]
        }
