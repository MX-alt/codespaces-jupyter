"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function setZeroes(matrix) {
    if (matrix.length === 0) {
        return;
    }
    const rows = matrix.length;
    const cols = matrix[0].length;
    const firstRowHasZero = matrix[0].some((value) => value === 0);
    const firstColHasZero = matrix.some((row) => row[0] === 0);
    for (let i = 1; i < rows; i++) {
        for (let j = 1; j < cols; j++) {
            if (matrix[i][j] === 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    for (let i = 1; i < rows; i++) {
        for (let j = 1; j < cols; j++) {
            if (matrix[i][0] === 0 || matrix[0][j] === 0) {
                matrix[i][j] = 0;
            }
        }
    }
    if (firstRowHasZero) {
        for (let j = 0; j < cols; j++) {
            matrix[0][j] = 0;
        }
    }
    if (firstColHasZero) {
        for (let i = 0; i < rows; i++) {
            matrix[i][0] = 0;
        }
    }
}
const sampleMatrix = [
    [1, 0, 3],
    [4, 5, 6],
    [7, 8, 0],
];
setZeroes(sampleMatrix);
console.log(sampleMatrix);
//# sourceMappingURL=25-set-matrix-zeroes.js.map