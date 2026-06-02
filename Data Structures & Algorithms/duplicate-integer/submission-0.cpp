#include <set>
#include <vector>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> set1;
        for(int i = 0;i< nums.size();i++){
            auto result = set1.insert(nums[i]);
            if(!result.second){
                return true;
            }
        }
        return false;
    }
};