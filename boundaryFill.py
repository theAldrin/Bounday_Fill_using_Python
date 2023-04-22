import numpy as np
import matplotlib.pyplot as plt


def draw_circle(center, radius):
    # Extract the x and y coordinates of the center
    cx, cy = center

    # Initialize the coordinates of the first point on the circle
    x = 0
    y = radius
    p = 5/4 - radius

    # Initialize the list of points on the circle
    points = []

    # Add the first point on the circle
    points.append((x+cx, y+cy))

    # Iterate until x is greater than y
    while x < y:
        x += 1

        # If the decision parameter is less than 0, choose E
        if p < 0:
            p += 2*x + 1
        # Otherwise, choose SE
        else:
            y -= 1
            p += 2*(x-y) + 1

        # Add the new points on the circle
        points.append((x+cx, y+cy))
        points.append((y+cx, x+cy))
        points.append((-x+cx, y+cy))
        points.append((-y+cx, x+cy))
        points.append((-x+cx, -y+cy))
        points.append((-y+cx, -x+cy))
        points.append((x+cx, -y+cy))
        points.append((y+cx, -x+cy))

    # Return the list of points on the circle
    return np.array(points)


def draw_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    x, y = x1, y1
    points = []
    
    while True:
        points.append((x, y))
        
        if x == x2 and y == y2:
            break
        
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    
    return points

def boundary_fill(image, x, y, fill_color, boundary_color):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if x >= 0 and x < image.shape[0] and y >= 0 and y < image.shape[1]:
            if not np.array_equal(image[x][y], boundary_color) and not np.array_equal(image[x][y], fill_color):
                image[x][y] = fill_color
                plt.imshow(image.astype(np.uint8))
                plt.show()
                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))
                stack.append((x+1,y+1))
                stack.append((x-1,y-1))
                stack.append((x+1,y-1))
                stack.append((x-1,y+1))

image = np.ones((100, 100, 3)) * 255 #Change the the first 100,100 to a plot of your required size

choice=int(input('Enter 1 for polygon 2 for circle'))

if choice==1:
    num_vertices = int(input("Enter the number of vertices: "))
    vertices = []
    for i in range(num_vertices):
        x = int(input("Enter x coordinate of vertex {}: ".format(i+1)))
        y = int(input("Enter y coordinate of vertex {}: ".format(i+1)))
        vertices.append((x, y))
       
    for i in range(num_vertices-1):
        p=draw_line(vertices[i][0],vertices[i][1],vertices[i+1][0],vertices[i+1][1])
        for i in p:
            x,y=i
            image[x][y] = (0,0,0)
            image[x+1][y] = (0,0,0)
elif choice==2:
    print("Enter circle center")
    x = int(input("Enter the x value :"))
    y = int(input("Enter the y value :"))
    radius=int(input("Enter radius :"))
    p=draw_circle((x,y), radius)
    for i in p:
        x,y=i
        image[x][y] = (0,0,0)
        image[x+1][y] = (0,0,0)
        image[x+1][y+1] = (0,0,0)
        image[x+1][y-1] = (0,0,0)
        image[x][y+1] = (0,0,0)
        image[x][y-1] = (0,0,0)
        image[x-1][y] = (0,0,0)
        image[x-1][y-1] = (0,0,0)
        image[x-1][y+1] = (0,0,0)
    
    

print('Enter the starting point for filling')
x = int(input("Enter the x value :"))
y = int(input("Enter the y value :"))

print("Enter the fill colour")
r = int(input("Enter the r value :"))
g = int(input("Enter the g value :"))
b = int(input("Enter the b value :"))
boundary_fill(image, x, y, (r,b,b), (0,0,0))
plt.imshow(image.astype(np.uint8))
plt.show()