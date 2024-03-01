class CuentaCorriente:
    #aqui va el codigo

    '''--------------------------------------------
    # Atributos 
    --------------------------------------------'''

    valor = 0
    
    '''--------------------------------------------
    # Atributos 
    --------------------------------------------'''

    def ConsignarValor(self, valor):
        self.valor += valor
        return "se retiraron 0" + (valor)
    
    def RetirarValor(self, valor):
        if valor <= self.valor:
            self.valor -= valor
            return "se retiraron 0" + (valor) + "de su cuenta."
        else:
            return "valor insuficiente para retirar 0 " + (valor) + "de su cuenta"
        
    def ConsultarValor(self):
        return "su valor actual es: 0" +(self.valor)