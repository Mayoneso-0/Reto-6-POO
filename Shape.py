import math

# Creamos una clase para representar un punto con coordenadas x y
class Point:
    def __init__(self, x=0, y=0):
        # Validar que x e y sean números, si no, mostrar error
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            print("Error: Las coordenadas deben ser números")
            raise ValueError("Error: Las coordenadas deben ser números")
        self.x = x
        self.y = y

# Creamos una clase para representar una línea con un punto de inicio y un punto de fin
class Line:
    def __init__(self, start: "Point" = None, end: "Point" = None
                 , length: float = 0, slope: float = 0):
        # Validar que los puntos no sean None
        if start is None or end is None:
            print("Error: Los puntos de la línea no pueden ser None")
            raise ValueError("Error: Los puntos de la línea no pueden ser None")
        self.start = start
        self.end = end
        self.length = length
        self.slope = slope
    
    # Definimos un método para calcular la longitud de la línea 
    # usando la fórmula de distancia
    def compute_length(self):
        # Validar que los puntos tengan atributos x e y
        if not (hasattr(self.start, 'x') and hasattr(self.start, 'y') and hasattr(self.end, 'x') and hasattr(self.end, 'y')):
            print("Error: Los puntos deben tener atributos x e y")
            raise ValueError("Error: Los puntos deben tener atributos x e y")
        length = ((self.start.x - self.end.x)**2 
                  + (self.start.y - self.end.y)**2)**0.5
        return length
    
    # Definimos un método para calcular la pendiente de la línea 
    # usando la fórmula de la tangente
    def compute_slope(self):
        # Validar que no se divida por cero
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        if dx == 0 and dy == 0:
            print("Error: Los puntos de la línea son iguales, no se puede calcular la pendiente")
            raise ValueError("Error: Los puntos de la línea son iguales, no se puede calcular la pendiente")
        slope = math.atan2(dy, dx) * 180 / math.pi
        return slope

# Definimos la superclase Shape que representa una forma geométrica
class Shape():
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        self.vertices = vertices
        self.edges = edges
        self.inner_angle = inner_angle
        self.is_regular = is_regular

    # Métodos para computar el área, perímetro y ángulo interno de la forma
    # Estos métodos serán sobreescritos por las subclases
    def compute_area(self):
        return "Debe seleccionar una forma para computar su area"
    def compute_perimeter(self):
        return "Debe seleccionar una forma para computar su perimetro"
    def compute_inner_angle(self):
        return "Debe seleccionar una forma para computar sus angulos internos"
    
    # Definimos métodos para obtener y establecer los atributos de la forma
    def get_vertices(self):
        return self.vertices
    def get_edges(self):
        return self.edges
    def get_inner_angle(self):
        return self.inner_angle
    def get_is_regular(self):
        return self.is_regular
    def set_vertices(self, vertices):
        self.vertices = vertices
    def set_edges(self, edges):
        self.edges = edges 
    def set_inner_angle(self, inner_angle):
        self.inner_angle = inner_angle
    def set_is_regular(self, is_regular):
        self.is_regular = is_regular

# Definimos la subclase Triangle que hereda de Shape
class Triangle(Shape):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        # Validar que se proporcionen los datos correctos para un triángulo
        if len(self.vertices) != 3 and len(self.edges) != 3:
            print("Error: Parametros no validos para un Triangulo")
            raise ValueError("Error: Parametros no validos para un Triangulo")
        # Si se proporcionan las aristas completamos los vertices
        if len(self.edges) != 0:
            for e in self.edges:
                if not isinstance(e, Line):
                    print("Error: Las aristas deben ser objetos Line")
                    raise ValueError("Error: Las aristas deben ser objetos Line")
            self.vertices = [self.edges[0].start, self.edges[0].end,
                             self.edges[1].start, self.edges[1].end,
                             self.edges[2].start, self.edges[2].end]
        # Si se proporcionan los vertices completamos las aristas
        elif len(self.vertices) != 0:
            for v in self.vertices:
                if not isinstance(v, Point):
                    print("Error: Los vertices deben ser objetos Point")
                    raise ValueError("Error: Los vertices deben ser objetos Point")
            self.edges = [Line(start = self.vertices[0], end = self.vertices[1]),
                          Line(start = self.vertices[1], end = self.vertices[2]),
                          Line(start = self.vertices[2], end = self.vertices[0]),]
        # Si no se proporcionan los vertices ni las aristas, mostramos un error
        else:
            print("Error: Falta de datos para el triangulo")
            raise ValueError("Error: Falta de datos para el triangulo")
        
    # Definimos un método para calcular el área del triángulo 
    # usando la fórmula de Herón
    def compute_area(self):
        # Si los lados no forman un triángulo válido, puede dar error matemático
        try:
            a = self.edges[0].compute_length()
            b = self.edges[1].compute_length()
            c = self.edges[2].compute_length()
            # Validar que los lados sean positivos
            if a <= 0 or b <= 0 or c <= 0:
                print("Error: Los lados deben ser mayores que cero")
                raise ValueError("Error: Los lados deben ser mayores que cero")
            s = (a + b + c) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            if area <= 0:
                print("Error: El área calculada no es válida")
                raise ValueError("Error: El área calculada no es válida")
            return area
        except Exception as error:
            print(f"Error al calcular el area del triangulo: {error}")
            raise ValueError(f"Error al calcular el area del triangulo: {error}")
    # Definimos un método para calcular el perímetro del triángulo
    def compute_perimeter(self):
        return self.edges[0].compute_length() + \
               self.edges[1].compute_length() + \
               self.edges[2].compute_length()
    # Definimos un método para calcular los ángulos internos del triángulo
    def compute_inner_angle(self):
        self.inner_angle = [abs(self.edges[0].compute_slope() - \
                                self.edges[1].compute_slope()),
                            abs(self.edges[1].compute_slope() - \
                                self.edges[2].compute_slope()),
                            abs(self.edges[2].compute_slope() - \
                                self.edges[0].compute_slope())]
        for i in range(len(self.inner_angle)):
            if self.inner_angle[i] > 180:
                self.inner_angle[i] = 360 - self.inner_angle[i]
        return self.inner_angle

