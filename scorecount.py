#!/usr/bin/python3

# Tasks
# * Add List of Scoring States
# * Extract data from only Scoring States
# * Add Logic to Determine if a State Scores
# * Report Score for Each Country
# * Convert Country Abbreviations to Full Country Name
# * Report List of Scoring States

import sys
import datetime


# Define Nation Table

nationTable = {
    "REB": "Rebels",
    "PIR": "Pirates",
    "NAT": "Natives",
    "SWE": "Sweden",
    "DAN": "Denmark",
    "FIN": "Finland",
    "GOT": "Gotland",
    "NOR": "Norway",
    "SHL": "Holstein",
    "SCA": "Scandinavia",
    "EST": "Estonia",
    "LVA": "Livonia",
    "SMI": "Sapmi",
    "KRL": "Karelia",
    "ICE": "Iceland",
    "ACH": "Achaea",
    "ALB": "Albania",
    "ATH": "Athens",
    "BOS": "Bosnia",
    "BUL": "Bulgaria",
    "BYZ": "Byzantium",
    "CEP": "Corfu",
    "CRO": "Croatia",
    "CRT": "Crete",
    "CYP": "Cyprus",
    "EPI": "Epirus",
    "GRE": "Greece",
    "KNI": "The Knights",
    "MOE": "Morea",
    "MOL": "Moldavia",
    "MON": "Montenegro",
    "NAX": "Naxos",
    "RAG": "Ragusa",
    "RMN": "Romania",
    "SER": "Serbia",
    "TRA": "Transylvania",
    "WAL": "Wallachia",
    "HUN": "Hungary",
    "SLO": "Nitra",
    "TUR": "Ottomans",
    "CNN": "Clanricarde",
    "CRN": "Cornwall",
    "ENG": "England",
    "LEI": "Leinster",
    "IRE": "Ireland",
    "MNS": "Thomond",
    "SCO": "Scotland",
    "TYR": "Tyrone",
    "WLS": "Wales",
    "NOL": "Northumberland",
    "GBR": "Great Britain",
    "MTH": "Meath",
    "ULS": "Ulster",
    "DMS": "Desmond",
    "SLN": "Sligo",
    "KID": "Kildare",
    "HSC": "Gaeldom",
    "ORD": "Ormond",
    "TRY": "Tyrconnell",
    "FLY": "Offaly",
    "MCM": "Munster",
    "KOI": "Mann",
    "LOI": "The Isles",
    "BRZ": "Brazil",
    "CAN": "Canada",
    "CHL": "Chile",
    "COL": "Colombia",
    "HAT": "Haiti",
    "LAP": "La Plata",
    "LOU": "Louisiana",
    "MEX": "Mexico",
    "PEU": "Peru",
    "PRG": "Paraguay",
    "QUE": "Quebec",
    "CAM": "United Central America",
    "USA": "United States",
    "VNZ": "Venezuela",
    "AUS": "Australia",
    "DNZ": "Danzig",
    "KRA": "Krakow",
    "LIT": "Lithuania",
    "LIV": "Livonian Order",
    "MAZ": "Mazovia",
    "POL": "Poland",
    "PRU": "Prussia",
    "KUR": "Kurland",
    "RIG": "Riga",
    "TEU": "Teutonic Order",
    "PLC": "Commonwealth",
    "VOL": "Galicia–Volhynia",
    "KIE": "Kiev",
    "CHR": "Chernigov",
    "OKA": "Odoyev",
    "ALE": "Alençon",
    "ALS": "Alsace",
    "AMG": "Armagnac",
    "AUV": "Auvergne",
    "AVI": "Avignon",
    "BOU": "Bourbonnais",
    "BRI": "Brittany",
    "BUR": "Burgundy",
    "CHP": "Champagne",
    "COR": "Corsica",
    "DAU": "Dauphine",
    "FOI": "Foix",
    "FRA": "France",
    "GUY": "Gascony",
    "NEV": "Nevers",
    "NRM": "Normandy",
    "ORL": "Orleans",
    "PIC": "Picardy",
    "PRO": "Provence",
    "SPI": "Sardinia-Piedmont",
    "TOU": "Toulouse",
    "BER": "Berry",
    "AAC": "Aachen",
    "ANH": "Anhalt",
    "ANS": "Ansbach",
    "AUG": "Augsburg",
    "BAD": "Baden",
    "BAV": "Bavaria",
    "BOH": "Bohemia",
    "BRA": "Brandenburg",
    "BRE": "Bremen",
    "BRU": "Brunswick",
    "EFR": "East Frisia",
    "FRN": "Frankfurt",
    "GER": "Germany",
    "HAB": "Austria",
    "HAM": "Hamburg",
    "HAN": "Hanover",
    "HES": "Hesse",
    "HLR": "Holy Roman Empire",
    "KLE": "Cleves",
    "KOL": "Cologne",
    "LAU": "Saxe-Lauenburg",
    "LOR": "Lorraine",
    "LUN": "Lüneburg",
    "MAG": "Magdeburg",
    "MAI": "Mainz",
    "MEI": "Meissen",
    "MKL": "Mecklenburg",
    "MUN": "Münster",
    "MVA": "Moravia",
    "OLD": "Oldenburg",
    "PAL": "The Palatinate",
    "POM": "Pomerania",
    "SAX": "Saxony",
    "SIL": "Silesia",
    "SLZ": "Salzburg",
    "STY": "Styria",
    "SWI": "Switzerland",
    "THU": "Thuringia",
    "TIR": "Tirol",
    "TRI": "Trier",
    "ULM": "Ulm",
    "WBG": "Wurzburg",
    "WES": "Westphalia",
    "WUR": "Wurttemberg",
    "NUM": "Nuremberg",
    "MEM": "Memmingen",
    "VER": "Verden",
    "NSA": "Nassau",
    "RVA": "Ravensburg",
    "DTT": "Dithmarschen",
    "ARA": "Aragon",
    "CAS": "Castile",
    "CAT": "Catalonia",
    "GRA": "Granada",
    "NAV": "Navarra",
    "POR": "Portugal",
    "SPA": "Spain",
    "GAL": "Galicia",
    "LON": "León",
    "ADU": "Andalusia",
    "AQU": "Aquileia",
    "ETR": "Etruria",
    "FER": "Ferrara",
    "GEN": "Genoa",
    "ITA": "Italy",
    "MAN": "Mantua",
    "MLO": "Milan",
    "MOD": "Modena",
    "NAP": "Naples",
    "PAP": "The Papal State",
    "PAR": "Parma",
    "PIS": "Pisa",
    "SAR": "Sardinia",
    "SAV": "Savoy",
    "SIC": "Sicily",
    "SIE": "Siena",
    "TUS": "Tuscany",
    "URB": "Urbino",
    "VEN": "Venice",
    "MFA": "Montferrat",
    "LUC": "Lucca",
    "LAN": "Florence",
    "JAI": "Malta",
    "BRB": "Brabant",
    "FLA": "Flanders",
    "FRI": "Friesland",
    "GEL": "Gelre",
    "HAI": "Hainaut",
    "HOL": "Holland",
    "LIE": "Liege",
    "LUX": "Luxembourg",
    "NED": "Netherlands",
    "UTR": "Utrecht",
    "ARM": "Armenia",
    "AST": "Astrakhan",
    "CRI": "Crimea",
    "GEO": "Georgia",
    "KAZ": "Kazan",
    "MOS": "Muscovy",
    "NOV": "Novgorod",
    "PSK": "Pskov",
    "QAS": "Qasim",
    "RUS": "Russia",
    "RYA": "Ryazan",
    "TVE": "Tver",
    "UKR": "Ruthenia",
    "YAR": "Yaroslavl",
    "ZAZ": "Zaporozhie",
    "NOG": "Nogai",
    "SIB": "Sibir",
    "PLT": "Polotsk",
    "PRM": "Perm",
    "FEO": "Theodoro",
    "BSH": "Bashkiria",
    "BLO": "Beloozero",
    "RSO": "Rostov",
    "GOL": "Great Horde",
    "GLH": "Golden Horde",
    "ADE": "Aden",
    "ALH": "Haasa",
    "ANZ": "Anizah",
    "ARB": "Arabia",
    "ARD": "Ardalan",
    "BHT": "Soran",
    "DAW": "Dawasir",
    "ERE": "Eretna",
    "FAD": "Fadl",
    "GRM": "Germiyan",
    "HDR": "Hadramut",
    "HED": "Hejaz",
    "LEB": "Lebanon",
    "MAK": "Makuria",
    "MDA": "Medina",
    "MFL": "Mikhlaf",
    "MHR": "Mahra",
    "NAJ": "Najd",
    "NJR": "Najran",
    "OMA": "Oman",
    "RAS": "Rassids",
    "SHM": "Shammar",
    "SHR": "Sharjah",
    "SRV": "Shirvan",
    "YAS": "Yas",
    "YEM": "Yemen",
    "HSN": "Hisn Kayfa",
    "BTL": "Bitlis",
    "AKK": "Aq Qoyunlu",
    "AYD": "Aydin",
    "CND": "Candar",
    "DUL": "Dulkadir",
    "IRQ": "Iraq",
    "KAR": "Karaman",
    "SYR": "Syria",
    "TRE": "Trebizond",
    "SRU": "Saruhan",
    "MEN": "Mentese",
    "RAM": "Ramazan",
    "AVR": "Avaria",
    "MLK": "Kharabakh",
    "SME": "Samtskhe",
    "ARL": "Ardabil",
    "MSY": "Mushasha",
    "RUM": "Rûm",
    "ALG": "Algiers",
    "FEZ": "Fez",
    "MAM": "Mamluks",
    "MOR": "Morocco",
    "TRP": "Tripoli",
    "TUN": "Tunis",
    "EGY": "Egypt",
    "KBA": "Kabylia",
    "TFL": "Tafilalt",
    "SOS": "Sus",
    "TLC": "Tlemcen",
    "TGT": "Touggourt",
    "GHD": "Djerid",
    "FZA": "Fezzan",
    "MZB": "Mzab",
    "KZH": "Kazakh",
    "KHI": "Khiva",
    "SHY": "Uzbek",
    "KOK": "Ferghana",
    "BUK": "Bukhara",
    "AFG": "Afghanistan",
    "KHO": "Khorasan",
    "PER": "Persia",
    "QAR": "Qara Qoyunlu",
    "TIM": "Timurids",
    "TRS": "Transoxiana",
    "KRY": "Gilan",
    "CIR": "Circassia",
    "GAZ": "Gazikumukh",
    "IME": "Imereti",
    "TAB": "Mazandaran",
    "ORM": "Hormuz",
    "LRI": "Luristan",
    "SIS": "Sistan",
    "BPI": "Biapas",
    "FRS": "Fars",
    "KRM": "Kerman",
    "YZD": "Yazd",
    "ISF": "Isfahan",
    "TBR": "Tabriz",
    "BSR": "Basra",
    "MGR": "Maregheh",
    "QOM": "Ajam",
    "AZT": "Aztec",
    "CHE": "Cherokee",
    "CHM": "Chimu",
    "CRE": "Creek",
    "HUR": "Huron",
    "INC": "Inca",
    "IRO": "Iroquois",
    "MAY": "Maya",
    "SHA": "Shawnee",
    "ZAP": "Zapotec",
    "ASH": "Ashanti",
    "BEN": "Benin",
    "ETH": "Ethiopia",
    "KON": "Kongo",
    "MAL": "Mali",
    "NUB": "Funj",
    "SON": "Songhai",
    "ZAN": "Kilwa",
    "ZIM": "Mutapa",
    "ADA": "Adal",
    "HAU": "Hausa",
    "KBO": "Kanem Bornu",
    "LOA": "Loango",
    "OYO": "Oyo",
    "SOF": "Segu",
    "SOK": "Sokoto",
    "JOL": "Jolof",
    "SFA": "Sofala",
    "MBA": "Mombasa",
    "MLI": "Malindi",
    "AJU": "Ajuuraan",
    "MDI": "Mogadishu",
    "ENA": "Ennarea",
    "AFA": "Aussa",
    "ALO": "Alodia",
    "DAR": "Darfur",
    "GLE": "Geledi",
    "HAR": "Harar",
    "HOB": "Hobyo",
    "KAF": "Kaffa",
    "MED": "Medri Bahri",
    "MJE": "Majeerteen",
    "MRE": "Marehan",
    "PTE": "Pate",
    "WAR": "Warsangali",
    "BTI": "Semien",
    "BEJ": "Beja",
    "JIM": "Jima",
    "WLY": "Welayta",
    "DAM": "Damot",
    "HDY": "Hadiya",
    "SOA": "Shewa",
    "JJI": "Janjiro",
    "ABB": "Dongola",
    "TYO": "Tyo",
    "SYO": "Soyo",
    "KSJ": "Kasanje",
    "LUB": "Luba",
    "LND": "Lunda",
    "CKW": "Chokwe",
    "KIK": "Kikondja",
    "KZB": "Kazembe",
    "YAK": "Yaka",
    "KLD": "Kalundwe",
    "KUB": "Kuba",
    "RWA": "Rwanda",
    "BUU": "Burundi",
    "BUG": "Buganda",
    "NKO": "Nkore",
    "KRW": "Karagwe",
    "BNY": "Bunyoro",
    "BSG": "Busoga",
    "UBH": "Buha",
    "MRA": "Maravi",
    "LDU": "Lundu",
    "TBK": "Tumbuka",
    "MKU": "Makua",
    "RZW": "Butua",
    "MIR": "Imerina",
    "SKA": "Sakalava",
    "BTS": "Betsimisaraka",
    "MFY": "Mahafaly",
    "ANT": "Antemoro",
    "ANN": "Annam",
    "ARK": "Arakan",
    "ATJ": "Aceh",
    "AYU": "Ayutthaya",
    "BLI": "Bali",
    "BAN": "Banten",
    "BEI": "Brunei",
    "CHA": "Champa",
    "CHG": "Chagatai",
    "CHK": "Champasak",
    "DAI": "Dai Viet",
    "JAP": "Japan",
    "AMA": "Amago",
    "ASA": "Asakura",
    "CSK": "Chosokabe",
    "DTE": "Date",
    "HJO": "Hojo",
    "HSK": "Hosokawa",
    "HTK": "Hatakeyama",
    "IKE": "Ikeda",
    "IMG": "Imagawa",
    "MAE": "Maeda",
    "MRI": "Mori",
    "ODA": "Oda",
    "OTM": "Otomo",
    "OUC": "Ouchi",
    "SBA": "Shiba",
    "SMZ": "Shimazu",
    "TKD": "Takeda",
    "TKG": "Tokugawa",
    "UES": "Uesugi",
    "YMN": "Yamana",
    "RFR": "Nanbu",
    "ASK": "Ashikaga",
    "KTB": "Kitabatake",
    "ANU": "Ainu",
    "AKM": "Akamatsu",
    "AKT": "Ando",
    "CBA": "Chiba",
    "ISK": "Isshiki",
    "ITO": "Ito",
    "KKC": "Kikuchi",
    "KNO": "Kono",
    "OGS": "Ogasawara",
    "SHN": "Shoni",
    "STK": "Satake",
    "TKI": "Toki",
    "UTN": "Utsunomiya",
    "TTI": "Tsutsui",
    "KHA": "Mongolia",
    "KHM": "Khmer",
    "KOR": "Korea",
    "LNA": "Lan Na",
    "LUA": "Luang Prabang",
    "LXA": "Lan Xang",
    "MAJ": "Majapahit",
    "MCH": "Manchu",
    "MKS": "Makassar",
    "MLC": "Malacca",
    "MNG": "Ming",
    "MTR": "Mataram",
    "OIR": "Oirat",
    "PAT": "Pattani",
    "PEG": "Pegu",
    "QNG": "Qing",
    "RYU": "Ryukyu",
    "SST": "Shan",
    "SUK": "Sukhothai",
    "SUL": "Sulu",
    "TAU": "Taungu",
    "TIB": "Tibet",
    "TOK": "Tonkin",
    "VIE": "Vientiane",
    "CZH": "Zhou",
    "CSH": "Shun",
    "CXI": "Xi",
    "YUA": "Yuan",
    "MYR": "Yeren",
    "MHX": "Haixi",
    "MJZ": "Jianzhou",
    "KRC": "Korchin",
    "KLK": "Khalkha",
    "HMI": "Kara Del",
    "ZUN": "Zunghar",
    "KAS": "Yarkand",
    "CHH": "Chahar",
    "KSD": "Khoshuud",
    "SYG": "Sarig Yogir",
    "UTS": "U-tsang",
    "KAM": "Kham",
    "GUG": "Guge",
    "CDL": "Dali",
    "CYI": "Yi",
    "CMI": "Miao",
    "MIN": "Min",
    "YUE": "Yue",
    "SHU": "Shu",
    "NNG": "Ning",
    "CHC": "Chu",
    "TNG": "Tang",
    "WUU": "Wu",
    "QIC": "Qi",
    "YAN": "Yan",
    "JIN": "Jin",
    "LNG": "Liang",
    "QIN": "Qin",
    "HUA": "Huai",
    "CGS": "Changsheng",
    "BAL": "Baluchistan",
    "BNG": "Bengal",
    "BIJ": "Bijapur",
    "BAH": "Bahmanis",
    "DLH": "Delhi",
    "GOC": "Golkonda",
    "DEC": "Deccan",
    "MAR": "Marathas",
    "MUG": "Mughals",
    "MYS": "Mysore",
    "VIJ": "Vijayanagar",
    "AHM": "Ahmednagar",
    "ASS": "Assam",
    "GUJ": "Gujarat",
    "JNP": "Jaunpur",
    "MAD": "Madurai",
    "MLW": "Malwa",
    "MAW": "Marwar",
    "MER": "Mewar",
    "MUL": "Multan",
    "NAG": "Nagpur",
    "NPL": "Nepal",
    "ORI": "Orissa",
    "PUN": "Punjab",
    "SND": "Sind",
    "BRR": "Berar",
    "JAN": "Jangladesh",
    "KRK": "Carnatic",
    "GDW": "Gondwana",
    "GRJ": "Garjat",
    "GWA": "Gwalior",
    "DHU": "Dhundhar",
    "KSH": "Kashmir",
    "KLN": "Keladi",
    "KHD": "Khandesh",
    "ODH": "Oudh",
    "VND": "Venad",
    "MAB": "Malabar",
    "MEW": "Mewat",
    "BDA": "Baroda",
    "BST": "Bastar",
    "BHU": "Bhutan",
    "BND": "Bundelkhand",
    "CEY": "Ceylon",
    "JSL": "Jaisalmer",
    "KAC": "Kachar",
    "KMT": "Koch",
    "KGR": "Kangra",
    "KAT": "Kathiawar",
    "KOC": "Kochin",
    "MLB": "Manipur",
    "HAD": "Hadoti",
    "NGA": "Nagaur",
    "RMP": "Rohilkhand",
    "LDK": "Ladakh",
    "BGL": "Bagelkhand",
    "JFN": "Jaffna",
    "PTA": "Patiala",
    "GHR": "Garhwal",
    "CHD": "Chanda",
    "NGP": "Jharkhand",
    "JAJ": "Habsan",
    "TRT": "Tirhut",
    "CMP": "Rewa Kantha",
    "BGA": "Baglana",
    "TPR": "Tripura",
    "SDY": "Sadiya",
    "BHA": "Bharat",
    "YOR": "Andhra",
    "DGL": "Maldives",
    "BAR": "Bar",
    "HSA": "Lübeck",
    "SMO": "Smolensk",
    "NZH": "Nizhny Novgorod",
    "KOJ": "Jerusalem",
    "MSA": "Malaya",
    "HIN": "Hindustan",
    "ABE": "Abenaki",
    "APA": "Apache",
    "ASI": "Assiniboine",
    "BLA": "Blackfoot",
    "CAD": "Caddo",
    "CHI": "Chickasaw",
    "CHO": "Choctaw",
    "CHY": "Cheyenne",
    "COM": "Comanche",
    "FOX": "Fox",
    "ILL": "Illiniwek",
    "LEN": "Lenape",
    "MAH": "Mahican",
    "MIK": "Mikmaq",
    "MMI": "Miami",
    "NAH": "Navajo",
    "OJI": "Ojibwe",
    "OSA": "Osage",
    "OTT": "Ottawa",
    "PAW": "Pawnee",
    "PEQ": "Pequot",
    "PIM": "Pima",
    "POT": "Potawatomi",
    "POW": "Powhatan",
    "PUE": "Pueblo",
    "SHO": "Shoshone",
    "SIO": "Sioux",
    "SUS": "Susquehannock",
    "WCR": "Cree",
    "AIR": "Air",
    "BON": "Bonoman",
    "DAH": "Dahomey",
    "DGB": "Dagbon",
    "FUL": "Fulo",
    "JNN": "Jenné",
    "KAN": "Kano",
    "KBU": "Kaabu",
    "KNG": "Kong",
    "KTS": "Katsina",
    "MSI": "Mossi",
    "NUP": "Nupe",
    "TMB": "Timbuktu",
    "YAO": "Yao",
    "YAT": "Yatenga",
    "ZAF": "Macina",
    "ZZZ": "Zazzau",
    "NDO": "Ndongo",
    "AVA": "Ava",
    "HSE": "Hsenwi",
    "JOH": "Johor",
    "KED": "Kedah",
    "LIG": "Ligor",
    "MPH": "Muan Phuang",
    "MYA": "Mong Yang",
    "PRK": "Perak",
    "CHU": "Chukchi",
    "HOD": "Khodynt",
    "CHV": "Chavchuveny",
    "KMC": "Kamchadals",
    "BRT": "Buryatia",
    "ARP": "Arapaho",
    "CLM": "Colima",
    "CNK": "Chinook",
    "COC": "Cocomes",
    "HDA": "Haida",
    "ITZ": "Itza",
    "KIC": "Kiche",
    "KIO": "Kiowa",
    "MIX": "Mixtec",
    "SAL": "Salish",
    "TAR": "Tarascan",
    "TLA": "Tlapanec",
    "TLX": "Tlaxcala",
    "TOT": "Totonac",
    "WIC": "Wichita",
    "XIU": "Xiu",
    "BLM": "Blambangan",
    "BTN": "Buton",
    "CRB": "Cirebon",
    "DMK": "Demak",
    "PGR": "Pagarruyung",
    "PLB": "Palembang",
    "PSA": "Pasai",
    "SAK": "Siak",
    "SUN": "Sunda",
    "KUT": "Kutai",
    "BNJ": "Banjar",
    "LFA": "Lanfang",
    "LNO": "Lanao",
    "LUW": "Luwu",
    "MGD": "Maguindanao",
    "TER": "Ternate",
    "TID": "Tidore",
    "MAS": "Madyas",
    "PGS": "Pangasinan",
    "TDO": "Tondo",
    "MNA": "Maynila",
    "CEB": "Cebu",
    "BTU": "Butuan",
    "CSU": "Cusco",
    "CCQ": "Calchaqui",
    "MPC": "Mapuche",
    "MCA": "Muisca",
    "QTO": "Quito",
    "CJA": "Cajamarca",
    "HJA": "Huyla",
    "PTG": "Potiguara",
    "TPQ": "Tupiniquim",
    "TPA": "Tupinamba",
    "TUA": "Tapuia",
    "GUA": "Guarani",
    "CUA": "Charrua",
    "WKA": "Wanka",
    "CYA": "Chachapoya",
    "CLA": "Colla",
    "CRA": "Charca",
    "PCJ": "Pacajes",
    "ARW": "Arawak",
    "CAB": "Carib",
    "ICM": "Ichma",
    "JMN": "Jan Mayen",
    "ROM": "Roman Empire",
    "JOM": "Jomsvikings",
    "HAH": "Hashashin",
    "ISR": "Israel",
    "TEM": "Knights Templar",
    "TRL": "Trapalanda",
    "MRK": "Marrakesh",
    "PGA": "Perugia",
    "KND": "Kandy",
    "BRG": "Berg",
    "SZO": "Saluzzo",
    "TTL": "Three Leagues",
    "PHA": "U",
    "UBV": "Munich",
    "LBV": "Landshut",
    "ING": "Ingolstadt",
    "PSS": "Passau",
    "MBZ": "Bregenz",
    "KNZ": "Konstanz",
    "ROT": "Rothenburg",
    "BYT": "Bayreuth",
    "REG": "Regensburg",
    "GNV": "Geneva",
    "YOK": "Yokotan",
    "MMA": "Mong Mao"

}

