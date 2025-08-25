# Guía de Instalación

## Requisitos previos

- Python 3.13.7 o superior
- Git

## Pasos de instalación

1. **Clona el repositorio:**
```sh
   git clone https://github.com/segmauricio/CHATbot.git
   cd CHATbot
```
   
2. **Instala las dependencias**
```sh
   pip install -r requirements.txt
```

3. **Configura las variables de entorno:**
- Crea un archivo .env en la raíz del proyecto.
- Añade tu clave de API de OpenAI:
 ```sh
   OPENAI_API_KEY=tu_clave_aqui
   ```
 ```sh
   ASSISTANT_ID=tu_assistant_id
   ```
4. Asegúrate de tener el archivo de preguntas frecuentes:
- El archivo files/preguntas_frecuentes.txt debe existir y estar completo.
5. Ejecuta el asistente:
```sh
    python app.py
```
- Accede a la interfaz en http://localhost:5000.