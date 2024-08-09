seg = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = seg//(60*60*24)
diasRest = seg%(60*60*24)
horas = diasRest//(60*60)
horasRest = diasRest%(60*60)
minutos = horasRest//60
segundos = horasRest%60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")