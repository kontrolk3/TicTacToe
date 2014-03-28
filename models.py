import random

class TicTacToeBoard(object):
	
	def __init__(self):
		self.clear()

	def clear(self):
		board = []
		for x in range(3):
			board.append([" "] * 3)
		self.board = board

	def display(self):
		print "-------------"
		for row in self.board:
			for column in row[:-1]:
				print "| %s" % column,
			else:
				print "| %s |" % row[-1]
			print "-------------"
		
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
		
	def is_full(self):
		for row in self.board:
			for column in row:
				if column == " ":
					return False
		return True
	
"""
Requirements log:
	written 3/12/14
		xCreate git repository and commit (3/16/14)
		xPush to remote repository (3/16/14)
		xError checking on input (can't be out of bounds, can't be occupied (3/16/14)
		-TDD for python?
		xChoose 1 or 2 players.  If choose one, play computer, otherwise play human (3/16/14)
	written 3/16/14
		xRefactor to clean up code (3/17/14...kind of cleaner)
		-Better way to choose position?
		-Play unlimited games
		-Welcome message with game options
		-Enter a name for player 1 and track record within session
		-Store user name and record somewhere
		-Allow user to re-sign in as previous user and view record
	written 3/17/14
		-create an engine class that runs the game rather than global stuff
		-break out stuff into separate files?
		-fix bug: local variable 'ties' referenced before assignment
"""