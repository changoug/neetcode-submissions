class Node:

    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = Node()
        for word in words:
            curr = tree
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node()
                
                curr = curr.children[c]
            curr.word = True

        R = len(board)
        C = len(board[0])
        res = set()
    
        def dfs(node, r, c, s):

            if min(r, c) < 0 or r >= R or c >= C:
                return None

            curr = board[r][c]

            if curr == '*' or curr not in node.children:
                return None 

            temp = curr
            board[r][c] = '*'

            curr_s = s + curr

            if node.children[curr].word:
                res.add(curr_s)
            
            dfs(node.children[curr], r - 1, c, curr_s)
            dfs(node.children[curr], r + 1, c, curr_s)
            dfs(node.children[curr], r, c - 1, curr_s)
            dfs(node.children[curr], r, c + 1, curr_s)

            board[r][c] = temp

        for r in range(R):
            for c in range(C):
                dfs(tree, r, c, '')

        return list(res)

        