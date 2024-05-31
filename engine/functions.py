import tkinter
import tkintermapview

class mapa:

    def __init__(self, titulo, ancho, alto, coord_inicial, zoom_inicial, marcador_1, marcador_2):
        self.root_tk = tkinter.Tk()
        self.root_tk.geometry(f"{ancho}x{alto}")
        self.root_tk.title(titulo)

        # Crear widget mapa
        self.map_widget = tkintermapview.TkinterMapView(self.root_tk, width=ancho, height=alto, corner_radius=0)
        self.map_widget.pack(fill="both", expand=True)

        # Posición inicial y ajuste zoom
        self.map_widget.set_position(*coord_inicial, marker=False)
        self.map_widget.set_zoom(zoom_inicial)

        # Posición marcador
        self.marker_2 = self.map_widget.set_marker(*marcador_1, text="Lugar 1")
        self.marker_3 = self.map_widget.set_marker(*marcador_2, text="Lugar 2")

        # Trazo
        self.path_1 = self.map_widget.set_path([self.marker_2.position, self.marker_3.position, 
                                                (-32.94, -60.63), (-29.18, -58.06)])

    def run(self):
        self.root_tk.mainloop()