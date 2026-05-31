import importlib.util
import pathlib
import pytest

# Load the module directly from its file path so no package structure is needed
_src = pathlib.Path(__file__).parent / "../16-bit_flip_max_consecutive_ones.py"
_spec = importlib.util.spec_from_file_location("bit_flip", _src)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
sol = _mod.Solution()

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestReverseBits:

    def test_example_1775(self):
        # 1775 = 0b...11011101111, flipping one 0 yields a run of 8
        assert sol.reverseBits(1775) == 8

    def test_example_7(self):
        # 7 = 0b...0111, flipping the adjacent 0 yields a run of 4
        assert sol.reverseBits(7) == 4

    def test_all_ones_negative_one(self):
        # -1 in two's complement is 32 ones; guard clause returns 32 immediately
        assert sol.reverseBits(-1) == 32

    def test_thirty_one_ones_negative_two(self):
        # -2 = 0b1...10 (31 ones then a 0); flipping the trailing 0 gives 32
        assert sol.reverseBits(-2) == 32

    def test_negative_three(self):
        # -3 = 0b1...101; the two groups of ones are separated by a single 0,
        # so flipping that 0 merges them into a run of 32
        assert sol.reverseBits(-3) == 32

    def test_zero(self):
        # 0 = 32 zeros; flipping any one bit produces a run of exactly 1
        assert sol.reverseBits(0) == 1

    def test_single_bit_set(self):
        # 1 = 0b...0001; flipping the adjacent 0 gives a run of 2
        assert sol.reverseBits(1) == 2

    def test_alternating_bits(self):
        # 0b...010101 — every 1 is surrounded by 0s; best flip merges two 1s
        # separated by one 0, yielding a run of 3
        assert sol.reverseBits(0x55555555) == 3

    def test_two_adjacent_ones(self):
        # 3 = 0b...011; flipping the next 0 gives a run of 3
        assert sol.reverseBits(3) == 3

    def test_large_positive(self):
        # 0x7FFFFFFF = 31 ones followed by a leading 0;
        # flipping that 0 gives a run of 32
        assert sol.reverseBits(0x7FFFFFFF) == 32