# Definimos la subclase Isosceles que hereda de Triangle
class Isosceles(Triangle):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = False

        # Validamos que se proporcionen los datos correctos 
        # para un triángulo isósceles
        if len(self.vertices) != 3 and len(self.edges) != 3:
            print("Error: Parametros no validos para un Triangulo Isosceles")
        if self.edges[0].compute_length() != self.edges[1].compute_length() and \
           self.edges[1].compute_length() != self.edges[2].compute_length() and \
           self.edges[2].compute_length() != self.edges[0].compute_length():
            print("Error: Lados no forman un Triangulo Isosceles")
    
    # Definimos un metodo para calcular el area, perímetro y
    # ángulos internos del triángulo isósceles
    def compute_area(self):
        return super().compute_area()
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_inner_angle(self):
        return super().compute_inner_angle()

# Definimos la subclase Equilateral que hereda de Triangle
class Equilateral(Triangle):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = True

        # Validamos que se proporcionen los datos correctos 
        # para un triángulo equilátero
        if len(self.vertices) != 3 and len(self.edges) != 3:
            print("Error: Parametros no validos para un Triangulo Equilatero")
        if self.edges[0].compute_length() != self.edges[1].compute_length() or \
           self.edges[1].compute_length() != self.edges[2].compute_length() or \
           self.edges[2].compute_length() != self.edges[0].compute_length():
            print("Error: Lados no forman un Triangulo Equilatero")
    
    # Definimos un método para calcular el área, perímetro y
    # ángulos internos del triángulo equilátero
    def compute_area(self):
        return super().compute_area()
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_inner_angle(self):
        return super().compute_inner_angle()

# Definimos la subclase Scalene que hereda de Triangle
class Scalene(Triangle):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = False

        # Validamos que se proporcionen los datos correctos 
        # para un triángulo escaleno
        if len(self.vertices) != 3 and len(self.edges) != 3:
            print("Error: Parametros no validos para un Triangulo Escaleno")
        if self.edges[0].compute_length() == self.edges[1].compute_length() or \
           self.edges[1].compute_length() == self.edges[2].compute_length() or \
           self.edges[2].compute_length() == self.edges[0].compute_length():
            print("Error: Lados no forman un Triangulo Escaleno")
    
    # Definimos un método para calcular el área, perímetro y
    # ángulos internos del triángulo escaleno
    def compute_area(self):
        return super().compute_area()
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_inner_angle(self):
        return super().compute_inner_angle()
    
# Definimos la subclase TriRectanble que hereda de Triangle
class TriRectanble(Triangle):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = False

        # Validamos que se proporcionen los datos correctos 
        # para un triángulo rectángulo
        if len(self.vertices) != 3 and len(self.edges) != 3:
            print("Error: Parametros no validos para un Triangulo Rectangulo")
        self.compute_inner_angle()
        if 90 not in self.inner_angle:
            print("Error: Lados no forman un Triangulo Rectangulo")
        
    # Definimos un método para calcular el área, perímetro y
    # ángulos internos del triángulo rectángulo
    def compute_area(self):
        return super().compute_area()
    def compute_perimeter(self):
        return super().compute_perimeter()
    def compute_inner_angle(self):
        return super().compute_inner_angle()

