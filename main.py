import collections
import time
from result import *
import numpy as np
#import math NEED TESTING

def esdf(M, N, obstacle_list):
    """
    :param M: Row number
    :param N: Column number
    :param obstacle_list: Obstacle list
    :return: An array. The value of each cell means the closest distance to the obstacle
    """
    obstacle_tuples = [tuple(l) for l in obstacle_list] #contains root node, or the space itself
    grid = np.full((M,N), -1.0)
    queue = collections.deque([(tuple(l), tuple(l)) for l in obstacle_list]) #queue values must contain the target coordinate and BFS root
    seen = set(obstacle_tuples)

    #clockwise expansion from right
    row = [0, 1, 0, -1]
    col = [1, 0, -1, 0]

    while queue:
        #pseudocode time
        #pop space from queue
        #two cases: the space has already been processed, or not
        #if not (space val =... -1 i guess) then continue on your way
        #if it has... then do a comparison
        #    if it's a lesser distance, terminate your search
        #    if it's a greater distance
        #        hard to keep track of additional spaces from that point in the queue. not much that can be done
        #        unless thinking involved
        #        treat all adjacent spaces as zero and attempt to expand


        #Distance calc and storage
        space = queue.popleft()
        x = space[0][0]
        y = space[0][1]
        cur = np.array(space[0])
        root = np.array(space[1])
        cur_dist = np.linalg.norm(cur - root)
        stored_dist = grid[x][y]
        if stored_dist == -1 or stored_dist > cur_dist: #if this isn't true, nothing happens this round
            grid[x][y] = cur_dist

            #Add adjacent cells, with some caveats
            for i in range(4):
                adjx = x + row[i]
                adjy = y + col[i]

                test_space = (adjx, adjy)
                # this doesn't work. seen restricts it. either: testspace not in seen or: test space in seen, but still -1
                if 0 <= adjx < M and 0 <= adjy < N and (test_space not in seen or grid[adjx][adjy] == -1 or grid[adjx][adjy] > np.linalg.norm(np.array(test_space) - root)):
                    gridval = grid[adjx][adjy]
                    testval = np.linalg.norm(np.array(test_space)- root)
                    queue.append((test_space, space[1]))
                    seen.add((adjx, adjy))

        #print(queue)


    #print(grid)
    return grid


if __name__ == '__main__':
    st = time.time()
    for _ in range(int(2e4)):
        assert np.array_equal(esdf(M=3, N=3, obstacle_list=[[0, 1], [2, 2]]), res_1)
        assert np.array_equal(esdf(M=4, N=5, obstacle_list=[[0, 1], [2, 2], [3, 1]]), res_2)

    et = time.time()
    print(et-st)
