class Yikes:
    x: int = 0

    def __add__(self, rhs: Yikes) -> int:
        self.x += rhs.x
        return self.x

a: Yikes = Yikes()
a.x = 5
b: Yikes = Yikes()
b.x = 10
c: int = a + b
d: int = b + a
print(c)
print(d)