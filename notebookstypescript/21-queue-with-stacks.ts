class MyQueue<T> {
    private inStack: T[] = [];
    private outStack: T[] = [];

    push(value: T): void {
        this.inStack.push(value);
    }

    pop(): T {
        this.peek();
        const value = this.outStack.pop();
        if (value === undefined) {
            throw new Error("Queue is empty");
        }
        return value;
    }

    peek(): T {
        if (this.outStack.length === 0) {
            while (this.inStack.length > 0) {
                this.outStack.push(this.inStack.pop() as T);
            }
        }

        const value = this.outStack[this.outStack.length - 1];
        if (value === undefined) {
            throw new Error("Queue is empty");
        }
        return value;
    }

    empty(): boolean {
        return this.inStack.length === 0 && this.outStack.length === 0;
    }
}

const queue = new MyQueue<number>();
queue.push(1);
queue.push(2);
queue.push(3);

console.log(queue.pop());
console.log(queue.peek());
console.log(queue.empty());
