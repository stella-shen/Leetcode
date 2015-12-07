#include <iostream>
#include <vector>
 
 using namespace std;
 
vector<int> twoSum(vector<int>& nums, int target) {
  int index1 = 0, index2 = 0;
  bool find = false;
  for(int i = 0; i < nums.size(); i++) {
      for(int j = i + 1; j < nums.size(); j++) {
          if(nums[i] + nums[j] == target) {
              index1 = i + 1;
              index2 = j + 1;
              find = true;
              break;
          }
      }
      if(find == true) {
          break;
      }
  }
  vector<int> res;
  res.push_back(index1);
  res.push_back(index2);
  return res;
}

int main() {
	vector<int> nums, res;
	nums.push_back(3);
	nums.push_back(2);
	nums.push_back(4);
	int target = 6;
	res = twoSum(nums, target);
	for(int i = 0; i < res.size(); i++) {
		printf("%d\n", res[i]);
	}
	return 0;
}
 