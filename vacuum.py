def vacuum_cleaner(grid, vacuum_pos):
    # grid is the 2D array input by user
    # vacuum_pos is the position of the vacuum cleaner
    
    # get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # initialize the room and dirt counters
    num_rooms = 0
    num_dirt = 0
    
    # initialize the vacuum cleaner moves counter
    moves = 0
    
    # loop through the grid and count the number of rooms and dirt patches
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                num_rooms += 1
            elif grid[i][j] == 2:
                num_dirt += 1
    
    # initialize the cleaned dirt counter
    cleaned_dirt = 0
    
    # clean the initial dirt patch
    if grid[vacuum_pos[0]][vacuum_pos[1]] == 2:
        cleaned_dirt += 1
        grid[vacuum_pos[0]][vacuum_pos[1]] = 0
    
    # loop through the grid until all dirt patches are cleaned
    while cleaned_dirt < num_dirt:
        # get the coordinates of the adjacent rooms and check if they are valid
        adj_coords = [(vacuum_pos[0]-1, vacuum_pos[1]), (vacuum_pos[0]+1, vacuum_pos[1]),
                      (vacuum_pos[0], vacuum_pos[1]-1), (vacuum_pos[0], vacuum_pos[1]+1)]
        valid_adj_coords = [coord for coord in adj_coords if coord[0]>=0 and coord[0]<rows and coord[1]>=0 and coord[1]<cols]
        
        # find the first adjacent dirt patch and move the vacuum cleaner there
        found_dirt = False
        for coord in valid_adj_coords:
            if grid[coord[0]][coord[1]] == 2:
                vacuum_pos = coord
                found_dirt = True
                break
        
        # if no adjacent dirt patches are found, pick a random adjacent room and move there
        if not found_dirt:
            vacuum_pos = valid_adj_coords[0]
        
        # increment the moves counter
        moves += 1
        
        # clean the dirt patch
        if grid[vacuum_pos[0]][vacuum_pos[1]] == 2:
            cleaned_dirt += 1
            grid[vacuum_pos[0]][vacuum_pos[1]] = 0
    
    # return the number of rooms, dirt patches, and moves
    return num_rooms, num_dirt, moves
