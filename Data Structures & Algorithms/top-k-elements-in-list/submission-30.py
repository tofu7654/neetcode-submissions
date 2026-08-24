class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []

        for i, n in enumerate(nums):
            # get frequencies of each character
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            # put the values in the array with the freq as the index
            freq[c].append(n)

        # iterate from the back
        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                res.append(v)

                if len(res) == k:
                    return res

        return


        