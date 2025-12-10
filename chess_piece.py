


'''
Docstring for chess_piece
- position on the board in the form of [x, y] x rows y columns index
- Type of the piece ie rook king knight etc
'''
class PlayerChessPiece:
    def __init__(self, ):
        pass


class Rook:
    def __init__(self, board_width:int, board_height:int, location:list[int]):
        self.piece_type = 'rook'
        self.board_width = board_width
        self.board_height = board_height
        self.location = [location[0], location[1]]

    def get_movement_possibilities(self, point:list[int], piece_locations:list[list[int]])->list[list[int]]:
        '''
        :param point: the current point of the rook passed in the format of
        [row index, column index]
        :piece_locations: the next possible location that the piece could move to,
        if it is an friendly piece the max location is one index before the piece, if
        it is an enemy piece, it is the index of the enemy piece
        piece_locations is always passed in the format of a clockwise list of locations starting from 'North'
        '''
        min_and_max_indexes = self.get_max_movement_index(point, piece_locations)

        locations = []
        # columns
        for i in range(min_and_max_indexes[2], min_and_max_indexes[3], 1):
            if i != point[1]:
                locations.append([point[0], i])
        # rows
        for i in range(self.board_height):
            if i != point[0]:
                locations.append([i, point[1]])
        return locations
    
    def get_max_movement_index(self, point:list[int], piece_locations:list[list[int]])->list[int]:
        '''
        :param self: Description
        :param point: Description
        :type point: list[int]
        :param piece_locations:         
        4 locations of movement limitations, if there is no blocking piece, the point is passed as 
        empty [], with the topmost point in index 0, then all other points are added in a 
        clockwise orientation
        :return: list of minimum and maximum indexes in format of  [row_min, row_max, col_min, col_max] 
        '''
    
        # in format [row_min, row_max, col_min, col_max] 
        min_and_max_indexes = [0, self.board_height-1, 0, self.board_width-1]

        # max and min the rows
        if piece_locations[0] != []:
            min_and_max_indexes[0] = piece_locations[0][0]
        if piece_locations[2] != []:
            min_and_max_indexes[1] = piece_locations[2][0]
        # max and min for columns
        if piece_locations[1] != []:
            min_and_max_indexes[2] = piece_locations[3][1]
        if piece_locations[3] != []:
            min_and_max_indexes[3] = piece_locations[1][1]

        return min_and_max_indexes





class Bishop:
    def __init__(self, board_width:int, board_height:int):
        self.piece_type = 'bishop'
        self.board_width = board_width
        self.board_height = board_height

    def get_movement_possibilities(self, point:list[int], piece_locations:list[list[int]])->list[list[int]]:
        pass

