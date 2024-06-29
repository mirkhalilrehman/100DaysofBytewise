# 10. Boggle Game
#     - Implement a program that solves the Boggle game, given a board and a list of words.
#     - Expected output: The program should print all the words found in the Boggle board.

class Boggle:
    def __init__(self, board, words):
        self.board = board
        self.words = words
        self.result = set()
        self.rows = len(board)
        self.cols = len(board[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]
        self.trie = {}
        self._build_trie()

    def _build_trie(self):
        for word in self.words:
            node = self.trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True

    def find_words(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self._dfs(i, j, "", self.trie)
        return self.result

    def _dfs(self, i, j, prefix, node):
        if '#' in node:
            self.result.add(prefix)
        if not (0 <= i < self.rows and 0 <= j < self.cols) or self.visited[i][j] or self.board[i][j] not in node:
            return
        self.visited[i][j] = True
        self._dfs(i + 1, j, prefix + self.board[i][j], node[self.board[i][j]])
        self._dfs(i - 1, j, prefix + self.board[i][j], node[self.board[i][j]])
        self._dfs(i, j + 1, prefix + self.board[i][j], node[self.board[i][j]])
        self._dfs(i, j - 1, prefix + self.board[i][j], node[self.board[i][j]])
        self._dfs(i + 1, j + 1, prefix + self.board[i][j], node[self.board[i][j]])
        self._dfs(i + 1, j - 1, prefix + self.board[i][j], node[self.board[i][j]])
        self._dfs(i - 1, j + 1, prefix + self.board[i][j], node[self.board[i][j]])
        self._dfs(i - 1, j - 1, prefix + self.board[i][j], node[self.board[i][j]])
        self.visited[i][j] = False

board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
words = ["oath", "pea", "eat", "rain"]
boggle = Boggle(board, words)
result = boggle.find_words()
print(result)
