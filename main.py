from tictactoe import TicTacToeEngine

def main():
    TicTacToeEngine()

if __name__ == '__main__':
    main()
	
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
	written 4/15/14
		-bugs
			-computer won't win, only prevent
			-error when computer wins
"""