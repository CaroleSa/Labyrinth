


class Test:
    def machin(self):
        self.a=5
        print(self.a)
        
    
class Idee:
    def truc(self):
        self.b=5
        Test.machin(self)



    
lala = Idee()
lala.truc()
