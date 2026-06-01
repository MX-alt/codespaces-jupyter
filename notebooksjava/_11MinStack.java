import java.util.ArrayDeque;
import java.util.Deque;

public class _11MinStack {

    // 双スタック協調：_data は全要素、_min のトップは常に現在の最小値
    private final Deque<Integer> data = new ArrayDeque<>();
    private final Deque<Integer> min  = new ArrayDeque<>();

    public void push(int val) {
        data.push(val);
        if (min.isEmpty() || val <= min.peek()) {
            min.push(val);
        }
    }

    public void pop() {
        if (data.isEmpty()) throw new RuntimeException("pop from empty stack");
        int val = data.pop();
        if (val == min.peek()) {
            min.pop();
        }
    }

    public int top() {
        if (data.isEmpty()) throw new RuntimeException("top from empty stack");
        return data.peek();
    }

    public int min() {
        if (min.isEmpty()) throw new RuntimeException("min from empty stack");
        return min.peek();
    }

    public static void main(String[] args) {
        _11MinStack s = new _11MinStack();

        // 基本的な push と min
        s.push(3); s.push(5); s.push(1); s.push(2);
        assert s.min() == 1 : "min should be 1";
        assert s.top() == 2 : "top should be 2";

        // 最小値を pop した後、min が前の値に戻る
        s.pop(); // 2
        s.pop(); // 1（現在の最小値）
        assert s.min() == 3 : "min should restore to 3";
        assert s.top() == 5 : "top should be 5";

        // 重複する最小値
        s.push(3); s.push(3);
        assert s.min() == 3;
        s.pop();
        assert s.min() == 3 : "min should still be 3 after popping one duplicate";

        // 単一要素
        _11MinStack s2 = new _11MinStack();
        s2.push(42);
        assert s2.min() == 42;
        assert s2.top() == 42;

        // 空スタックの操作は例外を投げる
        _11MinStack s3 = new _11MinStack();
        try { s3.pop(); assert false : "should throw"; } catch (RuntimeException e) { /* expected */ }
        try { s3.min(); assert false : "should throw"; } catch (RuntimeException e) { /* expected */ }

        System.out.println("All test cases passed ✅");
    }
}
