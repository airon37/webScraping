import bs4
import requests
from datetime import date


url='https://www.filmaffinity.com/es/rdcat.php?id=upc_th_es'
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, 'lxml')
hoy = date.today()
meses =("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
fecha = format(hoy.day)+" de "+meses[hoy.month-1]

peliculas = soup.select('.top-movie')
for m in peliculas:
    fech = m.select('.date')[0].text
    print(m.select('h3 a')[0].attrs['title'])
    print(fech)
    print(m.select('.avg-rating')[0].text)
    print()
#if (peliculas.__contains__(fecha)):