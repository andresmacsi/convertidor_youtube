import shutil
from pathlib import Path

from yt_dlp import YoutubeDL


def descargar(url: str, formato: str, directorio: Path) -> Path:
    directorio.mkdir(parents=True, exist_ok=True)
    ffmpeg_instalado = shutil.which("ffmpeg") is not None

    opciones = {
        "noplaylist": True,
        "nooverwrites": True,
        "outtmpl": str(directorio / "%(title).150B [%(id)s].%(ext)s"),
        "restrictfilenames": True,
        "windowsfilenames": True,
    }

    if formato == "mp3":
        if not ffmpeg_instalado:
            raise RuntimeError(
                "No se encontró FFmpeg. Instálalo y asegúrate de que esté en PATH."
            )
        opciones.update(
            {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }
        )
    elif formato == "mp4":
        opciones.update(
            {
                "format": "best[ext=mp4]/bestvideo[ext=mp4]+bestaudio[ext=m4a]",
                "merge_output_format": "mp4",
            }
        )
    else:
        raise ValueError("El formato debe ser mp3 o mp4.")

    with YoutubeDL(opciones) as descargador:
        info = descargador.extract_info(url, download=False)
        if formato == "mp4" and not ffmpeg_instalado:
            formatos = info.get("formats", [])
            tiene_mp4_con_audio = any(
                formato_video.get("ext") == "mp4"
                and formato_video.get("vcodec") != "none"
                and formato_video.get("acodec") != "none"
                for formato_video in formatos
            )
            if not tiene_mp4_con_audio:
                raise RuntimeError(
                    "Este video requiere FFmpeg para combinar audio y video en MP4."
                )
            descargador.params["format"] = "best[ext=mp4]"

        destino = Path(descargador.prepare_filename(info)).with_suffix(f".{formato}")
        if destino.exists():
            raise FileExistsError(f"El archivo ya existe y no se sobrescribirá: {destino}")
        descargador.process_ie_result(info, download=True)

    return destino
