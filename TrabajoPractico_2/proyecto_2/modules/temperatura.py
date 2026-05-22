from ayedfiuner.estructuras.abb import AVL
import datetime

class Temperaturas_DB:
    def __init__(self):
        self.__avl = AVL()

    def _formatear_fecha(self, fecha_str):
        """Convierte string dd/mm/aaaa a objeto datetime para comparaciones."""
        return datetime.datetime.strptime(fecha_str, "%d/%m/%Y")

    def guardar_temperatura(self, temperatura, fecha):
        clave = self._formatear_fecha(fecha)
        self.__avl.agregar(clave, temperatura)

    def devolver_temperatura(self, fecha):
        clave = self._formatear_fecha(fecha)
        return self.__avl.obtener(clave)

    def borrar_temperatura(self, fecha):
        clave = self._formatear_fecha(fecha)
        self.__avl.eliminar(clave)

    def cantidad_muestras(self):
        return len(self.__avl)

    def _obtener_lista(self, nodo, f1, f2, resultados):
        """Recorrido in-order para obtener mediciones en rango."""
        if not nodo:
            return
        if nodo.clave > f1:
            self._obtener_lista(nodo.hijoIzquierdo, f1, f2, resultados)
        if f1 <= nodo.clave <= f2:
            resultados.append((nodo.clave, nodo.cargaUtil))
        if nodo.clave < f2:
            self._obtener_lista(nodo.hijoDerecho, f1, f2, resultados)

    def devolver_temperaturas(self, fecha1, fecha2):
        f1, f2 = self._formatear_fecha(fecha1), self._formatear_fecha(fecha2)
        muestras = []
        self._obtener_lista(self.__avl.raiz, f1, f2, muestras)
        return [f"{m[0].strftime('%d/%m/%Y')}: {m[1]} ºC" for m in muestras]

    def temp_extremos_rango(self, fecha1, fecha2):
        f1, f2 = self._formatear_fecha(fecha1), self._formatear_fecha(fecha2)
        muestras = []
        self._obtener_lista(self.__avl.raiz, f1, f2, muestras)
        if not muestras: return None, None
        temps = [m[1] for m in muestras]
        return min(temps), max(temps)

    def max_temp_rango(self, f1, f2):
        return self.temp_extremos_rango(f1, f2)[1]

    def min_temp_rango(self, f1, f2):
        return self.temp_extremos_rango(f1, f2)[0]
