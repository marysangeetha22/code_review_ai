import tempfile
import subprocess
import os

def extract_features_from_code(code: str):
    lines = code.strip().splitlines()
    loc = len(lines)

    docstring_present = 1 if '"""' in code or "'''" in code else 0

    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    indent_issues = 0
    total_warnings = 0

    try:
        result = subprocess.run(
            ["pylint", tmp_path, "--disable=all", "--enable=E,W,C,R"],
            capture_output=True,
            text=True,
            timeout=5
        )

        for line in result.stdout.splitlines():
            line_lower = line.lower()

            # Count anything that looks like a linting warning
            if ": e" in line_lower or ": w" in line_lower or ": c" in line_lower or ": r" in line_lower:
                total_warnings += 1

            # Catch parsing or indent errors
            if "parsing failed" in line_lower or "unexpected indent" in line_lower or "syntax-error" in line_lower:
                indent_issues += 1
                total_warnings += 1  # Also count it toward total

    except Exception as e:
        print(f"Error during linting: {e}")
        indent_issues = -1
        total_warnings = -1

    finally:
        os.remove(tmp_path)

    return {
        "loc": loc,
        "docstring_present": docstring_present,
        "indent_issues": indent_issues,
        "total_pylint_warnings": total_warnings
    }



if __name__ == "__main__":
    code = '''
    def greet(name):
    """Greet a person"""
    return "Hello " + name
    '''

    features = extract_features_from_code(code)
    print(features)
    # Output: {'loc': 4, 'docstring_present': 1, 'indent_issues': 0, 'total_pylint_warnings': 1}
