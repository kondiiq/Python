
class square_func:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    
    def delta(self):
        delta = self.b ** 2 - 4 * self.a * self.c
        print(delta)
        return delta


    def zero_value(self, delta):
        if delta > 0:
            print("Two zero places in reality numbers")
        elif delta == 0:
            print("1 zero places")
        else:
            print("Two zero places in complex numbers)")
            
    def is_square_func(self):
        if self.a == 0 :
            return False
        else:
            return True
        
func = square_func(1,5,1)
plus = func.delta()
print(func.is_square_func())
