from scripts.bob import bob


def test_input_is_question():
    assert bob("some question?") == "Sure."


def test_input_is_yell():
    assert bob("IS YELLING") == "Whoa, chill out!"


def test_question_is_yelled():
    assert bob("YELLING QUESTION?") == "Calm down, I know what I'm doing!"


def test_input_empty():
    assert bob("") == "Fine. Be that way!"


def test_any_other():
    assert bob("No") == "Whatever"


def test_a_string_of_spaces():
    assert bob("     ") == "Fine. Be that way!"


def test_case_1_spaces_at_end():
    assert bob("wtf?   ")
