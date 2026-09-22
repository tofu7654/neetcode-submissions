class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize these courses to empty lists
        preMap = {i:[] for i in range(numCourses) }

        # populate the preMap
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        

        # now we have to do the dfs
        visitSet = set()
        def dfs(crs):
            # if there is a loop
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                # if we found a loop
                if not dfs(pre): return False

            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


