class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize preMap to all empty lists
        preMap = {i:[] for i in range(numCourses)}

        # populate the preMap with the courses
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        def dfs(crs):
            # we are currently doing dfs for this course
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            # otherwise we do the visiting
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            # otherwise we got through all of them
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True