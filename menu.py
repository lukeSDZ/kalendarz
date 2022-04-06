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
    def __init__(self, receiver):
        self.receiver = receiver

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

    def description(self):
        return "Nowe wydarzenie."

    def __str__(self):
        return "Nowe wydarzenie"
		
    def execute(self):
        '''...'''
        self.description()
    
    def add_event(self):
        '''...'''

class ExportCommand(MenuCommand):
    def __init__(self, menu):
        '''...'''
        self.menu = menu                #to nie jest RECEIVER, an instance of a class that can execute the method, given the encapsulated information

    def __str__(self):
        return "Wyexportuj kalendarz"

    def description(self):
        return "Wyjście"
		
    def execute(self):
        '''...'''
        self.description()

class ListEventsCommand(MenuCommand):
    def __init__(self, menu):
        '''...'''
        self.menu = menu                #to nie jest RECEIVER, an instance of a class that can execute the method, given the encapsulated information

    def __str__(self):
        return "Wypisz wydarzenia"

    def description(self):
        return "Wyjście"
		
    def execute(self):
        '''...'''
        self.description()

class ExitCommand(MenuCommand):                 #Class dedicated to Command Implementation

    def __init__(self, menu):
        '''constructor'''               #w oryginale obok self tu było menu               
        self.menu = menu                #to nie jest RECEIVER, an instance of a class that can execute the method, given the encapsulated information

    def __str__(self):
        return "Wyjście"

    def description(self):                      #czyli musi się połączyć z kolejnym modułem RECEIVER ktory robi cos z exitem
        return "Wyjście"


    def execute(self):
        '''Executes the exit command.'''
        self.description()
        print("nic sie nei dzieje")

class Menu:                                  # to jest INVOKER ktory inicjuje subclassy MenuCommand. Decides when the method on the receiver will execute.
    def __init__(self):
        '''constructor'''
        self.commands = []
        self.cmd_num = 0

    def add_command(self, cmd):
        '''adds menu items'''
        self.cmd = cmd
        self.commands.append(cmd)

    def run(self):
        '''...'''
        self._display_menu()
        self._execute_selected_command()

		
    def stop(self):
        '''...'''

    def _display_menu(self):
        '''...'''
        for cmd in self.commands:
            self.cmd_num += 1
            print(self.cmd_num, cmd)


    def _execute_selected_command(self):
        '''
		 Wczytanie od użytkownika numeru pozycji menu:
		cmd_num = ...
		
		Wybór i wykonanie polecenia

        cmd = ...
        cmd.execute()
        '''
        cmd_number = int(input("Select menu item (1-4):"))
        if cmd


#potem kod jest taki : 
# command1 = Command(receiver, "Execute Command 1")
# np. DodajEvent = NewEventCommand(receiver, "jakies tam wykonanie")
