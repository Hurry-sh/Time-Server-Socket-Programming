import socket
import datetime
import pytz
import time
from _thread import *
import threading
import ssl

print_lock = threading.Lock()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = "127.0.0.1"
# host = "172.20.10.4"


ThreadCount = 0


locations = {
    "afghanistan": "Asia/Kabul",
    "albania": "Europe/Tirane",
    "algeria": "Africa/Algiers",
    "andorra": "Europe/Andorra",
    "angola": "Africa/Luanda",
    "antigua and barbuda": "America/Antigua",
    "argentina": "America/Argentina/Buenos_Aires",
    "armenia": "Asia/Yerevan",
    "australia": "Australia/Sydney",
    "austria": "Europe/Vienna",
    "azerbaijan": "Asia/Baku",
    "bahamas": "America/Nassau",
    "bahrain": "Asia/Bahrain",
    "bangladesh": "Asia/Dhaka",
    "barbados": "America/Barbados",
    "belarus": "Europe/Minsk",
    "belgium": "Europe/Brussels",
    "belize": "America/Belize",
    "benin": "Africa/Porto-Novo",
    "bhutan": "Asia/Thimphu",
    "bolivia": "America/La_Paz",
    "bosnia and herzegovina": "Europe/Sarajevo",
    "botswana": "Africa/Gaborone",
    "brazil": "America/Sao_Paulo",
    "brunei": "Asia/Brunei",
    "bulgaria": "Europe/Sofia",
    "burkina faso": "Africa/Ouagadougou",
    "burundi": "Africa/Bujumbura",
    "cabo verde": "Atlantic/Cape_Verde",
    "cambodia": "Asia/Phnom_Penh",
    "cameroon": "Africa/Douala",
    "canada": "America/Toronto",
    "central african republic": "Africa/Bangui",
    "chad": "Africa/Ndjamena",
    "chile": "America/Santiago",
    "china": "Asia/Shanghai",
    "colombia": "America/Bogota",
    "comoros": "Indian/Comoro",
    "congo (congo-brazzaville)": "Africa/Brazzaville",
    "costa rica": "America/Costa_Rica",
    "croatia": "Europe/Zagreb",
    "cuba": "America/Havana",
    "cyprus": "Asia/Nicosia",
    "czechia (czech republic)": "Europe/Prague",
    "democratic republic of the congo (congo-kinshasa)": "Africa/Kinshasa",
    "denmark": "Europe/Copenhagen",
    "djibouti": "Africa/Djibouti",
    "dominica": "America/Dominica",
    "dominican republic": "America/Santo_Domingo",
    "east timor (timor-leste)": "Asia/Dili",
    "ecuador": "America/Guayaquil",
    "egypt": "Africa/Cairo",
    "el salvador": "America/El_Salvador",
    "equatorial guinea": "Africa/Malabo",
    "eritrea": "Africa/Asmara",
    "estonia": "Europe/Tallinn",
    "eswatini (fmr. 'swaziland')": "Africa/Mbabane",
    "ethiopia": "Africa/Addis_Ababa",
    "fiji": "Pacific/Fiji",
    "finland": "Europe/Helsinki",
    "france": "Europe/Paris",
    "gabon": "Africa/Libreville",
    "gambia": "Africa/Banjul",
    "georgia": "Asia/Tbilisi",
    "germany": "Europe/Berlin",
    "ghana": "Africa/Accra",
    "greece": "Europe/Athens",
    "grenada": "America/Grenada",
    "guatemala": "America/Guatemala",
    "guinea": "Africa/Conakry",
    "guinea-bissau": "Africa/Bissau",
    "guyana": "America/Guyana",
    "haiti": "America/Port-au-Prince",
    "holy see": "Europe/Vatican",
    "honduras": "America/Tegucigalpa",
    "hungary": "Europe/Budapest",
    "iceland": "Atlantic/Reykjavik",
    "india": "Asia/Kolkata",
    "indonesia": "Asia/Jakarta",
    "iran": "Asia/Tehran",
    "iraq": "Asia/Baghdad",
    "ireland": "Europe/Dublin",
    "israel": "Asia/Jerusalem",
    "italy": "Europe/Rome",
    "ivory coast": "Africa/Abidjan",
    "jamaica": "America/Jamaica",
    "japan": "Asia/Tokyo",
    "jordan": "Asia/Amman",
    "kazakhstan": "Asia/Almaty",
    "kenya": "Africa/Nairobi",
    "kiribati": "Pacific/Tarawa",
    "kuwait": "Asia/Kuwait",
    "kyrgyzstan": "Asia/Bishkek",
    "laos": "Asia/Vientiane",
    "latvia": "Europe/Riga",
    "lebanon": "Asia/Beirut",
    "lesotho": "Africa/Maseru",
    "liberia": "Africa/Monrovia",
    "libya": "Africa/Tripoli",
    "liechtenstein": "Europe/Vaduz",
    "lithuania": "Europe/Vilnius",
    "luxembourg": "Europe/Luxembourg",
    "madagascar": "Indian/Antananarivo",
    "malawi": "Africa/Blantyre",
    "malaysia": "Asia/Kuala_Lumpur",
    "maldives": "Indian/Maldives",
    "mali": "Africa/Bamako",
    "malta": "Europe/Malta",
    "marshall islands": "Pacific/Majuro",
    "mauritania": "Africa/Nouakchott",
    "mauritius": "Indian/Mauritius",
    "mexico": "America/Mexico_City",
    "micronesia": "Pacific/Chuuk",
    "moldova": "Europe/Chisinau",
    "monaco": "Europe/Monaco",
    "mongolia": "Asia/Ulaanbaatar",
    "montenegro": "Europe/Podgorica",
    "morocco": "Africa/Casablanca",
    "mozambique": "Africa/Maputo",
    "myanmar (formerly burma)": "Asia/Yangon",
    "namibia": "Africa/Windhoek",
    "nauru": "Pacific/Nauru",
    "nepal": "Asia/Kathmandu",
    "netherlands": "Europe/Amsterdam",
    "new zealand": "Pacific/Auckland",
    "nicaragua": "America/Managua",
    "niger": "Africa/Niamey",
    "nigeria": "Africa/Lagos",
    "north korea": "Asia/Pyongyang",
    "north macedonia (formerly macedonia)": "Europe/Skopje",
    "norway": "Europe/Oslo",
    "oman": "Asia/Muscat",
    "pakistan": "Asia/Karachi",
    "palau": "Pacific/Palau",
    "palestine state": "Asia/Gaza",
    "panama": "America/Panama",
    "papua new guinea": "Pacific/Port_Moresby",
    "paraguay": "America/Asuncion",
    "peru": "America/Lima",
    "philippines": "Asia/Manila",
    "poland": "Europe/Warsaw",
    "portugal": "Europe/Lisbon",
    "qatar": "Asia/Qatar",
    "romania": "Europe/Bucharest",
    "russia": "Europe/Moscow",
    "rwanda": "Africa/Kigali",
    "saint kitts and nevis": "America/St_Kitts",
    "saint lucia": "America/St_Lucia",
    "saint vincent and the grenadines": "America/St_Vincent",
    "samoa": "Pacific/Apia",
    "san marino": "Europe/San_Marino",
    "sao tome and principe": "Africa/Sao_Tome",
    "saudi arabia": "Asia/Riyadh",
    "senegal": "Africa/Dakar",
    "serbia": "Europe/Belgrade",
    "seychelles": "Indian/Mahe",
    "sierra leone": "Africa/Freetown",
    "singapore": "Asia/Singapore",
    "slovakia": "Europe/Bratislava",
    "slovenia": "Europe/Ljubljana",
    "solomon islands": "Pacific/Guadalcanal",
    "somalia": "Africa/Mogadishu",
    "south africa": "Africa/Johannesburg",
    "south korea": "Asia/Seoul",
    "south sudan": "Africa/Juba",
    "spain": "Europe/Madrid",
    "sri lanka": "Asia/Colombo",
    "sudan": "Africa/Khartoum",
    "suriname": "America/Paramaribo",
    "sweden": "Europe/Stockholm",
    "switzerland": "Europe/Zurich",
    "syria": "Asia/Damascus",
    "tajikistan": "Asia/Dushanbe",
    "tanzania": "Africa/Dar_es_Salaam",
    "thailand": "Asia/Bangkok",
    "togo": "Africa/Lome",
    "tonga": "Pacific/Tongatapu",
    "trinidad and tobago": "America/Port_of_Spain",
    "tunisia": "Africa/Tunis",
    "turkey": "Europe/Istanbul",
    "turkmenistan": "Asia/Ashgabat",
    "tuvalu": "Pacific/Funafuti",
    "uganda": "Africa/Kampala",
    "ukraine": "Europe/Kiev",
    "united arab emirates": "Asia/Dubai",
    "united kingdom": "Europe/London",
    "united states": "America/New_York",
    "uruguay": "America/Montevideo",
    "uzbekistan": "Asia/Samarkand",
    "vanuatu": "Pacific/Efate",
    "venezuela": "America/Caracas",
    "vietnam": "Asia/Ho_Chi_Minh",
    "yemen": "Asia/Aden",
    "zambia": "Africa/Lusaka",
    "zimbabwe": "Africa/Harare",
}

