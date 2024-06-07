import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl

# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]. Dodaj etykietę do linii wykresu i wyświetl legendę.
# Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).

x = np.linspace(1,20,1000)
wykres = plt.plot(x, 1/x, ':', marker='>', markevery=50, color='green')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) dla x [1,20]')
plt.legend(['f(x) = 1/x'])
plt.xlim(0,20)
plt.ylim(0,1)
plt.show()


# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1.
# Dodaj etykiety i legendę do wykresu.

x = np.arange(0,30.1,0.1)
s = np.sin(x)
c = np.cos(x)
plt.plot(x,s,label='sin(x)')
plt.plot(x,c,label='cos(x)')
plt.legend(loc='upper right')
plt.show()


# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8.
# Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
# 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.
# 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla każdego roku z osobna.
# Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
# 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.

# Wczytanie danych z pliku Excel
xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx, header=0)
df = pd.DataFrame(data)

# Tworzenie wspólnego płótna z trzema osiami obok siebie
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# Wykres 1 - suma urodzeń z podziałem na płeć
grupa = df.groupby(['Plec'])['Liczba'].sum()
grupa.plot(kind='bar', color=['pink', 'blue'], ax=ax1)
ax1.set_title('Suma urodzeń z podziałem na płeć')
ax1.set_xlabel('Płeć')
ax1.set_ylabel('Liczba urodzeń')

# Wykres 2 - suma urodzeń w poszczególnych latach dla kobiet i mężczyzn (wykres liniowy)
km = df.groupby(['Rok', 'Plec'])['Liczba'].sum().unstack()
km.plot(ax=ax2)
ax2.set_title('Suma urodzeń w latach')
ax2.set_xlabel('Rok')
ax2.set_ylabel('Liczba urodzeń')

# Wykres 3 - suma urodzeń w poszczególnych latach dla kobiet i mężczyzn (wykres słupkowy)
km.plot(kind='bar', color=['red', 'green'], ax=ax3)
ax3.set_title('Suma urodzeń w latach (słupki)')
ax3.set_xlabel('Rok')
ax3.set_ylabel('Liczba urodzeń')

# Dopasowanie układu
plt.tight_layout()

# Wyświetlenie wykresów
plt.show()