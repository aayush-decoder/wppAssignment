# from sys import maxsize

def dist(point1, point2):
    point1 = [int(i) for i in point1.split(" ")]
    point2 = [int(i) for i in point2.split(" ")]
    result = 0
    for i in range(0, 3):
        result += ((point1[i]-point2[i])**2)
    return result

points = [input("Enter a 3D point in format x y z: ") for i in range(0, 10)]
nearestPoints = []
nearestDist = 99999
temp = ''

for p in points:
    for point in points:
        if nearestDist > dist(point, p) and p != point:
            nearestDist = dist(point, p)
            temp = p + ": " + point
    nearestPoints.append(temp)
    nearestDist = 999999
    # print(p)

print()
print(nearestPoints)