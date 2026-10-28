def add(a, b, c=0):
    return a + b + c

print(add(2, 3))
print(add(2, 3, 4))

class Bird:
    def fly(self): print("Bird flies")
class Penguin(Bird):
    def fly(self): print("Penguin cannot fly")
for bird in (Bird(), Penguin()): bird.fly()
