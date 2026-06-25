function convertInteger(A: number, B: number): number {
    let xorResult = A ^ B;
    let count = 0;
    while (xorResult !== 0) {
        xorResult &= (xorResult - 1);
        count++;
    }
    return count;
}

console.log(convertInteger(29, 15));
console.log(convertInteger(1, 2));