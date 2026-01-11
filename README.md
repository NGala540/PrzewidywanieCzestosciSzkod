# Predykcja częstości szkód

## Problem

Celem tego projektu jest analiza oraz przeprowadzenie testów statystycznych na podstawie historycznych danych ubezpieczeniowych. Wykorzystując techniki data science, przeanalizuję kluczowe czynniki wpływające na częstość szkód, takie jak dane demograficzne ubezpieczonych, charakterystyka pojazdów oraz wzorce historycznych roszczeń. Ostatecznym celem jest dostarczenie ubezpieczycielom praktycznych informacji umożliwiających optymalizację strategii taryfowych oraz usprawnienie zarządzania ryzykiem.

## Wprowadzenie

### Częstość szkód

Zrozumienie i przewidywanie częstości szkód ma kluczowe znaczenie dla oceny ryzyka, ustalania składek oraz podejmowania decyzji w branży ubezpieczeniowej. W przeciwieństwie do prawdopodobieństwa wystąpienia pojedynczej szkody, częstość szkód mierzy, jak często występują roszczenia w danym okresie. **Definiuje się ją jako liczbę szkód podzieloną przez łączną liczbę lat ochrony ubezpieczeniowej**, nazywaną również ekspozycją. Dla polis aktywnych krócej niż rok ekspozycja jest proporcjonalnie korygowana.

### System bonus–malus

W ubezpieczeniach system bonus–malus (BMS) to mechanizm dostosowujący wysokość składki klienta w zależności od jego indywidualnej historii szkód. **Bonus** to zazwyczaj zniżka w składce przy odnowieniu polisy, jeśli w poprzednim roku nie zgłoszono szkody. **Malus** oznacza natomiast podwyższenie składki w przypadku wystąpienia szkody w poprzednim roku. Podstawowa zasada BMS mówi, że im wyższa częstość szkód danego ubezpieczonego, tym wyższe koszty ubezpieczenia są mu przeciętnie naliczane. Zasada ta obowiązuje również w systemach ubezpieczeniowych z wysokim udziałem własnym (tzw. franszyzą), wspólnym dla wszystkich ubezpieczonych.

## Opis danych

Źródło danych: R-Package CASDatasets, Version 1.0-6 (2016) by Christophe Dutang [aut, cre], Arthur Charpentier [ctb]

* **IDpol** – identyfikator polisy
* **ClaimNb** – liczba szkód w okresie ekspozycji
* **Exposure** – okres ekspozycji
* **Area** – kod obszaru
* **VehPower** – moc pojazdu, jako kategoria
* **VehAge** – wiek pojazdu (w latach)
* **DrivAge** – wiek kierowcy (w latach; we Francji prawo jazdy można uzyskać od 18 roku życia)
* **BonusMalus** – współczynnik bonus/malus, w przedziale 50–230 (wartości <100 oznaczają bonus, >100 – malus)
* **VehBrand** – marka pojazdu (zakodowana kategoria)
* **VehGas** – rodzaj paliwa (Diesel lub benzyna)
* **Density** – gęstość zaludnienia (liczba mieszkańców na km²) w mieście, w którym mieszka kierowca
* **Region** – region ubezpieczenia we Francji (na podstawie standardowej klasyfikacji francuskiej)
