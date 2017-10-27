"""
Deklaracja zmiennych. Tak jak wspominałem, to jest moja subiektywna opinia, ale nie przepadam za takim sposobem deklaracji zmiennych.
Mimo, że zajmuje to więcej miejsca to wolę deklaracje w stylu
total = 0
correct = 0
itd

PESEL_length to długość numeru PESEL. Trzeba pamiętać, że długość numeru to 11 znaków(cyfr) ALE stringi, tablice, tuple i inne
tego typu elementy są numerowane od 0.
PESEL_weights - tupla z wagami każdej cyfry w numerze PESEL. Tupla, jak mówiłem, różni się od listy tym, że nie można z niej
nic usunąć, zmienić ani nic do niej dodać

days_31 i days_30 - tuple, w których będą numery miesięcy z 30 dniami i 31 dniami. Wykorzystamy je później do sprawdzenia poprawności daty
"""
# counters
total = correct = male = female = 0
invalid_length = invalid_digit = invalid_date = invalid_checksum = 0
checksum = 0

# date variables
day = month = year = 0

PESEL_length = 11
PESEL_weigths = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)

days_31 = (1, 3, 5, 7, 8, 10, 12)
days_30 = (4, 6, 9, 11)

"""
Funkcja make_year.
Jako argumenty tej funkcji podajemy miesiąc (w formacie MM jako integer) i rok (w formacie YY jako string)
Zależnie od stulecia do miesiąca dodaje się 20, 40, 60, 80 lub nic. Idea tej funkcji polega na tym, żeby
po kolei odejmować od miesiąca w/w liczby i sprawdzać czy wynik jest ujemny. Przykład:

Miesiąc: 52, rok: 02
Sprawdzamy czy 52-80 jest większe od zera. Nie jest, czyli sprawdzamy dalej
Sprawdzamy czy 52-60 jest większe od zera. Nie jest, czyli sprawdzamy dalej
Sprawdzamy czy 52-40 jest większe od zera. Jest, więc podany rok mieści się między 2100 a 2199.
    Łączymy dwa stringi: "21" (czyli stulecie, do którego należy PESEL) + "02" (czyli rok w numerze PESEL)
    Powstały string "2102" rzutujemy (czyli konwertujemy) na intiger i zwracamy.
    
Funkcja sprawdza liczby malejąco z prostej przeczyny. Spróbujmy ten sam miesiąc i rok, ale odwrotnie.
Sprawdzamy czy 52-20 jest większe od zera. Jest. Czyli funkcja błędnie zwróciłaby rok 2002 (mimo, że PESEL jest ze stulecia 2100-2199)
"""
def make_year(m, y):

    if m - 80 > 0:
        y = "18" + y
    elif m - 60 > 0:
        y = "22" + y
    elif m - 40 > 0:
        y = "21" + y
    elif m - 20 > 0:
        y = "20" + y
    else:
        y = "19" + y

    return int(y)


file = open("1e3.dat", 'r') # otworzenie pliku w trybie odczytu. Przy próbie zapisu wyskoczyłby błąd)

