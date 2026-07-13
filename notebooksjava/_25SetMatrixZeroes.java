public class _25SetMatrixZeroes {

    public void setZeroes(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return;
        }

        int rows = matrix.length;
        int cols = matrix[0].length;
        boolean firstRowHasZero = false;
        boolean firstColHasZero = false;

        for (int j = 0; j < cols; j++) {
            if (matrix[0][j] == 0) {
                firstRowHasZero = true;
                break;
            }
        }

        for (int i = 0; i < rows; i++) {
            if (matrix[i][0] == 0) {
                firstColHasZero = true;
                break;
            }
        }

        for (int i = 1; i < rows; i++) {
            for (int j = 1; j < cols; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < rows; i++) {
            for (int j = 1; j < cols; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        if (firstRowHasZero) {
            for (int j = 0; j < cols; j++) {
                matrix[0][j] = 0;
            }
        }

        if (firstColHasZero) {
            for (int i = 0; i < rows; i++) {
                matrix[i][0] = 0;
            }
        }
    }

    public static void main(String[] args) {
        _25SetMatrixZeroes sol = new _25SetMatrixZeroes();

        int[][] matrix = {
                {1, 1, 1},
                {1, 0, 1},
                {1, 1, 1}
        };
        sol.setZeroes(matrix);
        int[][] expected = {
                {1, 0, 1},
                {0, 0, 0},
                {1, 0, 1}
        };
        assert java.util.Arrays.deepEquals(matrix, expected) : "case 1 failed";

        int[][] matrix2 = {
                {0, 1, 2},
                {3, 4, 5}
        };
        sol.setZeroes(matrix2);
        int[][] expected2 = {
                {0, 0, 0},
                {0, 0, 0}
        };
        assert java.util.Arrays.deepEquals(matrix2, expected2) : "case 2 failed";

        System.out.println("All test cases passed ✅");
    }
}
