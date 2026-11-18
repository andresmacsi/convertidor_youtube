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

## Despliegue privado en Render

El repositorio incluye `render.yaml` y `Dockerfile` para desplegar la aplicación en Render. El servicio pide autenticación HTTP Basic al abrirse: el usuario es `convertidor` y la contraseña se configura como secreto en Render, no en el código.

1. Sube a GitHub los archivos de esta versión, incluido `render.yaml`, `Dockerfile` y `.dockerignore`.
2. En Render, crea un **Blueprint** conectado al repositorio. Revisa el servicio `convertidor-youtube` y selecciona el plan que prefieras.
3. Cuando Render solicite `APP_PASSWORD`, define una contraseña larga y única. `SECRET_KEY` se genera automáticamente.
4. Despliega y abre la URL `https://...onrender.com`. El navegador pedirá las credenciales; ingresa el usuario `convertidor` y la contraseña configurada.

No escribas la contraseña en el repositorio ni la compartas públicamente. La app y FFmpeg se instalan en el contenedor; Render termina HTTPS y reenvía las solicitudes al puerto del servicio.

## Aplicación de escritorio

Ejecuta `iniciar_convertidor.bat` para usar la interfaz existente.
