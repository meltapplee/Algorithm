class FourCal:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def plus(self):
         result = self.a + self.b
         return int(result)
    def sub(self):
        result = self.a - self.b
        return int(result)
    def mul(self):
         result = self.a * self.b
         return int(result)
    def div(self):
         result = self.a / self.b
         return int(result)
    def rem(self):
        result = self.a % self.b
        return int(result)
    def pow(self):
        result = self.a ** self.b
        return int(result)
    
    
yap = FourCal(3.8, 4.2)

print("sum:",  yap.plus())
print("sub:",  yap.sub())
print("mul:",  yap.mul())
print("div:",  yap.div())
print("rem:",  yap.rem())
print("pow:",  yap.pow())