''' importy 
from menu import Menu
from calendar import ...
'''
from menu import *


#
# w tym miejscu możesz napisać kod odpowiedzialny za menu (polecenia)
# i strategie wyświetlania wydarzeń z kalendarza
#



def main():
    # wydarzenia przechowuj w liście
    calendar = []

    # zakładamy, że wydarzenie to słownik z kluczami title, date, time
    # jeśli chcesz przechowywać wydarzenie w innej strukturze danych
    # to pamiętaj o zmianie jej obsługi w funkcji list_calendar
    #event = {
    #    'title': 'Programowanie obiektowe w jezyku PYTHON - Cwiczenia',
    #    'date': '27.03.2022',
    #    'time': '9:00',
    #}
    #
    #dodaj wydarzenie event do kalendarza calendar

    menu = Menu()                                   #invoker = MenuInvoker()
    #if __name__ == "__main__":
    # tutaj możesz dodać kolejne polecenia do menu
    menu.add_command(NewEventCommand(menu))
    menu.add_command(ListEventsCommand(menu))
    menu.add_command(ExportCommand(menu))
    menu.add_command(ExitCommand(menu))

    menu.run()

main()
