import requests
import os
import chardet
from googletrans import Translator

# Definir la URL base sin el número de segmento
base_url = "https://house-fastly-signed-eu-west-1-prod.brightcovecdn.com/media/v1/hls/v4/clear/6057955885001/df9bf581-bcef-4531-a8db-80563d7745dc/448c598e-972c-452d-ab6f-dcb7c80fe3e5/segment"

# Parámetros adicionales de la URL después de .vtt
token = "?fastly_token=NjcxYWQ4ZWFfNGUzMWVhNjk2Mjk1MDA4MmVmZTg0NWQxMTJlMDM0ZDc2OTc1ZTA3Y2U1NDBhMjZiY2UzYzlmMGUxNjg4ZDYzZF8vL2hvdXNlLWZhc3RseS1zaWduZWQtZXUtd2VzdC0xLXByb2QuYnJpZ2h0Y292ZWNkbi5jb20vbWVkaWEvdjEvaGxzL3Y0L2NsZWFyLzYwNTc5NTU4ODUwMDEvZGY5YmY1ODEtYmNlZi00NTMxLWE4ZGItODA1NjNkNzc0NWRjLzQ0OGM1OThlLTk3MmMtNDUyZC1hYjZmLWRjYjdjODBmZTNlNS8%3D"

# Ruta de la carpeta donde se descargará el archivo
output_dir = r"C:\Users\alfre\OneDrive\Documentos\Lahorafosca"
output_file = os.path.join(output_dir, "subtitles_combined.vtt")

# Inicializar el archivo de salida con la cabecera WEBVTT
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write("WEBVTT\n\n")

# Descargar los segmentos
for i in range(1, 126):
    # Crear la URL para cada segmento
    url = f"{base_url}{i}.vtt{token}"

    # Descargar el archivo VTT
    response = requests.get(url)

    # Verificar si la descarga fue exitosa
    if response.status_code == 200:
        print(f"Descargando segmento {i}")
        
        # Guardar el contenido, omitiendo la primera línea (WEBVTT)
        vtt_content = response.text.splitlines()
        with open(output_file, "a", encoding="utf-8") as outfile:
            outfile.write("\n".join(vtt_content[1:]) + "\n")
    else:
        print(f"Error al descargar el segmento {i}: {response.status_code}")

# Leer y corregir la codificación del archivo
with open(output_file, 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

with open(output_file, 'r', encoding=encoding) as f:
    content = f.read()

# Traducir el contenido a español
translator = Translator()
translated_lines = []
total_lines = len(content.splitlines())

for index, line in enumerate(content.splitlines()):
    if line and not line.startswith('WEBVTT'):
        translated_line = translator.translate(line, src='ca', dest='es').text
        translated_lines.append(translated_line)

        # Mostrar progreso en la consola
        if (index + 1) % 10 == 0:  # Cada 10 líneas
            print(f"Traducidas {index + 1} de {total_lines} líneas.")
    else:
        translated_lines.append(line)

# Convertir a formato SRT
srt_lines = []
for i, line in enumerate(translated_lines):
    if " --> " in line:
        # Mantener los tiempos
        srt_lines.append(line)
    elif line.strip():
        srt_lines.append(f"{len(srt_lines)//4 + 1}\n{line}\n")

# Guardar el archivo SRT
srt_file = os.path.join(output_dir, "subtitles_combined.srt")
with open(srt_file, "w", encoding="utf-8") as f:
    f.write("\n".join(srt_lines))

# Eliminar el archivo VTT original
os.remove(output_file)

print(f"Subtítulos traducidos y guardados en {srt_file}")
