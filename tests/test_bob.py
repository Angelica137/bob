from scripts.bob import bob


def test_input_is_question():
    assert bob("some question?") == "Sure."