global stack
stack = 0


def pushStack():
    global stack
    stack = stack + 1


def popStack():
    global stack
    if stack == 0:
        return
    else:
        stack = stack - 1


def removePrefix(s, prefix):
    return s[len(prefix):] if s.startswith(prefix) else s

def getRelType(dipBlock):
    relType = ""
    for item in dipBlock:
        if "subject_type=" in item:
            relType = item
            relType = removePrefix(relType.strip(), "subject_type=")
            relType = relType.replace('"','')
    return relType


def relParser(dipBlock, playerNations):
    relAtribs = []
    firstAtrib = ""
    secondAtrib = ""
    thirdAtrib = ""
    careAboutNation = False

    firstAtrib = dipBlock[0]
    firstAtrib = removePrefix(firstAtrib.strip(), "first=")
    firstAtrib = firstAtrib.replace('"','')

    if firstAtrib in playerNations:
        careAboutNation = True
        secondAtrib = dipBlock[1]
        secondAtrib = removePrefix(secondAtrib.strip(), "second=")
        secondAtrib = secondAtrib.replace('"','')

        thirdAtrib = getRelType(dipBlock)

        relAtribs.append(firstAtrib)
        relAtribs.append(secondAtrib)
        relAtribs.append(thirdAtrib)

        return relAtribs

    return relAtribs


