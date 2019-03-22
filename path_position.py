
class Truc:
        def __init__(self):
                self.a=2
                self.b=self.bidule()

        def bidule(self):
                return self.a*2

new_truc = Truc()
print(new_truc.bidule())