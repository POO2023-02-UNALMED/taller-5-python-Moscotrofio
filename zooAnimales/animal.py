import zooAnimales
class Animal:
    _totalAnimales = 0
    def _init_(self, nombre, edad, habitat, genero, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    def movimiento():
        return "desplazarce"
    
    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos: "+ str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) +"\nAves: "+ str(zooAnimales.ave.Ave.cantidadAves()) +"\nReptiles: " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) + "\nPeces: "+ str(zooAnimales.pez.Pez.cantidadPeces()) +"\nAnfibios: " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())
    
    def __str__(self):
        if self.getZona() != None:
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero() + ", la zona en la que me ubico es " + self.getZona().getNombre() + ", en el "+ self.getZona().getZoo().getNombre()
        else:
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero()

    
    @classmethod
    def getTotalAnimales(cls):
        return Animal._totalAnimales
     
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona
