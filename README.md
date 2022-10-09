# multi-drone-quiz

Breadth first search outward from each obstacle, staying at the same 
level for each until the combined queue has been expended for that level. For example,
with k obstacles, check the adjacent spaces to the first, then second's and so on
to the kth's, then proceed to the next level for each. At each space, calculate the distance 
to the root (i.e. the closest obstacle) and store within the corresponding index in the array. 
If a space has already been traversed, then there's a chance that the distance from another 
obstacle is shorter. If that's the case, the space is enqueued again, with the new obstacle as 
its root. Traverse until the combined BFS queue is depleted.

Note that the BFS for each obstacle has to pass down the obstacle's coordinates for 
distance calculation. The distance calculation uses math.dist for faster calculation, 
and the queue uses collections.deque for faster appending and popping.