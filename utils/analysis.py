import subprocess
import tempfile
import radon.complexity as cc
import black

def run_flake8(code):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name
    result = subprocess.run(["flake8", tmp_path], capture_output=True, text=True)
    return result.stdout.strip()

def run_black(code):
    try:
        formatted = black.format_str(code, mode=black.FileMode())
        return formatted
    except Exception as e:
        return f"Black formatting failed: {str(e)}"

def run_radon(code):
    analyzed = cc.cc_visit(code)
    return [
        {"name": item.name, "lineno": item.lineno, "complexity": item.complexity}
        for item in analyzed
    ]
