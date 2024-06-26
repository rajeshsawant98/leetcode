class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        int fill = m + n - 1;

        while (m > 0 && n > 0) {
            if (nums1[m - 1] <= nums2[n - 1]) {
                nums1[fill] = nums2[n - 1];
                n--;
            }

            else {
                nums1[fill] = nums1[m - 1];
                m--;
            }

            fill--;
        }

        while (n > 0) {
            nums1[fill] = nums2[n - 1];
            n--;
            fill--;
        }

    }
}