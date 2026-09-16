from flask import Flask, render_template

app = Flask(__name__)

SERVICIOS = [
    {"titulo": "Mantenimiento Industrial", "icono": "⚙️", "texto": "Mantenimiento preventivo y correctivo de equipos y sistemas industriales."},
    {"titulo": "Servicio Técnico", "icono": "🔧", "texto": "Diagnóstico, reparación y puesta en marcha de equipos de soldadura y maquinaria."},
    {"titulo": "Extracción y Filtrado de Humos", "icono": "💨", "texto": "Diseño e instalación de soluciones para extracción y filtrado de humos de soldadura."},
    {"titulo": "Estructuras Metálicas", "icono": "🏗️", "texto": "Fabricación y montaje de estructuras y soluciones metálicas para la industria."},
    {"titulo": "Insumos de Soldadura", "icono": "🔥", "texto": "Suministro de insumos y accesorios para procesos de soldadura industrial."},
]

@app.route("/")
def inicio():
    return render_template("index.html", servicios=SERVICIOS)

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
