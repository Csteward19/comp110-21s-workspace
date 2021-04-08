def a(b: int, c: str) -> float:
    b = b + 23
    c = c + str(b)
    abc:  float = float(c)
    return abc


b: str = "1"
c: int = 0

print(a(c, b))
