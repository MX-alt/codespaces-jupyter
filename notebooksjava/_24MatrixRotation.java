public class _24MatrixRotation {

    public void rotate(int[][] matrix) {
        int n = matrix.length;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int left = 0, right = n - 1; left < right; left++, right--) {
                int temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;
            }
        }
    }

    public static void main(String[] args) {
        _24MatrixRotation sol = new _24MatrixRotation();

        int[][] matrix = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };
        sol.rotate(matrix);
        int[][] expected = {
                {7, 4, 1},
                {8, 5, 2},
                {9, 6, 3}
        };
        assert java.util.Arrays.deepEquals(matrix, expected) : "case 1 failed";

        int[][] matrix2 = {{1}};
        sol.rotate(matrix2);
        assert java.util.Arrays.deepEquals(matrix2, new int[][]{{1}}) : "case 2 failed";

        System.out.println("All test cases passed ✅");
    }
}
