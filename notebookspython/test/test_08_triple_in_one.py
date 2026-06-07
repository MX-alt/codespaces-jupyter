from helpers import load_py


mod = load_py("08-triple_in_one.py", "triple_in_one")


def test_triple_in_one_push_peek_pop(capsys):
    stack = mod.TripleInOne(2)

    assert "空" in stack.isEmpty(0)
    assert "[10]" in stack.push(0, 10)
    assert "[20]" in stack.push(0, 20)
    assert "満杯" in stack.push(0, 30)
    assert stack.sizes[0] == 2
    assert "[20]" in stack.peek(0)
    assert "[20]" in stack.pop(0)
    assert "[10]" in stack.pop(0)
    assert "空" in stack.pop(0)

    capsys.readouterr()


def test_three_stacks_are_independent(capsys):
    stack = mod.TripleInOne(1)

    stack.push(0, 1)
    stack.push(1, 2)
    stack.push(2, 3)

    assert stack.array == [1, 2, 3]
    assert "[1]" in stack.peek(0)
    assert "[2]" in stack.peek(1)
    assert "[3]" in stack.peek(2)

    capsys.readouterr()
