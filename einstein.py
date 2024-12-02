m = int(input("What's The mass? "))
c = 300000000
def square(n):
    return n * n
E = (m * square(c)) # or E = (m * c * c)
string_E = str(E)
print("E = " + string_E)