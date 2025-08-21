# 🖥️ Buscador de Hostname y direcciones IP

Este proyecto busca obtener el nombre del equipo (hostname) y la dirección IP del dispositivo. 
Es útil en ámbito de ciberseguridad, redes o simplemente para identificar una máquina en una red local.
Ideal como punto de partida para proyectos de seguridad y auditoría.

🌍 Idiomas disponibles | [EN](README.md) 🔁 [ES](README.es.md)

## ✨ Características
- Obtiene el hostname del equipo actual.
- Obtiene la dirección IP asociada al hostname.
- Código simple y fácil de entender.

## 📚 Requisitos
- Python 3.x
- No requiere paquetes externos. No obstante, puede suceder que se requiera instalar el módulo *socket* mediante el uso del comando:
```bash
pip install sockets
```
Esto permitirá administrar la red desde Python.

## 🎯 Uso
Clona el repositorio y ejecuta el script desde la terminal:

```bash
python hostname_ip_finder.py
```

## ✍️ Ejemplo
<img width="337" height="39" alt="image" src="https://github.com/user-attachments/assets/f1c2b60f-ec62-4012-ac2e-f164073b1ba5" />

## 📌 Recomendaciones
- Este script solo devulve la IP principal asociada al hostname.
- Para listar todas las IPs por interfaz se puede considerar hacer uso de las librerías *psutil* o *netifaces*.
- Opciones avanzadas: integración con escaneo de puertos o exportar resultados a CSV/JSON para auditorías.
