'''
W tym pliku znajdziesz kod odpowiedzialny za wyświetlanie zdarzeń z kalendarza.

Do zmiany zachowania funkcji list_calendar wykorzystaj strategię ListingStrategy.

'''

#Powinna istnieć
#ogólna funkcja wypisująca zawartość kalendarza, ale format wypisywanych 
# danych powinien
# być określony za pomocą określonego obiektu strategii.
#plik calendar.py z funkcją list_calendar wraz z klasą ListingStrategy, funkcja
#ta jest odpowiedzialna za wywoływanie odpowiednich metod klasy ListingStrategy,
#metody te powinny wypisywać na ekranie dane w odpowiednim formacie,

import re

class ListingStrategy:
    def begin(self):
        pass

    def event(self, title, date, time):
        pass
        Podaj nazwę wydarzenia:
        Podaj datę:
        Podaj godzinę:

    def end(self):
        pass


def list_calendar(calendar, listing_strategy):
    listing_strategy.begin()

    for event in calendar:
        '''...'''
	#	pass

   # listing_strategy.end()

# ..................................pomysl taki: 
class Strategy1(ListingStrategy):
    def execute(self) -> str:
        return "nazwa wydarzenia"
        Title = input()
        if not re.search("[a-z]", Title):
        \w - to 

class Strategy2(ListingStrategy):
    def execute(self) -> str:
        return "strategia 2"

class Strategy3(ListingStrategy):
    def execute(self) -> str:
        return "strategia 3"