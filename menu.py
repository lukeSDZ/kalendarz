'''
W tym pliku znajdziesz obsługę menu.
Aby utworzyć własny wpis w menu musisz:
1. Stworzyć nową klasę dziedziczącą po MenuCommand.
   * funkcja description() powinna zwracać napis, który zostanie wyświetlony użytkownikowi
   * funkcja execute() powinna zawierać kod, który zostanie wykonany w przypadku wywołania danej opcji w menu
2. Za pomocą funkcji add_command() dodać utworzony obiekt stworzonej przez siebie klasy do menu.
3. Polecenia menu wskazane jest przechowywać na liście np. _commands
'''


class MenuCommand:
    def __init__(self):
        pass
        self.descr = "text"

    def description(self):
        '''Zwróć nazwę z pozycji menu'''
        print(self.descr)
        raise NotImplementedError("Subclass powinny to zaimplementować!")

    def execute(self):
        '''Wykonanie kodu dla danej pozycji menu'''
        raise NotImplementedError("Subclass powinny to zaimplementować!")


class ExitCommand(MenuCommand):
    def __init__(self):
        '''...'''

    def description(self):
        return "Wyjście"
		

    def execute(self):
        '''...'''


class Menu:                         # to jest invoker ktory inicjuje subclassy MenuCommand.
    def __init__(self):
        '''...'''
        self.commands = []

    def add_command(self, cmd):
        '''...'''
        self.commands.append(cmd)

    def run(self):
        '''...'''
        # 1. bedzie display_menu
		
    def stop(self):
        '''...'''

    def _display_menu(self):
        '''...'''

    def _execute_selected_command(self):
        '''
		 Wczytanie od użytkownika numeru pozycji menu:
		cmd_num = ...
		
		Wybór i wykonanie polecenia

        cmd = ...
        cmd.execute()
        '''

menu = ExitCommand()
print(menu.description())