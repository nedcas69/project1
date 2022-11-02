def city_country(city, country):
    cc = f'{city} - {country}'
    return cc.title()

cc = city_country('las vegas', 'united states of america')
print(cc)

cc = city_country('brazil', 'brazilia')
print(cc)

cc = city_country('moscow', 'russia')
print(cc)