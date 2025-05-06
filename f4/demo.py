def format_cpr(cpr):
    """
    Formats a Danish CPR number to the format 000000-0000.

    Args:
        cpr (str): The CPR number as a string, either with or without a hyphen.

    Returns:
        str: The formatted CPR number, or raises a ValueError if invalid.
    """
    # Remove any existing hyphen
    cpr = cpr.replace("-", "")

    # Validate the length
    if len(cpr) != 10 or not cpr.isdigit():
        raise ValueError("Invalid CPR number. It must contain exactly 10 digits.")

    # Insert the hyphen
    return f"{cpr[:6]}-{cpr[6:]}"