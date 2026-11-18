import secrets
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urlsplit

from flask import Flask, Response, render_template, request, session
from yt_dlp.utils import DownloadError

from downloader import descargar


YOUTUBE_HOSTS = {
    "youtube.com",
    "www.youtube.com",
    "m.youtube.com",
    "music.youtube.com",
    "youtu.be",
}

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"


def es_url_youtube(url: str) -> bool:
    try:
        parsed_url = urlsplit(url.strip())
        puerto = parsed_url.port
    except ValueError:
        return False

    puerto_permitido = puerto is None or puerto == (
        443 if parsed_url.scheme == "https" else 80
    )
    return (
        parsed_url.scheme in {"http", "https"}
        and parsed_url.hostname in YOUTUBE_HOSTS
        and parsed_url.username is None
        and parsed_url.password is None
        and puerto_permitido
    )


def renderizar_formulario(
    csrf_token: str,
    error: str | None = None,
    url: str = "",
    formato: str = "mp3",
    status: int = 200,
):
    return (
        render_template(
            "index.html",
            csrf_token=csrf_token,
            error=error,
            url=url,
            formato=formato,
        ),
        status,
    )


@app.route("/", methods=["GET", "POST"])
def index():
    csrf_token = session.get("csrf_token")
    if csrf_token is None:
        csrf_token = secrets.token_urlsafe(32)
        session["csrf_token"] = csrf_token

    if request.method == "GET":
        return renderizar_formulario(csrf_token)

    token_enviado = request.form.get("csrf_token", "")
    if not secrets.compare_digest(token_enviado, csrf_token):
        return renderizar_formulario(
            csrf_token, error="La sesión expiró. Recarga la página e intenta de nuevo.", status=400
        )

    url = request.form.get("url", "").strip()
    formato = request.form.get("formato", "").lower()

    if not es_url_youtube(url):
        return renderizar_formulario(
            csrf_token,
            error="Pega un enlace válido de YouTube.",
            url=url,
            formato=formato,
            status=400,
        )
    if formato not in {"mp3", "mp4"}:
        return renderizar_formulario(
            csrf_token,
            error="Selecciona MP3 o MP4.",
            url=url,
            formato="mp3",
            status=400,
        )

    directorio_temporal = TemporaryDirectory(prefix="convertidor-youtube-")
    try:
        archivo = descargar(url, formato, Path(directorio_temporal.name))
    except (DownloadError, OSError, RuntimeError) as error:
        directorio_temporal.cleanup()
        return renderizar_formulario(
            csrf_token,
            error=f"No se pudo preparar el archivo: {error}",
            url=url,
            formato=formato,
            status=500,
        )

    def transmitir_archivo():
        try:
            with archivo.open("rb") as archivo_abierto:
                while bloque := archivo_abierto.read(64 * 1024):
                    yield bloque
        finally:
            directorio_temporal.cleanup()

    respuesta = Response(transmitir_archivo(), mimetype="application/octet-stream")
    respuesta.headers.set("Content-Disposition", "attachment", filename=archivo.name)
    respuesta.headers.set("Content-Length", str(archivo.stat().st_size))
    return respuesta


if __name__ == "__main__":
    print("Abre http://127.0.0.1:5000 en tu navegador.")
    app.run(host="127.0.0.1", port=5000, debug=False, threaded=False)
