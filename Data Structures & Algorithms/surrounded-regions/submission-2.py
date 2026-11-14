import copy

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        res=[['X' for _ in range(len(board[0]))] for a in range(len(board))]
        q=deque([])
        for c in range(len(board[0])):
            if board[0][c]=='O':
                res[0][c]='O'
                q.append([0,c])

        for r in range(len(board)):
            if board[r][0]=='O':
                res[r][0]='O'
                q.append([r,0])
        
        for c in range(len(board[0])):
            if board[-1][c]=='O':
                res[-1][c]='O'
                q.append([len(board)-1,c])

        for r in range(len(board)):
            if board[r][-1]=='O':
                res[r][-1]='O'
                q.append([r,len(board[0])-1])
        # print(res)
        # print(q)
        while q:
            r,c = q.popleft()

            for a,b in [[0,1],[0,-1],[1,0],[-1,0]]:
                x=r+a
                y=c+b
                if x<0 or y<0 or x>=len(board) or y>=len(board[0]) or res[x][y]=='O' or board[x][y]=='X':
                    continue

                res[x][y]='O'

                q.append([x,y])

        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = res[r][c]

