import subprocess
import tempfile
import google.generativeai as genai
import dotenv
import os

dotenv.load_dotenv()
# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def get_code_explanation(code: str) -> str:
    # for m in genai.list_models():
    #     print(m.name)
    prompt = f"""Explain the following Python function in clear, beginner-friendly English:

                ```python
                {code}
                ```"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini error: {str(e)}"


# def get_code_explanation(code: str) -> str:
#     """
#     Generates a natural language explanation of the given code using CodeT5.
#     """
#     input_text = f"summarize: {code.strip()[:512]}"
#     inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)

#     with torch.no_grad():
#         output_ids = model.generate(
#             inputs['input_ids'],
#             num_beams=4,
#             length_penalty=2.0,
#             max_length=128,
#             early_stopping=True
#         )

#     summary = tokenizer.decode(output_ids[0], skip_special_tokens=True)
#     return summary


def get_pylint_feedback(code: str):
    """
    Runs pylint on the given code and returns errors and suggestions.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    result = subprocess.run(
        ["pylint", tmp_path, "--disable=all", "--enable=E,W,C,R"],
        capture_output=True,
        text=True
    )

    suggestions = []
    bugs = []

    for line in result.stdout.splitlines():
        line_lower = line.lower()
        cleaned = line.strip()
        if "parsing failed" in line_lower or "unexpected indent" in line_lower or "syntax-error" in line_lower:
            if ":" in cleaned:
                cleaned = cleaned.split(":")[-1]
            bugs.append(cleaned.strip())
        elif ": w" in line_lower or ": c" in line_lower or ": r" in line_lower:
            if ":" in cleaned:
                cleaned = cleaned.split(":")[-1]
            suggestions.append(cleaned.strip())
        elif ": e" in line_lower:
            if ":" in cleaned:
                cleaned = cleaned.split(":")[-1]
            bugs.append(cleaned.strip())

    return bugs, suggestions
