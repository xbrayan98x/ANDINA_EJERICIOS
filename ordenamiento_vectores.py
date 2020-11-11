import random

class OrdenaVector(Exception):
    
    # tipo compuesto pasado por refencia
    vector  = []

    ''''
    funcion que carga un vector de X posiciones
    dinamicamente con valores enteros comprendidos
    entre a - b
    '''

    def cargar_vector(self, tamanio, a, b):

        try:
            tamanio = int(tamanio)
            a = int(a)
            b = int(b)
        except ValueError:
            raise OrdenaVector('Los parametros de la funcion: cargar_vector son numericos')

        if tamanio <= 1:
            raise OrdenaVector('El tamanio del vector es muy corto')
        
        if a <= 0 or b <=0:
            raise OrdenaVector('El rango de los numeros aleatorios deben ser postivos')

        if a >= b:
            raise OrdenaVector('El rango aleatorio A debe ser < al rango aleatorio B')

        for i in range(1, tamanio + 1):
            # Paso por referencia
            self.vector.append(random.randint(a, b))

    '''
    funcion que ordena un vector de mayor a menor
    e imprime el resultado en pantalla
    '''
    def ordenar_vector(self):
        longitud_vector = len(self.vector) - 1
        # Bucle para las pasadas de cada numero
        for i in range(0, longitud_vector):
            # bucle para comparar e intercambiar posiciones
            for k in range(0, longitud_vector):
                if self.vector[k] > self.vector[k + 1]:
                    aux = self.vector[k]
                    self.vector[k] = self.vector[k + 1]
                    self.vector[k + 1] = aux
        
        print(self.vector)


if __name__ == "__main__":
    ObjOrdenaVector = OrdenaVector()
    ObjOrdenaVector.cargar_vector(100, 1, 100000)
    ObjOrdenaVector.ordenar_vector()
    