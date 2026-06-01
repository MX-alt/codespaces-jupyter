import java.util.Arrays;

public class _15MergeInPlace {

    // 後ろから書き込むことで上書きを回避する。nums1 の末尾 n スロットは 0 埋め
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;

        while (i >= 0 && j >= 0) {
            if (nums1[i] >= nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }

        // nums2 に残った要素をコピー（nums1 の残りはすでに正位置）
        while (j >= 0) {
            nums1[k--] = nums2[j--];
        }
    }

    public static void main(String[] args) {
        _15MergeInPlace sol = new _15MergeInPlace();

        // Case 1: 標準マージ
        int[] a = {1, 3, 5, 0, 0, 0};
        sol.merge(a, 3, new int[]{2, 4, 6}, 3);
        assert Arrays.equals(a, new int[]{1, 2, 3, 4, 5, 6}) : "case 1 failed";

        // Case 2: nums2 が空 → nums1 変化なし
        a = new int[]{1, 2, 3};
        sol.merge(a, 3, new int[]{}, 0);
        assert Arrays.equals(a, new int[]{1, 2, 3}) : "case 2 failed";

        // Case 3: nums1 の有効要素が空 → 結果は nums2
        a = new int[]{0, 0, 0};
        sol.merge(a, 0, new int[]{1, 2, 3}, 3);
        assert Arrays.equals(a, new int[]{1, 2, 3}) : "case 3 failed";

        // Case 4: nums2 の全要素が nums1 より小さい
        a = new int[]{4, 5, 6, 0, 0, 0};
        sol.merge(a, 3, new int[]{1, 2, 3}, 3);
        assert Arrays.equals(a, new int[]{1, 2, 3, 4, 5, 6}) : "case 4 failed";

        // Case 5: 重複値あり
        a = new int[]{1, 2, 2, 0, 0};
        sol.merge(a, 3, new int[]{2, 3}, 2);
        assert Arrays.equals(a, new int[]{1, 2, 2, 2, 3}) : "case 5 failed";

        // Case 6: 単一要素同士
        a = new int[]{2, 0};
        sol.merge(a, 1, new int[]{1}, 1);
        assert Arrays.equals(a, new int[]{1, 2}) : "case 6 failed";

        System.out.println("All test cases passed ✅");
    }
}
