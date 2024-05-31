from engine.functions import mapa

# Reemplace los valores de las variables con sus datos
# Las coordenadas pueden sacarse desde google maps

#Crear un mapa
titulo = "Título de la ventana"    #Modifique el titulo
ancho = 856                        # Ancho de la ventana
alto = 645                         # Alto de la ventana
coord_inicial = (-30.95, -59.04)   # Posición del mapa
zoom_inicial = 7                   # 'Acercamiento' de la vista
marcador_1 = (-32.94, -60.63)      # Marcador de la posición 1
marcador_2 = (-29.18, -58.06)      # Marcador de la posicion 2

ventana = mapa(titulo, ancho, alto, coord_inicial, zoom_inicial, marcador_1, marcador_2)

#Correr la ventana
ventana.run()