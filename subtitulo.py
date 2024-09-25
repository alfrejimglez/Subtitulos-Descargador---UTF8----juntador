import os
import chardet
import requests

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

for i in range(1, 126):
    # Crear la URL para cada segmento
    url = f"{base_url}{i}.vtt{token}"

    # Descargar el archivo VTT
    response = requests.get(url)

    # Verificar si la descarga fue exitosa
    if response.status_code == 200:
        print(f"Descargando segmento {i}")

        # Detectar la codificación del contenido recibido
        result = chardet.detect(response.content)
        encoding = result['encoding']

        # Leer el contenido con la codificación detectada
        vtt_content = response.content.decode(encoding).splitlines()

        # Guardar el contenido, omitiendo la primera línea (WEBVTT)
        with open(output_file, "a", encoding="utf-8") as outfile:
            outfile.write("\n".join(vtt_content[1:]) + "\n")
    else:
        print(f"Error al descargar el segmento {i}: {response.status_code}")

print(f"Subtítulos combinados guardados en {output_file}")