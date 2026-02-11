class Solution:
    def kthSmallest(self, arr, k):
        freq = [0] * (100001)

        # freq count 
        for num in arr:
            freq[num] += 1

        count = 0
        for i in range(100001):
            count += freq[i]
            if count >= k:
                return i
