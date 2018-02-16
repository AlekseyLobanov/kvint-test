"""
Модуль обработки пользовательских запросов.
"""

import logging

from transitions import Machine

STATES = ["begin", "big_payment_select", "big_cash_confirm", "success", "failure"]
STATE_TO_TEXT = {
    "begin": "Какую вы хотите пиццу? Большую или маленькую?",
    "big_payment_select": "Как вы будете платить?",
    "big_cash_confirm": "Вы хотите большую пиццу, оплата - наличкой?",
    "success": "Спасибо за заказ",
    "failure": "Я вас не поняла, давайте начнём сначала"
}

def _normalize_text(text):
    """
    Нормализует текст: приводит к нижнему регистру
    """
    text = text.lower()
    
    if len(text.split(" ")) == 1:
        if "больш" in text:
            return "big"
        elif "наличк" in text or "наличн" in text:
            return "cash"
        elif text == "да" or text == "yes":
            return "yes"
    return text


def _place_order(uid:str):
    """
    Принимает готовый заказ
    """
    def _place_order():
        print("order from {}".format(uid))
    
    return _place_order


def _get_state_machine(uid:str):
    """
    Строит необходимую машину состояний
    """
        
    transitions = [
        {
            'trigger': 'big',
            'source': 'begin',
            'dest': 'big_payment_select'
        },
        {
            'trigger': 'cash',
            'source': 'big_payment_select',
            'dest': 'big_cash_confirm'
        },
        {
            'trigger': 'yes',
            'source': 'big_cash_confirm',
            'dest': 'success',
            'after': _place_order(uid)
        },
        {
            'trigger': 'fail',
            'source': '*',
            'dest': 'failure'
        }
    ]

    machine = Machine(states=STATES, transitions=transitions, initial='begin')
    return machine


class DialogProcessor(object):
    """
    Обрабатывает диалоги вместе с контекстом.
    Хранит контекст.
    """
    def __init__(self):
        self.machines = {}  # на каждый id своя машина состояний
    
    def proc(self, uid:str, text:str) -> str:
        """
        Обрабатывает текст от uid
        """
        if uid not in self.machines:
            self.machines[uid] = _get_state_machine(uid)
            return STATE_TO_TEXT[self.machines[uid].state]
        
        try:
            self.machines[uid].trigger(_normalize_text(text))
            return STATE_TO_TEXT[self.machines[uid].state]
        except:
            logging.info("Wrong text from {} state {} text is {}".format(
                uid,
                self.machines[uid].state,
                text
            ))
            return "Переформулируйте, пожалуйста"

    def _get_state(self, uid:str):
        if uid in self.machines:
            return self.machines[uid].state
        else:
            return None

dialog = DialogProcessor()

if __name__ == "__main__":
    print("Don't run this file!")
