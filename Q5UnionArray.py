class Solution:    
    def findUnion(self, a, b):
        freq = [0] * 100001
        result = []

        # process array a
        for x in a:
            if freq[x] == 0:
                freq[x] = 1
                result.append(x)

        # process array b
        for x in b:
            if freq[x] == 0:
                freq[x] = 1
                result.append(x)

        return result
