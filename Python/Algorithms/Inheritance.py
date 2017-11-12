"""Inheritance"""

class Progression:
    """Iterator producing a generic progression."""

    def __init__(self, start=0):
        self.current = start

    def _advance(self):
        self.current += 1

    def __next__(self):
        if self.current is None: 
            raise StopIteration()
        else:
            answer = self.current
            self._advance()
        return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(self.__doc__)
        print(', '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression"""
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self.current += self._increment

class GeometricProgression(Progression):
    """Iterator producing a geometric progression"""
    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self.current *= self._base

class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression"""
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self.current = self.current, self._prev + self.current

if __name__ == '__main__':
    Progression().print_progression(10)
    ArithmeticProgression(4).print_progression(10)
    GeometricProgression(2).print_progression(10)
    FibonacciProgression().print_progression(10)
