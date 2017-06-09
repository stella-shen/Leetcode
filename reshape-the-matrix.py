
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        raw_r = len(nums)
        raw_c = len(nums[0])
        if raw_c*raw_r < r*c:
            return nums

        flag = False
        ret = list()
        cur_append_list = list()
        for cur_list in nums:
            if flag == True:
                break
            for num in cur_list:
                cur_append_list.append(num)
                if len(cur_append_list) == c:
                    ret.append(cur_append_list)
                    if len(ret) == r:
                        flag = True
                        break
                    cur_append_list = list()
        return ret