try:
    server_socket.bind((host, 9999))
    server_socket.listen(5)

except socket.error as e:
    print(str(e))

print('\n\t\t\t\t\t\t\t  Naa Ready!')
print("\t\t\t\t\tCreated by Harish K, Hari Shankar & K R Druva")
server_socket.listen(5)

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="CN\server.crt", keyfile="CN\server.key")

def get_time(location):
    tz = pytz.timezone(locations.get(location))
    local_time = datetime.datetime.now(tz)
    return local_time.strftime("%H:%M:%S")

def client_thread(conn , addr):
    conn.send(str.encode('\n\tTIME SERVER\n\t-----------\n\nEnter a location : '))
    location = conn.recv(1024).decode().lower()
    
    while True:
        conn.send(str.encode('\nDisplay current time? (Y/N): '))
        response = conn.recv(1024).decode().upper()
        
        if response == 'Y':
            start_time = datetime.datetime.now(pytz.timezone(locations.get(location, "UTC")))
            while (datetime.datetime.now(pytz.timezone(locations.get(location, "UTC"))) - start_time).seconds < 10:
                current_time = get_time(location)
                conn.sendall(str.encode(f"\nCurrent time in {location.title()}: {current_time}"))
                time.sleep(1)
        else:
            break

    conn.close()

def main():
    while True:
        conn, addr = server_socket.accept()
        conn = context.wrap_socket(conn, server_side=True)
        print("\n\t\t\t\t\t   ---------------------------------------")
        print(f"\t\t\t\t\t   | Connected to : {addr} | ")
        print("\t\t\t\t\t   ---------------------------------------")
        threading.Thread(target=client_thread, args=(conn, addr)).start()

if __name__ == "__main__":
    main()