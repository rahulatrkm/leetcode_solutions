class Solution {
    public int trap(int[] height) {
        int n=height.length;
        int leftMax[]=new int[n];
        leftMax[0]=height[0];
        // calculating left max  boundary
        for(int i=1;i<n;i++){
            leftMax[i]=Math.max(leftMax[i-1], height[i]);
        }
        int rightMax[]=new int[n];
        rightMax[n-1]=height[n-1];
        // calculating right max boundary
        for(int i=n-2;i>=0;i--){
            rightMax[i]=Math.max(rightMax[i+1],height[i]);
        }
        int trappedWater=0;
        // calculating trapped water
        for(int i=0;i<n;i++){
            int waterLevel= Math.min(rightMax[i],leftMax[i]);
            trappedWater += waterLevel-height[i];
        }
        return trappedWater;
    }
}
