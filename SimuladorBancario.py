from CuentaCorriente import CuentaCorriente
from CuentaAhorros import CuentaAhorros

class SimuladorBancario:
    #Aqui va el codigo

    '''----------------------------------------------------------------------------
    # Atributos 
    ----------------------------------------------------------------------------'''

    cedula = ''
    nombres = ''
    tipocliente = ''
    mesactual = 0
    
    '''----------------------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------------------'''
    ahorros = CuentaAhorros()
    corriente = CuentaCorriente()

    
    '''----------------------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------------------'''
    
    def __init__(self, cedula, nombres, tipocliente, mesactual = 0):
        self.cedula = cedula
        self.nombres = nombres
        self.tipocliente = tipocliente
        self.mesactual = mesactual

    def ConsignarCuentaCorriente(self, valor):
        #Aqui va el codigo del metodo
        self.corriente.ConsignarValor(valor)

    def CalcularValorTotal(self):
        #Aqui va el codigo del metodo
        return self.corriente.ConsultarValor() + self.ahorros.ConsultarValor()
    
    def PasarAhorrosACorriente(self, valor):
        #Aqui va el codigo del metodo
        if self.ahorros.ConsultarValor() >= valor:
            self.ahorros.RetirarValor()
            self.corriente.ConsignarValor()
            return "Transferencia exitosa"
        else:
            return "Valor insuficiente en la cuenta de ahorros"
        
    def ConsultarValorCorriente(self):
        #Aqui va el codigo del metodo
        return "Tu saldo es:" + self.corriente.ConsultarValor()
    
    def DuplicarAhorros(self):
        #Aqui va el codigo del metodo 
        valor_actual_ahorros = self.ahorros.ConsultarValor()
        nuevo_valor_ahorros = valor_actual_ahorros * 2
        self.ahorros.ConsignarValor(nuevo_valor_ahorros)
        return "¡El valor de la cuenta de ahorros se ha duplicado!"
    
    def RetirarFondos(self):
        #Aqui va el codigo del metodo
        self.corriente.RetirarValor(self.corriente.ConsultarValor())
        self.ahorros.RetirarValor(self.ahorros.ConsignarValor())
        return "Has retirado:" + self.CalcularValorTotal
    
    def cambiarTipoCliente(self, nuevotipocliente):
        #Aqui va el codigo del metodo
        self.tipocliente = nuevotipocliente
    
    def retirarValor(self, valor):
        #Aqui va el codigo del metodo
        descuento = valor * 0.01
        self.valor += -(valor + descuento)
