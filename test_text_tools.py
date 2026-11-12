from text_tools import is_palindrome, count_words, reverse_string

def test_reverse_string():
  assert reverse_string("hello") == "olleh"

def test_count_words():
  assert count_words("I love Naduni") == 3

def test_count_words_empty():
  assert count_words("") == 0

def test_is_palindrome():
  assert is_palindrome("level") is True

def test_is_not_palindrome():
  assert is_palindrome("hello") is False
