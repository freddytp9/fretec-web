# Fretec SpA — Web

Primera versión funcional de la página web de Fretec SpA, construida con Python + Flask.

## Estructura

- `app.py`: aplicación Flask y rutas.
- `templates/`: páginas HTML.
- `static/css/style.css`: diseño responsive.
- `static/js/main.js`: menú móvil y formulario hacia WhatsApp.
- `requirements.txt`: dependencias.
- `Procfile`: comando de producción con Gunicorn.

## Ejecutar localmente

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Iniciar:

```bash
flask --app app run --debug
```

Abrir `http://127.0.0.1:5000`.

## Producción

El proceso de producción está preparado para Gunicorn:

```bash
gunicorn app:app
```

La web puede desplegarse posteriormente en un servidor Linux, VPS o plataforma compatible con Flask.

## Próxima etapa

Agregar logo oficial de Fretec, fotografías reales, proyectos destacados, datos corporativos, formulario de contacto avanzado y panel de administración para gestionar informes, proyectos y productos.
