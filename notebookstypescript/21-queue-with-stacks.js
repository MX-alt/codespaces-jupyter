"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class MyQueue {
    inStack = [];
    outStack = [];
    push(value) {
        this.inStack.push(value);
    }
    pop() {
        this.peek();
        const value = this.outStack.pop();
        if (value === undefined) {
            throw new Error("Queue is empty");
        }
        return value;
    }
    peek() {
        if (this.outStack.length === 0) {
            while (this.inStack.length > 0) {
                this.outStack.push(this.inStack.pop());
            }
        }
        const value = this.outStack[this.outStack.length - 1];
        if (value === undefined) {
            throw new Error("Queue is empty");
        }
        return value;
    }
    empty() {
        return this.inStack.length === 0 && this.outStack.length === 0;
    }
}
const queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.push(3);
console.log(queue.pop());
console.log(queue.peek());
console.log(queue.empty());
//# sourceMappingURL=21-queue-with-stacks.js.map