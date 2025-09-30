# POO_AP_171_N2
Proyecto desarrollo modular de POO

<h1>Modularización de un Proyecto POO</h1>

<p>
La modularización en un proyecto de Programación Orientada a Objetos consiste en dividir el sistema en partes bien definidas y organizadas, cada una con responsabilidades específicas. 
Esto favorece la reutilización, el mantenimiento, la escalabilidad y la claridad del código.
</p>

<h2>Módulos del Proyecto</h2>

<h3>1. Módulo Auxiliares</h3>
<ul>
  <li>Contiene clases y funciones de apoyo que no pertenecen directamente a la lógica principal del negocio pero que resultan necesarias para el correcto funcionamiento del sistema.</li>
  <li>Ejemplos: validaciones, conversiones de formatos, manejo de fechas, utilidades matemáticas o de cadenas.</li>
  <li>Su objetivo es centralizar la lógica de apoyo para evitar duplicación de código.</li>
</ul>

<h3>2. Módulo Datos</h3>
<ul>
  <li>Encargado de la persistencia y acceso a la información.</li>
  <li>Implementa clases y métodos para la conexión a bases de datos, lectura/escritura de archivos o interacción con servicios externos de almacenamiento.</li>
  <li>Aísla el manejo de datos de las demás capas, lo que permite cambiar la fuente de información sin afectar la lógica de negocio.</li>
</ul>

<h3>3. Módulo Negocio</h3>
<ul>
  <li>Contiene la lógica principal del sistema.</li>
  <li>Implementa reglas de negocio, cálculos, procesos y flujos que definen cómo funciona la aplicación.</li>
  <li>Se apoya en los módulos de datos y auxiliares, pero mantiene independencia de la interfaz de usuario.</li>
</ul>

<h3>4. Módulo Modelos</h3>
<ul>
  <li>Define las clases que representan las entidades principales del dominio del problema.</li>
  <li>Cada modelo encapsula atributos y comportamientos propios de la entidad (por ejemplo: Cliente, Producto, Pedido).</li>
  <li>Sirven como base para la comunicación entre los diferentes módulos, especialmente entre la lógica de negocio y los datos.</li>
</ul>

<h3>5. Módulo GUI (Interfaz Gráfica de Usuario)</h3>
<ul>
  <li>Proporciona la interacción con el usuario mediante ventanas, formularios o componentes visuales.</li>
  <li>Se comunica con el módulo de negocio para ejecutar acciones y mostrar resultados.</li>
  <li>Debe ser lo más independiente posible de la lógica interna, para facilitar cambios en la presentación sin afectar al resto del sistema.</li>
</ul>
