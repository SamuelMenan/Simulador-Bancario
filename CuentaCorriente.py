class CuentaCorriente:
    #Aqui va el codigo

    '''----------------------------------------------------------------------------
    # Atributos 
    ----------------------------------------------------------------------------'''

    valor = 0
    
    '''----------------------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------------------'''
    
    def __init__(self, valor = 0):
        self.valor = valor
    
    def ConsignarValor(self, valor):
        #Aqui va el codigo del metodo
        self.valor += valor
        return "se retiro: " + (valor)
    
    def RetirarValor(self, valor):
        #Aqui va el codigo del metodo
        if valor <= self.valor:
            self.valor -= valor
            return "se retiraron 0" + (valor) + "de su cuenta."
        else:
            return "valor insuficiente para retirar 0 " + (valor) + "de su cuenta"
        
    def ConsultarValor(self):
        #Aqui va el codigo del metodo
        return "su valor actual es: 0" +(self.valor)
    