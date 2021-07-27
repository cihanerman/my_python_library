
# -*- coding: utf-8 -*-
import requests
import xmltodict
import functools

URL = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?WSDL"

HEADERS = {
    "Host": "tckimlik.nvi.gov.tr",
    "Content-Type": "application/soap+xml; charset=utf-8",
    "Content-Length": "length"
}


def is_turk(tcno: str, name: str, surname: str, bird_year: str) -> bool:
    """
    Republic of Turkey Tc identity number verification function

    Parameters:
        tcno (str):11 digit Tc identification number
        name (str):citizen's name
        name (str):citizen's surname
        bird_year (str):citizen's birthday year

    Returns:
        bool:Is there a citizen registered with the information given ?

    """

    if not (tcno and name and surname and bird_year):
        raise ValueError("Variables cannot express null !")

    if len(tcno) != 11:
        raise ValueError("tcno must be 11 digits !")

    if not bird_year.isdigit():
        raise ValueError("bird_year must be numeric !")

    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
      <soap12:Body>
        <TCKimlikNoDogrula xmlns="http://tckimlik.nvi.gov.tr/WS">
          <TCKimlikNo>{tcno}</TCKimlikNo>
          <Ad>{name}</Ad>
          <Soyad>{surname}</Soyad>
          <DogumYili>{bird_year}</DogumYili>
        </TCKimlikNoDogrula>
      </soap12:Body>
    </soap12:Envelope>"""

    road = ['soap:Envelope', 'soap:Body',
            'TCKimlikNoDogrulaResponse', 'TCKimlikNoDogrulaResult']
    response = requests.post(URL, data=body.encode('utf-8'), headers=HEADERS)
    response.raise_for_status()
    res = functools.reduce(dict.get, road,  xmltodict.parse(response.content))
    return res == "true"
