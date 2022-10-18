import phonenumbers 
from phonenumbers import timezone, carrier, geocoder #Libraries

number = input("Telefon numarası giriniz: ") #Enter Phone number with country code like +90 531 600 00 00
phone = phonenumbers.parse(number) #Parse number

time = timezone.time_zones_for_geographical_number(phone)
car = carrier.name_for_number(phone, "ülke_kodu")
reg = geocoder.description_for_number(phone, "ülke_kodu")

print(phone) #Country Code
print(time) #Adress
print(car) #Provider
#print(reg) #Doesnt work