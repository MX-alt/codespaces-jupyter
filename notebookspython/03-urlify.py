class Solution:
    def replaceSpaces(self, chars: str, true_length: int) -> str:
        """Replace spaces in the true string section with %20."""
        s_list = list(chars)
        space_count = 0

        for i in range(true_length):
            if chars[i] == " ":
                space_count += 1

        new_index = true_length + space_count * 2

        for i in range(true_length - 1, -1, -1):
            if s_list[i] == " ":
                s_list[new_index - 1] = "0"
                s_list[new_index - 2] = "2"
                s_list[new_index - 3] = "%"
                new_index -= 3
            else:
                s_list[new_index - 1] = s_list[i]
                new_index -= 1

        return "".join(s_list).strip()


def urlify_pythonic(s: str, true_length: int) -> str:
    return s[:true_length].replace(" ", "%20")


if __name__ == "__main__":
    sol = Solution()

    assert sol.replaceSpaces("Mr John Smith    ", 13) == "Mr%20John%20Smith"
    assert sol.replaceSpaces("a b  ", 3) == "a%20b"
    assert sol.replaceSpaces("abc", 3) == "abc"
    assert urlify_pythonic("Mr John Smith    ", 13) == "Mr%20John%20Smith"

    print("All test cases passed ✅")
