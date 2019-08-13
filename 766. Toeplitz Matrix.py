class Solution(object):
    def isToeplitzMatrix(self, matrix):
        M=len(matrix)
        N=len(matrix[0])
        #y=x+M
        for m in range(M-1,-1,-1):
            v=matrix[m][0]
            for x in range(0,M):
                if x+m < M and x < N :
                    #print(i,' ', i+m)
                    if v != matrix [x+m][x]:
                        return False
        # x=y+N
        for n in range(N-1,0,-1):
            v = matrix[0][n]
            for y in range(0,N):
                if y+n < N and y < M:
                    #print(i+n,' ', i)
                    if v != matrix[y][y+n]:
                        return False
        return True

sln=Solution()
assert True==sln.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
assert False==sln.isToeplitzMatrix([[1,2],[2,2]])
assert True==sln.isToeplitzMatrix([[65,98,57]])

