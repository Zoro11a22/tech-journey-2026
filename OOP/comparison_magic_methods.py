import functools

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def __eq__(self, other):
        return self.rating == other.rating
    def __lt__(self, other):
        return self.rating < other.rating
    def __gt__(self, other):
        return self.rating > other.rating

m1 = Movie("Interstellar", 9.5)
m2 = Movie("Inception", 9.0)
m3 = Movie("Another", 9.5)

print(m1 == m3)
print(m2 < m1)
print(m1 > m2)

@functools.total_ordering
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.score == other.score
    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.score < other.score
        
p1 = Player("A", 120)
p2 = Player("B", 150)
p3 = Player("C", 120)

print(p1 == p3)
print(p1 < p2)
print(p2 > p1)
print(p2 <= p1)
print(p2 >= p1)
print(p2 != p1)