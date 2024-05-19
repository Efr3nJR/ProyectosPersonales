def verificar_presion_arterial(sys_mmhg, dia_mmhg, pulse_min):
    if sys_mmhg < 90 or dia_mmhg < 60 or pulse_min < 60:
        return "Bajo - Consulta médica recomendada."
    elif sys_mmhg >= 140 or dia_mmhg >= 90 or pulse_min >= 100:
        return "Alto - Consulta médica recomendada."
    else:
        return "Bien - Valores dentro del rango normal."
   
if __name__ =="__main__":
    validar = True
    while validar:
        try:
            sys_mmhg = float(input("Ingrese SYS mmHg: "))
            dia_mmhg  = float(input("Ingrese DIA mmHg: "))
            pulse_min = float(input("Ingrese Pulse/min: "))
            print(verificar_presion_arterial(sys_mmhg, dia_mmhg, pulse_min))
            continuar = input("¿Desea continuar? (s/n): ")
            if continuar.lower() != 's':
                validar = False
        except ValueError:
            print("Por favor, introduce números válidos.")
