import openpyxl
archivo_xlsx=openpyxl.load_workbook("productos.xlsx")
hoja_trabajo=archivo_xlsx["productos_precios"]
for fila in hoja_trabajo.iter_rows(values_only=True):
    print(fila)

