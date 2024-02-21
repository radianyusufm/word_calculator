from project import replace_word, list_word, total_word

def test_replace_word():
    assert replace_word("radian the yusuf the mahendra", 'the') == "radian  yusuf  mahendra"
    assert replace_word("am radian yusuf mahendra", 'am') == " radian yusuf mahendra"

def test_list_word():
    assert list_word("radian yusuf mahendra") == ["radian", "yusuf", "mahendra"]
    assert list_word("This is CS50") == ["This", "is", "CS50"]


def test_total_word():
    assert total_word(["radian", "radian", "yusuf", "mahendra"]) == {'radian': 2, 'yusuf': 1, 'mahendra': 1}