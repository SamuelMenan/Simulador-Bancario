from CuentaCorriente import CuentaCorriente
from CuentaAhorros import CuentaAhorros

class SimuladorBancario:
    #aqui va el codigo

    '''--------------------------------------------
    # Atributos 
    --------------------------------------------'''

    cedula = ''
    nombres = ''
    mesactual = 0
    
    '''--------------------------------------
    # Asociaciones
    --------------------------------------'''
    ahorros = CuentaAhorros()
    corriente = CuentaCorriente()

    
    '''--------------------------------------------
    # Medodos
    --------------------------------------------'''

    def ConsignarCuentaCorriente(self, valor):
        #Aqui va el codigo del metodo
        self.corriente.ConsignarValor()

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