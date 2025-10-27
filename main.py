from servicios.clima import consultar_clima

def main():
    ciudad = input("Introduce el nombre de una población: ")
    info = consultar_clima(ciudad)

    if info:
        print(f"\nClima en {ciudad}:")
        print(f"\tTemperatura: {info['temperatura']} °C")
        print(f"\tSensación térmica: {info['sensacion']} °C")
        print(f"\tDescripción: {info['descripcion']}")
    else:
        print("No se pudo obtener la información meteorológica.")

if __name__ == "__main__":
    main()