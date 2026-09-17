# LCA 3: To find out whether the triangle is right angled or not.

a = int(input("Enter the value for a:"))
b = int(input("Enter the value for b:"))
c = int(input("Enter the value for c:"))

def right_triangle(a, b, c):
    if a*a + b*b == c*c:
        print("\nThe triangle is a right angled triangle.")
    else:
        print("\nThe triangle is not a right angled triangle.")

right_triangle(a, b, c)