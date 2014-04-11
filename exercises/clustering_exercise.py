'''In each of the parts below, I have provided a function definition (with the
correct arguments but no implementation) and some tests that will pass *if* 
you fill in the correct implementation for each function. If you run this file
 (i.e. run `python clustering_exercise.py` from your shell) and it does not throw
 any errors, then you have finished the exercise!
'''

def cluster_points(points, number_of_clusters):
    '''This function should take a list of points (in two dimensions) and return a list of clusters,
    each of which is a list of points. For example, if you passed in [(0, 0), (-0.1, 0.1), (2,3), (2.1, 3)] 
    with number_of_clusters set to 2, it should return [[(0, 0), (-0.1, 0.1)], [(2,3), (2.1, 3)]].'''

### Test code below ###

assert map(set, cluster_points([(0, 0), (-0.1, 0.1), (2,3), (2.1, 3)], 2)) == [set([(0, 0), (-0.1, 0.1)]), set([(2,3), (2.1, 3)])]

test_points = [(2.84535, -1.30685), (0.323241, -3.16368), (2.7458, -0.968439), (-0.431551, -3.21857), (0.571862, 0.81639), (4.10261, 1.78914), (0.956781, 1.2333), (1.41663, 0.857323), (3.79403, 2.27617), (0.324651, -3.43075), (4.31886, 1.52439), (-0.29597, -2.51867), (4.46602, 2.46859), (0.550688, 0.957447), (3.43546, -0.754756), (2.532, -0.864198), (1.38974, 0.656894), (0.0387609, -2.72697), (3.9467, 1.78742), (2.90352, -1.43381)]
clusters = cluster_points(test_points, 4)
fst = lambda x: x[0]
snd = lambda x: x[1]
def cluster_range(pts):
    return (fst(max(pts, key = fst)) - fst(min(pts, key = fst)), snd(max(pts, key = snd)) - snd(min(pts, key = snd)))
assert len(clusters) == 4, "Not enough clusters"
lens = map(len, clusters)
assert min(lens) == max(lens), "Some clusters are bigger than others (which should not happen with this test set)"
assert all(max(cluster_range(pts)) <= 1.0 for pts in clusters), "Some clusters are larger than 1.0 units (which should not happen with this test set)"

### Test code above ###

print 'All tests passed!'
