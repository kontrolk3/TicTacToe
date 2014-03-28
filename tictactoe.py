from models import TicTacToeBoard
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
			if self.game_over(board, player_one, player_two):
				self.handle_game_over(player_one, player_two, num_players, ties)
				if self.play_again():
					board.clear()
					continue
				else:
					break
			
			player_two.take_turn(board)
			if self.game_over(board, player_one, player_two):
				handle_game_over(player_two, player_two, num_players, ties)
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
			self.handle_player_won(player_two)
			return True
		elif board.is_full():
			board.display()
			print "Tie game!"
			ties += 1
			return True
		else:
			return False

	def handle_player_won(self, player, board):
		board.display()
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
		