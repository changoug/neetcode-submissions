from collections import deque

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cnt_dict = defaultdict(int)
        q = deque()
        for n in nums:
            if cnt_dict[n] > 0:
                return True
            q.append(n)
            cnt_dict[n] += 1
            
            if len(q) > k:
                cnt_dict[q.popleft()] -= 1

        return False

