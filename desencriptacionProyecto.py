from itertools import chain


# GENERAR MATRIZ CON LLAVE
def generateKeyMatrix ( key ): 
    #CREAR MATRIZ 5X5 CON 0s
    matrix_5x7 = [[0 for i in range (5)] for j in range(7)]
    
    # LLAVE SIN CHAR REPETIDOS
    simpleKeyArr = []
    for c in key:
        # SI NO ESTA EL CARACTER, AÑADIRLO
        if c.upper() not in simpleKeyArr:
            if c == 'J':
                simpleKeyArr.append('I')
            else:
                simpleKeyArr.append( c.upper() )    

    is_I_exist = "I" in simpleKeyArr

    # A-Z EN ASCII 65-90
    for i in chain( range( 48, 58 ), range( 65, 91 ) ):
        if chr( i ) not in simpleKeyArr:
            # PONER I EN ARREGLO Y NO J
            if i == 73 and not is_I_exist:
                simpleKeyArr.append( "I" )
            # SI YA EXISTE, NO HACER NADA
            elif i == 73 or i == 74 and is_I_exist:
                pass
            else:
                simpleKeyArr.append( chr(i) )
    
    # MAPEAR ARREGLO A MATRIX 5X5
    index = 0
    for i in range( 0, 7 ):
        for j in range( 0, 5 ):
            matrix_5x7[i][j] = simpleKeyArr[index]
            index += 1

    return matrix_5x7

# LOCALIZAR INDICES
def indexLocator( char, matrix ):
    indexChar = []

    if char == "J":
        char == "I"

    # ENUMERAR ( ( 0, ['A', 'B', 'C', ....] ) )
    for i, j in enumerate( matrix ):
        # ENUMERAR ( [ (0, 'A' ), ( 1, 'B' ) ]  )
        for k, l in enumerate( j ):
            if char == l:
                indexChar.append(i)
                indexChar.append(k)
                return indexChar


def calculateNewIndexImpair( n1, n2, keyMatrix ):
    n = ''

    x1 = []
    x2 = []

    # SI ES EL FINAL, PONER AL PRINCIPIO
    if n1[0] == 6 and n1[1] == 4:
        x1.append(0)
        x1.append(0)
    # SI ES ULTIMA COLUMNA, PONER AL PRINCPIO
    elif n1[0] == 6 and n1[1] != 4:
        x1.append(0)
        x1.append( n1[1] + 1 )
    # SI ES ULTIMA FILA, PONER AL PRINCIPIO
    elif n1[0] != 6 and n1[1] == 4:
        x1.append( n1[0] + 1 )
        x1.append(0)
    # MOVER ABAJO DERECHA
    else:
        x1.append( n1[0] + 1 )
        x1.append( n1[1] + 1 )


    # SI ES EL FINAL, PONER AL PRINCIPIO
    if n2[0] == 6 and n2[1] == 4:
        x2.append(0)
        x2.append(0)
    # SI ES ULTIMA COLUMNA, PONER AL PRINCPIO
    elif n2[0] == 6 and n2[1] != 4:    
        x2.append(0)
        x2.append( n2[1] + 1 )
    # SI ES ULTIMA FILA, PONER AL PRINCIPIO
    elif n2[0] != 6 and n2[1] == 4:
        x2.append( n2[0] + 1 )
        x2.append(0)
    # MOVER ABAJO DERECHA
    else:
        x2.append( n2[0] + 1 )
        x2.append( n2[1] + 1 )

    n = keyMatrix[ x2[0] ][ x1[1] ] + keyMatrix[ x1[0] ][ x2[1] ]
    return n


def calculateNewIndexPair( n1, keyMatrix ):
    n = ''
    # AL PRINCIPIO, ESQUINA INFERIOR DERECHA
    if n1[0] == 0 and n1[1] == 0:
        n = n + keyMatrix[6][4]
    # PRINCIPIO DE COLUMNA
    elif n1[0] == 0 and n1[1] != 0:
        n = n + keyMatrix[6][ n1[1] - 1 ]
    # PRINCIPIO DE FILA
    elif n1[0] != 0 and n1[1] == 0:
        n = n + keyMatrix[ n1[0] + 1 ][4]
    # DIAGONAL A LA DERECHA
    else:
        n = n + keyMatrix[ n1[0] - 1 ][ n1[1] - 1 ]
    return n



# ENCRIPTAR
def decipher( plainText, key ):
    # VAR DE RESULTADO
    n = ''
    # GENERAR MATRIZ
    keyMatrix = generateKeyMatrix( key )

    #ENCRIPTAR
    i = 0
    while i < len( plainText ):
        # OBTENER INDICES DE DIGRAMA
        n1 = indexLocator( plainText[i], keyMatrix )
        n2 = indexLocator( plainText[ i + 1 ], keyMatrix )
        
        # MISMA FILA O COLUMNA (DIAGONAL)
        if n1[0] == n2[0] or n1[1] == n2[1]:
            n = n + calculateNewIndexPair( n1, keyMatrix )
            n = n + calculateNewIndexPair( n2, keyMatrix )

        else: 
            n = n + calculateNewIndexImpair( n1, n2, keyMatrix )

        i += 2

    return "".join( map( str, n ) )


cipher = 'GF5YXB9CTH'
print( cipher )
cipherText = "".join( decipher( cipher, 'Luis' ) )
print( cipherText )

cipher = 'BJDUPXQ89PQ8LSI9BJMW'
print( cipher )
cipherText = "".join( decipher( cipher , 'Konay' ) )
print( cipherText )