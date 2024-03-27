
class Televisao:
    def __init__(self, c_inicial, c_min = 2, c_max = 14):
        self.c_inicial = c_inicial
        self.c_max = c_max
        self.c_min = c_min
        self.ligado = False

    def __str__(self):
        return f'Canal Atual: {self.c_inicial} | {self.c_min} - {self.c_max}' if self.ligado else 'TV Desligada'

    def ligar_tv(self):
        self.ligado = not self.ligado

    def canal_cima(self):
        self.c_inicial += 1
        if self.c_inicial > self.c_max:
            self.c_inicial = self.c_min
            
    
    def canal_baixo(self):
        self.c_inicial -=1
        if self.c_inicial < self.c_min:
            self.c_inicial = self.c_max


tv1 = Televisao(2, 1, 10)
tv2 = Televisao(4)

tv1.ligar_tv()
tv2.ligar_tv()


print('tv1 - ', tv1)
print('tv2 - ', tv2)



