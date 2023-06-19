class Caneta:

    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, novaCor):
        self._cor = novaCor
    

caneta = Caneta('Preto')

print(caneta.cor)