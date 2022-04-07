'''
W tym pliku znajdziesz obsługę menu.
Aby utworzyć własny wpis w menu musisz:
1. Stworzyć nową klasę dziedziczącą po MenuCommand.
   * funkcja description() powinna zwracać napis, który zostanie wyświetlony użytkownikowi
   * funkcja execute() powinna zawierać kod, który zostanie wykonany w przypadku wywołania danej opcji w menu
2. Za pomocą funkcji add_command() dodać utworzony obiekt stworzonej przez siebie klasy do menu.
3. Polecenia menu wskazane jest przechowywać na liście np. _commands
'''


import cmd


class MenuCommand:                          #to jest COMMAND. Class used to encapsulate information needed by some other method in order to execute
    def __init__(self, menu):
        self.menu = menu

    def description(self):
        '''Zwróć nazwę z pozycji menu'''
        print("Description")
        raise NotImplementedError("Subclassy powinny to zaimplementować!")

    def execute(self):
        '''Wykonanie kodu dla danej pozycji menu'''
        raise NotImplementedError("Subclassy powinny to zaimplementować!")

class NewEventCommand(MenuCommand):         
    def __init__(self, menu):               
        '''...'''
        self.menu = menu                #to nie jest RECEIVER, an instance of a class that can execute the method, given the encapsulated information

    def __str__(self):
        return "Nowe wydarzenie"

    def description(self):
        '''Dodaje wydarzenie'''
        print("Nowe wydarzenie.")
	
    def execute(self):
        '''Uruchamia NewEventCommand'''
        self.description()
        self.add_event()
    
    def add_event(self):
        '''Dodaje wydarzenie'''
        print("na razie nic")

class ExportCommand(MenuCommand):
    def __init__(self, menu):
        '''...'''
        self.menu = menu                #to nie jest RECEIVER, an instance of a class that can execute the method, given the encapsulated information

    def __str__(self):
        return "Wyexportuj kalendarz"

    def description(self):
        '''Exportuje wydarzenia'''
        return "Wyjście"
		
    def execute(self):
        '''Uruchamia ExportCommand'''
        self.description()

class ListEventsCommand(MenuCommand):
    def __init__(self, menu):
        '''...'''
        self.menu = menu                #to nie jest RECEIVER, an instance of a class that can execute the method, given the encapsulated information

    def __str__(self):
        return "Wypisz wydarzenia"

    def description(self):
        '''Wypisuje wydarzenia'''
        print("Wypisz wydarzenia")
		
    def execute(self):
        '''Uruchamia ListEventsCommand'''
        self.description()

class ExitCommand(MenuCommand):                 #Class dedicated to Command Implementation

    def __init__(self, menu):
        '''constructor'''                            
        self.menu = menu                #to nie jest RECEIVER, an instance of a class that can execute the method, given the encapsulated information

    def __str__(self):
        return "Wyjście"

    def description(self):                     #czyli musi się połączyć z kolejnym modułem RECEIVER ktory robi cos z exitem
        '''Zamknięcie kalendarza'''
        print("Zamknięcie kalendarza")

    def execute(self):
        '''Wykonanie komendy wyjścia'''
        self.description()

class Menu:                                  # to jest INVOKER ktory inicjuje subclassy MenuCommand. Decides when the method on the receiver will execute.
    def __init__(self):
        '''constructor'''
        self._commands = []
        self.dzialanie_menu = True
        self.czy_dzialac = True

    def add_command(self, cmd):
        '''Dodaje pozycje menu'''
        self.cmd = cmd
        self._commands.append(cmd)

    def run(self):
        '''...'''
        while self.dzialanie_menu == True:
            self._display_menu()
            self._execute_selected_command()

		
    def stop(self):
        '''...'''

    def _display_menu(self):
        '''Wyświetla dodane pozycje menu z listy'''
        self._cmd_num = 0
        for cmd in self._commands:
            self._cmd_num += 1
            print(self._cmd_num, cmd, "\n")


    def _execute_selected_command(self):
        '''
		 Wczytanie od użytkownika numeru pozycji menu:
		cmd_num = ...
		
		Wybór i wykonanie polecenia

        cmd = ...
        cmd.execute()
        '''
        cmd_number = int(input("Dokonaj wyboru pozycji (1-4):"))
# wiem, ze ogranicza mnie to do manualnego wpisania ilosci warunków, ale nie umiem innaczej
        if cmd_number == 1:
            #print(self._commands[0])
            #self._commands[0].execute()
            cmd = self._commands[0]
            cmd.execute()
        elif cmd_number == 2:
            cmd = self._commands[1]
            cmd.execute()
        elif cmd_number == 3:
            cmd = self._commands[2]
            cmd.execute()
        elif cmd_number == 4:
            cmd = self._commands[3]
            cmd.execute()
            self.dzialanie_menu = False
        else:
            print("\n Niepoprawny numer. Wybierz jeszcze raz")




#potem kod jest taki : 
# command1 = Command(receiver, "Execute Command 1")
# np. DodajEvent = NewEventCommand(receiver, "jakies tam wykonanie")
