def format_field(attribute):
    if type(attribute) == float:
        return f"{attribute:.1f}"
    else:
        return f"{attribute}"
