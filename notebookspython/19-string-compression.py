def compress_string(s: str) -> str:
    """Compress a string by replacing repeated characters with counts.

    If the compressed string is not shorter than the original, return the
    original string.
    """
    if not s:
        return s

    compressed_parts = []
    count = 1
    compressed_length = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            part = f"{s[i - 1]}{count}"
            compressed_parts.append(part)
            compressed_length += len(part)
            if compressed_length >= len(s):
                return s
            count = 1

    last_part = f"{s[-1]}{count}"
    compressed_parts.append(last_part)
    result = "".join(compressed_parts)

    return result if len(result) < len(s) else s


if __name__ == "__main__":
    assert compress_string("aabcccccaaa") == "a2b1c5a3"
    assert compress_string("abcd") == "abcd"
    print("All built-in tests passed.")