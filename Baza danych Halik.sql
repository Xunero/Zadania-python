-- Tworzenie tabeli Uzytkownik
CREATE TABLE Uzytkownik (
    id_uzytkownik INT PRIMARY KEY,
    imie VARCHAR(50),
    imie2 VARCHAR(50),
    nazwisko VARCHAR(50),
    ulica VARCHAR(100),
    nr_domu VARCHAR(10),
    nr_mieszkania VARCHAR(10),
    miejscowosc VARCHAR(100),
    kod_pocztowy VARCHAR(10),
    nr_telefonu VARCHAR(20),
    email VARCHAR(100) UNIQUE
);

-- Tworzenie tabeli HistoriaWypozyczaniaKsiazek
CREATE TABLE HistoriaWypozyczaniaKsiazek (
    id_historia INT PRIMARY KEY,
    id_uzytkownik INT,
    id_pracownik INT,
    id_ksiazka INT,
    id_termin INT,
    id_oplata INT,
    FOREIGN KEY (id_uzytkownik) REFERENCES Uzytkownik(id_uzytkownik),
    FOREIGN KEY (id_pracownik) REFERENCES Pracownik(id_pracownika),
    FOREIGN KEY (id_ksiazka) REFERENCES Ksiazka(id_ksiazka),
    FOREIGN KEY (id_termin) REFERENCES Termin(id_termin),
    FOREIGN KEY (id_oplata) REFERENCES Oplata(id_oplata)
);

-- Tworzenie tabeli Ksiazka
CREATE TABLE Ksiazka (
    id_ksiazka INT PRIMARY KEY,
    tytul VARCHAR(100),
    id_autor INT,
    rok_wydania INT,
    id_uzytkownika INT,
    FOREIGN KEY (id_autor) REFERENCES Autor(id_autor),
    FOREIGN KEY (id_uzytkownika) REFERENCES Uzytkownik(id_uzytkownik)
);

-- Tworzenie tabeli Autor
CREATE TABLE Autor (
    id_autor INT PRIMARY KEY,
    imie VARCHAR(50),
    imie2 VARCHAR(50),
    nazwisko VARCHAR(50)
);

-- Tworzenie tabeli Status
CREATE TABLE Status (
    id_status INT PRIMARY KEY,
    nazwa VARCHAR(50)
);

-- Tworzenie tabeli Zamowienie
CREATE TABLE Zamowienie (
    id_zamowienie INT PRIMARY KEY,
    tytul_ksiazki VARCHAR(100),
    id_pracownika INT,
    ilosc INT,
    Data DATE,
    id_status INT,
    FOREIGN KEY (id_pracownika) REFERENCES Pracownik(id_pracownika),
    FOREIGN KEY (id_status) REFERENCES Status(id_status)
);

-- Tworzenie tabeli Termin
CREATE TABLE Termin (
    id_termin INT PRIMARY KEY,
    id_ksiazka INT,
    data_wypozyczenia DATE,
    termin_oddania DATE,
    data_oddania DATE,
    FOREIGN KEY (id_ksiazka) REFERENCES Ksiazka(id_ksiazka)
);

-- Tworzenie tabeli Oplata
CREATE TABLE Oplata (
    id_oplata INT PRIMARY KEY,
    kwota DECIMAL(10, 2),
    id_typ_oplata INT,
    data DATE,
    id_uzytkownika INT,
    id_pracownika INT,
    FOREIGN KEY (id_typ_oplata) REFERENCES TypOplaty(id_typ_oplaty),
    FOREIGN KEY (id_uzytkownika) REFERENCES Uzytkownik(id_uzytkownik),
    FOREIGN KEY (id_pracownika) REFERENCES Pracownik(id_pracownika)
);

-- Tworzenie tabeli TypOplaty
CREATE TABLE TypOplaty (
    id_typ_oplaty INT PRIMARY KEY,
    nazwa VARCHAR(50)
);

-- Tworzenie tabeli Logowanie
CREATE TABLE Logowanie (
    id_logowania INT PRIMARY KEY,
    id_uzytkownika INT,
    id_pracownika INT,
    login_email VARCHAR(100),
    haslo VARCHAR(100),
    FOREIGN KEY (id_uzytkownika) REFERENCES Uzytkownik(id_uzytkownik),
    FOREIGN KEY (id_pracownika) REFERENCES Pracownik(id_pracownika)
);

-- Tworzenie tabeli Pracownik
CREATE TABLE Pracownik (
    id_pracownika INT PRIMARY KEY,
    imie VARCHAR(50),
    imie2 VARCHAR(50),
    nazwisko VARCHAR(50),
    ulica VARCHAR(100),
    nr_domu VARCHAR(10),
    nr_mieszkania VARCHAR(10),
    miejscowosc VARCHAR(100),
    kod_pocztowy VARCHAR(10),
    nr_telefonu VARCHAR(20),
    email VARCHAR(100) UNIQUE
);