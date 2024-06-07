import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

plt.plot([1,2,3,4])
plt.ylabel('jakies liczby')
plt.show()

plt.plot([1,2,3,4],[1,4,9,16], 'ro-')
plt.axis((0,6,0,20))
plt.show()

plt.plot([1,2,3,4],[1,4,9,16],'r')
plt.plot([1,2,3,4],[1,4,9,16],'o')
plt.xlim(0,6)
plt.ylim(0,20)
plt.show()

x = np.linspace(0,2,100)
plt.plot(x,x,label="liniowa")
plt.plot(x,x**2,label="kwadratowa")
plt.plot(x,x**3,label="szescienna")
plt.xlabel('etykieta x')
plt.ylabel('etykieta y')
plt.title("Prosty wykres")
plt.legend()
plt.savefig("wykres matplot.png")
plt.show()
im1 = Image.open("wykres matplot.png")
im1 = im1.convert("RGB")
im1.save('nowy.jpg')

x = np.arange(0,10,0.1)
s = np.sin(x)
plt.plot(x,s,label="sin(x)")
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x)')
plt.legend(loc='upper right')
plt.show()

data = {'a': np.arange(50), #50 elementow od 0 do 49
        'c': np.random.randint(0,50,50), #generuje wartosci losowe i sa to liczby calkowite
        'd': np.random.randn(50)} #wartosci losowe rozkladu normalnego (od 0 do 1)?
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
print(f"a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]}, d={data['d'][0]}")
plt.scatter('a', 'b', c='c', cmap='magma', s='d', data=data)
plt.xlabel('wartosc a')
plt.ylabel('wartosc b')
plt.show()

x1 = np.arange(0,2,0.02)
x2 = np.arange(0,2,0.02)

