# test_app.py — Pruebas automaticas para el pipeline
 
from app import obtener_estado_pipeline, calcular_version
 
def test_estado_pipeline():
    assert obtener_estado_pipeline() == "Pipeline activo y funcionando"
 
def test_version():
    assert calcular_version(1, 0, 0) == "1.0.0"
    assert calcular_version(2, 1, 3) == "2.1.3"
