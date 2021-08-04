import math

def solve_quadratic(a,b,c):
    try:
        x = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        y = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    
        return set([round(x),round(y)])
    except ValueError:
        return None
