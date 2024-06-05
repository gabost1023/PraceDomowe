import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3,3.5,0.5, dtype=float) #wartosci od -3 do 3 co 0.5
print(x)
s = np.sin(x)
plt.plot(x,s*x) #wykres funkcji f(x) = sin(x)*x
plt.xlim([-3,3]) #zakres osi x na [-3,3]
plt.xlabel('Oś x')
plt.ylabel('Oś y')
plt.title('Wykres funkcji f(x) = sin(x)*x')
plt.show()
