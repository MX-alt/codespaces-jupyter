import java.util.ArrayDeque;
import java.util.Deque;

public class _21QueueWithStacks {

    static class MyQueue {
        private final Deque<Integer> inStack = new ArrayDeque<>();
        private final Deque<Integer> outStack = new ArrayDeque<>();

        public void push(int x) {
            inStack.push(x);
        }

        public int pop() {
            peek();
            return outStack.pop();
        }

        public int peek() {
            if (outStack.isEmpty()) {
                while (!inStack.isEmpty()) {
                    outStack.push(inStack.pop());
                }
            }
            return outStack.peek();
        }

        public boolean empty() {
            return inStack.isEmpty() && outStack.isEmpty();
        }
    }

    public static void main(String[] args) {
        MyQueue queue = new MyQueue();
        queue.push(1);
        queue.push(2);

        if (queue.peek() != 1) {
            throw new AssertionError("Peek failed");
        }
        if (queue.pop() != 1) {
            throw new AssertionError("Pop failed");
        }
        if (queue.pop() != 2) {
            throw new AssertionError("Second pop failed");
        }
        if (!queue.empty()) {
            throw new AssertionError("Queue should be empty");
        }

        System.out.println("All test cases passed ✅");
    }
}
