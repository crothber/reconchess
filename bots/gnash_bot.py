import random
from reconchess import *
from reconchess.utilities import capture_square_of_move
from game.BeliefState import BeliefState


class GnashBot(Player):
    def __init__(self):
        self.color = None
        self.board = None
        self.beliefState = None

    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        self.color = color
        self.board = board
        print('Game has started.')
        print('\nUpdating our belief states...')
        self.beliefState = BeliefState(board.fen())
        print('Our original belief state is as follows:')
        self.beliefState.display()

    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        print('\nOpponent moved.')
        print(captured_my_piece)
        if captured_my_piece:
            print('Piece captured!', capture_square)
        else:
            print('No pieces captured.')
        print('Updating belief state...')
        self.beliefState.opp_move_result_update(captured_my_piece, capture_square)
        print('Our updated belief state is now as follows:')
        self.beliefState.display()
        pass

    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> \
            Optional[Square]:
        print('\nSensing now...')
        return 15

    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        print('\nSense result is', sense_result)
        print('Updating belief state...')
        self.beliefState.sense_update(sense_result)
        print('Our updated belief state is now as follows:')
        self.beliefState.display()

    def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        print('\nChoosing move')
        return random.choice(move_actions + [None])

    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move],
                           captured_opponent_piece: bool, capture_square: Optional[Square]):
        print('\nRequested move', requested_move, ', took move', taken_move)
        print('Updating belief state...')
        self.beliefState.our_move_result_update(requested_move, taken_move, captured_opponent_piece, capture_square)
        print('Our updated belief state is now as follows:')
        self.beliefState.display()

    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason],
                        game_history: GameHistory):
        pass