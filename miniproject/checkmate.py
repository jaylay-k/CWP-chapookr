def get_board(board): 
    lines = board.split('\n')
    clean_lines = [] 
    
    for line in lines:
        if len(line) > 0:
            clean_lines.append(line) 
    if len(clean_lines) == 0:
        return None
        
    size = len(clean_lines)
    for line in clean_lines:     
        if len(line) != size:
            return None
            
    return clean_lines

def find_king(clean_lines, size):  
    king_r = -1
    king_c = -1
    king_count = 0
    for r in range(size):
        for c in range(size):
            if clean_lines[r][c] == 'K':
                king_r = r
                king_c = c
                king_count += 1
    if king_count != 1:
        return -1, -1 
        
    return king_r, king_c

def straight_check(clean_lines, king_r, king_c, size): 

    straight_moves = [
        [-1, 0], 
        [1, 0], 
        [0, -1], 
        [0, 1]   
    ]
    
    for move in straight_moves:
        step_r = move[0]
        step_c = move[1]
        current_r = king_r + step_r   
        current_c = king_c + step_c
        
        while current_r >= 0 and current_r < size and current_c >= 0 and current_c < size:
            piece = clean_lines[current_r][current_c]
            if piece == 'R' or piece == 'Q': 
                return True
            elif piece == 'P' or piece == 'B' or piece == 'K': 
                break 
            current_r += step_r 
            current_c += step_c
            
    return False

def diagonal_check(clean_lines, king_r, king_c, size):
    diagonal_moves = [
        [-1, -1], 
        [-1, 1], 
        [1, -1],  
        [1, 1]    
    ]
    
    for move in diagonal_moves:
        step_r = move[0]
        step_c = move[1]
        current_r = king_r + step_r
        current_c = king_c + step_c
        distance = 1
        
        while current_r >= 0 and current_r < size and current_c >= 0 and current_c < size:
            piece = clean_lines[current_r][current_c]  
            if piece == 'B' or piece == 'Q':             
                return True
            
            elif piece == 'P' and distance == 1 and step_r == 1:
                return True
            elif piece == 'P' or piece == 'R' or piece == 'K':
                break
            current_r += step_r
            current_c += step_c
            distance += 1 
    return False


def checkmate(board):
    
    clean_lines = get_board(board)
    if clean_lines == None:
        return
    size = len(clean_lines)

    king_r, king_c = find_king(clean_lines, size)
    if king_r == -1:
        return
        
    if straight_check(clean_lines, king_r, king_c, size) == True:
        print("Success")
        return
        
    if diagonal_check (clean_lines, king_r, king_c, size) == True:
        print("Success")
        return
    print("Fail")