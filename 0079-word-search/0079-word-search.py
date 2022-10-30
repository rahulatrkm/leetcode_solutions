class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r,c = len(board), len(board[0])
        def dfs(visited,i,j,idx):
            if idx == len(word):
                return True
            if 0 <= i < r and 0 <= j < c and not visited[i][j]:
                visited[i][j] = True
                if board[i][j] == word[idx]:
                    if dfs(visited,i+1,j,idx+1):
                        return True
                    if dfs(visited,i-1,j,idx+1):
                        return True
                    if dfs(visited,i,j+1,idx+1):
                        return True
                    if dfs(visited,i,j-1,idx+1):
                        return True
                visited[i][j] = False
            return False
                
        visited = [[False]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if dfs(visited, i,j, 0):
                        return True
        return False