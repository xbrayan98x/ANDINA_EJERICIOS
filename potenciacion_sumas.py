class ElevaSumando(Exception):
    
    r = 0
    n = 1 

    def potenciar_numero_suma(self,base, potencia):
        try:
            b = int(base)
            e = int(potencia)
        except ValueError:
            raise ElevaSumando('Los parametros de la funcion: potenciar_numero_suma son numericos')
        
        
        for i in range(e):
            self.r=0
            for j in range(b):
                self.r += self.n
            self.n = self.r
        print(f"{base}^{potencia} = {self.r}")

if __name__ == "__main__":
    ObjElevaSumando = ElevaSumando()
    ObjElevaSumando.potenciar_numero_suma(5,4)