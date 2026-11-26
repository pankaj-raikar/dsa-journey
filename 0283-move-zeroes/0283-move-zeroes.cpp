class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int pos=0;

        for (int x:nums){
            if (x!=0){
                nums[pos++]=x;
            }
        }

        while(pos<nums.size()){
            nums[pos++]=0;
        }
    }
};