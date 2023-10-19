temperatura=float(input("indica la temperatura"))
tiempoenf=float(input("indica el tiempo de enfermedad del paciente"))
dificultades=str(input("tiene dificultades para respirar?"))
tos=str(input("tiene tos o dolor de garganta?"))

if temperatura <= 36.5:
  print("no tiene fiebre")

elif temperatura >36 and temperatura <38:
  print("fiebre baja")

elif temperatura >=38: 
  print("fiebre alta")
  
if tiempoenf >= 7 and dificultades == "si" and tos == "si":
  print("Enfermedad cronica")


if temperatura >= 36 or temperatura <= 36.5 and tos== "si":
  print("infeccion respiratoria leve")

if temperatura <= 36.5 or temperatura >= 38 and tos == "si":
  print("infeccion respiratoria media")

if temperatura >= 38 and dificultades=="si":
  print("infeccion respiratoria grave")
