def bob(statement: str) -> str:
    # you still do not know if this is all caps
    if statement[-1] == "?":
        return "Sure."
    elif statement.isupper():
        return "Whoa, chill out!"
