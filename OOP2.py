class TriangleCheaker:
        def __init__(self, a, b, c):
          self.a = a
          self.b = b
          self.c = c
        def is_triagle(self):
            if self.a + self.b > self.c or self.b + self.c > self.a or self.b < self.a + self.c:
                return "Ура, трикутник можна побудувати"
            elif not all(isinstance(side, (int, float)) and side > 0
                       for side in (self.a, self.b, self.c)):
                return "Потрібно вводити тільки числа!"
            else:
                return "Жаль, але з цього трикутник не зробити."

class Triangle(TriangleCheaker):
    def __init__(self, a, b, c):
        if not all(isinstance(side, (int, float)) and side > 0
                   for side in (self.a, self.b, self.c)):
            raise ValueError("Потрібно вводити тільки числа!")
        super().__init__(a, b, c)

class ExtTriangle(Triangle):
    def is_triagle(self):
        if any(side <= 0 for side in (self.a, self.b, self.c)):
            return "З негативними числами нічого не вийде!"
        return super().is_triagle()