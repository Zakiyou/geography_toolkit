import json
import os


data = {
    "Antarctic": [
        {
            "country": "South Georgia",
            "capital": "King Edward Point",
            "population": 30,
            "area_km2": 3903.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "SHP"
            ],
            "timezones": [
                "UTC-02:00"
            ],
            "flag": "https://flagcdn.com/w320/gs.png",
            "subregion": "N/A",
            "borders": []
        },
        {
            "country": "Antarctica",
            "capital": "N/A",
            "population": 1000,
            "area_km2": 14000000.0,
            "languages": [],
            "currencies": [],
            "timezones": [
                "UTC-03:00",
                "UTC+03:00",
                "UTC+05:00",
                "UTC+06:00",
                "UTC+07:00",
                "UTC+08:00",
                "UTC+10:00",
                "UTC+12:00"
            ],
            "flag": "https://flagcdn.com/w320/aq.png",
            "subregion": "N/A",
            "borders": []
        },
        {
            "country": "Bouvet Island",
            "capital": "N/A",
            "population": 0,
            "area_km2": 49.0,
            "languages": [
                "Norwegian"
            ],
            "currencies": [],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/bv.png",
            "subregion": "N/A",
            "borders": []
        },
        {
            "country": "French Southern and Antarctic Lands",
            "capital": "Port-aux-Français",
            "population": 400,
            "area_km2": 7747.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+05:00"
            ],
            "flag": "https://flagcdn.com/w320/tf.png",
            "subregion": "N/A",
            "borders": []
        },
        {
            "country": "Heard Island and McDonald Islands",
            "capital": "N/A",
            "population": 0,
            "area_km2": 412.0,
            "languages": [
                "English"
            ],
            "currencies": [],
            "timezones": [
                "UTC+05:00"
            ],
            "flag": "https://flagcdn.com/w320/hm.png",
            "subregion": "N/A",
            "borders": []
        }
    ],
    "Americas": [
        {
            "country": "Grenada",
            "capital": "St. George's",
            "population": 112519,
            "area_km2": 344.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "XCD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/gd.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Barbados",
            "capital": "Bridgetown",
            "population": 287371,
            "area_km2": 430.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "BBD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/bb.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Saint Kitts and Nevis",
            "capital": "Basseterre",
            "population": 53192,
            "area_km2": 261.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "XCD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/kn.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Caribbean Netherlands",
            "capital": "Kralendijk",
            "population": 25987,
            "area_km2": 328.0,
            "languages": [
                "English",
                "Dutch",
                "Papiamento"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/bq.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Mexico",
            "capital": "Mexico City",
            "population": 128932753,
            "area_km2": 1964375.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "MXN"
            ],
            "timezones": [
                "UTC-08:00",
                "UTC-07:00",
                "UTC-06:00"
            ],
            "flag": "https://flagcdn.com/w320/mx.png",
            "subregion": "North America",
            "borders": [
                "BLZ",
                "GTM",
                "USA"
            ]
        },
        {
            "country": "Saint Barthélemy",
            "capital": "Gustavia",
            "population": 4255,
            "area_km2": 21.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/bl.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Peru",
            "capital": "Lima",
            "population": 32971846,
            "area_km2": 1285216.0,
            "languages": [
                "Aymara",
                "Quechua",
                "Spanish"
            ],
            "currencies": [
                "PEN"
            ],
            "timezones": [
                "UTC-05:00"
            ],
            "flag": "https://flagcdn.com/w320/pe.png",
            "subregion": "South America",
            "borders": [
                "BOL",
                "BRA",
                "CHL",
                "COL",
                "ECU"
            ]
        },
        {
            "country": "Aruba",
            "capital": "Oranjestad",
            "population": 106766,
            "area_km2": 180.0,
            "languages": [
                "Dutch",
                "Papiamento"
            ],
            "currencies": [
                "AWG"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/aw.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Montserrat",
            "capital": "Plymouth",
            "population": 4922,
            "area_km2": 102.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "XCD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/ms.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "United States Virgin Islands",
            "capital": "Charlotte Amalie",
            "population": 106290,
            "area_km2": 347.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/vi.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Colombia",
            "capital": "Bogotá",
            "population": 50882884,
            "area_km2": 1141748.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "COP"
            ],
            "timezones": [
                "UTC-05:00"
            ],
            "flag": "https://flagcdn.com/w320/co.png",
            "subregion": "South America",
            "borders": [
                "BRA",
                "ECU",
                "PAN",
                "PER",
                "VEN"
            ]
        },
        {
            "country": "Puerto Rico",
            "capital": "San Juan",
            "population": 3194034,
            "area_km2": 8870.0,
            "languages": [
                "English",
                "Spanish"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/pr.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Dominican Republic",
            "capital": "Santo Domingo",
            "population": 10847904,
            "area_km2": 48671.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "DOP"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/do.png",
            "subregion": "Caribbean",
            "borders": [
                "HTI"
            ]
        },
        {
            "country": "Paraguay",
            "capital": "Asunción",
            "population": 7132530,
            "area_km2": 406752.0,
            "languages": [
                "Guaraní",
                "Spanish"
            ],
            "currencies": [
                "PYG"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/py.png",
            "subregion": "South America",
            "borders": [
                "ARG",
                "BOL",
                "BRA"
            ]
        },
        {
            "country": "El Salvador",
            "capital": "San Salvador",
            "population": 6486201,
            "area_km2": 21041.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC-06:00"
            ],
            "flag": "https://flagcdn.com/w320/sv.png",
            "subregion": "Central America",
            "borders": [
                "GTM",
                "HND"
            ]
        },
        {
            "country": "Greenland",
            "capital": "Nuuk",
            "population": 56367,
            "area_km2": 2166086.0,
            "languages": [
                "Greenlandic"
            ],
            "currencies": [
                "DKK"
            ],
            "timezones": [
                "UTC-04:00",
                "UTC-03:00",
                "UTC-01:00",
                "UTC+00:00"
            ],
            "flag": "https://flagcdn.com/w320/gl.png",
            "subregion": "North America",
            "borders": []
        },
        {
            "country": "Cuba",
            "capital": "Havana",
            "population": 11326616,
            "area_km2": 109884.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "CUC",
                "CUP"
            ],
            "timezones": [
                "UTC-05:00"
            ],
            "flag": "https://flagcdn.com/w320/cu.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Canada",
            "capital": "Ottawa",
            "population": 38005238,
            "area_km2": 9984670.0,
            "languages": [
                "English",
                "French"
            ],
            "currencies": [
                "CAD"
            ],
            "timezones": [
                "UTC-08:00",
                "UTC-07:00",
                "UTC-06:00",
                "UTC-05:00",
                "UTC-04:00",
                "UTC-03:30"
            ],
            "flag": "https://flagcdn.com/w320/ca.png",
            "subregion": "North America",
            "borders": [
                "USA"
            ]
        },
        {
            "country": "Saint Pierre and Miquelon",
            "capital": "Saint-Pierre",
            "population": 6069,
            "area_km2": 242.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC-03:00"
            ],
            "flag": "https://flagcdn.com/w320/pm.png",
            "subregion": "North America",
            "borders": []
        },
        {
            "country": "Sint Maarten",
            "capital": "Philipsburg",
            "population": 40812,
            "area_km2": 34.0,
            "languages": [
                "English",
                "French",
                "Dutch"
            ],
            "currencies": [
                "ANG"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/sx.png",
            "subregion": "Caribbean",
            "borders": [
                "MAF"
            ]
        },
        {
            "country": "Argentina",
            "capital": "Buenos Aires",
            "population": 45376763,
            "area_km2": 2780400.0,
            "languages": [
                "Guaraní",
                "Spanish"
            ],
            "currencies": [
                "ARS"
            ],
            "timezones": [
                "UTC-03:00"
            ],
            "flag": "https://flagcdn.com/w320/ar.png",
            "subregion": "South America",
            "borders": [
                "BOL",
                "BRA",
                "CHL",
                "PRY",
                "URY"
            ]
        },
        {
            "country": "Turks and Caicos Islands",
            "capital": "Cockburn Town",
            "population": 38718,
            "area_km2": 948.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/tc.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Dominica",
            "capital": "Roseau",
            "population": 71991,
            "area_km2": 751.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "XCD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/dm.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Costa Rica",
            "capital": "San José",
            "population": 5094114,
            "area_km2": 51100.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "CRC"
            ],
            "timezones": [
                "UTC-06:00"
            ],
            "flag": "https://flagcdn.com/w320/cr.png",
            "subregion": "Central America",
            "borders": [
                "NIC",
                "PAN"
            ]
        },
        {
            "country": "Haiti",
            "capital": "Port-au-Prince",
            "population": 11402533,
            "area_km2": 27750.0,
            "languages": [
                "French",
                "Haitian Creole"
            ],
            "currencies": [
                "HTG"
            ],
            "timezones": [
                "UTC-05:00"
            ],
            "flag": "https://flagcdn.com/w320/ht.png",
            "subregion": "Caribbean",
            "borders": [
                "DOM"
            ]
        },
        {
            "country": "Honduras",
            "capital": "Tegucigalpa",
            "population": 9904608,
            "area_km2": 112492.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "HNL"
            ],
            "timezones": [
                "UTC-06:00"
            ],
            "flag": "https://flagcdn.com/w320/hn.png",
            "subregion": "Central America",
            "borders": [
                "GTM",
                "SLV",
                "NIC"
            ]
        },
        {
            "country": "Saint Lucia",
            "capital": "Castries",
            "population": 183629,
            "area_km2": 616.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "XCD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/lc.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Guadeloupe",
            "capital": "Basse-Terre",
            "population": 400132,
            "area_km2": 1628.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/gp.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Suriname",
            "capital": "Paramaribo",
            "population": 586634,
            "area_km2": 163820.0,
            "languages": [
                "Dutch"
            ],
            "currencies": [
                "SRD"
            ],
            "timezones": [
                "UTC-03:00"
            ],
            "flag": "https://flagcdn.com/w320/sr.png",
            "subregion": "South America",
            "borders": [
                "BRA",
                "GUF",
                "GUY"
            ]
        },
        {
            "country": "British Virgin Islands",
            "capital": "Road Town",
            "population": 30237,
            "area_km2": 151.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/vg.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Trinidad and Tobago",
            "capital": "Port of Spain",
            "population": 1399491,
            "area_km2": 5130.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "TTD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/tt.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Guyana",
            "capital": "Georgetown",
            "population": 786559,
            "area_km2": 214969.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "GYD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/gy.png",
            "subregion": "South America",
            "borders": [
                "BRA",
                "SUR",
                "VEN"
            ]
        },
        {
            "country": "Uruguay",
            "capital": "Montevideo",
            "population": 3473727,
            "area_km2": 181034.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "UYU"
            ],
            "timezones": [
                "UTC-03:00"
            ],
            "flag": "https://flagcdn.com/w320/uy.png",
            "subregion": "South America",
            "borders": [
                "ARG",
                "BRA"
            ]
        },
        {
            "country": "Antigua and Barbuda",
            "capital": "Saint John's",
            "population": 97928,
            "area_km2": 442.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "XCD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/ag.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Panama",
            "capital": "Panama City",
            "population": 4314768,
            "area_km2": 75417.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "PAB",
                "USD"
            ],
            "timezones": [
                "UTC-05:00"
            ],
            "flag": "https://flagcdn.com/w320/pa.png",
            "subregion": "Central America",
            "borders": [
                "COL",
                "CRI"
            ]
        },
        {
            "country": "Curaçao",
            "capital": "Willemstad",
            "population": 155014,
            "area_km2": 444.0,
            "languages": [
                "English",
                "Dutch",
                "Papiamento"
            ],
            "currencies": [
                "ANG"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/cw.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "French Guiana",
            "capital": "Cayenne",
            "population": 254541,
            "area_km2": 83534.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC-03:00"
            ],
            "flag": "https://flagcdn.com/w320/gf.png",
            "subregion": "South America",
            "borders": [
                "BRA",
                "SUR"
            ]
        },
        {
            "country": "United States Minor Outlying Islands",
            "capital": "Washington DC",
            "population": 300,
            "area_km2": 34.2,
            "languages": [
                "English"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC-11:00",
                "UTC-10:00",
                "UTC+12:00"
            ],
            "flag": "https://flagcdn.com/w320/um.png",
            "subregion": "North America",
            "borders": []
        },
        {
            "country": "Falkland Islands",
            "capital": "Stanley",
            "population": 2563,
            "area_km2": 12173.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "FKP"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/fk.png",
            "subregion": "South America",
            "borders": []
        },
        {
            "country": "Bolivia",
            "capital": "Sucre",
            "population": 11673029,
            "area_km2": 1098581.0,
            "languages": [
                "Aymara",
                "Guaraní",
                "Quechua",
                "Spanish"
            ],
            "currencies": [
                "BOB"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/bo.png",
            "subregion": "South America",
            "borders": [
                "ARG",
                "BRA",
                "CHL",
                "PRY",
                "PER"
            ]
        },
        {
            "country": "Chile",
            "capital": "Santiago",
            "population": 19116209,
            "area_km2": 756102.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "CLP"
            ],
            "timezones": [
                "UTC-06:00",
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/cl.png",
            "subregion": "South America",
            "borders": [
                "ARG",
                "BOL",
                "PER"
            ]
        },
        {
            "country": "United States",
            "capital": "Washington, D.C.",
            "population": 329484123,
            "area_km2": 9372610.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC-12:00",
                "UTC-11:00",
                "UTC-10:00",
                "UTC-09:00",
                "UTC-08:00",
                "UTC-07:00",
                "UTC-06:00",
                "UTC-05:00",
                "UTC-04:00",
                "UTC+10:00",
                "UTC+12:00"
            ],
            "flag": "https://flagcdn.com/w320/us.png",
            "subregion": "North America",
            "borders": [
                "CAN",
                "MEX"
            ]
        },
        {
            "country": "Saint Vincent and the Grenadines",
            "capital": "Kingstown",
            "population": 110947,
            "area_km2": 389.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "XCD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/vc.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Bermuda",
            "capital": "Hamilton",
            "population": 63903,
            "area_km2": 54.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "BMD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/bm.png",
            "subregion": "North America",
            "borders": []
        },
        {
            "country": "Guatemala",
            "capital": "Guatemala City",
            "population": 16858333,
            "area_km2": 108889.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "GTQ"
            ],
            "timezones": [
                "UTC-06:00"
            ],
            "flag": "https://flagcdn.com/w320/gt.png",
            "subregion": "Central America",
            "borders": [
                "BLZ",
                "SLV",
                "HND",
                "MEX"
            ]
        },
        {
            "country": "Ecuador",
            "capital": "Quito",
            "population": 17643060,
            "area_km2": 276841.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC-06:00",
                "UTC-05:00"
            ],
            "flag": "https://flagcdn.com/w320/ec.png",
            "subregion": "South America",
            "borders": [
                "COL",
                "PER"
            ]
        },
        {
            "country": "Martinique",
            "capital": "Fort-de-France",
            "population": 378243,
            "area_km2": 1128.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/mq.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Bahamas",
            "capital": "Nassau",
            "population": 393248,
            "area_km2": 13943.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "BSD",
                "USD"
            ],
            "timezones": [
                "UTC-05:00"
            ],
            "flag": "https://flagcdn.com/w320/bs.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Brazil",
            "capital": "Brasília",
            "population": 212559409,
            "area_km2": 8515767.0,
            "languages": [
                "Portuguese"
            ],
            "currencies": [
                "BRL"
            ],
            "timezones": [
                "UTC-05:00",
                "UTC-04:00",
                "UTC-03:00",
                "UTC-02:00"
            ],
            "flag": "https://flagcdn.com/w320/br.png",
            "subregion": "South America",
            "borders": [
                "ARG",
                "BOL",
                "COL",
                "GUF",
                "GUY",
                "PRY",
                "PER",
                "SUR",
                "URY",
                "VEN"
            ]
        },
        {
            "country": "Belize",
            "capital": "Belmopan",
            "population": 397621,
            "area_km2": 22966.0,
            "languages": [
                "Belizean Creole",
                "English",
                "Spanish"
            ],
            "currencies": [
                "BZD"
            ],
            "timezones": [
                "UTC-06:00"
            ],
            "flag": "https://flagcdn.com/w320/bz.png",
            "subregion": "Central America",
            "borders": [
                "GTM",
                "MEX"
            ]
        },
        {
            "country": "Venezuela",
            "capital": "Caracas",
            "population": 28435943,
            "area_km2": 916445.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "VES"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/ve.png",
            "subregion": "South America",
            "borders": [
                "BRA",
                "COL",
                "GUY"
            ]
        },
        {
            "country": "Jamaica",
            "capital": "Kingston",
            "population": 2961161,
            "area_km2": 10991.0,
            "languages": [
                "English",
                "Jamaican Patois"
            ],
            "currencies": [
                "JMD"
            ],
            "timezones": [
                "UTC-05:00"
            ],
            "flag": "https://flagcdn.com/w320/jm.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Cayman Islands",
            "capital": "George Town",
            "population": 65720,
            "area_km2": 264.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "KYD"
            ],
            "timezones": [
                "UTC-05:00"
            ],
            "flag": "https://flagcdn.com/w320/ky.png",
            "subregion": "Caribbean",
            "borders": []
        },
        {
            "country": "Saint Martin",
            "capital": "Marigot",
            "population": 38659,
            "area_km2": 53.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/mf.png",
            "subregion": "Caribbean",
            "borders": [
                "SXM"
            ]
        },
        {
            "country": "Nicaragua",
            "capital": "Managua",
            "population": 6624554,
            "area_km2": 130373.0,
            "languages": [
                "Spanish"
            ],
            "currencies": [
                "NIO"
            ],
            "timezones": [
                "UTC-06:00"
            ],
            "flag": "https://flagcdn.com/w320/ni.png",
            "subregion": "Central America",
            "borders": [
                "CRI",
                "HND"
            ]
        },
        {
            "country": "Anguilla",
            "capital": "The Valley",
            "population": 13452,
            "area_km2": 91.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "XCD"
            ],
            "timezones": [
                "UTC-04:00"
            ],
            "flag": "https://flagcdn.com/w320/ai.png",
            "subregion": "Caribbean",
            "borders": []
        }
    ],
    "Europe": [
        {
            "country": "Switzerland",
            "capital": "Bern",
            "population": 8654622,
            "area_km2": 41284.0,
            "languages": [
                "French",
                "Swiss German",
                "Italian",
                "Romansh"
            ],
            "currencies": [
                "CHF"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/ch.png",
            "subregion": "Western Europe",
            "borders": [
                "AUT",
                "FRA",
                "ITA",
                "LIE",
                "DEU"
            ]
        },
        {
            "country": "Hungary",
            "capital": "Budapest",
            "population": 9749763,
            "area_km2": 93028.0,
            "languages": [
                "Hungarian"
            ],
            "currencies": [
                "HUF"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/hu.png",
            "subregion": "Central Europe",
            "borders": [
                "AUT",
                "HRV",
                "ROU",
                "SRB",
                "SVK",
                "SVN",
                "UKR"
            ]
        },
        {
            "country": "Italy",
            "capital": "Rome",
            "population": 59554023,
            "area_km2": 301336.0,
            "languages": [
                "Italian"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/it.png",
            "subregion": "Southern Europe",
            "borders": [
                "AUT",
                "FRA",
                "SMR",
                "SVN",
                "CHE",
                "VAT"
            ]
        },
        {
            "country": "Andorra",
            "capital": "Andorra la Vella",
            "population": 77265,
            "area_km2": 468.0,
            "languages": [
                "Catalan"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/ad.png",
            "subregion": "Southern Europe",
            "borders": [
                "FRA",
                "ESP"
            ]
        },
        {
            "country": "France",
            "capital": "Paris",
            "population": 67391582,
            "area_km2": 551695.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC-10:00",
                "UTC-09:30",
                "UTC-09:00",
                "UTC-08:00",
                "UTC-04:00",
                "UTC-03:00",
                "UTC+01:00",
                "UTC+02:00",
                "UTC+03:00",
                "UTC+04:00",
                "UTC+05:00",
                "UTC+10:00",
                "UTC+11:00",
                "UTC+12:00"
            ],
            "flag": "https://flagcdn.com/w320/fr.png",
            "subregion": "Western Europe",
            "borders": [
                "AND",
                "BEL",
                "DEU",
                "ITA",
                "LUX",
                "MCO",
                "ESP",
                "CHE"
            ]
        },
        {
            "country": "North Macedonia",
            "capital": "Skopje",
            "population": 2077132,
            "area_km2": 25713.0,
            "languages": [
                "Macedonian"
            ],
            "currencies": [
                "MKD"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/mk.png",
            "subregion": "Southeast Europe",
            "borders": [
                "ALB",
                "BGR",
                "GRC",
                "UNK",
                "SRB"
            ]
        },
        {
            "country": "Guernsey",
            "capital": "St. Peter Port",
            "population": 62999,
            "area_km2": 78.0,
            "languages": [
                "English",
                "French",
                "Guernésiais"
            ],
            "currencies": [
                "GBP",
                "GGP"
            ],
            "timezones": [
                "UTC+00:00"
            ],
            "flag": "https://flagcdn.com/w320/gg.png",
            "subregion": "Northern Europe",
            "borders": []
        },
        {
            "country": "Svalbard and Jan Mayen",
            "capital": "Longyearbyen",
            "population": 2562,
            "area_km2": 61399.0,
            "languages": [
                "Norwegian"
            ],
            "currencies": [
                "NOK"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/sj.png",
            "subregion": "Northern Europe",
            "borders": []
        },
        {
            "country": "Faroe Islands",
            "capital": "Tórshavn",
            "population": 48865,
            "area_km2": 1393.0,
            "languages": [
                "Danish",
                "Faroese"
            ],
            "currencies": [
                "DKK",
                "FOK"
            ],
            "timezones": [
                "UTC+00:00"
            ],
            "flag": "https://flagcdn.com/w320/fo.png",
            "subregion": "Northern Europe",
            "borders": []
        },
        {
            "country": "United Kingdom",
            "capital": "London",
            "population": 67215293,
            "area_km2": 242900.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "GBP"
            ],
            "timezones": [
                "UTC-08:00",
                "UTC-05:00",
                "UTC-04:00",
                "UTC-03:00",
                "UTC-02:00",
                "UTC",
                "UTC+01:00",
                "UTC+02:00",
                "UTC+06:00"
            ],
            "flag": "https://flagcdn.com/w320/gb.png",
            "subregion": "Northern Europe",
            "borders": [
                "IRL"
            ]
        },
        {
            "country": "Finland",
            "capital": "Helsinki",
            "population": 5530719,
            "area_km2": 338424.0,
            "languages": [
                "Finnish",
                "Swedish"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/fi.png",
            "subregion": "Northern Europe",
            "borders": [
                "NOR",
                "SWE",
                "RUS"
            ]
        },
        {
            "country": "Greece",
            "capital": "Athens",
            "population": 10715549,
            "area_km2": 131990.0,
            "languages": [
                "Greek"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/gr.png",
            "subregion": "Southern Europe",
            "borders": [
                "ALB",
                "BGR",
                "TUR",
                "MKD"
            ]
        },
        {
            "country": "Croatia",
            "capital": "Zagreb",
            "population": 4047200,
            "area_km2": 56594.0,
            "languages": [
                "Croatian"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/hr.png",
            "subregion": "Southeast Europe",
            "borders": [
                "BIH",
                "HUN",
                "MNE",
                "SRB",
                "SVN"
            ]
        },
        {
            "country": "Netherlands",
            "capital": "Amsterdam",
            "population": 16655799,
            "area_km2": 41850.0,
            "languages": [
                "Dutch"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/nl.png",
            "subregion": "Western Europe",
            "borders": [
                "BEL",
                "DEU"
            ]
        },
        {
            "country": "Liechtenstein",
            "capital": "Vaduz",
            "population": 38137,
            "area_km2": 160.0,
            "languages": [
                "German"
            ],
            "currencies": [
                "CHF"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/li.png",
            "subregion": "Western Europe",
            "borders": [
                "AUT",
                "CHE"
            ]
        },
        {
            "country": "Monaco",
            "capital": "Monaco",
            "population": 39244,
            "area_km2": 2.02,
            "languages": [
                "French"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/mc.png",
            "subregion": "Western Europe",
            "borders": [
                "FRA"
            ]
        },
        {
            "country": "Montenegro",
            "capital": "Podgorica",
            "population": 621718,
            "area_km2": 13812.0,
            "languages": [
                "Montenegrin"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/me.png",
            "subregion": "Southeast Europe",
            "borders": [
                "ALB",
                "BIH",
                "HRV",
                "UNK",
                "SRB"
            ]
        },
        {
            "country": "Ukraine",
            "capital": "Kyiv",
            "population": 44134693,
            "area_km2": 603500.0,
            "languages": [
                "Ukrainian"
            ],
            "currencies": [
                "UAH"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/ua.png",
            "subregion": "Eastern Europe",
            "borders": [
                "BLR",
                "HUN",
                "MDA",
                "POL",
                "ROU",
                "RUS",
                "SVK"
            ]
        },
        {
            "country": "Isle of Man",
            "capital": "Douglas",
            "population": 85032,
            "area_km2": 572.0,
            "languages": [
                "English",
                "Manx"
            ],
            "currencies": [
                "GBP",
                "IMP"
            ],
            "timezones": [
                "UTC+00:00"
            ],
            "flag": "https://flagcdn.com/w320/im.png",
            "subregion": "Northern Europe",
            "borders": []
        },
        {
            "country": "Bulgaria",
            "capital": "Sofia",
            "population": 6927288,
            "area_km2": 110879.0,
            "languages": [
                "Bulgarian"
            ],
            "currencies": [
                "BGN"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/bg.png",
            "subregion": "Southeast Europe",
            "borders": [
                "GRC",
                "MKD",
                "ROU",
                "SRB",
                "TUR"
            ]
        },
        {
            "country": "Germany",
            "capital": "Berlin",
            "population": 83240525,
            "area_km2": 357114.0,
            "languages": [
                "German"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/de.png",
            "subregion": "Western Europe",
            "borders": [
                "AUT",
                "BEL",
                "CZE",
                "DNK",
                "FRA",
                "LUX",
                "NLD",
                "POL",
                "CHE"
            ]
        },
        {
            "country": "Sweden",
            "capital": "Stockholm",
            "population": 10353442,
            "area_km2": 450295.0,
            "languages": [
                "Swedish"
            ],
            "currencies": [
                "SEK"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/se.png",
            "subregion": "Northern Europe",
            "borders": [
                "FIN",
                "NOR"
            ]
        },
        {
            "country": "Russia",
            "capital": "Moscow",
            "population": 144104080,
            "area_km2": 17098242.0,
            "languages": [
                "Russian"
            ],
            "currencies": [
                "RUB"
            ],
            "timezones": [
                "UTC+03:00",
                "UTC+04:00",
                "UTC+06:00",
                "UTC+07:00",
                "UTC+08:00",
                "UTC+09:00",
                "UTC+10:00",
                "UTC+11:00",
                "UTC+12:00"
            ],
            "flag": "https://flagcdn.com/w320/ru.png",
            "subregion": "Eastern Europe",
            "borders": [
                "AZE",
                "BLR",
                "CHN",
                "EST",
                "FIN",
                "GEO",
                "KAZ",
                "PRK",
                "LVA",
                "LTU",
                "MNG",
                "NOR",
                "POL",
                "UKR"
            ]
        },
        {
            "country": "Cyprus",
            "capital": "Nicosia",
            "population": 1207361,
            "area_km2": 9251.0,
            "languages": [
                "Greek",
                "Turkish"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/cy.png",
            "subregion": "Southern Europe",
            "borders": []
        },
        {
            "country": "Bosnia and Herzegovina",
            "capital": "Sarajevo",
            "population": 3280815,
            "area_km2": 51209.0,
            "languages": [
                "Bosnian",
                "Croatian",
                "Serbian"
            ],
            "currencies": [
                "BAM"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/ba.png",
            "subregion": "Southeast Europe",
            "borders": [
                "HRV",
                "MNE",
                "SRB"
            ]
        },
        {
            "country": "Spain",
            "capital": "Madrid",
            "population": 47351567,
            "area_km2": 505992.0,
            "languages": [
                "Spanish",
                "Catalan",
                "Basque",
                "Galician"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC",
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/es.png",
            "subregion": "Southern Europe",
            "borders": [
                "AND",
                "FRA",
                "GIB",
                "PRT",
                "MAR"
            ]
        },
        {
            "country": "Slovenia",
            "capital": "Ljubljana",
            "population": 2100126,
            "area_km2": 20273.0,
            "languages": [
                "Slovene"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/si.png",
            "subregion": "Central Europe",
            "borders": [
                "AUT",
                "HRV",
                "ITA",
                "HUN"
            ]
        },
        {
            "country": "San Marino",
            "capital": "City of San Marino",
            "population": 33938,
            "area_km2": 61.0,
            "languages": [
                "Italian"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/sm.png",
            "subregion": "Southern Europe",
            "borders": [
                "ITA"
            ]
        },
        {
            "country": "Iceland",
            "capital": "Reykjavik",
            "population": 366425,
            "area_km2": 103000.0,
            "languages": [
                "Icelandic"
            ],
            "currencies": [
                "ISK"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/is.png",
            "subregion": "Northern Europe",
            "borders": []
        },
        {
            "country": "Luxembourg",
            "capital": "Luxembourg",
            "population": 632275,
            "area_km2": 2586.0,
            "languages": [
                "German",
                "French",
                "Luxembourgish"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/lu.png",
            "subregion": "Western Europe",
            "borders": [
                "BEL",
                "FRA",
                "DEU"
            ]
        },
        {
            "country": "Belarus",
            "capital": "Minsk",
            "population": 9398861,
            "area_km2": 207600.0,
            "languages": [
                "Belarusian",
                "Russian"
            ],
            "currencies": [
                "BYN"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/by.png",
            "subregion": "Eastern Europe",
            "borders": [
                "LVA",
                "LTU",
                "POL",
                "RUS",
                "UKR"
            ]
        },
        {
            "country": "Latvia",
            "capital": "Riga",
            "population": 1901548,
            "area_km2": 64559.0,
            "languages": [
                "Latvian"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/lv.png",
            "subregion": "Northern Europe",
            "borders": [
                "BLR",
                "EST",
                "LTU",
                "RUS"
            ]
        },
        {
            "country": "Gibraltar",
            "capital": "Gibraltar",
            "population": 33691,
            "area_km2": 6.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "GIP"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/gi.png",
            "subregion": "Southern Europe",
            "borders": [
                "ESP"
            ]
        },
        {
            "country": "Denmark",
            "capital": "Copenhagen",
            "population": 5831404,
            "area_km2": 43094.0,
            "languages": [
                "Danish"
            ],
            "currencies": [
                "DKK"
            ],
            "timezones": [
                "UTC-04:00",
                "UTC-03:00",
                "UTC-01:00",
                "UTC",
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/dk.png",
            "subregion": "Northern Europe",
            "borders": [
                "DEU"
            ]
        },
        {
            "country": "Czechia",
            "capital": "Prague",
            "population": 10698896,
            "area_km2": 78865.0,
            "languages": [
                "Czech",
                "Slovak"
            ],
            "currencies": [
                "CZK"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/cz.png",
            "subregion": "Central Europe",
            "borders": [
                "AUT",
                "DEU",
                "POL",
                "SVK"
            ]
        },
        {
            "country": "Estonia",
            "capital": "Tallinn",
            "population": 1331057,
            "area_km2": 45227.0,
            "languages": [
                "Estonian"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/ee.png",
            "subregion": "Northern Europe",
            "borders": [
                "LVA",
                "RUS"
            ]
        },
        {
            "country": "Romania",
            "capital": "Bucharest",
            "population": 19286123,
            "area_km2": 238391.0,
            "languages": [
                "Romanian"
            ],
            "currencies": [
                "RON"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/ro.png",
            "subregion": "Southeast Europe",
            "borders": [
                "BGR",
                "HUN",
                "MDA",
                "SRB",
                "UKR"
            ]
        },
        {
            "country": "Vatican City",
            "capital": "Vatican City",
            "population": 451,
            "area_km2": 0.44,
            "languages": [
                "Italian",
                "Latin"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/va.png",
            "subregion": "Southern Europe",
            "borders": [
                "ITA"
            ]
        },
        {
            "country": "Austria",
            "capital": "Vienna",
            "population": 8917205,
            "area_km2": 83871.0,
            "languages": [
                "German"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/at.png",
            "subregion": "Central Europe",
            "borders": [
                "CZE",
                "DEU",
                "HUN",
                "ITA",
                "LIE",
                "SVK",
                "SVN",
                "CHE"
            ]
        },
        {
            "country": "Ireland",
            "capital": "Dublin",
            "population": 4994724,
            "area_km2": 70273.0,
            "languages": [
                "English",
                "Irish"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/ie.png",
            "subregion": "Northern Europe",
            "borders": [
                "GBR"
            ]
        },
        {
            "country": "Norway",
            "capital": "Oslo",
            "population": 5379475,
            "area_km2": 323802.0,
            "languages": [
                "Norwegian Nynorsk",
                "Norwegian Bokmål",
                "Sami"
            ],
            "currencies": [
                "NOK"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/no.png",
            "subregion": "Northern Europe",
            "borders": [
                "FIN",
                "SWE",
                "RUS"
            ]
        },
        {
            "country": "Åland Islands",
            "capital": "Mariehamn",
            "population": 29458,
            "area_km2": 1580.0,
            "languages": [
                "Swedish"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/ax.png",
            "subregion": "Northern Europe",
            "borders": []
        },
        {
            "country": "Lithuania",
            "capital": "Vilnius",
            "population": 2794700,
            "area_km2": 65300.0,
            "languages": [
                "Lithuanian"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/lt.png",
            "subregion": "Northern Europe",
            "borders": [
                "BLR",
                "LVA",
                "POL",
                "RUS"
            ]
        },
        {
            "country": "Slovakia",
            "capital": "Bratislava",
            "population": 5458827,
            "area_km2": 49037.0,
            "languages": [
                "Slovak"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/sk.png",
            "subregion": "Central Europe",
            "borders": [
                "AUT",
                "CZE",
                "HUN",
                "POL",
                "UKR"
            ]
        },
        {
            "country": "Moldova",
            "capital": "Chișinău",
            "population": 2617820,
            "area_km2": 33846.0,
            "languages": [
                "Romanian"
            ],
            "currencies": [
                "MDL"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/md.png",
            "subregion": "Eastern Europe",
            "borders": [
                "ROU",
                "UKR"
            ]
        },
        {
            "country": "Jersey",
            "capital": "Saint Helier",
            "population": 100800,
            "area_km2": 116.0,
            "languages": [
                "English",
                "French",
                "Jèrriais"
            ],
            "currencies": [
                "GBP",
                "JEP"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/je.png",
            "subregion": "Northern Europe",
            "borders": []
        },
        {
            "country": "Malta",
            "capital": "Valletta",
            "population": 525285,
            "area_km2": 316.0,
            "languages": [
                "English",
                "Maltese"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/mt.png",
            "subregion": "Southern Europe",
            "borders": []
        },
        {
            "country": "Kosovo",
            "capital": "Pristina",
            "population": 1775378,
            "area_km2": 10908.0,
            "languages": [
                "Albanian",
                "Serbian"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/xk.png",
            "subregion": "Southeast Europe",
            "borders": [
                "ALB",
                "MKD",
                "MNE",
                "SRB"
            ]
        },
        {
            "country": "Albania",
            "capital": "Tirana",
            "population": 2837743,
            "area_km2": 28748.0,
            "languages": [
                "Albanian"
            ],
            "currencies": [
                "ALL"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/al.png",
            "subregion": "Southeast Europe",
            "borders": [
                "MNE",
                "GRC",
                "MKD",
                "UNK"
            ]
        },
        {
            "country": "Serbia",
            "capital": "Belgrade",
            "population": 6908224,
            "area_km2": 88361.0,
            "languages": [
                "Serbian"
            ],
            "currencies": [
                "RSD"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/rs.png",
            "subregion": "Southeast Europe",
            "borders": [
                "BIH",
                "BGR",
                "HRV",
                "HUN",
                "UNK",
                "MKD",
                "MNE",
                "ROU"
            ]
        },
        {
            "country": "Poland",
            "capital": "Warsaw",
            "population": 37950802,
            "area_km2": 312679.0,
            "languages": [
                "Polish"
            ],
            "currencies": [
                "PLN"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/pl.png",
            "subregion": "Central Europe",
            "borders": [
                "BLR",
                "CZE",
                "DEU",
                "LTU",
                "RUS",
                "SVK",
                "UKR"
            ]
        },
        {
            "country": "Portugal",
            "capital": "Lisbon",
            "population": 10305564,
            "area_km2": 92090.0,
            "languages": [
                "Portuguese"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC-01:00",
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/pt.png",
            "subregion": "Southern Europe",
            "borders": [
                "ESP"
            ]
        },
        {
            "country": "Belgium",
            "capital": "Brussels",
            "population": 11555997,
            "area_km2": 30528.0,
            "languages": [
                "German",
                "French",
                "Dutch"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/be.png",
            "subregion": "Western Europe",
            "borders": [
                "FRA",
                "DEU",
                "LUX",
                "NLD"
            ]
        }
    ],
    "Africa": [
        {
            "country": "Sierra Leone",
            "capital": "Freetown",
            "population": 7976985,
            "area_km2": 71740.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "SLL"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/sl.png",
            "subregion": "Western Africa",
            "borders": [
                "GIN",
                "LBR"
            ]
        },
        {
            "country": "Ivory Coast",
            "capital": "Yamoussoukro",
            "population": 26378275,
            "area_km2": 322463.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "XOF"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/ci.png",
            "subregion": "Western Africa",
            "borders": [
                "BFA",
                "GHA",
                "GIN",
                "LBR",
                "MLI"
            ]
        },
        {
            "country": "Tunisia",
            "capital": "Tunis",
            "population": 11818618,
            "area_km2": 163610.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "TND"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/tn.png",
            "subregion": "Northern Africa",
            "borders": [
                "DZA",
                "LBY"
            ]
        },
        {
            "country": "Benin",
            "capital": "Porto-Novo",
            "population": 12123198,
            "area_km2": 112622.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "XOF"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/bj.png",
            "subregion": "Western Africa",
            "borders": [
                "BFA",
                "NER",
                "NGA",
                "TGO"
            ]
        },
        {
            "country": "Cape Verde",
            "capital": "Praia",
            "population": 555988,
            "area_km2": 4033.0,
            "languages": [
                "Portuguese"
            ],
            "currencies": [
                "CVE"
            ],
            "timezones": [
                "UTC-01:00"
            ],
            "flag": "https://flagcdn.com/w320/cv.png",
            "subregion": "Western Africa",
            "borders": []
        },
        {
            "country": "Uganda",
            "capital": "Kampala",
            "population": 45741000,
            "area_km2": 241550.0,
            "languages": [
                "English",
                "Swahili"
            ],
            "currencies": [
                "UGX"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/ug.png",
            "subregion": "Eastern Africa",
            "borders": [
                "COD",
                "KEN",
                "RWA",
                "SSD",
                "TZA"
            ]
        },
        {
            "country": "Burundi",
            "capital": "Gitega",
            "population": 11890781,
            "area_km2": 27834.0,
            "languages": [
                "French",
                "Kirundi"
            ],
            "currencies": [
                "BIF"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/bi.png",
            "subregion": "Eastern Africa",
            "borders": [
                "COD",
                "RWA",
                "TZA"
            ]
        },
        {
            "country": "South Africa",
            "capital": "Pretoria",
            "population": 59308690,
            "area_km2": 1221037.0,
            "languages": [
                "Afrikaans",
                "English",
                "Southern Ndebele",
                "Northern Sotho",
                "Southern Sotho",
                "Swazi",
                "Tswana",
                "Tsonga",
                "Venda",
                "Xhosa",
                "Zulu"
            ],
            "currencies": [
                "ZAR"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/za.png",
            "subregion": "Southern Africa",
            "borders": [
                "BWA",
                "LSO",
                "MOZ",
                "NAM",
                "SWZ",
                "ZWE"
            ]
        },
        {
            "country": "Libya",
            "capital": "Tripoli",
            "population": 6871287,
            "area_km2": 1759540.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "LYD"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/ly.png",
            "subregion": "Northern Africa",
            "borders": [
                "DZA",
                "TCD",
                "EGY",
                "NER",
                "SDN",
                "TUN"
            ]
        },
        {
            "country": "Gabon",
            "capital": "Libreville",
            "population": 2225728,
            "area_km2": 267668.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "XAF"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/ga.png",
            "subregion": "Middle Africa",
            "borders": [
                "CMR",
                "COG",
                "GNQ"
            ]
        },
        {
            "country": "Egypt",
            "capital": "Cairo",
            "population": 102334403,
            "area_km2": 1002450.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "EGP"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/eg.png",
            "subregion": "Northern Africa",
            "borders": [
                "ISR",
                "LBY",
                "PSE",
                "SDN"
            ]
        },
        {
            "country": "Senegal",
            "capital": "Dakar",
            "population": 16743930,
            "area_km2": 196722.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "XOF"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/sn.png",
            "subregion": "Western Africa",
            "borders": [
                "GMB",
                "GIN",
                "GNB",
                "MLI",
                "MRT"
            ]
        },
        {
            "country": "Zambia",
            "capital": "Lusaka",
            "population": 18383956,
            "area_km2": 752612.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "ZMW"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/zm.png",
            "subregion": "Eastern Africa",
            "borders": [
                "AGO",
                "BWA",
                "COD",
                "MWI",
                "MOZ",
                "NAM",
                "TZA",
                "ZWE"
            ]
        },
        {
            "country": "Niger",
            "capital": "Niamey",
            "population": 24206636,
            "area_km2": 1267000.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "XOF"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/ne.png",
            "subregion": "Western Africa",
            "borders": [
                "DZA",
                "BEN",
                "BFA",
                "TCD",
                "LBY",
                "MLI",
                "NGA"
            ]
        },
        {
            "country": "Guinea-Bissau",
            "capital": "Bissau",
            "population": 1967998,
            "area_km2": 36125.0,
            "languages": [
                "Portuguese",
                "Upper Guinea Creole"
            ],
            "currencies": [
                "XOF"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/gw.png",
            "subregion": "Western Africa",
            "borders": [
                "GIN",
                "SEN"
            ]
        },
        {
            "country": "Réunion",
            "capital": "Saint-Denis",
            "population": 840974,
            "area_km2": 2511.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+04:00"
            ],
            "flag": "https://flagcdn.com/w320/re.png",
            "subregion": "Eastern Africa",
            "borders": []
        },
        {
            "country": "Djibouti",
            "capital": "Djibouti",
            "population": 988002,
            "area_km2": 23200.0,
            "languages": [
                "Arabic",
                "French"
            ],
            "currencies": [
                "DJF"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/dj.png",
            "subregion": "Eastern Africa",
            "borders": [
                "ERI",
                "ETH",
                "SOM"
            ]
        },
        {
            "country": "Mauritius",
            "capital": "Port Louis",
            "population": 1265740,
            "area_km2": 2040.0,
            "languages": [
                "English",
                "French",
                "Mauritian Creole"
            ],
            "currencies": [
                "MUR"
            ],
            "timezones": [
                "UTC+04:00"
            ],
            "flag": "https://flagcdn.com/w320/mu.png",
            "subregion": "Eastern Africa",
            "borders": []
        },
        {
            "country": "Morocco",
            "capital": "Rabat",
            "population": 36910558,
            "area_km2": 446550.0,
            "languages": [
                "Arabic",
                "Berber"
            ],
            "currencies": [
                "MAD"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/ma.png",
            "subregion": "Northern Africa",
            "borders": [
                "DZA",
                "ESH",
                "ESP"
            ]
        },
        {
            "country": "Algeria",
            "capital": "Algiers",
            "population": 44700000,
            "area_km2": 2381741.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "DZD"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/dz.png",
            "subregion": "Northern Africa",
            "borders": [
                "TUN",
                "LBY",
                "NER",
                "ESH",
                "MRT",
                "MLI",
                "MAR"
            ]
        },
        {
            "country": "Sudan",
            "capital": "Khartoum",
            "population": 43849269,
            "area_km2": 1886068.0,
            "languages": [
                "Arabic",
                "English"
            ],
            "currencies": [
                "SDG"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/sd.png",
            "subregion": "Northern Africa",
            "borders": [
                "CAF",
                "TCD",
                "EGY",
                "ERI",
                "ETH",
                "LBY",
                "SSD"
            ]
        },
        {
            "country": "Botswana",
            "capital": "Gaborone",
            "population": 2351625,
            "area_km2": 582000.0,
            "languages": [
                "English",
                "Tswana"
            ],
            "currencies": [
                "BWP"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/bw.png",
            "subregion": "Southern Africa",
            "borders": [
                "NAM",
                "ZAF",
                "ZMB",
                "ZWE"
            ]
        },
        {
            "country": "Mayotte",
            "capital": "Mamoudzou",
            "population": 226915,
            "area_km2": 374.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "EUR"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/yt.png",
            "subregion": "Eastern Africa",
            "borders": []
        },
        {
            "country": "Madagascar",
            "capital": "Antananarivo",
            "population": 27691019,
            "area_km2": 587041.0,
            "languages": [
                "French",
                "Malagasy"
            ],
            "currencies": [
                "MGA"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/mg.png",
            "subregion": "Eastern Africa",
            "borders": []
        },
        {
            "country": "Eswatini",
            "capital": "Mbabane",
            "population": 1160164,
            "area_km2": 17364.0,
            "languages": [
                "English",
                "Swazi"
            ],
            "currencies": [
                "SZL",
                "ZAR"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/sz.png",
            "subregion": "Southern Africa",
            "borders": [
                "MOZ",
                "ZAF"
            ]
        },
        {
            "country": "Namibia",
            "capital": "Windhoek",
            "population": 2540916,
            "area_km2": 825615.0,
            "languages": [
                "Afrikaans",
                "German",
                "English",
                "Herero",
                "Khoekhoe",
                "Kwangali",
                "Lozi",
                "Ndonga",
                "Tswana"
            ],
            "currencies": [
                "NAD",
                "ZAR"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/na.png",
            "subregion": "Southern Africa",
            "borders": [
                "AGO",
                "BWA",
                "ZAF",
                "ZMB"
            ]
        },
        {
            "country": "São Tomé and Príncipe",
            "capital": "São Tomé",
            "population": 219161,
            "area_km2": 964.0,
            "languages": [
                "Portuguese"
            ],
            "currencies": [
                "STN"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/st.png",
            "subregion": "Middle Africa",
            "borders": []
        },
        {
            "country": "Malawi",
            "capital": "Lilongwe",
            "population": 19129955,
            "area_km2": 118484.0,
            "languages": [
                "English",
                "Chewa"
            ],
            "currencies": [
                "MWK"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/mw.png",
            "subregion": "Eastern Africa",
            "borders": [
                "MOZ",
                "TZA",
                "ZMB"
            ]
        },
        {
            "country": "Ethiopia",
            "capital": "Addis Ababa",
            "population": 114963583,
            "area_km2": 1104300.0,
            "languages": [
                "Amharic"
            ],
            "currencies": [
                "ETB"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/et.png",
            "subregion": "Eastern Africa",
            "borders": [
                "DJI",
                "ERI",
                "KEN",
                "SOM",
                "SSD",
                "SDN"
            ]
        },
        {
            "country": "Lesotho",
            "capital": "Maseru",
            "population": 2142252,
            "area_km2": 30355.0,
            "languages": [
                "English",
                "Sotho"
            ],
            "currencies": [
                "LSL",
                "ZAR"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/ls.png",
            "subregion": "Southern Africa",
            "borders": [
                "ZAF"
            ]
        },
        {
            "country": "Western Sahara",
            "capital": "El Aaiún",
            "population": 510713,
            "area_km2": 266000.0,
            "languages": [
                "Berber",
                "Hassaniya",
                "Spanish"
            ],
            "currencies": [
                "DZD",
                "MAD",
                "MRU"
            ],
            "timezones": [
                "UTC+00:00"
            ],
            "flag": "https://flagcdn.com/w320/eh.png",
            "subregion": "Northern Africa",
            "borders": [
                "DZA",
                "MRT",
                "MAR"
            ]
        },
        {
            "country": "Equatorial Guinea",
            "capital": "Malabo",
            "population": 1402985,
            "area_km2": 28051.0,
            "languages": [
                "French",
                "Portuguese",
                "Spanish"
            ],
            "currencies": [
                "XAF"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/gq.png",
            "subregion": "Middle Africa",
            "borders": [
                "CMR",
                "GAB"
            ]
        },
        {
            "country": "Cameroon",
            "capital": "Yaoundé",
            "population": 26545864,
            "area_km2": 475442.0,
            "languages": [
                "English",
                "French"
            ],
            "currencies": [
                "XAF"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/cm.png",
            "subregion": "Middle Africa",
            "borders": [
                "CAF",
                "TCD",
                "COG",
                "GNQ",
                "GAB",
                "NGA"
            ]
        },
        {
            "country": "Guinea",
            "capital": "Conakry",
            "population": 13132792,
            "area_km2": 245857.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "GNF"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/gn.png",
            "subregion": "Western Africa",
            "borders": [
                "CIV",
                "GNB",
                "LBR",
                "MLI",
                "SEN",
                "SLE"
            ]
        },
        {
            "country": "DR Congo",
            "capital": "Kinshasa",
            "population": 108407721,
            "area_km2": 2344858.0,
            "languages": [
                "French",
                "Kikongo",
                "Lingala",
                "Tshiluba",
                "Swahili"
            ],
            "currencies": [
                "CDF"
            ],
            "timezones": [
                "UTC+01:00",
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/cd.png",
            "subregion": "Middle Africa",
            "borders": [
                "AGO",
                "BDI",
                "CAF",
                "COG",
                "RWA",
                "SSD",
                "TZA",
                "UGA",
                "ZMB"
            ]
        },
        {
            "country": "Somalia",
            "capital": "Mogadishu",
            "population": 15893219,
            "area_km2": 637657.0,
            "languages": [
                "Arabic",
                "Somali"
            ],
            "currencies": [
                "SOS"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/so.png",
            "subregion": "Eastern Africa",
            "borders": [
                "DJI",
                "ETH",
                "KEN"
            ]
        },
        {
            "country": "Saint Helena, Ascension and Tristan da Cunha",
            "capital": "Jamestown",
            "population": 53192,
            "area_km2": 394.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "GBP",
                "SHP"
            ],
            "timezones": [
                "UTC+00:00"
            ],
            "flag": "https://flagcdn.com/w320/sh.png",
            "subregion": "Western Africa",
            "borders": []
        },
        {
            "country": "Togo",
            "capital": "Lomé",
            "population": 8278737,
            "area_km2": 56785.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "XOF"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/tg.png",
            "subregion": "Western Africa",
            "borders": [
                "BEN",
                "BFA",
                "GHA"
            ]
        },
        {
            "country": "Kenya",
            "capital": "Nairobi",
            "population": 53771300,
            "area_km2": 580367.0,
            "languages": [
                "English",
                "Swahili"
            ],
            "currencies": [
                "KES"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/ke.png",
            "subregion": "Eastern Africa",
            "borders": [
                "ETH",
                "SOM",
                "SSD",
                "TZA",
                "UGA"
            ]
        },
        {
            "country": "Rwanda",
            "capital": "Kigali",
            "population": 12952209,
            "area_km2": 26338.0,
            "languages": [
                "English",
                "French",
                "Kinyarwanda"
            ],
            "currencies": [
                "RWF"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/rw.png",
            "subregion": "Eastern Africa",
            "borders": [
                "BDI",
                "COD",
                "TZA",
                "UGA"
            ]
        },
        {
            "country": "Mozambique",
            "capital": "Maputo",
            "population": 31255435,
            "area_km2": 801590.0,
            "languages": [
                "Portuguese"
            ],
            "currencies": [
                "MZN"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/mz.png",
            "subregion": "Eastern Africa",
            "borders": [
                "MWI",
                "ZAF",
                "SWZ",
                "TZA",
                "ZMB",
                "ZWE"
            ]
        },
        {
            "country": "Central African Republic",
            "capital": "Bangui",
            "population": 4829764,
            "area_km2": 622984.0,
            "languages": [
                "French",
                "Sango"
            ],
            "currencies": [
                "XAF"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/cf.png",
            "subregion": "Middle Africa",
            "borders": [
                "CMR",
                "TCD",
                "COD",
                "COG",
                "SSD",
                "SDN"
            ]
        },
        {
            "country": "Burkina Faso",
            "capital": "Ouagadougou",
            "population": 20903278,
            "area_km2": 272967.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "XOF"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/bf.png",
            "subregion": "Western Africa",
            "borders": [
                "BEN",
                "CIV",
                "GHA",
                "MLI",
                "NER",
                "TGO"
            ]
        },
        {
            "country": "Eritrea",
            "capital": "Asmara",
            "population": 5352000,
            "area_km2": 117600.0,
            "languages": [
                "Arabic",
                "English",
                "Tigrinya"
            ],
            "currencies": [
                "ERN"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/er.png",
            "subregion": "Eastern Africa",
            "borders": [
                "DJI",
                "ETH",
                "SDN"
            ]
        },
        {
            "country": "Tanzania",
            "capital": "Dodoma",
            "population": 59734213,
            "area_km2": 945087.0,
            "languages": [
                "English",
                "Swahili"
            ],
            "currencies": [
                "TZS"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/tz.png",
            "subregion": "Eastern Africa",
            "borders": [
                "BDI",
                "COD",
                "KEN",
                "MWI",
                "MOZ",
                "RWA",
                "UGA",
                "ZMB"
            ]
        },
        {
            "country": "Mauritania",
            "capital": "Nouakchott",
            "population": 4649660,
            "area_km2": 1030700.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "MRU"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/mr.png",
            "subregion": "Western Africa",
            "borders": [
                "DZA",
                "MLI",
                "SEN",
                "ESH"
            ]
        },
        {
            "country": "Angola",
            "capital": "Luanda",
            "population": 32866268,
            "area_km2": 1246700.0,
            "languages": [
                "Portuguese"
            ],
            "currencies": [
                "AOA"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/ao.png",
            "subregion": "Middle Africa",
            "borders": [
                "COG",
                "COD",
                "ZMB",
                "NAM"
            ]
        },
        {
            "country": "Mali",
            "capital": "Bamako",
            "population": 20250834,
            "area_km2": 1240192.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "XOF"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/ml.png",
            "subregion": "Western Africa",
            "borders": [
                "DZA",
                "BFA",
                "GIN",
                "CIV",
                "MRT",
                "NER",
                "SEN"
            ]
        },
        {
            "country": "Seychelles",
            "capital": "Victoria",
            "population": 98462,
            "area_km2": 452.0,
            "languages": [
                "Seychellois Creole",
                "English",
                "French"
            ],
            "currencies": [
                "SCR"
            ],
            "timezones": [
                "UTC+04:00"
            ],
            "flag": "https://flagcdn.com/w320/sc.png",
            "subregion": "Eastern Africa",
            "borders": []
        },
        {
            "country": "British Indian Ocean Territory",
            "capital": "Diego Garcia",
            "population": 3000,
            "area_km2": 60.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC+06:00"
            ],
            "flag": "https://flagcdn.com/w320/io.png",
            "subregion": "Eastern Africa",
            "borders": []
        },
        {
            "country": "Gambia",
            "capital": "Banjul",
            "population": 2416664,
            "area_km2": 10689.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "GMD"
            ],
            "timezones": [
                "UTC+00:00"
            ],
            "flag": "https://flagcdn.com/w320/gm.png",
            "subregion": "Western Africa",
            "borders": [
                "SEN"
            ]
        },
        {
            "country": "Nigeria",
            "capital": "Abuja",
            "population": 206139587,
            "area_km2": 923768.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "NGN"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/ng.png",
            "subregion": "Western Africa",
            "borders": [
                "BEN",
                "CMR",
                "TCD",
                "NER"
            ]
        },
        {
            "country": "South Sudan",
            "capital": "Juba",
            "population": 11193729,
            "area_km2": 619745.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "SSP"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/ss.png",
            "subregion": "Middle Africa",
            "borders": [
                "CAF",
                "COD",
                "ETH",
                "KEN",
                "SDN",
                "UGA"
            ]
        },
        {
            "country": "Liberia",
            "capital": "Monrovia",
            "population": 5057677,
            "area_km2": 111369.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "LRD"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/lr.png",
            "subregion": "Western Africa",
            "borders": [
                "GIN",
                "CIV",
                "SLE"
            ]
        },
        {
            "country": "Comoros",
            "capital": "Moroni",
            "population": 869595,
            "area_km2": 1862.0,
            "languages": [
                "Arabic",
                "French",
                "Comorian"
            ],
            "currencies": [
                "KMF"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/km.png",
            "subregion": "Eastern Africa",
            "borders": []
        },
        {
            "country": "Ghana",
            "capital": "Accra",
            "population": 31072945,
            "area_km2": 238533.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "GHS"
            ],
            "timezones": [
                "UTC"
            ],
            "flag": "https://flagcdn.com/w320/gh.png",
            "subregion": "Western Africa",
            "borders": [
                "BFA",
                "CIV",
                "TGO"
            ]
        },
        {
            "country": "Chad",
            "capital": "N'Djamena",
            "population": 16425859,
            "area_km2": 1284000.0,
            "languages": [
                "Arabic",
                "French"
            ],
            "currencies": [
                "XAF"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/td.png",
            "subregion": "Middle Africa",
            "borders": [
                "CMR",
                "CAF",
                "LBY",
                "NER",
                "NGA",
                "SDN"
            ]
        },
        {
            "country": "Zimbabwe",
            "capital": "Harare",
            "population": 14862927,
            "area_km2": 390757.0,
            "languages": [
                "Chibarwe",
                "English",
                "Kalanga",
                "Khoisan",
                "Ndau",
                "Northern Ndebele",
                "Chewa",
                "Shona",
                "Sotho",
                "Tonga",
                "Tswana",
                "Tsonga",
                "Venda",
                "Xhosa",
                "Zimbabwean Sign Language"
            ],
            "currencies": [
                "ZWL"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/zw.png",
            "subregion": "Southern Africa",
            "borders": [
                "BWA",
                "MOZ",
                "ZAF",
                "ZMB"
            ]
        },
        {
            "country": "Republic of the Congo",
            "capital": "Brazzaville",
            "population": 5657000,
            "area_km2": 342000.0,
            "languages": [
                "French",
                "Kikongo",
                "Lingala"
            ],
            "currencies": [
                "XAF"
            ],
            "timezones": [
                "UTC+01:00"
            ],
            "flag": "https://flagcdn.com/w320/cg.png",
            "subregion": "Middle Africa",
            "borders": [
                "AGO",
                "CMR",
                "CAF",
                "COD",
                "GAB"
            ]
        }
    ],
    "Asia": [
        {
            "country": "Taiwan",
            "capital": "Taipei",
            "population": 23503349,
            "area_km2": 36193.0,
            "languages": [
                "Chinese"
            ],
            "currencies": [
                "TWD"
            ],
            "timezones": [
                "UTC+08:00"
            ],
            "flag": "https://flagcdn.com/w320/tw.png",
            "subregion": "Eastern Asia",
            "borders": []
        },
        {
            "country": "Indonesia",
            "capital": "Jakarta",
            "population": 273523621,
            "area_km2": 1904569.0,
            "languages": [
                "Indonesian"
            ],
            "currencies": [
                "IDR"
            ],
            "timezones": [
                "UTC+07:00",
                "UTC+08:00",
                "UTC+09:00"
            ],
            "flag": "https://flagcdn.com/w320/id.png",
            "subregion": "South-Eastern Asia",
            "borders": [
                "TLS",
                "MYS",
                "PNG"
            ]
        },
        {
            "country": "Laos",
            "capital": "Vientiane",
            "population": 7275556,
            "area_km2": 236800.0,
            "languages": [
                "Lao"
            ],
            "currencies": [
                "LAK"
            ],
            "timezones": [
                "UTC+07:00"
            ],
            "flag": "https://flagcdn.com/w320/la.png",
            "subregion": "South-Eastern Asia",
            "borders": [
                "MMR",
                "KHM",
                "CHN",
                "THA",
                "VNM"
            ]
        },
        {
            "country": "China",
            "capital": "Beijing",
            "population": 1402112000,
            "area_km2": 9706961.0,
            "languages": [
                "Chinese"
            ],
            "currencies": [
                "CNY"
            ],
            "timezones": [
                "UTC+08:00"
            ],
            "flag": "https://flagcdn.com/w320/cn.png",
            "subregion": "Eastern Asia",
            "borders": [
                "AFG",
                "BTN",
                "MMR",
                "HKG",
                "IND",
                "KAZ",
                "NPL",
                "PRK",
                "KGZ",
                "LAO",
                "MAC",
                "MNG",
                "PAK",
                "RUS",
                "TJK",
                "VNM"
            ]
        },
        {
            "country": "Yemen",
            "capital": "Sana'a",
            "population": 29825968,
            "area_km2": 527968.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "YER"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/ye.png",
            "subregion": "Western Asia",
            "borders": [
                "OMN",
                "SAU"
            ]
        },
        {
            "country": "Uzbekistan",
            "capital": "Tashkent",
            "population": 34232050,
            "area_km2": 447400.0,
            "languages": [
                "Russian",
                "Uzbek"
            ],
            "currencies": [
                "UZS"
            ],
            "timezones": [
                "UTC+05:00"
            ],
            "flag": "https://flagcdn.com/w320/uz.png",
            "subregion": "Central Asia",
            "borders": [
                "AFG",
                "KAZ",
                "KGZ",
                "TJK",
                "TKM"
            ]
        },
        {
            "country": "Sri Lanka",
            "capital": "Sri Jayawardenepura Kotte",
            "population": 21919000,
            "area_km2": 65610.0,
            "languages": [
                "Sinhala",
                "Tamil"
            ],
            "currencies": [
                "LKR"
            ],
            "timezones": [
                "UTC+05:30"
            ],
            "flag": "https://flagcdn.com/w320/lk.png",
            "subregion": "Southern Asia",
            "borders": [
                "IND"
            ]
        },
        {
            "country": "Palestine",
            "capital": "Ramallah",
            "population": 4803269,
            "area_km2": 6220.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "EGP",
                "ILS",
                "JOD"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/ps.png",
            "subregion": "Western Asia",
            "borders": [
                "ISR",
                "EGY",
                "JOR"
            ]
        },
        {
            "country": "Bangladesh",
            "capital": "Dhaka",
            "population": 164689383,
            "area_km2": 147570.0,
            "languages": [
                "Bengali"
            ],
            "currencies": [
                "BDT"
            ],
            "timezones": [
                "UTC+06:00"
            ],
            "flag": "https://flagcdn.com/w320/bd.png",
            "subregion": "Southern Asia",
            "borders": [
                "MMR",
                "IND"
            ]
        },
        {
            "country": "Singapore",
            "capital": "Singapore",
            "population": 5685807,
            "area_km2": 710.0,
            "languages": [
                "English",
                "Chinese",
                "Malay",
                "Tamil"
            ],
            "currencies": [
                "SGD"
            ],
            "timezones": [
                "UTC+08:00"
            ],
            "flag": "https://flagcdn.com/w320/sg.png",
            "subregion": "South-Eastern Asia",
            "borders": []
        },
        {
            "country": "Turkey",
            "capital": "Ankara",
            "population": 84339067,
            "area_km2": 783562.0,
            "languages": [
                "Turkish"
            ],
            "currencies": [
                "TRY"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/tr.png",
            "subregion": "Western Asia",
            "borders": [
                "ARM",
                "AZE",
                "BGR",
                "GEO",
                "GRC",
                "IRN",
                "IRQ",
                "SYR"
            ]
        },
        {
            "country": "Afghanistan",
            "capital": "Kabul",
            "population": 40218234,
            "area_km2": 652230.0,
            "languages": [
                "Dari",
                "Pashto",
                "Turkmen"
            ],
            "currencies": [
                "AFN"
            ],
            "timezones": [
                "UTC+04:30"
            ],
            "flag": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_the_Taliban.svg/320px-Flag_of_the_Taliban.svg.png",
            "subregion": "Southern Asia",
            "borders": [
                "IRN",
                "PAK",
                "TKM",
                "UZB",
                "TJK",
                "CHN"
            ]
        },
        {
            "country": "Azerbaijan",
            "capital": "Baku",
            "population": 10110116,
            "area_km2": 86600.0,
            "languages": [
                "Azerbaijani"
            ],
            "currencies": [
                "AZN"
            ],
            "timezones": [
                "UTC+04:00"
            ],
            "flag": "https://flagcdn.com/w320/az.png",
            "subregion": "Western Asia",
            "borders": [
                "ARM",
                "GEO",
                "IRN",
                "RUS",
                "TUR"
            ]
        },
        {
            "country": "North Korea",
            "capital": "Pyongyang",
            "population": 25778815,
            "area_km2": 120538.0,
            "languages": [
                "Korean"
            ],
            "currencies": [
                "KPW"
            ],
            "timezones": [
                "UTC+09:00"
            ],
            "flag": "https://flagcdn.com/w320/kp.png",
            "subregion": "Eastern Asia",
            "borders": [
                "CHN",
                "KOR",
                "RUS"
            ]
        },
        {
            "country": "Nepal",
            "capital": "Kathmandu",
            "population": 29136808,
            "area_km2": 147181.0,
            "languages": [
                "Nepali"
            ],
            "currencies": [
                "NPR"
            ],
            "timezones": [
                "UTC+05:45"
            ],
            "flag": "https://flagcdn.com/w320/np.png",
            "subregion": "Southern Asia",
            "borders": [
                "CHN",
                "IND"
            ]
        },
        {
            "country": "Georgia",
            "capital": "Tbilisi",
            "population": 3714000,
            "area_km2": 69700.0,
            "languages": [
                "Georgian"
            ],
            "currencies": [
                "GEL"
            ],
            "timezones": [
                "UTC+04:00"
            ],
            "flag": "https://flagcdn.com/w320/ge.png",
            "subregion": "Western Asia",
            "borders": [
                "ARM",
                "AZE",
                "RUS",
                "TUR"
            ]
        },
        {
            "country": "Pakistan",
            "capital": "Islamabad",
            "population": 220892331,
            "area_km2": 881912.0,
            "languages": [
                "English",
                "Urdu"
            ],
            "currencies": [
                "PKR"
            ],
            "timezones": [
                "UTC+05:00"
            ],
            "flag": "https://flagcdn.com/w320/pk.png",
            "subregion": "Southern Asia",
            "borders": [
                "AFG",
                "CHN",
                "IND",
                "IRN"
            ]
        },
        {
            "country": "Lebanon",
            "capital": "Beirut",
            "population": 6825442,
            "area_km2": 10452.0,
            "languages": [
                "Arabic",
                "French"
            ],
            "currencies": [
                "LBP"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/lb.png",
            "subregion": "Western Asia",
            "borders": [
                "ISR",
                "SYR"
            ]
        },
        {
            "country": "Qatar",
            "capital": "Doha",
            "population": 2881060,
            "area_km2": 11586.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "QAR"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/qa.png",
            "subregion": "Western Asia",
            "borders": [
                "SAU"
            ]
        },
        {
            "country": "India",
            "capital": "New Delhi",
            "population": 1380004385,
            "area_km2": 3287590.0,
            "languages": [
                "English",
                "Hindi",
                "Tamil"
            ],
            "currencies": [
                "INR"
            ],
            "timezones": [
                "UTC+05:30"
            ],
            "flag": "https://flagcdn.com/w320/in.png",
            "subregion": "Southern Asia",
            "borders": [
                "BGD",
                "BTN",
                "MMR",
                "CHN",
                "NPL",
                "PAK"
            ]
        },
        {
            "country": "Syria",
            "capital": "Damascus",
            "population": 17500657,
            "area_km2": 185180.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "SYP"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/sy.png",
            "subregion": "Western Asia",
            "borders": [
                "IRQ",
                "ISR",
                "JOR",
                "LBN",
                "TUR"
            ]
        },
        {
            "country": "United Arab Emirates",
            "capital": "Abu Dhabi",
            "population": 9890400,
            "area_km2": 83600.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "AED"
            ],
            "timezones": [
                "UTC+04:00"
            ],
            "flag": "https://flagcdn.com/w320/ae.png",
            "subregion": "Western Asia",
            "borders": [
                "OMN",
                "SAU"
            ]
        },
        {
            "country": "Cambodia",
            "capital": "Phnom Penh",
            "population": 16718971,
            "area_km2": 181035.0,
            "languages": [
                "Khmer"
            ],
            "currencies": [
                "KHR",
                "USD"
            ],
            "timezones": [
                "UTC+07:00"
            ],
            "flag": "https://flagcdn.com/w320/kh.png",
            "subregion": "South-Eastern Asia",
            "borders": [
                "LAO",
                "THA",
                "VNM"
            ]
        },
        {
            "country": "Iraq",
            "capital": "Baghdad",
            "population": 40222503,
            "area_km2": 438317.0,
            "languages": [
                "Arabic",
                "Aramaic",
                "Sorani"
            ],
            "currencies": [
                "IQD"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/iq.png",
            "subregion": "Western Asia",
            "borders": [
                "IRN",
                "JOR",
                "KWT",
                "SAU",
                "SYR",
                "TUR"
            ]
        },
        {
            "country": "Kyrgyzstan",
            "capital": "Bishkek",
            "population": 6591600,
            "area_km2": 199951.0,
            "languages": [
                "Kyrgyz",
                "Russian"
            ],
            "currencies": [
                "KGS"
            ],
            "timezones": [
                "UTC+06:00"
            ],
            "flag": "https://flagcdn.com/w320/kg.png",
            "subregion": "Central Asia",
            "borders": [
                "CHN",
                "KAZ",
                "TJK",
                "UZB"
            ]
        },
        {
            "country": "Malaysia",
            "capital": "Kuala Lumpur",
            "population": 32365998,
            "area_km2": 330803.0,
            "languages": [
                "English",
                "Malay"
            ],
            "currencies": [
                "MYR"
            ],
            "timezones": [
                "UTC+08:00"
            ],
            "flag": "https://flagcdn.com/w320/my.png",
            "subregion": "South-Eastern Asia",
            "borders": [
                "BRN",
                "IDN",
                "THA"
            ]
        },
        {
            "country": "Saudi Arabia",
            "capital": "Riyadh",
            "population": 34813867,
            "area_km2": 2149690.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "SAR"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/sa.png",
            "subregion": "Western Asia",
            "borders": [
                "IRQ",
                "JOR",
                "KWT",
                "OMN",
                "QAT",
                "ARE",
                "YEM"
            ]
        },
        {
            "country": "Oman",
            "capital": "Muscat",
            "population": 5106622,
            "area_km2": 309500.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "OMR"
            ],
            "timezones": [
                "UTC+04:00"
            ],
            "flag": "https://flagcdn.com/w320/om.png",
            "subregion": "Western Asia",
            "borders": [
                "SAU",
                "ARE",
                "YEM"
            ]
        },
        {
            "country": "Macau",
            "capital": "N/A",
            "population": 649342,
            "area_km2": 30.0,
            "languages": [
                "Portuguese",
                "Chinese"
            ],
            "currencies": [
                "MOP"
            ],
            "timezones": [
                "UTC+08:00"
            ],
            "flag": "https://flagcdn.com/w320/mo.png",
            "subregion": "Eastern Asia",
            "borders": [
                "CHN"
            ]
        },
        {
            "country": "Thailand",
            "capital": "Bangkok",
            "population": 69799978,
            "area_km2": 513120.0,
            "languages": [
                "Thai"
            ],
            "currencies": [
                "THB"
            ],
            "timezones": [
                "UTC+07:00"
            ],
            "flag": "https://flagcdn.com/w320/th.png",
            "subregion": "South-Eastern Asia",
            "borders": [
                "MMR",
                "KHM",
                "LAO",
                "MYS"
            ]
        },
        {
            "country": "Philippines",
            "capital": "Manila",
            "population": 109581085,
            "area_km2": 342353.0,
            "languages": [
                "English",
                "Filipino"
            ],
            "currencies": [
                "PHP"
            ],
            "timezones": [
                "UTC+08:00"
            ],
            "flag": "https://flagcdn.com/w320/ph.png",
            "subregion": "South-Eastern Asia",
            "borders": []
        },
        {
            "country": "Bahrain",
            "capital": "Manama",
            "population": 1701583,
            "area_km2": 765.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "BHD"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/bh.png",
            "subregion": "Western Asia",
            "borders": []
        },
        {
            "country": "Timor-Leste",
            "capital": "Dili",
            "population": 1318442,
            "area_km2": 14874.0,
            "languages": [
                "Portuguese",
                "Tetum"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC+09:00"
            ],
            "flag": "https://flagcdn.com/w320/tl.png",
            "subregion": "South-Eastern Asia",
            "borders": [
                "IDN"
            ]
        },
        {
            "country": "Vietnam",
            "capital": "Hanoi",
            "population": 97338583,
            "area_km2": 331212.0,
            "languages": [
                "Vietnamese"
            ],
            "currencies": [
                "VND"
            ],
            "timezones": [
                "UTC+07:00"
            ],
            "flag": "https://flagcdn.com/w320/vn.png",
            "subregion": "South-Eastern Asia",
            "borders": [
                "KHM",
                "CHN",
                "LAO"
            ]
        },
        {
            "country": "Hong Kong",
            "capital": "City of Victoria",
            "population": 7500700,
            "area_km2": 1104.0,
            "languages": [
                "English",
                "Chinese"
            ],
            "currencies": [
                "HKD"
            ],
            "timezones": [
                "UTC+08:00"
            ],
            "flag": "https://flagcdn.com/w320/hk.png",
            "subregion": "Eastern Asia",
            "borders": [
                "CHN"
            ]
        },
        {
            "country": "Turkmenistan",
            "capital": "Ashgabat",
            "population": 6031187,
            "area_km2": 488100.0,
            "languages": [
                "Russian",
                "Turkmen"
            ],
            "currencies": [
                "TMT"
            ],
            "timezones": [
                "UTC+05:00"
            ],
            "flag": "https://flagcdn.com/w320/tm.png",
            "subregion": "Central Asia",
            "borders": [
                "AFG",
                "IRN",
                "KAZ",
                "UZB"
            ]
        },
        {
            "country": "South Korea",
            "capital": "Seoul",
            "population": 51780579,
            "area_km2": 100210.0,
            "languages": [
                "Korean"
            ],
            "currencies": [
                "KRW"
            ],
            "timezones": [
                "UTC+09:00"
            ],
            "flag": "https://flagcdn.com/w320/kr.png",
            "subregion": "Eastern Asia",
            "borders": [
                "PRK"
            ]
        },
        {
            "country": "Jordan",
            "capital": "Amman",
            "population": 10203140,
            "area_km2": 89342.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "JOD"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/jo.png",
            "subregion": "Western Asia",
            "borders": [
                "IRQ",
                "ISR",
                "PSE",
                "SAU",
                "SYR"
            ]
        },
        {
            "country": "Kazakhstan",
            "capital": "Nur-Sultan",
            "population": 18754440,
            "area_km2": 2724900.0,
            "languages": [
                "Kazakh",
                "Russian"
            ],
            "currencies": [
                "KZT"
            ],
            "timezones": [
                "UTC+05:00",
                "UTC+06:00"
            ],
            "flag": "https://flagcdn.com/w320/kz.png",
            "subregion": "Central Asia",
            "borders": [
                "CHN",
                "KGZ",
                "RUS",
                "TKM",
                "UZB"
            ]
        },
        {
            "country": "Armenia",
            "capital": "Yerevan",
            "population": 2963234,
            "area_km2": 29743.0,
            "languages": [
                "Armenian"
            ],
            "currencies": [
                "AMD"
            ],
            "timezones": [
                "UTC+04:00"
            ],
            "flag": "https://flagcdn.com/w320/am.png",
            "subregion": "Western Asia",
            "borders": [
                "AZE",
                "GEO",
                "IRN",
                "TUR"
            ]
        },
        {
            "country": "Japan",
            "capital": "Tokyo",
            "population": 125836021,
            "area_km2": 377930.0,
            "languages": [
                "Japanese"
            ],
            "currencies": [
                "JPY"
            ],
            "timezones": [
                "UTC+09:00"
            ],
            "flag": "https://flagcdn.com/w320/jp.png",
            "subregion": "Eastern Asia",
            "borders": []
        },
        {
            "country": "Tajikistan",
            "capital": "Dushanbe",
            "population": 9537642,
            "area_km2": 143100.0,
            "languages": [
                "Russian",
                "Tajik"
            ],
            "currencies": [
                "TJS"
            ],
            "timezones": [
                "UTC+05:00"
            ],
            "flag": "https://flagcdn.com/w320/tj.png",
            "subregion": "Central Asia",
            "borders": [
                "AFG",
                "CHN",
                "KGZ",
                "UZB"
            ]
        },
        {
            "country": "Kuwait",
            "capital": "Kuwait City",
            "population": 4270563,
            "area_km2": 17818.0,
            "languages": [
                "Arabic"
            ],
            "currencies": [
                "KWD"
            ],
            "timezones": [
                "UTC+03:00"
            ],
            "flag": "https://flagcdn.com/w320/kw.png",
            "subregion": "Western Asia",
            "borders": [
                "IRQ",
                "SAU"
            ]
        },
        {
            "country": "Maldives",
            "capital": "Malé",
            "population": 540542,
            "area_km2": 300.0,
            "languages": [
                "Maldivian"
            ],
            "currencies": [
                "MVR"
            ],
            "timezones": [
                "UTC+05:00"
            ],
            "flag": "https://flagcdn.com/w320/mv.png",
            "subregion": "Southern Asia",
            "borders": []
        },
        {
            "country": "Iran",
            "capital": "Tehran",
            "population": 83992953,
            "area_km2": 1648195.0,
            "languages": [
                "Persian (Farsi)"
            ],
            "currencies": [
                "IRR"
            ],
            "timezones": [
                "UTC+03:30"
            ],
            "flag": "https://flagcdn.com/w320/ir.png",
            "subregion": "Southern Asia",
            "borders": [
                "AFG",
                "ARM",
                "AZE",
                "IRQ",
                "PAK",
                "TUR",
                "TKM"
            ]
        },
        {
            "country": "Myanmar",
            "capital": "Naypyidaw",
            "population": 54409794,
            "area_km2": 676578.0,
            "languages": [
                "Burmese"
            ],
            "currencies": [
                "MMK"
            ],
            "timezones": [
                "UTC+06:30"
            ],
            "flag": "https://flagcdn.com/w320/mm.png",
            "subregion": "South-Eastern Asia",
            "borders": [
                "BGD",
                "CHN",
                "IND",
                "LAO",
                "THA"
            ]
        },
        {
            "country": "Bhutan",
            "capital": "Thimphu",
            "population": 771612,
            "area_km2": 38394.0,
            "languages": [
                "Dzongkha"
            ],
            "currencies": [
                "BTN",
                "INR"
            ],
            "timezones": [
                "UTC+06:00"
            ],
            "flag": "https://flagcdn.com/w320/bt.png",
            "subregion": "Southern Asia",
            "borders": [
                "CHN",
                "IND"
            ]
        },
        {
            "country": "Brunei",
            "capital": "Bandar Seri Begawan",
            "population": 437483,
            "area_km2": 5765.0,
            "languages": [
                "Malay"
            ],
            "currencies": [
                "BND",
                "SGD"
            ],
            "timezones": [
                "UTC+08:00"
            ],
            "flag": "https://flagcdn.com/w320/bn.png",
            "subregion": "South-Eastern Asia",
            "borders": [
                "MYS"
            ]
        },
        {
            "country": "Mongolia",
            "capital": "Ulan Bator",
            "population": 3278292,
            "area_km2": 1564110.0,
            "languages": [
                "Mongolian"
            ],
            "currencies": [
                "MNT"
            ],
            "timezones": [
                "UTC+07:00",
                "UTC+08:00"
            ],
            "flag": "https://flagcdn.com/w320/mn.png",
            "subregion": "Eastern Asia",
            "borders": [
                "CHN",
                "RUS"
            ]
        },
        {
            "country": "Israel",
            "capital": "Jerusalem",
            "population": 9216900,
            "area_km2": 20770.0,
            "languages": [
                "Arabic",
                "Hebrew"
            ],
            "currencies": [
                "ILS"
            ],
            "timezones": [
                "UTC+02:00"
            ],
            "flag": "https://flagcdn.com/w320/il.png",
            "subregion": "Western Asia",
            "borders": [
                "EGY",
                "JOR",
                "LBN",
                "PSE",
                "SYR"
            ]
        }
    ],
    "Oceania": [
        {
            "country": "Wallis and Futuna",
            "capital": "Mata-Utu",
            "population": 11750,
            "area_km2": 142.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "XPF"
            ],
            "timezones": [
                "UTC+12:00"
            ],
            "flag": "https://flagcdn.com/w320/wf.png",
            "subregion": "Polynesia",
            "borders": []
        },
        {
            "country": "Pitcairn Islands",
            "capital": "Adamstown",
            "population": 56,
            "area_km2": 47.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "NZD"
            ],
            "timezones": [
                "UTC-08:00"
            ],
            "flag": "https://flagcdn.com/w320/pn.png",
            "subregion": "Polynesia",
            "borders": []
        },
        {
            "country": "Northern Mariana Islands",
            "capital": "Saipan",
            "population": 57557,
            "area_km2": 464.0,
            "languages": [
                "Carolinian",
                "Chamorro",
                "English"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC+10:00"
            ],
            "flag": "https://flagcdn.com/w320/mp.png",
            "subregion": "Micronesia",
            "borders": []
        },
        {
            "country": "Solomon Islands",
            "capital": "Honiara",
            "population": 686878,
            "area_km2": 28896.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "SBD"
            ],
            "timezones": [
                "UTC+11:00"
            ],
            "flag": "https://flagcdn.com/w320/sb.png",
            "subregion": "Melanesia",
            "borders": []
        },
        {
            "country": "Cook Islands",
            "capital": "Avarua",
            "population": 18100,
            "area_km2": 236.0,
            "languages": [
                "English",
                "Cook Islands Māori"
            ],
            "currencies": [
                "CKD",
                "NZD"
            ],
            "timezones": [
                "UTC-10:00"
            ],
            "flag": "https://flagcdn.com/w320/ck.png",
            "subregion": "Polynesia",
            "borders": []
        },
        {
            "country": "Christmas Island",
            "capital": "Flying Fish Cove",
            "population": 2072,
            "area_km2": 135.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "AUD"
            ],
            "timezones": [
                "UTC+07:00"
            ],
            "flag": "https://flagcdn.com/w320/cx.png",
            "subregion": "Australia and New Zealand",
            "borders": []
        },
        {
            "country": "Tokelau",
            "capital": "Fakaofo",
            "population": 1411,
            "area_km2": 12.0,
            "languages": [
                "English",
                "Samoan",
                "Tokelauan"
            ],
            "currencies": [
                "NZD"
            ],
            "timezones": [
                "UTC+13:00"
            ],
            "flag": "https://flagcdn.com/w320/tk.png",
            "subregion": "Polynesia",
            "borders": []
        },
        {
            "country": "Fiji",
            "capital": "Suva",
            "population": 896444,
            "area_km2": 18272.0,
            "languages": [
                "English",
                "Fijian",
                "Fiji Hindi"
            ],
            "currencies": [
                "FJD"
            ],
            "timezones": [
                "UTC+12:00"
            ],
            "flag": "https://flagcdn.com/w320/fj.png",
            "subregion": "Melanesia",
            "borders": []
        },
        {
            "country": "Papua New Guinea",
            "capital": "Port Moresby",
            "population": 8947027,
            "area_km2": 462840.0,
            "languages": [
                "English",
                "Hiri Motu",
                "Tok Pisin"
            ],
            "currencies": [
                "PGK"
            ],
            "timezones": [
                "UTC+10:00"
            ],
            "flag": "https://flagcdn.com/w320/pg.png",
            "subregion": "Melanesia",
            "borders": [
                "IDN"
            ]
        },
        {
            "country": "Norfolk Island",
            "capital": "Kingston",
            "population": 2302,
            "area_km2": 36.0,
            "languages": [
                "English",
                "Norfuk"
            ],
            "currencies": [
                "AUD"
            ],
            "timezones": [
                "UTC+11:30"
            ],
            "flag": "https://flagcdn.com/w320/nf.png",
            "subregion": "Australia and New Zealand",
            "borders": []
        },
        {
            "country": "Marshall Islands",
            "capital": "Majuro",
            "population": 59194,
            "area_km2": 181.0,
            "languages": [
                "English",
                "Marshallese"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC+12:00"
            ],
            "flag": "https://flagcdn.com/w320/mh.png",
            "subregion": "Micronesia",
            "borders": []
        },
        {
            "country": "Nauru",
            "capital": "Yaren",
            "population": 10834,
            "area_km2": 21.0,
            "languages": [
                "English",
                "Nauru"
            ],
            "currencies": [
                "AUD"
            ],
            "timezones": [
                "UTC+12:00"
            ],
            "flag": "https://flagcdn.com/w320/nr.png",
            "subregion": "Micronesia",
            "borders": []
        },
        {
            "country": "Cocos (Keeling) Islands",
            "capital": "West Island",
            "population": 544,
            "area_km2": 14.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "AUD"
            ],
            "timezones": [
                "UTC+06:30"
            ],
            "flag": "https://flagcdn.com/w320/cc.png",
            "subregion": "Australia and New Zealand",
            "borders": []
        },
        {
            "country": "Australia",
            "capital": "Canberra",
            "population": 25687041,
            "area_km2": 7692024.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "AUD"
            ],
            "timezones": [
                "UTC+05:00",
                "UTC+06:30",
                "UTC+07:00",
                "UTC+08:00",
                "UTC+09:30",
                "UTC+10:00",
                "UTC+10:30",
                "UTC+11:30"
            ],
            "flag": "https://flagcdn.com/w320/au.png",
            "subregion": "Australia and New Zealand",
            "borders": []
        },
        {
            "country": "Tuvalu",
            "capital": "Funafuti",
            "population": 11792,
            "area_km2": 26.0,
            "languages": [
                "English",
                "Tuvaluan"
            ],
            "currencies": [
                "AUD",
                "TVD"
            ],
            "timezones": [
                "UTC+12:00"
            ],
            "flag": "https://flagcdn.com/w320/tv.png",
            "subregion": "Polynesia",
            "borders": []
        },
        {
            "country": "French Polynesia",
            "capital": "Papeetē",
            "population": 280904,
            "area_km2": 4167.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "XPF"
            ],
            "timezones": [
                "UTC-10:00",
                "UTC-09:30",
                "UTC-09:00"
            ],
            "flag": "https://flagcdn.com/w320/pf.png",
            "subregion": "Polynesia",
            "borders": []
        },
        {
            "country": "Palau",
            "capital": "Ngerulmud",
            "population": 18092,
            "area_km2": 459.0,
            "languages": [
                "English",
                "Palauan"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC+09:00"
            ],
            "flag": "https://flagcdn.com/w320/pw.png",
            "subregion": "Micronesia",
            "borders": []
        },
        {
            "country": "New Caledonia",
            "capital": "Nouméa",
            "population": 271960,
            "area_km2": 18575.0,
            "languages": [
                "French"
            ],
            "currencies": [
                "XPF"
            ],
            "timezones": [
                "UTC+11:00"
            ],
            "flag": "https://flagcdn.com/w320/nc.png",
            "subregion": "Melanesia",
            "borders": []
        },
        {
            "country": "Vanuatu",
            "capital": "Port Vila",
            "population": 307150,
            "area_km2": 12189.0,
            "languages": [
                "Bislama",
                "English",
                "French"
            ],
            "currencies": [
                "VUV"
            ],
            "timezones": [
                "UTC+11:00"
            ],
            "flag": "https://flagcdn.com/w320/vu.png",
            "subregion": "Melanesia",
            "borders": []
        },
        {
            "country": "Niue",
            "capital": "Alofi",
            "population": 1470,
            "area_km2": 260.0,
            "languages": [
                "English",
                "Niuean"
            ],
            "currencies": [
                "NZD"
            ],
            "timezones": [
                "UTC-11:00"
            ],
            "flag": "https://flagcdn.com/w320/nu.png",
            "subregion": "Polynesia",
            "borders": []
        },
        {
            "country": "Micronesia",
            "capital": "Palikir",
            "population": 115021,
            "area_km2": 702.0,
            "languages": [
                "English"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC+10:00",
                "UTC+11:00"
            ],
            "flag": "https://flagcdn.com/w320/fm.png",
            "subregion": "Micronesia",
            "borders": []
        },
        {
            "country": "Samoa",
            "capital": "Apia",
            "population": 198410,
            "area_km2": 2842.0,
            "languages": [
                "English",
                "Samoan"
            ],
            "currencies": [
                "WST"
            ],
            "timezones": [
                "UTC+13:00"
            ],
            "flag": "https://flagcdn.com/w320/ws.png",
            "subregion": "Polynesia",
            "borders": []
        },
        {
            "country": "Guam",
            "capital": "Hagåtña",
            "population": 168783,
            "area_km2": 549.0,
            "languages": [
                "Chamorro",
                "English",
                "Spanish"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC+10:00"
            ],
            "flag": "https://flagcdn.com/w320/gu.png",
            "subregion": "Micronesia",
            "borders": []
        },
        {
            "country": "Tonga",
            "capital": "Nuku'alofa",
            "population": 105697,
            "area_km2": 747.0,
            "languages": [
                "English",
                "Tongan"
            ],
            "currencies": [
                "TOP"
            ],
            "timezones": [
                "UTC+13:00"
            ],
            "flag": "https://flagcdn.com/w320/to.png",
            "subregion": "Polynesia",
            "borders": []
        },
        {
            "country": "Kiribati",
            "capital": "South Tarawa",
            "population": 119446,
            "area_km2": 811.0,
            "languages": [
                "English",
                "Gilbertese"
            ],
            "currencies": [
                "AUD",
                "KID"
            ],
            "timezones": [
                "UTC+12:00",
                "UTC+13:00",
                "UTC+14:00"
            ],
            "flag": "https://flagcdn.com/w320/ki.png",
            "subregion": "Micronesia",
            "borders": []
        },
        {
            "country": "American Samoa",
            "capital": "Pago Pago",
            "population": 55197,
            "area_km2": 199.0,
            "languages": [
                "English",
                "Samoan"
            ],
            "currencies": [
                "USD"
            ],
            "timezones": [
                "UTC-11:00"
            ],
            "flag": "https://flagcdn.com/w320/as.png",
            "subregion": "Polynesia",
            "borders": []
        },
        {
            "country": "New Zealand",
            "capital": "Wellington",
            "population": 5084300,
            "area_km2": 270467.0,
            "languages": [
                "English",
                "Māori",
                "New Zealand Sign Language"
            ],
            "currencies": [
                "NZD"
            ],
            "timezones": [
                "UTC-11:00",
                "UTC-10:00",
                "UTC+12:00",
                "UTC+12:45",
                "UTC+13:00"
            ],
            "flag": "https://flagcdn.com/w320/nz.png",
            "subregion": "Australia and New Zealand",
            "borders": []
        }
    ]
}

# Fonctions pour les continents
def get_continents():
    """
    Retourne la liste des continents disponibles.
    """
    return list(data.keys())

def get_countries(continent):
    """
    Retourne la liste des pays dans un continent donné.
    
    :param continent: Nom du continent (str)
    :return: Liste des pays (list) ou une liste vide si le continent n'existe pas.
    """
    return [country['country'] for country in data.get(continent, [])]

# Fonctions spécifiques pour les informations des pays
def get_capital(country_name):
    """
    Retourne la capitale d'un pays donné.
    
    :param country_name: Nom du pays (str)
    :return: Nom de la capitale (str) ou None si le pays n'est pas trouvé.
    """
    country = _find_country(country_name)
    if country:
        return country.get('capital', 'N/A')
    return None

def get_population(country_name):
    """
    Retourne la population d'un pays donné.
    
    :param country_name: Nom du pays (str)
    :return: Population (int) ou None si le pays n'est pas trouvé.
    """
    country = _find_country(country_name)
    if country:
        return country.get('population', 'N/A')
    return None

def get_area(country_name):
    """
    Retourne la superficie d'un pays donné en km².
    
    :param country_name: Nom du pays (str)
    :return: Superficie (float) ou None si le pays n'est pas trouvé.
    """
    country = _find_country(country_name)
    if country:
        return country.get('area_km2', 'N/A')
    return None

def get_languages(country_name):
    """
    Retourne la liste des langues officielles d'un pays donné.
    
    :param country_name: Nom du pays (str)
    :return: Liste des langues ou une liste vide si le pays n'est pas trouvé.
    """
    country = _find_country(country_name)
    if country:
        return country.get('languages', [])
    return []

def get_currencies(country_name):
    """
    Retourne la liste des devises d'un pays donné.
    
    :param country_name: Nom du pays (str)
    :return: Liste des devises ou une liste vide si le pays n'est pas trouvé.
    """
    country = _find_country(country_name)
    if country:
        return country.get('currencies', [])
    return []

def get_timezones(country_name):
    """
    Retourne la liste des fuseaux horaires d'un pays donné.
    
    :param country_name: Nom du pays (str)
    :return: Liste des fuseaux horaires ou une liste vide si le pays n'est pas trouvé.
    """
    country = _find_country(country_name)
    if country:
        return country.get('timezones', [])
    return []

def get_flag(country_name):
    """
    Retourne l'URL du drapeau d'un pays donné.
    
    :param country_name: Nom du pays (str)
    :return: URL du drapeau (str) ou None si le pays n'est pas trouvé.
    """
    country = _find_country(country_name)
    if country:
        return country.get('flag', 'N/A')
    return None

def get_subregion(country_name):
    """
    Retourne la sous-région d'un pays donné.
    
    :param country_name: Nom du pays (str)
    :return: Sous-région (str) ou None si le pays n'est pas trouvé.
    """
    country = _find_country(country_name)
    if country:
        return country.get('subregion', 'N/A')
    return None

def get_borders(country_name):
    """
    Retourne la liste des pays voisins d'un pays donné.
    
    :param country_name: Nom du pays (str)
    :return: Liste des codes des pays voisins ou une liste vide si le pays n'est pas trouvé.
    """
    country = _find_country(country_name)
    if country:
        return country.get('borders', [])
    return []

def get_all_info(country_name):
    """
    Retourne toutes les informations disponibles d'un pays donné.
    
    :param country_name: Nom du pays (str)
    :return: Dictionnaire contenant toutes les informations du pays ou None si le pays n'est pas trouvé.
    """
    return _find_country(country_name)

# Fonction interne pour trouver un pays
def _find_country(country_name):
    """
    Trouve et retourne les données d'un pays donné.
    
    :param country_name: Nom du pays (str)
    :return: Dictionnaire des données du pays ou None si non trouvé.
    """
    for continent, countries in data.items():
        for country in countries:
            if country['country'].lower() == country_name.lower():
                return country
    return None
