class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> nums = new HashMap<>();
        for (int num : arr) {
            if (nums.containsKey(num)) {
                nums.put(num, nums.get(num)+1);
            }
            else {
                nums.put(num, 1);
            }
        }
        HashSet<Integer> vals = new HashSet<Integer>();
        vals.addAll(nums.values());
        // System.out.println(vals);
        if (vals.size() == nums.size()) {
            return true;
        }
        return false;
    }
}