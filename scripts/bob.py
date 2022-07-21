def bob(statement: str) -> str:
    if statement[-1] == "?":
        return "Sure."
    elif statement.isupper():
        return "Whoa, chill out!"
