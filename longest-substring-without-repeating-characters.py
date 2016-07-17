
class Solution(object):
  def lengthOfLongestSubstring(self, s):
    """

    :type s: str
    :rtype: int
    """
    max_len = 0
    start = 0
    total_len = len(s)
    place = list()
    for j in range(0, 256):
      place.append(-1)
    for i in range(total_len):
      index = ord(s[i])
      if place[index] >= 0:
        cur_len = i - start
        for j in range(start, place[index]):
          cur_index = ord(s[j])
          place[cur_index] = -1
        start = place[index] + 1
        if cur_len > max_len:
          max_len = cur_len
      place[index] = i
    if total_len - start > max_len:
      max_len = total_len - start 
    if start == 0:
      max_len = total_len
    return max_len

if __name__ == '__main__':
  sol = Solution()
  s = 'aab'
  print sol.lengthOfLongestSubstring(s)

