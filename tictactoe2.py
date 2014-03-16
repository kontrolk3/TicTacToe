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
		while True:
			num_players = raw_input("How many players? ")
			if num_players != "1" and num_players != "2":
				print "Invalid number of players. Please enter 1 or 2."
			else:
				break
				
		self.print_board()
		while True:
			self.player_turn("X")
			
			if self.check_winner("X"):
				print "X wins!"
				break
			elif self.is_board_full():
				print "Tie game."
				break
			
			if num_players == "1":
				self.computer_turn()
			else:
				self.player_turn("O")
			
			if self.check_winner("O"):
				print "O wins!"
				break
				
	def player_turn(self, marker):
		while True:
			column = int(raw_input("Column: ")) - 1
			row = int(raw_input("Row: ")) - 1
			
			if column < 0 or column > 2 or row < 0 or row > 2:
				print "Out of range. Try again."
			elif self.board[row][column] != " ":
				print "Position occupied. Try again."
			else:
				break
				
		self.board[row][column] = marker
		self.print_board()
	
	def computer_turn(self):
		while True:
			rand_row = random.randint(0, 2)
			rand_column = random.randint(0, 2)
			if self.board[rand_row][rand_column] == " ":
				self.board[rand_row][rand_column] = "O"
				break
				
		self.print_board()
			
	def is_board_full(self):
		for row in self.board:
			for column in row:
				if column == " ":
					return False
		return True
		
game = TicTacToeGame()
game.play()

"""
Requirements log:
	written 3/12/14
		xCreate git repository and commit (3/16/14)
		xPush to remote repository (3/16/14)
		xError checking on input (can't be out of bounds, can't be occupied (3/16/14)
		-TDD for python?
		xChoose 1 or 2 players.  If choose one, play computer, otherwise play human (3/16/14)
	written 3/16/14
		-Refactor to clean up code
		-Better way to choose position?
		-Play unlimited games
		-Welcome message with game options
		-Enter a name for player 1 and track record within session
		-Store user name and record somewhere
		-Allow user to re-sign in as previous user and view record
"""