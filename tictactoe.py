from models import TicTacToeBoard
from views import TicTacToeDisplay
import random

class TicTacToeEngine(object):

	def __init__(self):
		print "Welcome to Tic Tac Toe!"
		while True:
			num_players = raw_input("How many players? ")
			if num_players != "1" and num_players != "2":
				print "Invalid number of players. Please enter 1 or 2."
			else:
				break

		player_one_name = raw_input("Enter player 1 name: ")
		player_one = Human(player_one_name)


		if num_players == "1":
			player_two = MediumComputer()
		else:
			player_two_name = raw_input("Enter player 2 name: ")
			player_two = Human(player_two_name)

		player_one.set_token("X")
		player_two.set_token("O")
		board = TicTacToeBoard()
		view = TicTacToeDisplay(board)
		ties = 0
			
		while True:
			view.display_board()
			player_one.take_turn(board)
			if self.game_over(board, player_one, player_two):
				self.handle_game_over(player_one, player_two, num_players, ties)
				if self.play_again():
					board.clear()
					continue
				else:
					break
			
			player_two.take_turn(board)
			if self.game_over(board, player_one, player_two):
				self.handle_game_over(player_two, player_two, num_players, ties)
				if play_again():
					board.clear()
					continue
				else:
					break
					
	def game_over(self, board, player_one, player_two):
		if board.has_won(player_one.token):
			self.handle_player_won(player_one, board)
			return True
		elif board.has_won(player_two.token):
			self.handle_player_won(player_two, board)
			return True
		elif board.is_full():
			view.display_board()
			print "Tie game!"
			ties += 1
			return True
		else:
			return False

	def handle_player_won(self, player, board):
		view.display_board()
		print "%s has won!" % player.name
		player.score += 1
		
	def handle_game_over(self, player_one, player_two, num_players, ties):
		print "%s: %s" % (player_one.name, player_one.score)
		if num_players == "1":
			print "Computer: %s" % player_two.score
		else:
			print "%s: %s" % (player_two.name, player_two.score)
		print "Ties: %s" % ties


	def play_again(self):
		while True:
			play_again = raw_input("Play again? (y or n) ")
			if play_again == 'y':
				return True
			elif play_again == 'n':
				return False
			else:
				print "Invalid input"
				

class Player(object):
	score = 0
	
	def __init__(self, name):
		self.name = name
		
	def set_token(self, token):
		self.token = token
	
	def increment_score(self):
		self.score += 1

class Human(Player):
	
	def __init__(self, name):
		super(Human, self).__init__(name)
		
	def take_turn(self, board):
		
		while True:
			column = int(raw_input("Column: ")) - 1
			row = int(raw_input("Row: ")) - 1
			
			if column < 0 or column > 2 or row < 0 or row > 2:
				print "Out of range. Try again."
			elif not board.set_value(row, column, self.token):
				print "Position occupied. Try again."
			else:
				break
					
class EasyComputer(Player):
	
	def __init__(self):
		super(EasyComputer, self).__init__("computer")
		
	def take_turn(self, board):
		while True:
			rand_column = random.randint(0, 2)
			rand_row = random.randint(0, 2)
			
			if board.set_value(rand_row, rand_column, self.token):
				break

class MediumComputer(Player):
	
	def __init__(self):
		super(MediumComputer, self).__init__("medium computer")
		
	def take_turn(self, board):	
		#If computer can win, play there
		if win_if_possible(self.token, self.token, board):
			return
		
		#If opponent can win, block
		other_token = "X"
		if self.token == "X":
			other_token = "O"
		if win_if_possible(self.token, other_token, board):
			return
			
		#Play a random space
		while True:
			rand_column = random.randint(0, 2)
			rand_row = random.randint(0, 2)
			
			if board.set_value(rand_row, rand_column, self.token):
				break
	
class HardComputer(Player):
	
	def __init__(self):
		super(HardComputer, self).__init__("hard computer")
		
	def take_turn(self, board):
		#If computer can win, play there
		if win_if_possible(self.token, self.token, board):
			return
		
		#If player can win, block win
		other_token = "X"
		if self.token == "X":
			other_token = "O"
		if win_if_possible(self.token, other_token, board):
			return
			
		#Play in corners if available
		
		#Play middle if available
		
		#Play anywhere else randomly
		while True:
			rand_column = random.randint(0, 2)
			rand_row = random.randint(0, 2)
			
			if board.set_value(rand_row, rand_column, self.token):
				break
				
class ImpossibleComputer(Player):
	def __init__(self):
		super(ImpossibleComputer, self).__init__("impossible computer")
	
	def take_turn(self, board):
		pass
		#Minimax algorithm to never lose

def win_if_possible(token_to_play, token_to_check, board):
	if amount_in_line(board.value_at(0,0), board.value_at(0,1), board.value_at(0,2), token_to_check) == 2:
		row, column = open_position(0,0,0,1,0,2, token_to_check, board)
		if board.set_value(row, column, token_to_play):
			return True
	
	if amount_in_line(board.value_at(1,0), board.value_at(1,1), board.value_at(1,2), token_to_check) == 2:
		row, column = open_position(1,0,1,1,1,2, token_to_check, board)
		if board.set_value(row, column, token_to_play):
			return True
		
	if amount_in_line(board.value_at(2,0), board.value_at(2,1), board.value_at(2,2), token_to_check) == 2:
		row, column = open_position(2,0,2,1,2,2, token_to_check, board)
		if board.set_value(row, column, token_to_play):
			return True
		
	if amount_in_line(board.value_at(0,0), board.value_at(1,0), board.value_at(2,0), token_to_check) == 2:
		row, column = open_position(0,0,1,0,2,0, token_to_check, board)
		if board.set_value(row, column, token_to_play):
			return True
		
	if amount_in_line(board.value_at(0,1), board.value_at(1,1), board.value_at(2,1), token_to_check) == 2:
		row, column = open_position(0,1,1,1,2,1, token_to_check, board)
		if board.set_value(row, column, token_to_play):
			return True
		
	if amount_in_line(board.value_at(0,2), board.value_at(1,2), board.value_at(2,2), token_to_check) == 2:
		row, column = open_position(0,2,1,2,2,2, token_to_check, board)
		if board.set_value(row, column, token_to_play):
			return True
		
	if amount_in_line(board.value_at(0,0), board.value_at(1,1), board.value_at(2,2), token_to_check) == 2:
		row, column = open_position(0,0,1,1,2,2, token_to_check, board)
		if board.set_value(row, column, token_to_play):
			return True
		
	if amount_in_line(board.value_at(0,2), board.value_at(1,1), board.value_at(2,0), token_to_check) == 2:
		row, column = open_position(0,2,1,1,2,0, token_to_check, board)
		if board.set_value(row, column, token_to_play):
			return True
	
	return False
			
def amount_in_line(position1, position2, position3, token):
	other_token = "X"
	if token == "X":
		other_token = "O"
		
	count = 0
	if position1 == token:
		count += 1
	if position2 == token:
		count += 1
	if position3 == token:
		count += 1
	return count
	
def open_position(position1row, position1column, position2row, position2column, position3row, 				position3column, token, board):
	if (board.value_at(position1row, position1column) != token):
		return (position1row, position1column)
	if (board.value_at(position2row, position2column) != token):
		return (position2row, position3column)
	if (board.value_at(position3row, position3column) != token):
		return (position3row, position3column)
		