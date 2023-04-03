# Import subprocess library
from subprocess import Popen
# Import pywinauto Desktop class and timings class
from pywinauto import Desktop, timings
# Import pywinauto Application class
from pywinauto.application import Application


credentials = {
    "manager": {
        "login": "vasilevich_i",
        "password": "123",
        "shopID": "1",
    },

    "admin": {
        "login": "romanova_a",
        "password": "123",
        "shopID": "2",
    },

    "analyst": {
        "login": "tkachenko_e",
        "password": "123",
        "shopID": "3",
    },
}


timings.always_wait_until(10, 10)
Popen('C:\\Debug\\Course.exe')
main_dlg = Desktop(backend="uia").LoginPage


main_dlg.print_control_identifiers()

user = credentials["manager"]

main_dlg.LoginEdit.type_keys(user['password'], pause=0.05)
main_dlg.Edit1.type_keys(user['shopID'], pause=0.05)
main_dlg.LoginEdit2.type_keys(user['login'], pause=0.05)

main_dlg.submitButton.click_input()
# assert
manager_dlg = Desktop(backend="uia").Manager


manager_dlg.print_control_identifiers()


print("")