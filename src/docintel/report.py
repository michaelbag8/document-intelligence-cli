
def generate_report(
    result: dict[str, list[str | None] | None],
) -> str:
    display_names = {
        "emails": "Emails",
        "phone_numbers": "Phone Numbers",
        "money": "Money",
        "dates": "Dates",
        "hashtags": "Hashtags",
        "mentions": "Mentions",
        "ip_addresses": "IP Addresses",
        "urls": "URLs",
    }

    report = "Document Intelligence Report\n"
    report += "===========================\n\n"

    for key, values in result.items():
        display_key = display_names.get(
            key,
            key.replace("_", " ").title(),
        )
        report += f"{display_key}:\n"

        for value in values or []:
            if value is None:
                continue

            cleaned_value = value.strip()
            if not cleaned_value:
                continue

            report += f"  - {cleaned_value}\n"

        report += "\n"

    return report