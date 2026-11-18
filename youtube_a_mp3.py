from pathlib import Path
from tkinter import Tk, filedialog

from downloader import descargar


def main() -> None:
    # Ejemplo: prueba el enlace de NASA, elige mp4 y una carpeta como C:\Videos.
    print("Convertidor de YouTube a MP3 o MP4")
    print("Ejemplo (NASA): https://www.youtube.com/watch?v=ouv1Un1F36A")
    print("MP3 necesita FFmpeg; MP4 puede necesitarlo para combinar pistas.\n")

    url = input("Pega el enlace de YouTube: ").strip()
    if not url:
        raise ValueError("Debes proporcionar un enlace de YouTube.")

    while True:
        formato = input("Formato deseado (mp3/mp4): ").strip().lower().lstrip(".")
        if formato in {"mp3", "mp4"}:
            break
        print("Formato no válido. Escribe mp3 o mp4.")

    ventana = Tk()
    ventana.withdraw()
    try:
        ruta_directorio = filedialog.askdirectory(
            title="Selecciona la carpeta de salida",
            initialdir=str(Path.cwd()),
            mustexist=True,
        )
    finally:
        ventana.destroy()

    if not ruta_directorio:
        print("No se seleccionó una carpeta. Descarga cancelada.")
        return

    directorio = Path(ruta_directorio)

    resultado = descargar(url, formato, directorio)
    print(f"\nArchivo guardado en: {resultado.resolve()}")


if __name__ == "__main__":
    main()