def diplomacyParser(file, playerNations):
    # Get file iterator to diplomacy section

    allAtribs = []
    relAtribs = []

    for line in file:
        if "trade_diplomacy=" in line:
            continue
        elif "diplomacy=" in line:
            pushStack()
            break
    while(stack > 0):
        line = file.readline()
        if "{" in line:
            pushStack()
            if "dependency=" in line:
                dipBlock = []
                while(stack > 1):
                    line = file.readline()
                    if "}" in line:
                        popStack()
                    else:
                        dipBlock.append(line.rstrip())
                relAtribs = relParser(dipBlock, playerNations)
                if(len(relAtribs) > 2):
                    allAtribs.append(relAtribs)
        elif "}" in line:
            popStack()
    return allAtribs


def dictValue(d, k):
    if k in d:
        return True
    else:
        return False

def getOverlord(nation, diploReps):
    nation = nation.replace('"','')
    for rep in diploReps:
        if nation == rep[1]:
            return rep[0]
    return nation


def getRelation(nation, diploReps):
    nation = nation.replace('"','')
    for rep in diploReps:
        if nation == rep[1]:
            return rep[2]
    return "none"

def isSameCountry(nationList, diploReps):
    uniqueNations = []
    for nation in nationList:
        overlord = getOverlord(nation, diploReps)
        if overlord not in uniqueNations:
            relation = getRelation(nation, diploReps)
            if "tributary" not in relation:
                uniqueNations.append(overlord)
    if len(uniqueNations) == 1:
        return True
    else:
        return False

