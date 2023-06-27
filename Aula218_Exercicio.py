class Carro:

    def __init__(self, nome):
        self.nome = nome
        self._motor = None

    def exibeNome(self):
        if self.motor:
            print(f'Nome do carro: {self.nome}')
        else:
            print('Carro ainda sem motor')

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

class Motor:

    def __init__(self, nome):
        self.nome = nome

    def exibeNome(self):
        print(f'Nome do motor: {self.nome}')

class Fabricante:

    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def exibeNome(self):
        print(f'Nome do fabricante: {self.nome}')

    def adicionaCarro(self, carro, motor=None):
        self.carros.append(Carro(carro))
        if motor:
            self.carros[-1].motor = motor

    def setCarroMotor(self, carro_nome, motor):
        for carros in (carronome for carronome in self.carros if carronome.nome == carro_nome):
            carros.motor = motor

    def exibeCarros(self):
        if self.carros:
            print('Modelo dos carros:')
            for carro in self.carros:
                print('-------------------------')
                carro.exibeNome()
                carro.motor.exibeNome()
            return
        print('sem carros a serem exibidos')

    def exibeInformacoes(self):
        self.exibeNome()
        self.exibeCarros()

        

motor1 = Motor('motor top1')
motor2 = Motor('motor top2')
fabricante = Fabricante('Gol')
fabricante.adicionaCarro('Gol bola', motor1)
fabricante.adicionaCarro('Fusca')
fabricante.setCarroMotor('Fusca', motor2)

fabricante.exibeInformacoes()