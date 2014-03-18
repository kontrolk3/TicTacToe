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
		
		
class Player(object):
	score = 0
	def __init__(self, name, computer):
		self.name = name
		self.computer = computer
		
	def set_token(self, token):
		self.token = token
	
	def increment_score(self):
		self.score += 1
		
	def take_turn(self, board):
		if self.computer:
			while True:
				rand_column = random.randint(0, 2)
				rand_row = random.randint(0, 2)
				
				if board.set_value(rand_row, rand_column, self.token):
					break
		else:
			board.display()
			while True:
				column = int(raw_input("Column: ")) - 1
				row = int(raw_input("Row: ")) - 1
				
				if column < 0 or column > 2 or row < 0 or row > 2:
					print "Out of range. Try again."
				elif not board.set_value(row, column, self.token):
					print "Position occupied. Try again."
				else:
					break
					
def game_over():
	if board.has_won(player_one.token):
		handle_player_won(player_one)
		return True
	elif board.has_won(player_two.token):
		handle_player_won(player_two)
		return True
	elif board.is_full():
		board.display()
		print "Tie game!"
		ties += 1
		return True
	else:
		return False

def handle_player_won(player):
	board.display()
	print "%s has won!" % player.name
	player.score += 1
	
def handle_game_over():
	if num_players == "1":
		print "%s: %s" % (player_one.name, player_one.score)
		print "Computer: %s" % player_two.score
		print "Ties: %s" % ties
	else:
		print "%s: %s" % (player_one.name, player_one.score)
		print "%s: %s" % (player_two.name, player_two.score)
		print "Ties: %s" % ties

def play_again():
	while True:
		play_again = raw_input("Play again? (y or n) ")
		if play_again == 'y':
			return True
		elif play_again == 'n':
			return False
		else:
			print "Invalid input"
	
print "Welcome to Tic Tac Toe!"
while True:
	num_players = raw_input("How many players? ")
	if num_players != "1" and num_players != "2":
		print "Invalid number of players. Please enter 1 or 2."
	else:
		break

player_one_name = raw_input("Enter player 1 name: ")
player_one = Player(player_one_name, False)


if num_players == "1":
	player_two = Player("computer", True)
else:
	player_two_name = raw_input("Enter player 2 name: ")
	player_two = Player(player_two_name, False)

player_one.set_token("X")
player_two.set_token("O")
board = TicTacToeBoard()
ties = 0
	
while True:
	player_one.take_turn(board)
	if game_over():
		handle_game_over()
		if play_again():
			board.clear()
			continue
		else:
			break
	
	player_two.take_turn(board)
	if game_over():
		handle_game_over()
		if play_again():
			board.clear()
			continue
		else:
			break
	
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