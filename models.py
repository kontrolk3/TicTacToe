class TicTacToeBoard(object):
	
	def __init__(self):
		self.clear()

	def clear(self):
		board = []
		for x in range(3):
			board.append([" "] * 3)
		self.board = board
		
	def has_won(self, token):
		if self.board[0][0] == token and self.board[0][1] == token and self.board[0][2] == token:
			return True
		if self.board[1][0] == token and self.board[1][1] == token and self.board[1][2] == token:
			return True
		if self.board[2][0] == token and self.board[2][1] == token and self.board[2][2] == token:
			return True
		if self.board[0][0] == token and self.board[1][0] == token and self.board[2][0] == token:
			return True
		if self.board[0][1] == token and self.board[1][1] == token and self.board[2][1] == token:
			return True
		if self.board[0][2] == token and self.board[1][2] == token and self.board[2][2] == token:
			return True
		if self.board[0][0] == token and self.board[1][1] == token and self.board[2][2] == token:
			return True
		if self.board[0][2] == token and self.board[1][1] == token and self.board[2][0] == token:
			return True
		return False
			
	def set_value(self, row, column, token):
		if self.board[row][column] != " ":
			return False
		else:
			self.board[row][column] = token
			return True
			
	def is_open(self, row, column):
		return self.board[row][column] == " "
		
	def value_at(self, row, column):
		return self.board[row][column]
		
	def is_full(self):
		for row in self.board:
			for column in row:
				if column == " ":
					return False
		return True
		
	def get_board(self):
		return self.board