# Definimos la subclase Rectangle que hereda de Shape
class Rectangle(Shape):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None, 
                 ancho: float = None, alto: float = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = True
        self.ancho = ancho
        self.alto = alto
        # Validar que se proporcionen los datos correctos para un rectángulo
        if len(self.vertices) != 4 and len(self.edges) != 4:
            print("Error: Parametros no validos para Rectangulo")
            raise ValueError("Error: Parametros no validos para Rectangulo")

        # Se se propicionan las aristas completamos los vertices y el ancho y alto
        if len(self.edges) != 0:
            self.vertices = [self.edges[0].start,self.edges[0].end,
                             self.edges[2].start,self.edges[2].end]
            self.alto = self.edges[0].compute_length()
            self.ancho = self.edges[1].compute_length()
        # Si se proporcionan los vertices completamos las aristas y el ancho y alto
        elif len(self.vertices) != 0:
            self.edges = [Line(start = self.vertices[0], end = self.vertices[1]),
                          Line(start = self.vertices[1], end = self.vertices[2]),
                          Line(start = self.vertices[2], end = self.vertices[3]),
                          Line(start = self.vertices[3], end = self.vertices[0]),]
            self.alto = self.edges[0].compute_length()
            self.ancho = self.edges[1].compute_length()
        # Si no se proporcionan los vertices ni las aristas, mostramos un error
        else:
            print("Error: Falta de datos para el rectangulo")
            raise ValueError("Error: Falta de datos para el rectangulo")
    
    # Definimos un método para calcular el área del rectángulo
    def compute_area(self):
        # Validar que ancho y alto sean positivos
        if self.ancho is None or self.alto is None or self.ancho <= 0 or self.alto <= 0:
            print("Error: El ancho y el alto deben ser mayores que cero")
            raise ValueError("Error: El ancho y el alto deben ser mayores que cero")
        return self.alto*self.ancho
    # Definimos un método para calcular el perímetro del rectángulo
    def compute_perimeter(self):
        return self.alto*2 + self.ancho*2
    # Definimos un método para calcular los ángulos internos del rectángulo
    def compute_inner_angle(self):
        self.inner_angle = [abs(self.edges[0].compute_slope() - \
                                self.edges[1].compute_slope()),
                            abs(self.edges[1].compute_slope() - \
                                self.edges[2].compute_slope()),
                            abs(self.edges[2].compute_slope() - \
                                self.edges[3].compute_slope()),
                            abs(self.edges[3].compute_slope() - \
                                self.edges[0].compute_slope())]
        for i in range(len(self.inner_angle)):
            if self.inner_angle[i] > 180:
                self.inner_angle[i] = 360 - self.inner_angle[i]
        return self.inner_angle

class Square(Rectangle):
    def __init__(self, vertices = [], edges = [],
                 inner_angle = [], is_regular: bool = None):
        super().__init__(vertices, edges, inner_angle, is_regular)
        self.is_regular = True
        # Validar que se proporcionen los datos correctos para un cuadrado
        if len(self.vertices) != 4 and len(self.edges) != 4:
            print("Error: Parametros no validos para Cuadrado")
            raise ValueError("Error: Parametros no validos para Cuadrado")
        # Validar que los lados sean iguales
        if len(self.edges) != 0:
            l0 = self.edges[0].compute_length()
            l1 = self.edges[1].compute_length()
            l2 = self.edges[2].compute_length()
            l3 = self.edges[3].compute_length()
            if l0 != l1 or l1 != l2 or l2 != l3 or l3 != l0:
                print("Error: Lados no forman un cuadrado")
                raise ValueError("Error: Lados no forman un cuadrado")
        elif len(self.vertices) != 0:
            # Validar que los vértices formen un cuadrado (simplificado)
            if self.vertices[0].x != self.vertices[1].x or \
               self.vertices[1].y != self.vertices[2].y or \
               self.vertices[2].x != self.vertices[3].x or \
               self.vertices[3].y != self.vertices[0].y:
                print("Error: Vertices no forman un cuadrado")
                raise ValueError("Error: Vertices no forman un cuadrado")

    # Definimos un método para calcular el área del cuadrado
    def compute_area(self):
        return super().compute_area()
    # Definimos un método para calcular el perímetro del cuadrado
    def compute_perimeter(self):
        return super().compute_perimeter()
    # Definimos un método para calcular los ángulos internos del cuadrado
    def compute_inner_angle(self):
        return super().compute_inner_angle()



# Ejemplo con un cuadrado 
punto1 = Point(0,0)
punto2 = Point(0,2)
punto3 = Point(2,2)
punto4 = Point(2,0)

listaPuntos1 = [punto1, punto2, punto3, punto4]

cuadrado1 = Square(vertices = listaPuntos1)

print("Area del cuadrado:", cuadrado1.compute_area())
print("Perimetro del cuadrado:", cuadrado1.compute_perimeter())
print("Angulos internos del cuadrado:", cuadrado1.compute_inner_angle())

print()
# Ejemplo con un triángulo rectángulo
punto5 = Point(0,0)
punto6 = Point(0,3)
punto7 = Point(4,0)

listaPuntos2 = [punto5, punto6, punto7]

trianguloRectangulo1 = TriRectanble(vertices = listaPuntos2)
print("Area del triangulo rectangulo:", trianguloRectangulo1.compute_area())
print("Perimetro del triangulo rectangulo:", trianguloRectangulo1.compute_perimeter())
print("Angulos internos del triangulo rectangulo:", trianguloRectangulo1.compute_inner_angle())

print()
# Ejemplo de set y get de is_regular
print("El triangulo rectangulo es regular?",trianguloRectangulo1.get_is_regular())
trianguloRectangulo1.set_is_regular(True)
print("El triangulo rectangulo es regular?",trianguloRectangulo1.get_is_regular())

