
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



file = open("1e3a.dat", 'r') # otworzenie pliku w trybie odczytu. Przy próbie zapisu wyskoczyłby błąd)

# main processing loop
for PESEL in file: # pętla iterująca po pliku linijka po linijce. Nazwa PESEL jest taką "tymczasową" zmienną na potrzeby aktualnego 
                   # przebiegu pętli, w której to zmiennej znajduje się aktualna linijka z pliku
    PESEL = PESEL.strip() # na końcu każdej linii znajduje się znak nowej linii. Metoda strip() usuwa ten znak (tak jak i inne białe znaki)
    print(len(PESEL))
        
file.close() #zamknięcie pliku. Ważna sprawa :)


