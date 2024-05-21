class SpaceShip:
    def __init__(self, contents, type_letter):
        self.contents = contents
        self.type_letter = type_letter

    def __str__(self):
        return f"Space Ship вид {self.type_letter}: {len(self.contents)}"

    def values(self):
        return self.contents

    def rang(self):
        return self.type_letter

    def __iadd__(self, value):
        new_position = (ord(self.type_letter) - ord('A') + value) % 26
        self.type_letter = chr(ord('A') + new_position)
        return self

    def __getitem__(self, index):
        return self.contents[index]

    def __setitem__(self, index, value):
        self.contents[index] = value

    def deli(self, index):
        del self.contents[index]

    def app(self, value):
        self.contents.append(value)

    def __len__(self):
        return len(self.contents)

    def __contains__(self, value):
        return value in self.contents

    def __eq__(self, other):
        return (self.type_letter == other.type_letter and 
                len(self.contents) == len(other.contents))

    def __gt__(self, other):
        return len(self.contents) > len(other.contents)

    def __lt__(self, other):
        return len(self.contents) < len(other.contents)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __call__(self, x):
        return min(self.contents[:x+1])

# Пример использования:
ss = SpaceShip([1, 2, 3, 4], 'A')
print(str(ss))  # "Space Ship вид A: 4"
print(ss.values())  # [1, 2, 3, 4]
print(ss.rang())  # "A"
ss += 2
print(ss.rang())  # "C"
print(ss[2])  # 3
ss[2] = 10
print(ss[2])  # 10
ss.deli(1)
print(ss.values())  # [1, 10, 4]
ss.app(5)
print(ss.values())  # [1, 10, 4, 5]
print(len(ss))  # 4
print(10 in ss)  # True
ss2 = SpaceShip([1, 10, 4, 5], 'C')
print(ss == ss2)  # True
ss3 = SpaceShip([1, 2], 'C')
print(ss > ss3)  # True
print(ss < ss3)  # False
print(ss != ss3)  # True
print(ss(2))  # 1
