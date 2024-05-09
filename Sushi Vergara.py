import os
import time

Menu = 1
Descuento = 0
LimpiarCMD = "cls"
dinero = 0

Pikroll = 0
Otkroll = 0
Pulroll = 0
Angroll = 0

print("Bienvenido a nuestra aplicacion de delivery.\n A continuación se mostrara nuestro listado (1-5)")

while Menu == 1:
    print("1. Pikachu roll: $4500")
    print("2. Otaku roll: $5000")
    print("3. Pulpo Venenoso roll: $5200")
    print("4. Anguila Eléctrica roll: $4800")
    print("5. Terminar Pedido.")
    pedido = int(input("Seleccione una de nuestras opciones: \n"))

    if pedido == 1:
        Pikroll += 1
        dinero += 4500
        print("Pikachu roll agregado al pedido")
        time.sleep(3)
        os.system(LimpiarCMD)

    elif pedido == 2:
        Otkroll += 1
        dinero += 5000
        print("Otaku roll agregado al pedido")
        time.sleep(3)
        os.system(LimpiarCMD)

    elif pedido == 3:
        Pulroll += 1
        dinero += 5200
        print("Pulpo Venenoso roll agregado a tu pedido")
        time.sleep(3)
        os.system(LimpiarCMD)

    elif pedido == 4:
        Angroll += 1
        dinero += 4800
        print("Anguila Eléctrica roll agregado a tu pedido")
        time.sleep(3)
        os.system(LimpiarCMD)
    
    elif pedido == 5:
        print("Terminando con el pedido, pasando al código de descuento.")
        Menu += 1
        time.sleep(3)
        os.system(LimpiarCMD)
        break

    else:
        print("Por favor, ingrese una opción correcta.")
        time.sleep(3)
        os.system(LimpiarCMD)

TotalPedido = (Pikroll + Otkroll + Pulroll + Angroll)

while Menu == 2:
    codigo = input("Ingrese codigo de descuento. (Escribir 'no' si es que no lo tiene.) \n")
    if codigo == "soyotaku":
        Descuento = 0.10
        Menu += 1
        time.sleep(3)
        os.system(LimpiarCMD)
    elif codigo == "no":
        Menu += 1
        Descuento = 0
        print("Ok, pasando a la boleta.")

    else:
        print("Por favor ingrese una opción valida.")
        time.sleep(3)
        os.system(LimpiarCMD)

ValorDesc = (Descuento * dinero)
TotalDesc = (dinero - ValorDesc)

if Menu == 3:
    print("******************************")
    print(f'Total productos {TotalPedido}')
    print("******************************")
    print(f'Pikachu Roll: {Pikroll}')
    print(f'Otaku Roll: {Otkroll}')
    print(f'Pulpo Venenoso Roll: {Pulroll}')
    print(f'Anguila Eléctrica Roll: {Angroll}')
    print("******************************")
    print(f'Subtotal a pagar: ${dinero}')
    print(f'Descuento por código: ${ValorDesc}')
    print(f'TOTAL: ${TotalDesc}')