print("Enter U1 and U2 values")
u1 = float(input())
u2 = float(input())
u1N = 20  # TODO should be something
u2N = 2  # TODO should be something
# This values should be like this
# TODO check класс точности
c = 1.5
d = 0.2
deltaU1 = c + d*(u1N/u1 - 1)
c = 0.5
deltaU2 = c + d*(u2N/u2 - 1)
print("Относительная погрешность: ", deltaU1, " ", deltaU2)
# Абсолютная погрешность
DeltaU1 = (deltaU1 * u1) / 100
DeltaU2 = (deltaU1 * u2) / 100
print("Абсолютная погрешность: ", DeltaU1, " ", DeltaU2)
# TODO Не забудь результат измерений

# Находим ток
r0 = 1000  # TODO find out value
i1 = u1 / r0
i2 = u2 / r0
print("Значения токов: ", i1, " ", i2)
# Относительная погрешность тока
deltaI1 = deltaU1 + 0.5
deltaI2 = deltaU2 + 0.5
print("Относительная погрешность токов: ", deltaI1, " ", deltaI2)
# Абсолютная погрешность тока
DeltaI1 = (i1 * deltaI1) / 100
DeltaI2 = (i2 * deltaI2) / 100
print("Абсолютная погрешность токов: ", DeltaI1, " ", DeltaI2)
# TODO Записать результаты
# Найдём мощность
p1 = u1 * i1
p2 = u2 * i2
print("Значения мощности : ", p1, " ", p2)
# Относительная погрешность мощности
deltaP1 = deltaU1 + deltaI1
deltaP2 = deltaU2 + deltaI2
print("Относительная погрешность мощностей: ", deltaP1, " ", deltaP2)
# Абсолютаня погрешность мощности
DeltaP1 = deltaP1 * p1 / 100
DeltaP2 = deltaP2 * p2 / 100
print("Абсолютная погрешность мощностей: ", deltaP1, " ", deltaP2)
# TODO записать результаты
