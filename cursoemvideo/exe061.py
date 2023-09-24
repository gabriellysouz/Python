primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
c = 1
while c != 10:
    pa = primeirotermo + (c - 1) * razao
    c += 1
    print(pa, end=' -> ')
print('Fim!')