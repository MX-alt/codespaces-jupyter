"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function convertInteger(A, B) {
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
//# sourceMappingURL=23-bit-conversion.js.map