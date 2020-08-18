
def iloczyn_liczby(n):
    if n == 0:
        wynik = 0
        print(wynik)
    else:
        wynik = 1        
        while n > 0:
            var = n % 10
            wynik *= var
            n = n // 10
            print(wynik)
        
iloczyn_liczby(6582)    
    