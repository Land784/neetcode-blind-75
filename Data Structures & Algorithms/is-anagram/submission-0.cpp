#include <vector>
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> v1(26,0);
        if(s.length() != t.length()){
            return false;
        }
        for(int i = 0;i<s.length();i++){
            v1[s[i]-97]++;
            v1[t[i]-97]--;
        }
        for(int i = 0;i<v1.size();i++){
            if(v1[i]!=0){
                return false;
            }
        }
        return true;
    }
};
