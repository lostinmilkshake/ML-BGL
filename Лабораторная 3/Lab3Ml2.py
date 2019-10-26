 #Функция принимает значение кванта, показаняи ЦИП, диапозон измерения
def lab3Ml(xmax, Rp, dip):
    if dip == 20:
        help = 0.005
    else:
        help = 0.002
    ed = xmax / 2000
    dR = Rp*help + ed
    delta = 100 * (dR / Rp)
    print(ed, dR, delta)

lab3Ml(1000, 8, 1)