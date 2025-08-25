# Guía de Administrador

## Configuración del Assistant en OpenAI Playground
1. Accede a [OpenAI Playground](https://platform.openai.com/playground/assistant).
2. Crea un nuevo Assistant y configura sus instrucciones, archivos adjuntos y parámetros según las necesidades del proyecto.
3. Copia el `Assistant ID` generado.

## Gestión de la clave API
- Obtén tu clave API en [OpenAI API Keys](https://platform.openai.com/api-keys).
- Guarda la clave en el archivo `.env`

## Mantenimiento del sistema
- Actualiza dependencias con:
```
pip install -r requirements.txt
```

- Revisa y actualiza el archivo `files/preguntas_frecuentes.txt` según sea necesario.
- Reinicia la aplicación tras cambios importantes:
```
python app.py
```
## Seguridad

- No compartas la clave API públicamente.
- Limita el acceso al archivo `.env` y a la configuración del Assistant.

## Solución de problemas

- Verifica logs en la terminal para identificar errores.
- Revisa la documentación oficial de OpenAI para cambios en la API.