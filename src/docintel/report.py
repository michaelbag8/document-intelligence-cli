def generate_report(result):
    report = "Document Intelligence Report\n"
    report += "===========================\n\n"

    for key, values in result.items():
        display_key = key.replace("_", " ").title()
        report += f"{display_key}:\n"

        for value in values or []:
            report += f"  - {value}\n"

        report += "\n"

    return report