class Animal:
    _totalAnimales = 0
    def _init_(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        _totalAnimales += 1

    def movimiento():
        return "desplazarce"
    
    def totalPorTipo():
        return "Mamiferos: "+ Mamifero.cantidadMamiferos() +"\nAves: "+ Ave.cantidadAves() +"\nReptiles: " + Reptil.cantidadReptiles() + "\nPeces: "+ Pez.cantidadPeces() +"\nAnfibios: " + Anfibio.cantidadAnfibios();
    
    def __str__(self):
        if self.getZona() != None:
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + self.getEdad() + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero() + ", la zona en la que me ubico es " + self.getZona().getNombre() + ", en el "+ self.getZona().getZoo().getNombre()
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getZona(self):
        return self._zona