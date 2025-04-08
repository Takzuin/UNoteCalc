import pandas as pd

def calcular_nota_real(materias):
    resultados = []
    for materia, calificaciones in materias.items():
        porcentaje_total = sum(p for _, p in calificaciones)
        nota_real = sum(nota * p for nota, p in calificaciones) / 100  # Ajuste para notas de 0 a 5
        nota_sin_fallas = sum(5 * p for _, p in calificaciones) / 100  # Nota máxima sin errores
        resultados.append([materia, round(nota_real, 2), round(porcentaje_total), round(nota_sin_fallas, 2)])
    return resultados

# Datos de ejemplo (notas en escala de 0 a 5)
materias = {
    "PENSAMIENTO IUE": [(4.0, 15.0), (3.5, 15)],
    "TALLER DE LENGUAJE": [(1.8, 15.0),(5, 15.0), (3.5, 20.0)],
    "ÁLGEBRA Y TRIGONOMETRÍA": [(3.9, 9.0), (0.0, 9.0)],
    "GEOMETRÍA": [(1.3, 9.0), (0.0, 9.0), (3.0, 20.0)],#, (0, 9.0), (0, 9.0), (0, 15.0), (0, 20.0), (0, 9.0)
    "INTRODUCCIÓN A LA INGENIERÍA INFORMÁTICA": [(4.2, 20.0)],
    "INFORMÁTICA BÁSICA": [(3.8, 15.0),(2.8, 20.0), (2.0, 5.0), (3.5, 5.0), (3.5, 5.0)],
    "INFRAESTRUCTURA TECNOLÓGICA": [(4.5, 2.0), (5.0, 5.0), (4.3, 2.0), (3.5, 12.0), (3.6, 5.0)]
}

# Generar DataFrame y mostrar resultados
df = pd.DataFrame(calcular_nota_real(materias), columns=["Materia", "Nota Acumulada", "% Evaluado", "Nota sin Fallas"])
print(df)
