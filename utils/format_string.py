def format_field(attribute):
    if type(attribute) is float:
        return f"{attribute:.1f}"
    else:
        return f"{attribute}"
