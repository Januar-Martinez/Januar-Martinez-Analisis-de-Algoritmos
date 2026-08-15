# Semana 02 - Entorno virtual y dependencias

En esta sesión se creó un entorno virtual de Python utilizando `venv`.
El entorno se creó con el comando `python -m venv venv`.
Para activarlo en Windows se utilizó `venv\Scripts\activate`.
Se verificó que el entorno estuviera activo mediante el prefijo `(venv)` en la terminal.
Dentro del entorno se instaló `matplotlib` con `pip install matplotlib`.
Las dependencias instaladas se registraron con `pip freeze > requirements.txt`.
Para reproducir el entorno, se debe crear y activar nuevamente el `venv`.
Finalmente, se instalan las dependencias ejecutando `pip install -r requirements.txt`.