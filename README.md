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

## Aplicación de escritorio

Ejecuta `iniciar_convertidor.bat` para usar la interfaz existente.
