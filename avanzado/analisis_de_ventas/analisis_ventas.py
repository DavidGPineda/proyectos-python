"""
Este script analiza las ventas de productos desde un archivo CSV.
Calcula total de ventas, producto más vendido y genera gráficos.
"""
import pandas as pd
import matplotlib.pyplot as plt

# 1. Leer CSV
df = pd.read_csv("ventas.csv", sep=";", parse_dates=["fecha"])

# 2. Convertir a fecha (muy importante)
df["fecha"] = pd.to_datetime(df["fecha"], dayfirst=True, errors="coerce")

# 3. Calcular total de ventas por fila
df["total"] = df["cantidad"] * df["precio_unitario"]

print("Datos cargados:")
print(df.head())

# 4. Total de ventas general
total_ventas = df["total"].sum()
print(f"\n💰 Total de ventas: ${total_ventas}")

# 5. Producto más vendido (en cantidad)
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
print(f"🏆 Producto más vendido: {producto_mas_vendido}")

# 6. Promedio de ventas mensual
df["mes"] = df["fecha"].dt.to_period("M")
ventas_mensuales = df.groupby("mes")["total"].sum()
print("\n📊 Ventas mensuales:")
print(ventas_mensuales)

# 7. Graficar ventas mensuales
ventas_mensuales.plot(kind="bar", title="Ventas por mes", ylabel="Total en $")
plt.show()

# 8. Gráfico de productos vendidos (pastel)
ventas_productos = df.groupby("producto")["cantidad"].sum()
ventas_productos.plot(kind="pie", autopct="%1.1f%%",
                      title="Distribución de productos vendidos")
plt.ylabel("")  # quita texto innecesario
plt.show()
