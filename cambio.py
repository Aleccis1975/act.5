# Función recursiva para calcular el mínimo número de monedas para devolver el cambio
def devolver_cambio(cambio, monedas, index=0):
    if cambio == 0:
        return []
    
    # Si ya se han recorrido todas las denominaciones o el cambio es menor a la moneda actual
    if index >= len(monedas):
        return []
    
    moneda_actual = monedas[index]
    cantidad_monedas = int(cambio // moneda_actual)
    
    # Llamada recursiva para el resto del cambio
    cambio_restante = cambio - cantidad_monedas * moneda_actual
    return [(moneda_actual, cantidad_monedas)] + devolver_cambio(cambio_restante, monedas, index + 1)

# Lista de denominaciones de monedas, en orden descendente
monedas = [100, 50, 20, 10, 5, 1, 0.50, 0.20, 0.01]
