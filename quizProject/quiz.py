#QUIZZZ
nombre = input("Ingrese su nombre: ")
dias = int(input("Ingrese los dias trabajados: "))
salario = float(input("ingrese su salario: "))
cesantias = (salario*dias)/360
prima = float((salario * dias)/360)
InteresesCesantias = (cesantias*0.12)/dias
vacaciones= (salario*dias)/720


print(f"Señor {nombre} para los {dias} dias laborados y salario {salario}, su liquidacion se compone asi: "
      f"prima = {(salario * dias)/360:.2f} "
      f"cesantia = {(salario * dias)/ 360:.2f} "
      f"InteresesCesantias = {(cesantias*0.12)/dias:.2f}"
      f"vacaciones= {(salario*dias)/720:.2f} "
      f"liquidacion = {(prima+cesantias+InteresesCesantias+vacaciones):.2f}")




