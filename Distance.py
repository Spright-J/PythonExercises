def dist(points):
    points.sort()
    return points[len(points) - 1 ] - points[0]


'''
Find the distance between the two furthest apart values in a list.

Create a dist function, receiving a list of numbers (integers or floating points), and returning the bigger distance between any two given values, so typically the distance between the biggest and the smallest, like:
'''