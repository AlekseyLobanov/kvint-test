import core

def test_simple():
    """Тест из спецификации"""
    uid = "tester"
    assert core.dialog.proc(uid, "/start") == "Какую вы хотите пиццу? Большую или маленькую?"
    assert core.dialog.proc(uid, "Большую") == "Как вы будете платить?"
    assert core.dialog.proc(uid, "Наличкой") == "Вы хотите большую пиццу, оплата - наличкой?"
    assert core.dialog.proc(uid, "Да") == "Спасибо за заказ"


def test_variation():
    """Если фразы немного поменяются"""
    uid = "tester2"
    assert core.dialog.proc(uid, "/start") == "Какую вы хотите пиццу? Большую или маленькую?"
    assert core.dialog.proc(uid, "большую") == "Как вы будете платить?"
    assert core.dialog.proc(uid, "наличными") == "Вы хотите большую пиццу, оплата - наличкой?"
    assert core.dialog.proc(uid, "YES!") == "Спасибо за заказ"


def test_two_users():
    """Возможно ли обрабатывать сразу двух пользователей"""
    uid = "tester3"
    uid2 = "tester4"
    assert core.dialog.proc(uid, "/start") == "Какую вы хотите пиццу? Большую или маленькую?"
    assert core.dialog.proc(uid, "Большую") == "Как вы будете платить?"
    assert core.dialog.proc(uid2, "/start") == "Какую вы хотите пиццу? Большую или маленькую?"
    assert core.dialog.proc(uid2, "большую") == "Как вы будете платить?"
    assert core.dialog.proc(uid, "Наличкой") == "Вы хотите большую пиццу, оплата - наличкой?"
    assert core.dialog.proc(uid, "Да") == "Спасибо за заказ"
    assert core.dialog.proc(uid2, "наличными") == "Вы хотите большую пиццу, оплата - наличкой?"
    assert core.dialog.proc(uid2, "YES!") == "Спасибо за заказ"

def test_return():
    """Что будет, если пользователь попробует написать повторно"""
    uid = "tester_return"
    assert core.dialog.proc(uid, "/start") == "Какую вы хотите пиццу? Большую или маленькую?"
    assert core.dialog.proc(uid, "Большую") == "Как вы будете платить?"
    assert core.dialog.proc(uid, "Наличкой") == "Вы хотите большую пиццу, оплата - наличкой?"
    assert core.dialog.proc(uid, "Да") == "Спасибо за заказ"
    
    assert core.dialog.proc(uid, "/start") == "Какую вы хотите пиццу? Большую или маленькую?"
    assert core.dialog.proc(uid, "большую") == "Как вы будете платить?"
    assert core.dialog.proc(uid, "наличными") == "Вы хотите большую пиццу, оплата - наличкой?"
    assert core.dialog.proc(uid, "YES!") == "Спасибо за заказ"
