# Convertidor de YouTube

Aplicación para convertir videos a MP3 o MP4. Usa únicamente contenido que tengas derecho a descargar.

## 🌐 Acceso público

**La aplicación está desplegada en:** https://convertidor-youtube-26n4.onrender.com/

Abre el enlace en tu navegador. No requiere instalación ni contraseña.

## Requisitos (para ejecutar localmente)

- **Python 3.10+**
- **FFmpeg**: descárgalo desde [ffmpeg.org](https://ffmpeg.org/download.html)
  - En Windows: puedes usar `choco install ffmpeg` (con Chocolatey) o descargar el ejecutable
  - En macOS: `brew install ffmpeg`
  - En Linux: `sudo apt install ffmpeg` (Debian/Ubuntu)

## Aplicación web local

1. Instala los requisitos arriba.
2. Ejecuta `iniciar_web.bat`, o en una terminal:

   ```powershell
   py -3 -m pip install -r requirements.txt
   py -3 web_app.py
   ```

3. Abre <http://127.0.0.1:5000> en el navegador.

El servidor escucha solo en `127.0.0.1`; no está publicado en Internet. El archivo convertido se envía al navegador y los archivos temporales se eliminan al terminar la descarga.

## Despliegue en Render

El repositorio incluye `render.yaml` y `Dockerfile` para desplegar la aplicación en Render sin costo.

Si quieres desplegar tu propia versión:

1. Crea un fork de este repositorio en GitHub.
2. Regístrate en [Render](https://render.com/) con GitHub.
3. Crea un **Blueprint** conectado a tu fork, rama `main`.
4. Render leerá `render.yaml` y creará el servicio automáticamente.
5. Cuando el servicio aparezca como **Live**, Render te asignará una URL pública.

FFmpeg se instala automáticamente en el contenedor. Las descargas son temporales y se limpian automáticamente.

## Notas

- FFmpeg es necesario para MP3 y para algunos videos MP4.
- Solo descarga videos de los que tengas derechos de autor o que estén bajo licencia que lo permita.
- Si YouTube pide autenticación, prueba con un video público sin restricciones.

## Aplicación de escritorio

Ejecuta `iniciar_convertidor.bat` para usar la interfaz de escritorio (solo local).
