import random

class TicTacToeGame(object):
	
	def __init__(self):
		self.build_board()

	def build_board(self):
		board = []
		for x in range(3):
			board.append([" "] * 3)
		self.board = board

	def print_board(self):
		print "-------------"
		for row in self.board:
			for column in row[:-1]:
				print "| %s" % column,
			else:
				print "| %s |" % row[-1]
			print "-------------"
		
	def check_winner(self, player):
		if self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player:
			return True
		if self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player:
			return True
		if self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player:
			return True
		if self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player:
			return True
		if self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player:
			return True
		if self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player:
			return True
		if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
			return True
		if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
			return True
		return False
		
	def play(self):
		self.print_board()
		for i in range(9):
			column = int(raw_input("Column: ")) - 1
			row = int(raw_input("Row: ")) - 1
			self.board[row][column] = "X"
			
			while True:
				rand_row = random.randint(0, 2)
				rand_column = random.randint(0, 2)
				if self.board[rand_row][rand_column] == " ":
					self.board[rand_row][rand_column] = "O"
					break
					
			self.print_board()
			
			if self.check_winner("X"):
				print "X wins!"
				break
				
			if self.check_winner("O"):
				print "O wins!"
				break
			
game = TicTacToeGame()
game.play()

"""Next steps:
	-Create git repository and commit
	-Error checking on input (can't be out of bounds, can't be occupied
	-TDD for python?
	-Choose 1 or 2 players.  If choose one, play computer, otherwise play human