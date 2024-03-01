class CuentaAhorros:
    #aqui va el codigo

    '''--------------------------------------------
    # Atributos 
    --------------------------------------------'''

    valor = 0
    interes = 0
    
    '''--------------------------------------------
    # Atributos 
    --------------------------------------------'''

    def ConsignarValor(self, valor):
        self.valor += valor
        return "se consignaron: " + (valor)
    
    def RetirarValor(self, valor):
        if valor <= self.valor:
            self.valor -= valor
            return "se retiraron: " + (valor) + "de su cuenta."
        else:
            return "valor insuficiente para retirar: " + (valor) + "de su cuenta"
        
    def ConsultarValor(self):
        return "su valor actual es: " +(self.valor)
    
    def ConsultarInteresMensual(self):
        interes_mensual= self.valor * self.interes
        return "El interes mensual de su cuenta es: " + (interes_mensual)