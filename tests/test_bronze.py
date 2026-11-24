from drug_safety_pipeline.bronze import build_bronze, guardar_bronze, main
from datetime import UTC, datetime

COLUMNAS_DE_PRUEBA={"results":[{"reportduplicate": {"algo": "value1"}, "primarysource": {"algo": "value2"}, "sender": {"algo": "value3"}, "receiver": {"algo": "value4"}, "patient": {"algo": "value5"}}]}
#columnas de prueba es el diccionario completo, su única clave es results

def test_build_bronze_filas():
    """Verifica que el DataFrame resultante tenga la misma cantidad de filas que el diccionario de prueba"""
    df=build_bronze(COLUMNAS_DE_PRUEBA, datetime(2026,1,1, tzinfo=UTC))
    assert len(df)==1

def test_build_bronze_anidacion():
    """Verifica que las columnas anidadas se hayan convertido en strings"""
    df=build_bronze(COLUMNAS_DE_PRUEBA, datetime(2026,1,1, tzinfo=UTC))
    for columna in COLUMNAS_DE_PRUEBA["results"][0]: #Le digo que entre a results y me de la lista de reportes. El [0] me dice, de la lista de reportes agarra el primero.
        assert isinstance(df[columna][0], str) #verifica que cada columna anidada se haya convertido en un string
