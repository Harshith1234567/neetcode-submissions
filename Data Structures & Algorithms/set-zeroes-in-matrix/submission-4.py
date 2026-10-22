class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        l,t=False,False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 and matrix[i][j]==0:
                    t=True
                    continue
                if j==0 and matrix[i][j]==0:
                    l=True
                    continue

                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        # print(matrix,l,t)



        for i in range(len(matrix)):

            if i==0 :
                continue

            if matrix[i][0]==0:

                for j in range(1,len(matrix[0])):
                    matrix[i][j]=0

        for j in range(len(matrix[0])):

            if j==0 :
                continue

            if matrix[0][j]==0:

                for i in range(1,len(matrix)):
                    matrix[i][j]=0

        if matrix[0][0]==0:
            for j in range(1,len(matrix[0])):
                matrix[0][j]=0
            for i in range(1,len(matrix)):
                matrix[i][0]=0

        if t:
            for j in range(0,len(matrix[0])):
                matrix[0][j]=0
        if l:
            for i in range(0,len(matrix)):
                matrix[i][0]=0



        


                


                        
        