package dp;

/**
 * Created by 申卓 on 2017/8/29.
 */
public class NumArray {
    private int[] nums;
    private int[] sums;

    public NumArray(int[] nums) {
        this.nums = nums;
        int n = nums.length;
        sums = new int[n];
        if (n < 1) return;
        sums[0] = this.nums[0];
        for (int i = 1; i < nums.length; i++) {
            sums[i] += sums[i - 1] + nums[i];
        }
    }

    public int sumRange(int i, int j) {
        if (i == 0)
            return sums[j];
        return sums[j] - sums[i - 1];
    }

    public static void main(String[] args) {

        int[] arr = {1,2,3,4,5};
        int[] arr1 = {};

        NumArray numArray = new NumArray(arr1);
        System.out.println(numArray.sumRange(0,0));
    }
}
/**
 * 改进
 *      1. sumRange方法中
 *          return i==0?sum[j]:sums[j]-sums[i-1]
 *
 *      2. 直接在本地更改，无需new一个新数组
 *
 */