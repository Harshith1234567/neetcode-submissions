class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nr, nc= len(board), len(board[0])
        q=deque([])
        for i in range(nr):
            for j in range(nc):
                if (i==0 or i==nr-1 or j==0 or j==nc-1) and board[i][j] == 'O':
                    q.append([i,j])


        while q:
            x,y=q.popleft()
            board[x][y] = "E"

            for a, b in [[0,1],[0,-1],[1,0],[-1,0]]:
                c,d= x+a, y+b 
                if c>=0 and c<nr and d>=0 and d<nc and board[c][d] == "O" :
                    board[c][d] = "E"
                    q.append([c,d])

        print(board)

        for i in range(nr):
            for j in range(nc):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "E":
                    board[i][j] = "O"

        #return board



