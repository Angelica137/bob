
def bob(statement: str) -> str:
    statement = statement.strip()
    if statement == "":
        return "Fine. Be that way!"
    elif statement.isupper() and statement[-1] == "?":
        return "Calm down, I know what I'm doing!"
    elif statement[-1] == "?":
        return "Sure."
    elif statement.isupper():
        return "Whoa, chill out!"
    return "Whatever"


s = "     "
s = s.strip()
print("h" + s + "h")
