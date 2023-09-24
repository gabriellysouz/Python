camp = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fluminense', 'Gremio',
        'Atletico -PR', 'Bragantino', 'Fortaleza', 'Cuiaba', 'Sao Paulo', 'Atletico Mineiro',
        'Cruzeiro', 'Corinthians', 'Internacional', 'Goias', 'Bahia', 'Santos', 'Vasco da Gama',
        'Coritiba', 'America-MG')
fortaleza = camp.index('Fortaleza')+1

print('Lista times do Brasileirao ', camp)
print('-=-' * 20)
print('Os 5 priemiros sao ', camp[:5])
print('-=-' * 20)
print('Os 4 ultimos sao ', camp[-4:])
print('-=-' * 20)
print('Em ordem alfabetica ', sorted(camp))
print('-=-' * 20)
print(f'Fortaleza esta na {camp.index("Fortaleza")+1}º posiçao')
