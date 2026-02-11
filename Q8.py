class Solution:
    def minJumps(self, arr):
        n = len(arr)

        # If first element is 0, we cannot move anywhere
        if arr[0] == 0:
            return -1

        # Initialization
        maxReach = arr[0]
        steps = arr[0]
        jumps = 1

        for i in range(1, n):
            # If we have reached the end
            if i == n - 1:
                return jumps

            # Update maxReach
            maxReach = max(maxReach, i + arr[i])

            # Use a step
            steps -= 1

            # If no steps left
            if steps == 0:
                jumps += 1

                # If current index is beyond maxReach, cannot move
                if i >= maxReach:
                    return -1

                # Reinitialize steps
                steps = maxReach - i

        return -1
