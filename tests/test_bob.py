from scripts.bob import bob


def test_input_is_question():
    assert bob("some question?") == "Sure."


def test_input_is_yell():
    assert bob("IS YELLING") == "Whoa, chill out!"
