def isValidChessBoard(board):
    # (Keep all the validation logic from the previous implementation)
     # ... [previous validation code here] ...



    def get_chess_board_from_user():
        board = {}
        print("Enter chess pieces in format 'position:piece' (e.g., '1a:wking')")
        print("Enter 'done' when finished:")
    
        while True:
            entry = input("> ").strip().lower()
            if entry == 'done':
                break
        
            try:
                pos, piece = entry.split(':')
                board[pos] = piece
            except ValueError:
                print("Invalid format! Please use 'position:piece'")
    
        return board

    # Main program
    if __name__ == "__main__":
       print("CHESS BOARD VALIDATOR")
    chess_board = get_chess_board_from_user()
    
    if isValidChessBoard(chess_board):
            print("\n Valid chess board!")
    else:
            print("\n Invalid chess board!")