class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None
    
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.largo = 0

    #Crea los nodos y los enlaza
    def link(self, tokens): 
        if len(tokens) == 0:
            return None
        self.largo = len(tokens)
        self.cabeza = Nodo(tokens[0])
        self.cola = Nodo(tokens[-1])
        actual = self.cabeza
        for dato in tokens[1 : -1]:
            actual.siguiente = Nodo(dato)
            actual = actual.siguiente
        actual.siguiente = self.cola
        return self.cabeza
    
    #Imprime los valores de los nodos enlazados
    def print_list(self): 
        if self.cabeza is None:
            raise Exception("Lista vacia")
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.datos)
            nodo_actual = nodo_actual.siguiente

    #Añade un nuevo nodo al final de la lista            
    def push(self, datos): 
        nuevo_nodo = Nodo(datos)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.largo += 1
        return nuevo_nodo
    
    #Elimina el último nodo de la lista
    def pop(self): 
        if self.cabeza is None:
            return "Lista vacia"
        nodo_actual = self.cabeza
        nueva_cola = None
        while nodo_actual.siguiente:
            nueva_cola = nodo_actual
            nodo_actual = nodo_actual.siguiente
        if nueva_cola is None:
            self.cabeza = None
            self.cola = None
        else:
            nueva_cola.siguiente = None
            self.cola = nueva_cola
        self.largo -= 1
        return nodo_actual
    
    #Añade un nuevo nodo al principio de la lista
    def add_firs(self, datos): 
        nuevo_nodo = Nodo(datos)
        if not self.cabeza and self.largo == 0:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.largo += 1
        return nuevo_nodo
    
    #Elimina el primer nodo de la lista
    def remove_firs(self): 
        if not self.cabeza and self.largo == 0:
            raise Exception("Lista vacia")
        actual = self.cabeza
        self.cabeza = actual.siguiente
        actual.siguiente = None
        self.largo -= 1
        return actual
    
    #Obtner el Nodo del índice indicado
    def get(self, indice): 
        if indice < 0 or indice >= self.largo:
            raise Exception(f"No hay nodo en el índice : {indice}")
        contador = 0
        actual = self.cabeza
        while contador != indice:
            actual = actual.siguiente
            contador += 1
        return actual
    
    #Añade el Nodo en el índice indicado
    def add(self, indice, datos): 
        nuevo_nodo = None
        if indice < 0 or indice > self.largo:
            raise Exception(f"No se puede añadir el nodo en el índice : {indice}")
        elif indice == 0:
            nuevo_nodo = self.add_firs(datos)
        elif indice == self.largo:
            nuevo_nodo = self.push(datos)
        else:
            nuevo_nodo = Nodo(datos)
            nodo_previo = self.get(indice - 1)
            nuevo_nodo.siguiente = nodo_previo.siguiente
            nodo_previo.siguiente = nuevo_nodo
            self.largo += 1
        return nuevo_nodo
    
    #Elimina el Nodo en el índice indicado
    def remove(self, indice): 
        if indice < 0 or indice >= self.largo or self.largo == 0:
            raise Exception(f"No se puede remover el nodo en el índice : {indice}")
        elif indice == 0:
            self.remove_firs()
        elif indice == self.largo - 1:
            self.pop()
        else:
            nodo_previo = self.get(indice - 1)
            nodo_a_remover = nodo_previo.siguiente
            nodo_previo.siguiente = nodo_a_remover.siguiente
            nodo_removido = nodo_a_remover
            nodo_a_remover = None
            self.largo -= 1
        return nodo_removido
    
    #Actualiza los datos del Nodo en el índice indicado
    def update(self, indice, nuevos_datos): 
        nodo = self.get(indice)
        if nodo:
            nodo.datos = nuevos_datos
            return nodo
        else:
            raise Exception(f"No se encontró el nodo en el índice : {indice}")
        
    #Invertir lista   
    def reverse(self):
        if self.largo == 0 or self.largo == 1:
            raise Exception(f"La lista no se puede invertir")
        temp = self.cabeza
        self.cabeza = self.cola
        self.cola = temp
        after = None
        prev = None
        for i in range(self.largo):
            after = temp.siguiente
            temp.siguiente = prev
            prev = temp
            temp = after
        
