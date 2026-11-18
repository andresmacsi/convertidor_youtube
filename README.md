# Convertidor de YouTube

Aplicación local para convertir videos a MP3 o MP4. Usa únicamente contenido que tengas derecho a descargar.

## Aplicación web local

1. Instala Python 3 y FFmpeg. FFmpeg debe estar disponible en `PATH` para MP3 y para algunos videos MP4.
2. Ejecuta `iniciar_web.bat`, o en una terminal:

   ```powershell
   py -3 -m pip install -r requirements.txt
   py -3 web_app.py
   ```

3. Abre <http://127.0.0.1:5000> en el navegador.

El servidor escucha solo en `127.0.0.1`; no está publicado en Internet. El archivo convertido se envía al navegador y los archivos temporales se eliminan al terminar la descarga.

## Despliegue público en Render

El repositorio incluye `render.yaml` y `Dockerfile` para desplegar la aplicación en Render sin costo.

1. Regístrate en [Render](https://render.com/) con GitHub.
2. Crea un **Blueprint** conectado a este repositorio, rama `main`.
3. Render leerá `render.yaml` y creará el servicio automáticamente.
4. Cuando el servicio aparezca como **Live**, abre la URL que Render asigna (`https://...onrender.com`).
5. Listo: cualquiera puede acceder desde Internet.

Nota: FFmpeg se instala en el contenedor. Las descargas son temporales y se limpian automáticamente.

## Aplicación de escritorio

Ejecuta `iniciar_convertidor.bat` para usar la interfaz existente.
