import ast
from exchangelib import DELEGATE, Account, Credentials, BaseProtocol, NoVerifyHTTPAdapter, Configuration, NTLM
import urllib3


#Раздел "Заплатки"
# Отключаю предупреждения об ошибках, чтобы не видеть что настоятельно просит сделать проверку сертифката 
urllib3.disable_warnings()
# Отключаю проверку сертифката
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter


class Organization(object):
    """0 is name \n\r
       1 is inn"""
    def __init__(
            self,
            name:str,
            inn:int
        )->None:

        self.name = name
        self.inn = inn

    def __call__(self):
        return self.name,self.inn
    

def get_data():

    """[to] - Получатель письма \n
    [type_subject] - ID темы письма\n
    [type_body] - ID тела письма \n
    [address] - Куда доставить \n
    [contact_phone_address] - Контактный телефон на месте \n
    [cartridge_name] - Название Картриджа \n
    [organization] - Организация получатель *Технически полезная часть
    """
    try:
        temp = open("data_file example", encoding='utf-8',mode='r+')
        answer = ast.literal_eval(str('{'+temp.read()+'}'))
        #temp.seek(0)
        #temp.write("Done")
        #temp.truncate()
        return answer

    finally:
        temp.close()
        
data = get_data()
contact_phone = str("+7(999)999-99-99")
contact_phone_admin = str("+7(999)999-99-99")
contact_email_admin = str("admin@domain.com")


ORG1=Organization("ООО Организация 1",int('INN-10digits'))
ORG2=Organization("ООО Организация 2",int('INN-10digits'))
ORG3=Organization("ООО Организация 3",int('INN-10digits'))
ORG4=Organization("ООО Организация 4",int('INN-10digits'))
try:
    if (data["organization"] != None) and (data["organization"] == 'VDB'):
        org = ORG1
    elif data["organization"] == 'VDS':
        org = ORG2
    elif data["organization"] == 'TV':
        org = ORG3
    else: org =ORG4
except:
    org = ""


class Models():
    def cartridge_order_subject(
            item:str='',
            date:str=''
        )->str:
        """Модель для темы для заказа \n\r 
        Заказ {item} на {organization} от {date}"""

        return f"Заказ {item} на {org()[0]} от {date}"
    

    def cartridge_order_body(
            quantity:int=1,
            **data
        )->str:
        """модель для тела письма для заказа"""

        return f"""Здравствуйте, хочу заказать картриджи на организацию: {org()[0]}, ИНН:{org()[1]},
                <br> Адрес для доставки: {data['data']['address']},
                <br> Модель картриджа: {data['data']['cartridge_name']},
                <br> Количество: {quantity},
                <br> Контактный телефон для доставки: {data['data']['contact_phone_address']},
                <br> Контактный телефон по заказу: {contact_phone},
                <br><br> Отправьте пожалуйста ответ на это письмо с указанием общей суммы заказа и вложенным счетом
                <br><br><br><br> Письмо было составлено автоматически, 
                <br> если вы увидели какие то недочеты или вам нужен определенный формат тела письма для общения с вами,
                <br> ниже есть контакты для связи =)
                <br> Контактная почта: {contact_email_admin},
                <br> Контактный телефон: {contact_phone_admin}
                """
robot= Credentials(
    username='Email-Username@domain.com',
    password='P@$$word'
)


config_excange=Configuration(
    credentials=robot,
    server='ip or domain',
    auth_type=NTLM
)
account = Account(
    primary_smtp_address=robot.username,
    credentials=robot,
    config=config_excange,
    autodiscover=False,
    access_type=DELEGATE
)

if __name__ == "__main__":
    pass

