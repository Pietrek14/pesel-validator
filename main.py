# ******************************************************
# nazwa funkcji:				sprawdz_plec
# opis funkcji:					Sprawdza plec zakodowana w numerze PESEL
# parametry:					pesel - numer PESEL
# zwracany typ i opis:			str, wartość 'K' jezeli plec to kobieta, lub 'M' jesli to mezczyzna
# autor:						12345678910
# ******************************************************
def sprawdz_plec(pesel: str) -> str:
	return 'K' if int(pesel[-2]) in [0, 2, 4, 6, 8] else 'M'

# ******************************************************
# nazwa funkcji:				sprawdz_sume_kontrolna
# opis funkcji:					Sprawdza, czy suma kontrolna jest zgodna w numerze PESEL
# parametry:					pesel - numer PESEL
# zwracany typ i opis:			bool, True jesli suma kontrolna jest zgodna, False w przeciwnym wypadku
# autor:						12345678910
# ******************************************************
def sprawdz_sume_kontrolna(pesel: str) -> bool:
	wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
	suma = 0

	for indeks, waga in enumerate(wagi):
		suma += int(pesel[indeks]) * waga

	modulo = suma % 10

	reszta = 0 if modulo == 0 else 10 - modulo

	return reszta == int(pesel[-1])

moj_pesel = "56030101193"
moj_pesel = input("Podaj numer PESEL: ")

plec = "Kobieta" if sprawdz_plec(moj_pesel) == 'K' else "Mężczyzna"

print(f"Twoja płeć to: {plec}.")

if sprawdz_sume_kontrolna(moj_pesel):
	print("Suma kontrolna zgadza się w podanym numerze PESEL")
else:
	print("Suma kontrolna nie zgadza się w podanym numerze PESEL!")
