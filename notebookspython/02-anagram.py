def is_anagram_sort(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


def CheckPermutation(s1: str, s2: str) -> bool:
    """Return whether two lowercase strings are permutations of each other."""
    if len(s1) != len(s2):
        return False

    counts = [0] * 26

    for char in s1:
        index = ord(char) - ord("a")
        counts[index] += 1

    for char in s2:
        index = ord(char) - ord("a")
        counts[index] -= 1

    return not any(counts)


if __name__ == "__main__":
    assert is_anagram_sort("abc", "cba") is True
    assert is_anagram_sort("apple", "pale") is False
    assert CheckPermutation("abc", "cba") is True
    assert CheckPermutation("apple", "pale") is False

    print("All test cases passed ✅")
