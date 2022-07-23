
def bob(statement: str) -> str:
    statement = statement.strip()
    if statement == "":
        return "Fine. Be that way!"
    elif statement.isupper() and statement.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif statement.endswith("?"):
        return "Sure."
    elif statement.isupper():
        return "Whoa, chill out!"
    return "Whatever."