fileName = sys.argv[1]
victoryCardList = sys.argv[2]

file = open(fileName, encoding='ISO-8859-1')
scoreFile = open("scoreList.csv", 'w')

# Generate a Dictionary of all Victory Cards with blank list as value
cards = open(victoryCardList)
vicCards = []

for card in cards:
    cardName = ""
    cardName = card
    cardName = cardName.rstrip("\n")
    cardName = cardName + "_area"
    vicCards.append(cardName)

cardDict = {i: [] for i in vicCards}

# Move the file iterator to the start of the area list
line = file.readline()
for line in file:
    if "map_area_data" in line:
        break

# Generate Player Nation List
pnFileName = sys.argv[3]
playerNationFile = open(pnFileName)
pNationList = []
for line in playerNationFile:
    pNationList.append(line.rstrip())

# Unnecessary Bools

endOfAreas = False
endOfState = False
endOfCountry = False

# Strip Country per Area from Save

while(not endOfAreas):
    line = file.readline()
    if "total_military_power" in line:
        break
    elif "state=" in line:
        vicCard = ""
        countryList = []
        while(not endOfCountry):
            line = file.readline()
            if "}" in line:
                break
            elif "area=" in line:
                vicCard = removePrefix(line.strip(), "area=")
                vicCard = vicCard.replace('"', '')
                continue
            elif "country_state=" in line:
                countryID = ""
                while(not endOfCountry):
                    line = file.readline()
                    if "}" in line:
                        break
                    elif "country=" in line:
                        countryID = removePrefix(line.strip(), "country=")
                        countryID.replace('"', '')
                        countryList.append(countryID)
                        continue
            if dictValue(cardDict, vicCard):
                cardDict[vicCard] = countryList


