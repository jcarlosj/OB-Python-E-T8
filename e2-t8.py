# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle

class Vehiculo :

    def __init__( self, marca, modelo, anio ) :
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def __repr__( self ) :
        return f'{ type( self ).__name__ }( marca: { self.marca }, modelo: { self.modelo }, anio: { self.anio } )'

def save( obj, file ) :
    file = open( file, 'wb' )
    pickle.dump( obj, file  )
    file.close()

def load( file ) :
    file = open( file, 'rb' )
    data = pickle.load( file )
    file.close()

    return data

def main() :
    filename = 'auto.bin'
    audi = Vehiculo( 'Audi', 'Sedan', 2022 )
    save( audi, filename )
    data = load( filename )

    print( type( data ) )
    print( data )


if __name__ == '__main__' :
    main()