# Параметры для ввода
Param(

$ip_shop,
$name_cartridge
)
#$ip_shop = '192.168.44.15' # Затычка, для проверки можно убрать
$email_to_order = "order@shop-domain.ru"
#$name_cartridge = "Какое_То_Название" # Затычка, для проверки можно убрать
$addr_path = "Disk:\Path\to\to\save\file" # так же расположение где лежит файл для сравнения принтера и его адреса и др данных
$regex = $ip_shop
foreach($line in Get-Content ($addr_path+"\addr_and_org") -Encoding UTF8) {
    if($line -match $regex){
        # Чтение файла и разбивка на данные, [0] = название магазина
        # [1] = Адрес
        # [2] = Организация
        # [3] = Телефон сотрудника рядом с принтером
        $array_data = [regex]::Split($line, '__')
        #echo $array_data
    }
}
try{rm ($addr_path+"\data_file example")}
catch{}
finally{}
New-Item -Path ($addr_path+"\data_file example") -value ('"to":"'+$email_to_order+'",'+"`r`n"+
                                                  '"type_subject":"0",'+"`r`n"+
                                                  '"type_body":"0",'+"`r`n"+
                                                  '"address":"'+$array_data[1]+'",'+"`r`n"+
                                                  '"contact_phone_address":"'+$array_data[3]+'",'+"`r`n"+
                                                  '"cartridge_name":"'+$name_cartridge+'",'+"`r`n"+
                                                  '"organization":"'+$array_data[2]+'"'
                                                 )