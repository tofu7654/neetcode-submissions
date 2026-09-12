class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if not stack:
                # append the value and the index
                stack.append([temperatures[i], i])
                continue
            
            # if stack i is greater than the top of the stack
            while stack and temperatures[i] > stack[-1][0]:
                # pop the stack
                val, index = stack.pop()
                # update the output list
                res[index] = i - index

            # append current value to stack
            stack.append([temperatures[i], i])

        while stack:
            # pop the stack
            val, index = stack.pop()

            # update the output list
            res[index] = 0
        
        return res



            
