class TicTacToeDisplay:
	def __init__(self, ttt_board):
		self.ttt_board = ttt_board

	def display_board(self):
		print "-------------"
		for row in self.ttt_board.get_board():
			for column in row[:-1]:
				print "| %s" % column,
			else:
				print "| %s |" % row[-1]
			print "-------------"