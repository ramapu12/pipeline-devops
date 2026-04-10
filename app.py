# app.py — Aplicacion de ejemplo para el pipeline DevOps
 
def obtener_estado_pipeline():
    return "Pipeline activo y funcionando"
 
def calcular_version(major, minor, patch):
    return f"{major}.{minor}.{patch}"
 
if __name__ == '__main__':
    print(obtener_estado_pipeline())
    print("Version:", calcular_version(1, 0, 0))
