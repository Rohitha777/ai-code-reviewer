def generate_report(name, original_code, formatted_code, flake8_output, radon_data, score):
    report = []
    report.append(f"AI Code Review Report for {name}\n")
    report.append("="*50 + "\n\n")
    report.append("Original Code:\n")
    report.append(original_code + "\n\n")
    report.append("Formatted Code:\n")
    report.append(formatted_code + "\n\n")
    report.append("Flake8 Issues:\n")
    report.append(flake8_output or "No issues found.\n")
    report.append("\nCode Complexity (Radon):\n")
    for item in radon_data:
        report.append(f"{item['name']} (line {item['lineno']}): Complexity {item['complexity']}\n")
    report.append(f"\nCode Quality Score: {score}%\n")
    return "\n".join(report)
