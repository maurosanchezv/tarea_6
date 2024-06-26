def introducir_puntuacion_comentarios():
   while True:
    print( 'Por favor, introduzca una puntuación en una escala de 1 a 5' )
    point = input()
    if point.isdecimal():
      point = int(point)
      if  point <= 0 or point > 5:
        print( 'Indíquelo en una escala de 1 a 5' )
        point = (point)
      else:
        print( 'Introduzca sus comentarios.' )
        comment = input()
        post = f'punto: {point} comentario: {comment}'
        file_pc = open("data.txt", 'a')
        file_pc.write( f'{ post } \n' )
        file_pc.close()
        break
    else: 
      print( 'Por favor ingrese su punto de calificación en números.' )

def comprobar_resultados():
    print( 'Resultados hasta la fecha.' )
    read_file = open("data.txt", "r")
    print( read_file.read() )
    read_file.close()

while True:

    print( 'Seleccione el proceso que desea aplicar' )
    print( '1:Ingresar punto de calificación y comentario' )
    print( '2: Comprueba los resultados obtenidos hasta ahora.' )
    print( '3: Terminación.' )
    num = input()

    if num.isdecimal():
        num = int(num)
        if num == 1:
            introducir_puntuacion_comentarios()
        elif num == 2:
          comprobar_resultados()
        elif num == 3:
          print( 'Terminación.' )
          break
        else:
            print( 'Introduzca de 1 a 3' )
    else:
        print( 'Introduzca de 1 a 3' )
        

        






















