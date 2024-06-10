import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from local_storage import LocalStorage
from cloud_backup import CloudBackup


class PasswordManagerApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)

        self.local_storage = LocalStorage()
        self.cloud_backup = CloudBackup()

        # UI Elements
        self.password_list = toga.Table(['Service', 'Username', 'Password'])
        self.add_button = toga.Button('Add', on_press=self.add_password)
        self.backup_button = toga.Button('Backup', on_press=self.backup_data)

        # Layout
        box = toga.Box(children=[
            self.password_list,
            self.add_button,
            self.backup_button
        ], style=Pack(direction=COLUMN))

        self.main_window.content = box
        self.main_window.show()

    def add_password(self, widget):
        # Implement password adding functionality
        pass

    def backup_data(self, widget):
        # Implement backup functionality
        pass


def main():
    return PasswordManagerApp('Password Manager', 'org.example.passwordmanager')


if __name__ == '__main__':
    main().main_loop()
