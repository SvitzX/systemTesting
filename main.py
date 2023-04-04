# Import subprocess library
from subprocess import Popen
# Import pywinauto Desktop class and timings class
from pywinauto import Desktop, timings
import pytest

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


@pytest.fixture
def login_page():
    Popen('C:\\Debug\\Course.exe')
    main = Desktop(backend="uia").LoginPage
    yield main
    main.TitleBar.Button3.click_input()


timings.always_wait_until(10, 10)


def login_to_account(main, user):
    main.LoginEdit.type_keys(user['password'], pause=0.05)
    main.Edit1.type_keys(user['shopID'], pause=0.05)
    main.LoginEdit2.type_keys(user['login'], pause=0.05)
    main.submitButton.click_input()

def test_manager_search(login_page):
    login_to_account(login_page, credentials["manager"])
    manager_dlg = Desktop(backend="uia").Manager
    manager_dlg.TabItem2.click_input()
    manager_dlg.Edit.type_keys("VHS", pause=0.05)
    manager_dlg.Button1.click_input()

    assert manager_dlg.DataGridView.Custom2.Edit4.legacy_properties()["Value"] == "Проигрыватель VHS кассет"

    manager_dlg.Button4.click_input()

def test_customer_add(login_page):
    login_to_account(login_page, credentials["manager"])
    manager_dlg = Desktop(backend="uia").Manager

    manager_dlg.Edit1.type_keys("Белый", pause=0.05)
    manager_dlg.Edit2.type_keys("Сергей", pause=0.05)
    manager_dlg.Listbox.click_input()
    manager_dlg.Button1.click_input()

    assert manager_dlg.Dialog2.Static0.legacy_properties()["Name"] == "Покупатель добавлен!"
    manager_dlg.Dialog2.Button.click_input()
    manager_dlg.Button4.click_input()





if __name__ == "__main__":
    Popen('C:\\Debug\\Course.exe')
    main = Desktop(backend="uia").LoginPage
    login_to_account(main, credentials["admin"])
    admin_dlg = Desktop(backend="uia").Administrator
    admin_dlg.print_control_identifiers()
    #ввод имени
    admin_dlg.LoginEdit5.type_keys("Сергей", pause=0.05)
    #ввод фамилии
    admin_dlg.LoginEdit4.type_keys("Спиров", pause=0.05)
    #ввод зарплаты
    admin_dlg.LoginEdit3.type_keys(70000, pause=0.05)
    #ввод логина
    admin_dlg.LoginEdit2.type_keys("spirov_s", pause=0.05)
    #ввод пароля
    admin_dlg.LoginEdit1.type_keys("123", pause=0.05)
    admin_dlg.Listbox4.click_input()
    from pywinauto import mouse

    rect = admin_dlg.rectangle()

    top, left = rect.top, rect.left

    mouse.click(coords=(top+(280-130), left+(460-130)))


    print("")
# #пока не понял, как выбрать роль, магазин, дату рождения и город


# #for analyst (it works)
# user = credentials["analyst"]
#
# main_dlg.LoginEdit.type_keys(user['password'], pause=0.05)
# main_dlg.Edit1.type_keys(user['shopID'], pause=0.05)
# main_dlg.LoginEdit2.type_keys(user['login'], pause=0.05)
# main_dlg.submitButton.click_input()
# analyst_dlg = Desktop(backend="uia").Analyst
# analyst_dlg.print_control_identifiers()
# #нажатие кнопки склад
# analyst_dlg.Button.click_input()
# #нажатие кнопки топ по продажам менеджеров
# analyst_dlg.Button2.click_input()
# #нажатие кнопки сумма продаж
# analyst_dlg.Button4.click_input()
# #нажатие кнопки топ по товарам
# analyst_dlg.Button3.click_input()
print("")