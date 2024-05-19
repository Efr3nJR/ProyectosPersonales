def verificar_presion_arterial(sys_mmhg, dia_mmhg, pulse_min):
    try:
        sys_mmhg = float(sys_mmhg)
        dia_mmhg = float(dia_mmhg)
        pulse_min = float(pulse_min)

        if sys_mmhg < 90 or dia_mmhg < 60 or pulse_min < 60:
            return "Bajo - Consulta médica recomendada."
        elif sys_mmhg >= 140 or dia_mmhg >= 90 or pulse_min >= 100:
            return "Alto - Consulta médica recomendada."
        else:
            return "Bien - Valores dentro del rango normal."
    except ValueError:
        return "Por favor, introduce números válidos."

if __name__ =="__main__":
    validar = True
    while validar:
        try:
            sys = float(input("Ingrese SYS mmHg: "))
            dia = float(input("Ingrese DIA mmHg: "))
            pulse = float(input("Ingrese Pulse/min: "))
            print(verificar_presion_arterial(sys, dia, pulse))
            continuar = input("¿Desea continuar? (s/n): ")
            if continuar.lower() != 's':
                validar = False
        except ValueError:
            print("Por favor, introduce números válidos.")
