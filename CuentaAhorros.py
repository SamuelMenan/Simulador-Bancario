class CuentaAhorros:
    #aqui va el codigo

    '''----------------------------------------------------------------------------
    # Atributos 
    ----------------------------------------------------------------------------'''

    valor = 0
    interes = 0
    
    '''----------------------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------------------'''
    
    def __init__(self, valor = 0, interes = 0):
        self.valor = valor
        self.interes = interes    

    def ConsignarValor(self, valor):
        #Aqui va el codigo del metodo
        self.valor += valor
        return "se consigno: " + (valor)
    
    def RetirarValor(self, valor):
        #Aqui va el codigo del metodo
        if valor <= self.valor:
            self.valor -= valor
            return "se retiraron: " + (valor) + "de su cuenta."
        else:
            return "valor insuficiente para retirar: " + (valor) + "de su cuenta"
        
    def ConsultarValor(self):
        #Aqui va el codigo del metodo
        return "su valor actual es: " +(self.valor)
    
    def ConsultarInteresMensual(self):
        #Aqui va el codigo del metodo
        interes_mensual= self.valor * self.interes
        return "El interes mensual de su cuenta es: " + (interes_mensual)