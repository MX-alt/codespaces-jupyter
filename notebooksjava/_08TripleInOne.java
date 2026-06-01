public class _08TripleInOne {

    private final int stackSize;
    private final int[] array;
    private final int[] sizes;

    public _08TripleInOne(int stackSize) {
        this.stackSize = stackSize;
        this.array = new int[stackSize * 3];
        this.sizes = new int[3];
    }

    public void push(int stackNum, int value) {
        if (sizes[stackNum] == stackSize) {
            System.out.println("❌ Stack " + stackNum + " is full, cannot push " + value);
            return;
        }
        int absIndex = stackNum * stackSize + sizes[stackNum];
        array[absIndex] = value;
        sizes[stackNum]++;
    }

    public int pop(int stackNum) {
        if (sizes[stackNum] == 0) {
            System.out.println("⚠️ Stack " + stackNum + " is empty, cannot pop");
            return -1;
        }
        sizes[stackNum]--;
        int absIndex = stackNum * stackSize + sizes[stackNum];
        return array[absIndex];
    }

    public int peek(int stackNum) {
        if (sizes[stackNum] == 0) {
            System.out.println("👀 Stack " + stackNum + " is empty");
            return -1;
        }
        int absIndex = stackNum * stackSize + (sizes[stackNum] - 1);
        return array[absIndex];
    }

    public boolean isEmpty(int stackNum) {
        return sizes[stackNum] == 0;
    }

    public static void main(String[] args) {
        // stackSize = 2 の三合一スタック
        _08TripleInOne obj = new _08TripleInOne(2);

        // push / peek / pop の基本動作
        obj.push(0, 10);
        obj.push(0, 20);
        assert obj.peek(0) == 20 : "peek should be 20";
        assert obj.pop(0)  == 20 : "pop should return 20";
        assert obj.peek(0) == 10 : "peek should be 10 after pop";
        assert !obj.isEmpty(0)   : "stack 0 should not be empty";
        obj.pop(0);
        assert obj.isEmpty(0)    : "stack 0 should be empty";

        // 満杯時の push は無視される
        obj.push(1, 1);
        obj.push(1, 2);
        obj.push(1, 3); // 無視
        assert obj.peek(1) == 2 : "stack 1 top should still be 2";

        // 空スタックの pop は -1 を返す
        assert obj.pop(2) == -1 : "pop from empty stack should return -1";

        // 各スタックが独立していることを確認
        obj.push(2, 99);
        assert obj.peek(2) == 99 : "stack 2 should have 99";
        assert obj.peek(1) == 2  : "stack 1 should be unaffected";

        System.out.println("All test cases passed ✅");
    }
}