# Strip Relationships

file.seek(0)
allDiplos = []

allDiplos = diplomacyParser(file, pNationList)



# Determine Scores

nations = []
for k in cardDict:
    if len(cardDict[k]) > 0:
        for n in cardDict[k]:
            if n not in nations:
                name = n
                name = name.strip('"')
                nations.append(name)

nationScores = {i: 0 for i in nations}


for k in cardDict:
    scoringList = []
    scoringNation = ""
    score = 0
    if len(cardDict[k]) == 1:
        scoringList = cardDict[k]
        scoringNation = getOverlord(scoringList[0],allDiplos)
        score = nationScores[scoringNation]
        score = score + 1
        nationScores[scoringNation] = score
    elif len(cardDict[k]) > 1:
        scoringList = cardDict[k]
        if isSameCountry(scoringList, allDiplos):
            scoringNation = getOverlord(scoringList[0], allDiplos)
            score = nationScores[scoringNation]
            score = score + 1
            nationScores[scoringNation] = score



scoreFile.write('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
scoreFile.write(',\n')

for pN in pNationList:
    if dictValue(nationScores, pN):
        scoreline = "Nation: " + nationTable[pN] + " - " + str(nationScores[pN])
        scoreFile.write(nationTable[pN] + ',' + str(nationScores[pN]))
        scoreFile.write('\n')
        print(scoreline)
    else:
        scoreline = "Nation: " + nationTable[pN] + " - 0"
        scoreFile.write(scoreline)
        print(scoreline)

# Close the documents
file.close()
scoreFile.close()
