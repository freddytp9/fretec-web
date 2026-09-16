from flask import Flask, render_template

app = Flask(__name__)

SERVICIOS = [
    {"titulo": "Mantenimiento Industrial", "icono": "⚙️", "texto": "Mantenimiento preventivo y correctivo, diagnóstico en terreno, reparación, montaje y apoyo en paradas de planta.", "detalle": ["Mantenimiento preventivo y correctivo", "Diagnóstico mecánico y eléctrico", "Reparación y recuperación de equipos", "Montajes, ajustes y puesta en marcha", "Apoyo técnico en paradas y contingencias"]},
    {"titulo": "Servicio Técnico Industrial", "icono": "🔧", "texto": "Diagnóstico, reparación y puesta en marcha de equipos de soldadura y maquinaria industrial.", "detalle": ["Máquinas MIG/MAG, TIG y plasma", "Soldadoras industriales", "Equipos CNC de corte", "Diagnóstico de fallas", "Pruebas y puesta en servicio"]},
    {"titulo": "Extracción y Filtrado de Humos", "icono": "💨", "texto": "Diseño, fabricación, instalación y mantenimiento de sistemas para captación y filtrado de humos de soldadura.", "detalle": ["Evaluación de estaciones de trabajo", "Diseño de redes de extracción", "Ductos Spiro y captación", "Brazos y mangas de aspiración", "Filtros y sistemas de limpieza"]},
    {"titulo": "Estructuras Metálicas", "icono": "🏗️", "texto": "Fabricación y montaje de estructuras y soluciones metálicas adaptadas a las necesidades de la industria.", "detalle": ["Plataformas y pasarelas", "Escaleras y barandas", "Soportes y estructuras especiales", "Fabricación a medida", "Montaje y modificaciones en terreno"]},
    {"titulo": "Insumos y Equipos de Soldadura", "icono": "🔥", "texto": "Suministro de consumibles, accesorios y equipamiento para procesos de soldadura y fabricación industrial.", "detalle": ["Consumibles de soldadura", "Accesorios y conexiones", "Cables y conectores", "Abrasivos y herramientas", "Equipos y accesorios de soldadura"]},
    {"titulo": "Fabricación y Soluciones a Medida", "icono": "🛠️", "texto": "Desarrollo de soluciones especiales cuando el requerimiento no corresponde a un producto estándar.", "detalle": ["Levantamiento de requerimientos", "Fabricación de componentes", "Adaptaciones y modificaciones", "Integración de soluciones", "Instalación y soporte técnico"]},
]

SECTORES = [
    "Metalurgia y fabricación", "Soldadura y estructuras", "Minería", "Manufactura", "Talleres industriales", "Procesos productivos"
]

@app.route("/")
def inicio():
    return render_template("index.html", servicios=SERVICIOS, sectores=SECTORES)

@app.route("/servicios")
def servicios():
    return render_template("servicios.html", servicios=SERVICIOS)

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/proyectos")
def proyectos():
    return render_template("proyectos.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
