package dp;

/**
 * Created by 申卓 on 2017/8/29.
 */
public class MaximumSubarray {

    /**
     * 使用O(1)计算i => j 的和
     * 遍历 i => 0 - n
     * j => i - n
     * 取最大值
     * 时间复杂度 O(n^2) 超时
     *
     * @param nums
     * @return
     */
    public int maxSubArrayI(int[] nums) {
        init(nums);
        int n = nums.length;
        int sum = Integer.MIN_VALUE;
        int temp = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                temp = sumRange(i, j, nums);
                sum = sum > temp ? sum : temp;
            }
        }
        return sum;
    }

    private int sumRange(int i, int j, int[] ints) {
        return i == 0 ? ints[j] : ints[j] - ints[i - 1];
    }

    private void init(int[] nums) {
        int n = nums.length;
        if (n < 1) return;
        for (int i = 1; i < n; i++) {
            nums[i] += nums[i - 1];
        }
    }

    public static void main(String[] args) {

    }
}