# main processing loop
for PESEL in file: # pętla iterująca po pliku linijka po linijce. Nazwa PESEL jest taką "tymczasową" zmienną na potrzeby aktualnego 
                   # przebiegu pętli, w której to zmiennej znajduje się aktualna linijka z pliku
    PESEL = PESEL.strip() # na końcu każdej linii znajduje się znak nowej linii. Metoda strip() usuwa ten znak (tak jak i inne białe znaki)
    total +=1 # zliczamy linijkę po linijce
    if len(PESEL) != PESEL_length: # sprawdzenie czy PESEL ma poprawną długość. Używamy != bo możemy napotkać zarówno za długie
                                   # jak i za krótkie numery
        invalid_length += 1        # jeśli długość się nie zgadza to zwiększamy zmienną invalid
        continue                   # i przerywamy AKTUALNĄ iterację przechodząc do kolejnej (żeby niepotrzebnie nie wykonywał się dalszy kod)
    elif not PESEL.isdigit():      # sprawdzamy czy nie ma innych znaków niż cyfry. Na końcu pliku w komentarzu napiszę różnicę między
        invalid_digit += 1         # isnumeric a isdigit
        continue
    
    day = int(PESEL[4:6])          # wycinamy z numeru PESEL dwie cyfry odpowiadające za dzień
    month = int(PESEL[2:4])%20     # analogicznie, przy czym dodatkowo wykonujemy modulo. Tak, żeby w przypadku innego stulecia niż 1900-1999
                                   # otrzymać poprawny numer miesiąca
    year = make_year(month, PESEL[0:2]) # patrz opis funkcji :)
    
    if month > 12: # sprawdzenie czy numer m-ca się zgadza. Jeśli nie, zwiększamy zmienną, przerywamy aktualną iterację
        invalid_date += 1
        continue

    """
    Sprawdzamy czy miesiąc ma 31 dni czy 30 (czyli sprawdzamy czy numer miesiąca znajduje się w jednej czy w drugiej tupli)
    i w zależności od wyniku sprawdzamy czy dzień jest większy od 31 lub 30.
    Jeśli miesiąc nie znajduje się ani w jednej ani w drugiej tupli to znaczy, że mamy do czynienia z lutym i tutaj zaczyna się jazda bez trzymanki.
    Pokazuję i objaśniam (mam nadzieję, że podstawy logiki znasz ;)):

    Rok przestępny jest wtedy, kiedy spełniony jest jeden z warunków:
    Rok _jest_ podzielny przez 4 (czyli rok MODULO 4 == 0) I _nie_jest_ podzielny przez 100 (czyli rok MODULO 100 != 0)
    LUB
    Rok _jest_ podzielny przez 400 (czyli rok MODULO 400 == 0).

    Jeśli jest spełniony jeden z tych warunków to mamy rok przestępny, czyli luty ma 29 dni. Więc sprawdzamy czy dzień jest większy od 29.
    Jeśli żaden z tych warunków nie jest spełniony to mamy "normalny" rok, czyli luty ma 28 dni. Więc sprawdzamy czy dzień jest większy od 28.

    I tyle, jeśli chodzi o zmiany.
    """
    if month in days_31:
        if day > 31:
            invalid_date += 1
            continue
    elif month in days_30:
        if day > 30:
            invalid_date += 1
            continue
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                invalid_date += 1
                continue
        else:
            if day > 28:
                invalid_date += 1
                continue
       
    """
    Po kolei:
    PESEL ma 11 cyfr. Ostatnia cyfra jest cyfrą kontrolną, więc jej nie bierzemy pod uwagę, jeśli chodzi o obliczenia.
    Czyli obchodzi nas 10 cyfr. Jak na początku wspomniałem - stringi są numerowane od 0, więc pierwszy indeks będzie równy 0 a ostatni 9
    PESEL_lenght jest równy 11 (czyli tyle, ile cyfr jest w numerze PESEL)
    
    Tupla (PESEL_weights) ma 10 elementów i obchodzi nas 10 cyfr w numerze PESEL jeśli chodzi o liczenie sumy kontrolnej.
    Więc musimy iterować od pierwszego elemetu (o indeksie 0) do 10 elementu (o indeksie 9)
    
    for i range(PESEL_lenght - 1) po przetłumaczeniu na ludzki brzmi tak:
    stwórz tymczasową zmienną i.
    Nadaj jej wartość 0 (to i poprzedni wiersz to deklaracja pętli)
    wykonaj jakieś tam działania
    Zwiększ wartość i o 1. Sprawdż czy mieści się w zakresie (a zakres to range(PESEL_lenght - 1)  czyli range(10) czyli 0...9
    Jeśli tak - wykonaj pętlę ponownie. Jeśli nie - wyjdż z pętli.
    
    
    Ta tymczasowa zmienna "i" jest dostępna dla zmiennych, tablic i generalnie wszystkiego WEWNĄTRZ tę pętli. Czyli działa to tak:
    Zmienna i = 0.
    Mnożymy element o indeksie i (czyli 0) z tupli przez cyfrę o indeksie i (czyli 0). Wynik dodajemy do checksum
    i = i+1
    i = 1 (mieści sie w zakresie, więc wykonujemy pętlę)
    Mnożymy element o indeksie i (czyli 1) z tupli przez cyfrę o indeksie i (czyli 1). Wynik dodajemy do checksum
    itd itd...
    """
    for i in range(PESEL_length - 1):
        checksum += PESEL_weigths[i] * int(PESEL[i])

    checksum = (10 - (checksum % 10)) % 10

    # analogicznie j/w
    if checksum != int(PESEL[10]):
        invalid_checksum += 1
        continue

    correct += 1 # jeśli do tej pory nie przerwało pętli to znaczy, że PESEL jest poprawny. Czyli zwiększamy zmienną correct
    if (int(PESEL[9]) % 2) == 0: # i sprawdzamy płeć
        female += 1
    else:
        male += 1
        
file.close() #zamknięcie pliku. Ważna sprawa :)

print(total, correct, female, male)
print(invalid_length, invalid_digit, invalid_date, invalid_checksum)

"""
Różnica między isdigit a isnumeric: Nie chcąc się już rozpisywać i mącić: wspomniany stackoverflow :)
https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python
"""
