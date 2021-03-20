# Algoritmo pra converter metro em centímetro e centímetro em milímetro.
# 1m tem 100 cm. 1cm tem  1 milímetro
# muito avançado pra mim '-'
M = float(input('Digite uma distância em metros: '))
cm = M * 100
mm = M * 1000
km = M / 1000
print('A medida de {}m corresponde a {}km, {:.0f}cm e {:.0f}mm'.format(M, km, cm, mm))
