# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

def crear_archivo( filename ) :
    file = open( filename, 'x' )
    file.close()

def escribir_archivo( filename, data ) :
    file = open( filename, 'w' )
    file.write( data )
    file.close()

def main() :
    filename = 'ejercicio-1-tema-8.txt'
    data = 'Juan C Jiménez G'

    crear_archivo( filename )
    escribir_archivo( filename, data )

if __name__ == '__main__' :
    main()