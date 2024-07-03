import random
import tkinter
import tkinter.font

"""
File: graphics.py
Authors: Chris Piech, Lisa Yan and Nick Troccoli, Daniel Arango Cruz
Version Date: August 19, 2020 """

class Canvas(tkinter.Canvas):
    """ Canvas es una interfaz simplificada sobre el Canvas de tkinter para permitir una manipulación más sencilla de los objetos gráficos.
    Canvas tiene una variedad de funcionalidades para crear, modificar y borrar objetos gráficos, y también obtener información
    sobre el contenido del lienzo.  Canvas es una subclase de `tkinter.Canvas`, por lo que toda la funcionalidad de tkinter también está disponible
    si es necesario."""
    ANCHO_PREDETERMINADO = 754
    """El ancho predeterminado del canvas es de 754."""

    ALTO_PREDETERMINADO = 492
    """El alto predeterminado del canvas es de 492."""

    TITULO_PREDETERMINADO = "Canvas"
    """El texto mostrado en la brrra de titulo del canvas es 'Canvas'."""
    COLORES = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace', 'linen', 'antique white',
              'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 'mint cream',
              'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'dark slate gray', 'dim gray',
              'slate gray', 'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue',
              'dark slate blue', 'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',
              'blue', 'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
              'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise', 'cyan',
              'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
              'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
              'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green', 'forest green',
              'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow', 'light yellow', 'yellow',
              'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown', 'indian red', 'saddle brown',
              'sandy brown', 'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange', 'coral', 'light coral',
              'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink', 'pale violet red', 'maroon',
              'medium violet red', 'violet red', 'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple',
              'medium purple', 'thistle', 'snow2', 'snow3', 'snow4', 'seashell2', 'seashell3', 'seashell4',
              'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4',
              'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'LemonChiffon2',
              'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'ivory2', 'ivory3', 'ivory4',
              'honeydew2', 'honeydew3', 'honeydew4', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2',
              'MistyRose3', 'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
              'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4', 'DodgerBlue2',
              'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2',
              'DeepSkyBlue3', 'DeepSkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1',
              'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4',
              'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue1', 'LightBlue2',
              'LightBlue3', 'LightBlue4', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
              'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'turquoise1',
              'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3', 'cyan4', 'DarkSlateGray1', 'DarkSlateGray2',
              'DarkSlateGray3', 'DarkSlateGray4', 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2',
              'DarkSeaGreen3', 'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
              'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'green2', 'green3', 'green4',
              'chartreuse2', 'chartreuse3', 'chartreuse4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1',
              'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
              'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightYellow2',
              'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4', 'gold2', 'gold3', 'gold4', 'goldenrod1',
              'goldenrod2', 'goldenrod3', 'goldenrod4', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3',
              'DarkGoldenrod4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
              'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1', 'burlywood2',
              'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1', 'tan2', 'tan4', 'chocolate1',
              'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'brown1', 'brown2',
              'brown3', 'brown4', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3',
              'LightSalmon4', 'orange2', 'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3',
              'DarkOrange4', 'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
              'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'HotPink1',
              'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4', 'LightPink1', 'LightPink2',
              'LightPink3', 'LightPink4', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4',
              'maroon1', 'maroon2', 'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
              'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1', 'plum2', 'plum3',
              'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2',
              'DarkOrchid3', 'DarkOrchid4', 'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1',
              'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
              'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10', 'gray11',
              'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20', 'gray21',
              'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray30', 'gray31',
              'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray40', 'gray42',
              'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray50', 'gray51', 'gray52',
              'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62',
              'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72',
              'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82',
              'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
              'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
    """
    Esta es una lista de nombres de todos los colores disponibles para usar graficos en el canvas. Esta lista de colores de
    de Tkinter fue tomada de: https://stackoverflow.com/questions/4969543/colour-chart-for-tkinter-and-tix.
    """

    IZQUIERDA = tkinter.LEFT
    """
    Indicaciones para añadir interactores a diferentes lados del lienzo.  
    IZQUIERDA se refiere al lado izquierdo de la ventana.
    """

    INFERIOR = tkinter.BOTTOM
    """
    Indicaciones para añadir interactores a diferentes lados del lienzo.  
    INFERIOR se refiere al lado inferior de la ventana.
    """

    DERECHA = tkinter.RIGHT
    """
    Indicaciones para añadir interactores a diferentes lados del lienzo.  
    DERECHA se refiere al lado derecho de la ventana.
    """

    SUPERIOR = tkinter.TOP
    """
    Indicaciones para añadir interactores a diferentes lados del lienzo.  
    SUPERIOR se refiere al lado superior de la ventana.
    """
    def __init__(self, width=ANCHO_PREDETERMINADO, height=ALTO_PREDETERMINADO):
        """
        Al crear un lienzo, puede especificar opcionalmente una anchura y una altura.  Si no se especifican anchura y altura
        el lienzo se inicializa con su tamaño por defecto.

        Parametros:
            width: la anchura del lienzo que se va a crear (si no se especifica, se utiliza `Canvas.ANCHO_PREDETERMINADO`)
            height: la altura del lienzo a crear (o si no se especifica, utiliza `Canvas.ALTO_PREDETERMINADO`)
        """

        # Crea la ventana principal
        self.main_window = tkinter.Tk()
        self.main_window.geometry("{}x{}".format(width, height))
        self.main_window.title(self.TITULO_PREDETERMINADO)

        # Crear 4 marcos perimetrales para alojar los botones que se añadan posteriormente
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.bottom_frame.pack(side=Canvas.INFERIOR)

        self.top_frame = tkinter.Frame(self.main_window)
        self.top_frame.pack(side=Canvas.SUPERIOR)

        self.right_frame = tkinter.Frame(self.main_window)
        self.right_frame.pack(side=Canvas.DERECHA)

        self.left_frame = tkinter.Frame(self.main_window)
        self.left_frame.pack(side=Canvas.IZQUIERDA)

        # llamar al constructor tkinter Canvas.
        super().__init__(self.main_window, width=width, height=height, bd=0, highlightthickness=0)

        # Llamadas de retorno opcionales que el cliente puede especificar para cada evento.
        self.on_mouse_pressed = None
        self.on_mouse_released = None
        self.on_key_pressed = None
        self.on_button_clicked = None

        # Rastrea si el ratón está actualmente en la parte superior del lienzo.
        self.mouse_on_canvas = False

        # Lista de pulsaciones de mouse no gestionadas por una devolución de llamada
        self.mouse_presses = []

        # Lista de pulsaciones de teclas no gestionadas por una devolución de llamada
        self.key_presses = []

        # Lista de pulsaciones de botón no gestionadas por una devolución de llamada
        self.button_clicks = []

        # Map of name -> (text field, label) tuple
        self.text_fields = {}

        # Estas son variables de estado para que wait_for_click sepa cuando dejar de esperar y 
        # para no llamar a los manejadores cuando estamos esperando el click
        self.wait_for_click_click_happened = False
        self.currently_waiting_for_click = False

        # vincular eventos
        self.focus_set()
        self.bind("<Button-1>", lambda event: self.__mouse_presionado(event))
        self.bind("<ButtonRelease-1>", lambda event: self.__mouse_liberado(event))
        self.bind("<Key>", lambda event: self.__tecla_presionada(event))
        self.bind("<Enter>", lambda event: self.__mouse_entrado())
        self.bind("<Leave>", lambda event: self.__mouse_salido())

        self._image_gb_protection = {}
        self.pack()
        self.update()
    def establecer_color_fondo_lienzo(self, color):
        """
        Establece el color de fondo del lienzo a la cadena de color especificada.
        Args:
            color: el color (String) para establecer el fondo del lienzo.
        """
        self.config(background=color)
    def obtener_color_fondo_lienzo(self):
        """
        Obtiene el nombre del color de fondo del lienzo.
        Devuelve:
            El color del fondo del lienzo, como cadena.
        """
        return self["background"]
    def obtener_ancho_lienzo(self):
        """
        Obtiene el ancho del lienzo.
        Devuelve:
            La anchura actual del lienzo.
        """
        return self.winfo_width()
    def obtener_altura_lienzo(self):
        """
        Obtiene la altura del lienzo.
        Devuelve:
            La altura actual del lienzo.
        """
        return self.winfo_height()
    def establecer_titulo_lienzo(self, title):
        """
        Establece que el texto del título mostrado en la barra de título de la ventana del lienzo sea el texto especificado.
        Args:
            title: el texto a mostrar en la barra de título
        """
        self.main_window.title(title)
    def establecer_tamanio_lienzo(self, ancho, alto):
        """
        Establece el tamaño del lienzo y de la ventana que lo contiene a la anchura y altura especificadas.

        Args:
            ancho: anchura del lienzo y de la ventana que lo contiene
            alto: altura del lienzo y de la ventana que lo contiene.
        """
        self.main_window.geometry("{}x{}".format(ancho, alto))
        self.config(width=ancho, height=alto)
    
    """ ----------- MANEJADOR DE EVENTOS --------------------- """
    def establecer_mouse_presionado(self, callback):
        """
        Establece la función especificada para que sea llamada cada vez que se pulse el ratón.  Si se llama a esta función
        varias veces, sólo se llamará a la última función especificada cuando se pulse el ratón.

        Args:
            callback: una función a llamar cada vez que se pulse el ratón.  Debe recibir dos parámetros, que
                son las coordenadas x e y (en ese orden) de la pulsación del ratón que acaba de producirse.  Por ejemplo, func(x, y).  Si
                este parámetro es None, no se llamará a ninguna función cuando se pulse el ratón.
        """
        self.on_mouse_pressed = callback

    def establecer_mouse_liberado(self, callback):
        """
        Establece la función especificada que se llamará cada vez que se suelte el ratón.  Si se llama a esta función
        varias veces, sólo se llamará a la última función especificada cuando se suelte el ratón.

        Args:
            callback: una función a llamar cada vez que se suelta el ratón.  Debe recibir dos parámetros, que
                son las coordenadas x e y (en ese orden) del ratón que se acaba de soltar.  Por ejemplo, func(x, y).
                Si este parámetro es None, no se llamará a ninguna función cuando se suelte el ratón.
        """
        self.on_mouse_released = callback

    def establecer_tecla_presionada(self, callback):
        """
        Establece la función especificada para que sea llamada cada vez que se pulse una tecla del teclado.  Si se llama a esta función
        varias veces, sólo se llamará a la última función especificada cuando se pulse una tecla.

        Args:
            callback: una función a llamar cada vez que se pulsa una tecla.  Debe recibir un parámetro, que
                es el nombre de texto de la tecla que se acaba de pulsar (por ejemplo, 'a' para la tecla a, 'b' para la tecla b, etc).
                Por ejemplo, func(tecla_char).  Si este parámetro es None, no se llamará a ninguna función cuando se pulse una tecla.
        """
        self.on_key_pressed = callback

    def establecer_boton_clickeado(self, callback):
        """
        Establece la función especificada que se llamará cada vez que se haga clic en un botón.  Si se llama a esta función
        varias veces, sólo se llamará a la última función especificada cuando se pulse un botón.

        Args:
            callback: una función a llamar cada vez que se pulsa un botón.  Debe recibir un parámetro, que
                es el nombre del texto del botón que se acaba de pulsar.
                Por ejemplo, func(nombre_boton).  Si este parámetro es None, no se llamará a ninguna función cuando se pulse un botón.
        """
        self.on_button_clicked = callback

    def __boton_clickeado(self, title):
        """
        Llamada cada vez que se pulsa un botón.  Si tenemos un manejador de clic de botón registrado, llámalo.  Si no,
        añade el botón pulsado a la lista de botones pulsados que se manejarán más tarde.

        Args:
            title: el nombre del botón pulsado.
        """
        if self.on_button_clicked:
            self.on_button_clicked(title)
        else:
            self.button_clicks.append(title)

    def obtener_nuevos_clics_mouse(self):
        """
        Devuelve una lista de todos los clics de ratón que se han producido desde la última llamada a esta función o a cualquier
        ratón registrado.

        Devuelve:
            Una lista de todos los clics de ratón que se han producido desde la última llamada a esta función o a cualquier manejador de ratón registrado.
                controlador de ratón registrado.  Cada clic del ratón contiene propiedades x e y para la ubicación del clic, por ejemplo
                clics = canvas.obtener_nuevos_clics_del_mouse(); print(clics[0].x).
        """
        presses = self.mouse_presses
        self.mouse_presses = []
        return presses
    def obtener_nuevos_clics_boton(self):
        """
        Devuelve una lista de todas las pulsaciones de botón que se han producido desde la última llamada a esta función o a cualquier
        registrado.

        Devuelve
            una lista de todas las pulsaciones de botón que se han producido desde la última llamada a esta función o a cualquier gestor de botones registrado.
                registrado.  Cada clic de botón es el nombre del botón pulsado, por ejemplo
                clicks = canvas.obtener_nuevos_clics_de_boton(); print(clicks[0]).
        """
        clicks = self.key_presses
        self.key_presses = []
        return clicks

    def __mouse_presionado(self, event):
        """
        Llamada cada vez que se pulsa el ratón.  Si estamos esperando un clic del ratón mediante
        wait_for_click, no se hace nada.  De lo contrario, si tenemos un controlador de pulsación de ratón registrado, llámalo.  En caso contrario,
        añade la pulsación a la lista de pulsaciones de ratón que se gestionarán más tarde.

        Args:
            event: un objeto que representa la pulsación del ratón que acaba de ocurrir.  Se supone que tiene propiedades x e y
                que contienen las coordenadas x e y de la pulsación del ratón.
        """
        if not self.currently_waiting_for_click and self.on_mouse_pressed:
            self.on_mouse_pressed(event.x, event.y)
        elif not self.currently_waiting_for_click:
            self.mouse_presses.append(event)

    def __mouse_liberado(self, event):
        """
        Llamada cada vez que se suelta el ratón.  Si estamos esperando un clic del ratón mediante
        wait_for_click, actualiza nuestro estado para reflejar que se ha producido un clic.  De lo contrario, si tenemos un manejador
        release, llámalo.

        Args:
            event: un objeto que representa la liberación del ratón que acaba de ocurrir.  Se supone que tiene propiedades x e y
                que contienen las coordenadas x e y de esta liberación del ratón.
        """

        # Hacer todo esto de una sola vez para evitar el establecimiento de clic sucedido a True,
        # a continuación, tener que esperar a que el conjunto clic actualmente en espera a falso, entonces vamos
        if self.currently_waiting_for_click:
            self.wait_for_click_click_happened = True
            return

        self.wait_for_click_click_happened = True
        if self.on_mouse_released:
            self.on_mouse_released(event.x, event.y)

    def __tecla_presionada(self, event):
        """
        Llamada cada vez que se pulsa una tecla del teclado.  Si tenemos un controlador de pulsación de tecla registrado, llámalo.  Si no,
        añade la pulsación de tecla a la lista de pulsaciones de tecla que se gestionarán más tarde.

        Args:
            event: un objeto que representa la pulsación de tecla que acaba de ocurrir.  Se supone que tiene una propiedad keysym
                que contiene el nombre de esta pulsación de tecla.
        """
        if self.on_key_pressed:
            self.on_key_pressed(event.keysym)
        else:
            self.key_presses.append(event)

    def __mouse_entrado(self):
        """
        Llamado cada vez que el ratón entra en el lienzo.  Actualiza el estado interno para registrar que
        el ratón está actualmente en el lienzo.
        """
        self.mouse_on_canvas = True

    def __mouse_salido(self):
        """
        Llamado cada vez que el ratón sale del lienzo.  Actualiza el estado interno para registrar que
        que el ratón no está actualmente en el lienzo.
        """
        self.mouse_on_canvas = False

    def mouse_esta_sobre_lienzo(self):
        """
        Devuelve si el ratón está actualmente sobre el lienzo.

        Devuelve:
            True si el ratón está actualmente sobre el lienzo, o False en caso contrario.
        """
        return self.mouse_on_canvas

    def esperar_por_clic(self):
        """
        Espera hasta que un clic de mouse ocurre, luego retorna.
        """
        self.currently_waiting_for_click = True
        self.wait_for_click_click_happened = False
        while not self.wait_for_click_click_happened:
            self.update()
        self.currently_waiting_for_click = False
        self.wait_for_click_click_happened = False

    def obtener_mouse_x(self):
        """
        Devuelve la posición X actual del ratón en el lienzo.

        Devuelve:
            La posición X actual del ratón en el lienzo.
        """
        """
        Nota: winfo_pointerx es la posición absoluta del ratón (en la pantalla, no en la ventana),
              winfo_rootx es la posición absoluta de la ventana (en la pantalla).
        Dado que move tiene en cuenta la posición relativa a la ventana,
        ajustamos este mouse_x para que sea la posición relativa a la ventana.
        """
        return self.winfo_pointerx() - self.winfo_rootx()
    def obtener_mouse_y(self):
        """
        Devuelve la posición Y actual del ratón en el lienzo.

        Devuelve:
            La posición Y actual del ratón en el lienzo.
        """
        """
        Nota: winfo_pointerx es la posición absoluta del ratón (en la pantalla, no en la ventana),
              winfo_rootx es la posición absoluta de la ventana (en la pantalla).
        Dado que move tiene en cuenta la posición relativa a la ventana,
        ajustamos este mouse_x para que sea la posición relativa a la ventana.
        """
        return self.winfo_pointery() - self.winfo_rooty()

    def __get_frame_and_pack_location_for_location(self, location):
        """
        Returns the frame and pack location that should be used for an interactor given the
        specified interactor location on the canvas.

        Args:
            location: the region (Canvas.TOP/LEFT/BOTTOM/RIGHT) to get the frame and pack location for.

        Returns:
            First, the frame, and second, the pack location, for the given interactor location.
            For instance, for the top and bottom locations, the pack location should be Canvas.LEFT
            to align interactors left to right.
        """
        frame = self.top_frame
        pack_location = Canvas.IZQUIERDA
        if location == Canvas.INFERIOR:
            frame = self.bottom_frame
        elif location == Canvas.IZQUIERDA:
            frame = self.left_frame
            pack_location = Canvas.SUPERIOR
        elif location == Canvas.DERECHA:
            frame = self.right_frame
            pack_location = Canvas.SUPERIOR

        return frame, pack_location

    def crear_boton(self, title, location, **kwargs):
        """
        Añade un botón al lienzo con el título especificado en la ubicación especificada.  Los botones se añaden de izquierda
        a la derecha en la parte superior e inferior de la ventana y de arriba a abajo en los lados de la ventana.

        Args:
            title: el título a mostrar en el botón.  Debe ser único entre los nombres de los botones.
            location: la región (Canvas.TOP/LEFT/BOTTOM/RIGHT) donde el botón debe ser añadido alrededor del lienzo.
            kwargs: otras palabras clave de tkinter.

        Devuelve:
            una referencia al botón añadido a la ventana en la ubicación especificada.  Utilícelo con la función .destroy()
            para eliminar el botón más tarde si es necesario.  Por ejemplo button = crear_boton(...); button.destroy();
        """
        frame, pack_location = self.__get_frame_and_pack_location_for_location(location)
        button = tkinter.Button(frame, text=title, command=lambda: self.__boton_clickeado(title), **kwargs)
        button.pack(side=pack_location)
        self.update()
        return button

    def crear_campo_texto(self, label, location, **kwargs):
        """
        Adds a label and text field pair to the canvas with the specified label text at the specified location.
        Interactors are added from left to right at the top and bottom of the window and top to bottom on the sides
        of the window.  Stores a reference to this text field in the Canvas map of text fields.

        Args:
            label: the label text to display next to the text field, and the name of the text field.
                Must be unique among text field names.
            location: the region (Canvas.TOP/LEFT/BOTTOM/RIGHT) where the label/text field
                should be added around the canvas.
            kwargs: other tkinter keyword args for the text field

        Returns:
            a reference to the text field and the label (in that order) added to the window at the specified location.
        """
        frame, pack_location = self.__get_frame_and_pack_location_for_location(location)
        text_field_label = tkinter.Label(frame, text=label)
        text_field_label.pack(side=pack_location)
        text_field = tkinter.Entry(frame, **kwargs)
        text_field.pack(side=pack_location)
        self.text_fields[label] = (text_field, text_field_label)
        self.update()
        return text_field, text_field_label

    def eliminar_campo_texto(self, text_field_name):
        """
        Elimina el campo de texto y la etiqueta correspondiente tanto del lienzo como de las estructuras de datos internas
        de los campos de texto.

        Args:
            nombre_campo_texto: el nombre dado al crear el campo de texto.
        """
        if text_field_name in self.text_fields:
            self.text_fields[text_field_name][0].destroy()
            self.text_fields[text_field_name][1].destroy()
            del self.text_fields[text_field_name]
            self.update()

    def obtener_texto_de_campo_text(self, text_field_name):
        """
        Devuelve el contenido actual del campo de texto con el nombre especificado.

        Args:
            nombre_campo_texto: el nombre dado al crear el campo de texto.

        Devuelve:
            el contenido actual del campo de texto dado, o None si no hay campo de texto con el nombre dado.
        """
        if text_field_name in self.text_fields:
            return self.text_fields[text_field_name][0].get()
        else:
            return None

    """ ----------- MANIPULACION DE OBJETOS GRAFICOS ---------- """

    def obtener_x_izquierda(self, obj):
        """
        Devuelve la coordenada x más a la izquierda del objeto gráfico especificado.

        Args:
            obj: el objeto para el que calcular la coordenada x más a la izquierda

        Devuelve:
            La coordenada x más a la izquierda del objeto gráfico especificado.
        """
        if self.type(obj) != "text":
            return self.coords(obj)[0]
        else:
            return self.coords(obj)[0] - self.obtener_ancho(obj) / 2

    def obtener_top_y(self, obj):
        """
        Devuelve la coordenada Y superior del objeto gráfico especificado.

        Args:
            obj: objeto para el que se calcula la coordenada y superior

        Devuelve
            La coordenada y superior del objeto gráfico especificado.
        """
        if self.type(obj) != "text":
            return self.coords(obj)[1]
        else:
            return self.coords(obj)[1] - self.obtener_altura(obj) / 2
    def obtener_ancho(self, obj):
        """
        Devuelve la anchura del objeto gráfico especificado.

        Args:
            obj: el objeto para el que calcular la anchura

        Devuelve:
            La anchura del objeto gráfico especificado.
        """
        if len(self.coords(obj)) == 2:  # coordenadas de dos dimensiones
            return self.bbox(obj)[2] - self.bbox(obj)[0]
        return self.coords(obj)[2] - self.coords(obj)[0]

    def obtener_altura(self, obj):
        """
        Devuelve la altura del objeto gráfico especificado.

        Args:
            obj: el objeto para el que calcular la altura

        Devuelve:
            La altura del objeto gráfico especificado.
        """
        if len(self.coords(obj)) == 2:  # coordenadas de dos dimensiones
            return self.bbox(obj)[3] - self.bbox(obj)[1]
        return self.coords(obj)[3] - self.coords(obj)[1]

    def mover_hacia(self, obj, new_x, new_y):
        """
        Similar a `Canvas.moverse`.
        """
        # Note: Implementa manualmente debido a inconsistencias en algunas máquinas de bbox vs. coord.
        old_x = self.obtener_x_izquierda(obj)
        old_y = self.obtener_top_y(obj)
        self.move(obj, new_x - old_x, new_y - old_y)

    def moverse_hacia(self, obj, x='', y=''):
        """
        Mueve el objeto gráfico especificado a la ubicación especificada, que es la nueva esquina superior izquierda de su cuadro delimitador.
        nueva esquina superior izquierda.

        Args:
            obj: el objeto a mover
            x: nueva coordenada x de la esquina superior izquierda del objeto
            y: nueva coordenada y de la esquina superior izquierda del objeto
        """
        self.mover_hacia(obj, float(x), float(y))

    def moverse(self, obj, dx, dy):
        """
        Mueve el objeto gráfico especificado en las cantidades especificadas en las direcciones x e y.

        Args:
            obj: objeto a mover
            dx: la cantidad en la que cambia la posición x del objeto
            dy: cantidad en la que se modifica la posición y del objeto.
        """
        super(Canvas, self).move(obj, dx, dy)

    def establecer_tamanio(self, obj, width, height):
        """
        Establece la anchura y la altura del objeto gráfico especificado.  No puede utilizarse para cambiar el tamaño de una imagen.

        Args:
            obj: el objeto cuya anchura y altura se desea modificar
            width: nueva anchura del objeto
            Altura: nueva altura del objeto
        """
        if self.type(obj) == "image":
            assert False, "El tamaño de la imagen no se puede cambiar después de crearla"
        x = self.obtener_x_izquierda(obj)
        y = self.obtener_top_y(obj)
        self.coords(obj, x, y, x + width, y + height)

    def eliminar(self, obj):
        """
        Elimina del lienzo el objeto gráfico especificado.

        Args:
            obj: el objeto gráfico a eliminar del lienzo
        """
        super(Canvas, self).delete(obj)

    def eliminar_todo(self):
        """
        Remover todos los objetos graficos del canvas.
        """
        super(Canvas, self).delete('all')

    def establecer_oculto(self, obj, hidden):
        """
        Establece el objeto gráfico dado para que esté oculto o visible en el lienzo.

        Args:
            obj: el objeto gráfico a ocultar o hacer visible en el lienzo.
            oculto: True si el objeto debe estar oculto, False si el objeto debe estar visible.
        """
        self.itemconfig(obj, state='hidden' if hidden else 'normal')

    def esta_oculto(self, obj):
        """
        Obtiene si el objeto gráfico dado está oculto o visible en el lienzo.

        Args:
            obj: el objeto gráfico cuyo estado se desea obtener

        Devuelve:
            True si el objeto gráfico dado está oculto, o False en caso contrario.
        """
        return self.itemcget(obj, "state") == 'hidden'

    def encontrar_elemento_en(self, x, y):
        """
        Busca el elemento superior que se superpone a esta ubicación.

        Args:
            x: coordenada x de la posición
            y: coordenada y de la ubicación

        Devuelve
            El objeto gráfico situado más arriba en el lienzo en esta posición (Ninguno en caso contrario)
        """
        closest = self.find_closest(x, y)[0]

        closest_left_x = self.obtener_x_izquierda(closest)
        closest_right_x = closest_left_x + self.obtener_ancho(closest)
        closest_top_y = self.obtener_top_y(closest)
        closest_bottom_y = closest_top_y + self.obtener_altura(closest)

        # Si este objeto contiene por completo este punto, devuélvelo.  De lo contrario, no hay ningún objeto aquí.
        if closest_left_x <= x <= closest_right_x and closest_top_y <= y <= closest_bottom_y:
            return closest

        return None

    def encontrar_superposicion(self, x1, y1, x2, y2):
        """
        Obtiene una lista de objetos gráficos del lienzo que se solapan con la caja delimitadora especificada.

        Args:
            x1: coordenada x de la esquina superior izquierda del cuadro delimitador
            y1: coordenada y de la esquina superior izquierda del cuadro delimitador
            x2: coordenada x de la esquina inferior derecha del cuadro delimitador
            y2: coordenada y de la esquina inferior derecha del cuadro delimitador

        Devuelve
            una lista de objetos gráficos del lienzo que se solapan con este cuadro delimitador.
        """
        return super(Canvas, self).find_overlapping(x1, y1, x2, y2)

    def encontrar_todos_los_objetos(self):
        """
        Obtiene una lista de todos los objetos gráficos del lienzo.

        Devuelve:
            Una lista de todos los objetos gráficos en el lienzo.
        """
        return super(Canvas, self).find_all()

    def obtener_color_aleatorio(self):
        """
        Devuelve un color seleccionado aleatoriamente.

        Devuelve:
            Un color seleccionado aleatoriamente, en forma de cadena.
        """
        return random.choice(self.COLORES)

    def establecer_color_relleno(self, obj, fill_color):
        """
        Establece el color de relleno del objeto gráfico especificado.  No se puede utilizar para cambiar el color de relleno
        de objetos no rellenables como imágenes - lanza un tkinter.TclError.

        Args:
            obj: el objeto para el que establecer el color de relleno
            fill_color: el color de relleno, como una cadena.  Si es una cadena vacía,
                el objeto no se rellenará.
        """
        try:
            self.itemconfig(obj, fill=fill_color)
        except tkinter.TclError:
            raise tkinter.TclError("You can't set the fill color on this object")

    def obtener_color_relleno(self, obj):
        """
        Obtiene el color de relleno del objeto gráfico especificado.  No se puede utilizar para obtener el color de relleno
        de objetos no rellenables como imágenes - lanza un tkinter.TclError.

        Args:
            obj: el objeto para el que se establece el color de relleno

        Devuelve:
            El color de relleno actual del objeto, como cadena.  Si es la cadena vacía
                el objeto no se rellena.
        """
        try:
            return self.itemcget(obj, 'fill')
        except tkinter.TclError:
            raise tkinter.TclError("You can't get the fill color of this object")

    def establecer_color_contorno(self, obj, outline_color):
        """
        Establece el color del contorno del objeto gráfico especificado.  No puede usarse para cambiar el color del contorno de objetos no contorneados, como imágenes o texto.
        de objetos no contorneados como imágenes o texto - lanza un tkinter.TclError.

        Args:
            obj: el objeto para el que se establece el color del contorno
            outline_color: el color del contorno, como una cadena.  Si es una cadena vacía,
                el objeto no tendrá contorno.
        """
        try:
            self.itemconfig(obj, outline=outline_color)
        except tkinter.TclError:
            raise tkinter.TclError("You can't set the outline color on this object")

    def obtener_color_contorno(self, obj):
        """
        Obtiene el color del contorno del objeto gráfico especificado.  No se puede utilizar para obtener el color del contorno
        de objetos no contorneados como imágenes o texto - arroja un tkinter.TclError.

        Args:
            obj: el objeto del que se desea obtener el color del contorno

        Devuelve:
            El color del contorno del objeto dado, como una cadena.  Si es la cadena vacía
                el objeto no tiene contorno.
        """
        try:
            return self.itemcget(obj, 'outline')
        except tkinter.TclError:
            raise tkinter.TclError("You can't get the outline color of this object")

    def establecer_color(self, obj, color):
        """
        Establece el color de relleno y contorno del objeto gráfico especificado.  Si el objeto no
        tiene uno o más colores de relleno o contorno, el ajuste de ese color se ignora.

        Args:
            obj: el objeto para el que se establece el color
            color: el color de relleno y contorno, en forma de cadena.  Si la cadena está vacía
                el objeto no tendrá relleno ni contorno.
        """
        try:
            self.establecer_color_relleno(obj, color)
        except tkinter.TclError:
            pass

        try:
            self.establecer_color_contorno (obj, color)
        except tkinter.TclError:
            pass

    def establecer_ancho_contorno(self, obj, width):
        """
        Establece el grosor del contorno del objeto gráfico especificado.  No puede utilizarse en objetos
        que no se pueden contornear, como imágenes o texto.

        Args:
            obj: objeto para el que se fija el grosor del contorno
            width: anchura del contorno.
        """
        self.itemconfig(obj, width=width)

    def crear_linea(self, x1, y1, x2, y2, *args, **kwargs):
        """
        Crea y devuelve un objeto gráfico de línea en la pantalla desde el punto especificado hasta el punto especificado.
        La línea se dibuja en negro.

        Args:
            x1: posición x inicial de la línea
            y1: posición y inicial de la línea
            x2: posición x final de la línea
            y2: posición y final de la línea
            args: puedes especificar opcionalmente puntos adicionales en la línea o forma
            kwargs: otros argumentos de palabras clave de tkinter

        Devuelve
            el objeto línea gráfica entre los dos puntos especificados.
        """
        return super(Canvas, self).create_line(x1, y1, x2, y2, *args, **kwargs)

    def crear_rectangulo(self, x1, y1, x2, y2, *args, **kwargs):
        """
        Crea y devuelve un objeto gráfico rectángulo en la pantalla con su esquina superior izquierda en la primera coordenada
        y su esquina inferior derecha en la segunda coordenada.  El rectángulo se dibuja sin rellenar con un contorno negro.

        Args:
            x1: posición x superior izquierda del rectángulo
            y1: coordenada y superior izquierda del rectángulo
            x2: coordenada x inferior derecha del rectángulo
            y2: posición y inferior derecha del rectángulo
            kwargs: otros argumentos de palabras clave tkinter

        Devuelve
            el objeto rectángulo gráfico en la posición especificada.
        """
        return super(Canvas, self).create_rectangle(x1, y1, x2, y2, **kwargs)

    def crear_ovalo(self, x1, y1, x2, y2, **kwargs):
        """
        Crea y devuelve un objeto gráfico ovalado en la pantalla contenido dentro de la caja delimitadora cuya esquina superior izquierda es la primera coordenada y cuya esquina inferior derecha es la segunda coordenada.
        es la primera coordenada y cuya esquina inferior derecha es la segunda coordenada.  El óvalo se dibuja
        con un contorno negro.

        Args:
            x1: la posición x superior izquierda de la caja delimitadora
            y1: coordenada y superior izquierda del cuadro delimitador
            x2: posición x inferior derecha del cuadro delimitador
            y2: posición y inferior derecha del cuadro delimitador
            kwargs: otros argumentos de palabras clave de tkinter

        Devuelve
            el objeto gráfico ovalado en la posición especificada.
        """
        return super(Canvas, self).create_oval(x1, y1, x2, y2, **kwargs)

    def crear_texto(self, x, y, text, **kwargs):
        """
        Crea y devuelve un objeto gráfico de texto en la pantalla en la ubicación especificada con el texto especificado.
        Las posiciones x e y especificadas corresponden al centro del texto.  El texto tendrá una fuente de tamaño 13.

        Args:
            x: posición x del centro del texto
            y: la posición y del centro del texto
            text: el texto que debe mostrarse en el lienzo en la posición dada
            kwargs: otras palabras clave de tkinter

        Devuelve
            el objeto texto gráfico que muestra el texto especificado en la posición especificada.
        """
        return super().create_text(x, y, text=text, **kwargs)

    def establecer_texto(self, obj, text):
        """
        Establece el texto mostrado por el objeto de texto dado.  No puede utilizarse en ningún objeto gráfico que no sea de texto.

        Args:
            obj: el objeto de texto cuyo texto se va a mostrar
            text: el nuevo texto a mostrar para este objeto gráfico
        """
        self.itemconfig(obj, text=text)

    def obtener_texto(self, obj):
        """
        Devuelve el texto mostrado por el objeto de texto dado.  No puede utilizarse en ningún objeto gráfico que no sea de texto.

        Args:
            obj: el objeto de texto del que se desea obtener el texto mostrado

        Devuelve
            El texto mostrado actualmente por este objeto gráfico.
        """
        return self.itemcget(obj, 'text')

    def establecer_fuente(self, obj, font, size):
        """
        Establece la fuente y el tamaño del texto mostrado por el objeto de texto dado.  No puede utilizarse en ningún objeto
        objeto gráfico.

        Args:
            obj: el objeto de texto para el que se va a establecer la fuente y el tamaño
            font: el nombre de la fuente, en forma de cadena
            size: el tamaño de la fuente.
        """
        self.itemconfig(obj, font=(font, size))

    def traer_al_frente(self, obj):
        """
        Envía el objeto dado al frente de todos los demás objetos del lienzo.

        Args:
            obj: el objeto a poner al frente de los objetos del lienzo
        """
        self.traer_al_frente_de(obj, 'all')

    def traer_al_frente_de(self, obj, above):
        """
        Establece que el primer objeto esté directamente delante del segundo en el orden Z del lienzo.  En otras palabras
        el primer objeto aparecerá ahora delante del segundo objeto y de todos los objetos detrás del segundo objeto,
        pero detrás de todos los objetos detrás de los que también esté el segundo objeto.

        Args:
            obj: el objeto a poner delante del segundo objeto
            above: el objeto que hay que poner directamente delante del primer objeto
        """
        self.tag_raise(obj, above)

    def enviar_al_fondo(self, obj):
        """
        Envía el objeto dado a estar detrás de todos los demás objetos en el lienzo

        Args:
            obj: el objeto a colocar detrás de todos los demás objetos del lienzo
        """
        self.enviar_detras_de(obj, 'all')

    def enviar_detras_de(self, obj, behind):
        """
        Establece que el primer objeto esté directamente detrás del segundo en el orden Z del lienzo.  En otras palabras
        el primer objeto aparecerá directamente detrás del segundo objeto y de todos los objetos delante del
        segundo objeto, pero delante de todos los objetos de los que el segundo objeto también esté delante.

        Args:
            obj: el objeto a poner delante del segundo objeto
            behind: el objeto detrás del cual se situará el primer objeto
        """
        self.tag_lower(obj, behind)

    def crear_imagen(self, x, y, file_path, **kwargs):
        """
        Crea una imagen con el nombre de archivo especificado en la posición especificada en el lienzo.  La imagen
        tendrá el mismo tamaño que el archivo de imagen cargado.

        Args:
            x: coordenada x de la esquina superior izquierda de la imagen en el lienzo
            y: coordenada y de la esquina superior izquierda de la imagen en el lienzo
            file_path: la ruta al archivo de imagen para cargar y mostrar en el lienzo
            kwargs: otras palabras clave de tkinter

        Devuelve
            el objeto imagen gráfica que muestra la imagen especificada en la ubicación especificada.
        """
        return self.__crear_imagen_con_tamanio_opcional(x, y, file_path, **kwargs)

    def crear_imagen_con_tamanio(self, x, y, width, height, file_path, **kwargs):
        """
        Crea una imagen con el nombre de archivo especificado en la posición especificada en el lienzo, y redimensionada
        a la anchura y altura especificadas.

        Args:
            x: coordenada x de la esquina superior izquierda de la imagen en el lienzo
            y: coordenada y de la esquina superior izquierda de la imagen en el lienzo
            anchura: anchura de la imagen
            altura: la altura de la imagen
            file_path: la ruta del archivo de imagen a cargar y mostrar en el lienzo
            kwargs: otras palabras clave de tkinter

        Devuelve
            el objeto imagen gráfica que muestra la imagen especificada en la ubicación especificada con el
                tamaño especificado.
        """
        return self.__crear_imagen_con_tamanio_opcional(x, y, file_path, width=width, height=height, **kwargs)

    def __crear_imagen_con_tamanio_opcional(self, x, y, file_path, width=None, height=None, **kwargs):
        """
        Crea una imagen con el nombre de archivo especificado en la posición especificada en el lienzo.
        Opcionalmente, especifique la anchura y la altura para cambiar el tamaño de la imagen.

        Args:
            x: coordenada x de la esquina superior izquierda de la imagen en el lienzo
            y: coordenada y de la esquina superior izquierda de la imagen en el lienzo
            ruta_archivo: ruta del archivo de imagen que se cargará y mostrará en el lienzo
            anchura: anchura opcional de la imagen.  Si no hay ninguna, se utiliza la anchura del archivo de imagen.
            height: altura opcional a incluir para la imagen. Si no hay ninguna, utiliza la altura del archivo de imagen.
            kwargs: otras palabras clave de tkinter.

        Devuelve
            el objeto imagen gráfica que muestra la imagen especificada en la ubicación especificada.
        """
        from PIL import ImageTk
        from PIL import Image
        image = Image.open(file_path)

        # Resize the image if another width and height is specified
        if width is not None and height is not None:
            image = image.resize((width, height))

        image = ImageTk.PhotoImage(image)
        img_obj = super().create_image(x, y, anchor="nw", image=image, **kwargs)
        # note: if you don't do this, the image gets garbage collected!!!
        # this introduces a memory leak which can be fixed by overloading delete
        self._image_gb_protection[img_obj] = image
        return img_obj



        
        

