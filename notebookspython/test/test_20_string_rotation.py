import pytest

from helpers import load_py

mod = load_py("20-string-rotation.py", "string_rotation")

@pytest.mark.parametrize(
    ("s1", "s2", "expected"),
    [
        ("waterbottle", "erbottlewat", True),
        ("abcde", "cdeab", True),
        ("abcde", "abced", False),
        ("a", "a", True),
        ("a", "aa", False),
        ("", "", True),
        ("", "a", False),
    ],
)
def test_is_fliped_string(s1, s2, expected):
    assert mod.is_fliped_string(s1, s2) is expected


def test_invalid_input_type():
    with pytest.raises(TypeError):
        mod.is_fliped_string(None, "abc")
