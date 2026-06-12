def is_fliped_string(s1: str, s2: str) -> bool:
    """Return True if s2 is a rotation of s1."""
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Inputs must be strings.")

    if len(s1) != len(s2):
        return False

    if not s1:
        return True

    return s2 in (s1 + s1)


if __name__ == "__main__":
    assert is_fliped_string("waterbottle", "erbottlewat") is True
    assert is_fliped_string("abcde", "cdeab") is True
    assert is_fliped_string("abcde", "abced") is False
    assert is_fliped_string("", "") is True
    print("All built-in tests passed.")