from exchangelib import Message, Mailbox, HTMLBody
from config import Models
from datetime import date
import config



def preform_letter(
        type_of_letter:int,
        **pref
    )->Message:
    """Сборщик письма, возвращает пиьсмо готовое к отправке \n
    Типы писем: \n
    0 : Заказ картриджей
    """
    data=config.data
    if type_of_letter == 0:
        """Это заказ картриджа"""
        subject = Models.cartridge_order_subject(item = "Картриджи",
                                                 date = date.today())
        
        body = Models.cartridge_order_body(data=data,
                                           quantity=pref['quantity']
                                           )

    m = Message(
        account=config.account,
        subject=subject,
        body=HTMLBody(body),
        to_recipients = [Mailbox(email_address=data['to'])]
    )


    return m