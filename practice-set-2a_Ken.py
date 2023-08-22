def TriangleArea(a, b, c):

    if a + b > c and a + c > b and b + c > a:

        s = (a + b + c) / 2

        area = (s * (s - a) * (s - b) * (s - c)) ** 1/2
        return area
    else:
        return "These sides cannot form a triangle."