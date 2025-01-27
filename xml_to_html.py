import xml.etree.ElementTree as ET
from yattag import Doc

def convert_xml_to_html_polish(xml_file, output_html):
   
    tree = ET.parse(xml_file)
    root = tree.getroot()

   
    doc, tag, text = Doc().tagtext()

    with tag('html'):
        with tag('head'):
            with tag('title'):
                text('Raport Testów Jednostkowych')
            with tag('style'):
                text("""
                    body { font-family: Arial, sans-serif; margin: 20px; }
                    table { border-collapse: collapse; width: 100%; }
                    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                    th { background-color: #f2f2f2; }
                    .pass { color: green; }
                    .fail { color: red; }
                """)
        with tag('body'):
            with tag('h1'):
                text('Raport Testów Jednostkowych')

            for testsuite in root.findall('testsuite'):
                nazwa_pakietu = testsuite.get('name', 'Nieznany Pakiet')
                testy = int(testsuite.get('tests', 0))
                porażki = int(testsuite.get('failures', 0))
                błędy = int(testsuite.get('errors', 0))
                pominięte = int(testsuite.get('skipped', 0))
                czas = testsuite.get('time', '0.0')

                with tag('h2'):
                    text(f'Pakiet: {nazwa_pakietu}')

                with tag('p'):
                    text(f'Testy: {testy}, Porażki: {porażki}, Błędy: {błędy}, Pominięte: {pominięte}, Czas: {czas}s')

                with tag('table'):
                    with tag('tr'):
                        for nagłówek in ['Nazwa Testu', 'Status', 'Czas (s)', 'Plik', 'Linia']:
                            with tag('th'):
                                text(nagłówek)

                    for testcase in testsuite.findall('testcase'):
                        nazwa = testcase.get('name', 'Nieznany Test')
                        status = 'sukces' if not testcase.findall('failure') and not testcase.findall('error') else 'porażka'
                        czas = testcase.get('time', '0.0')
                        plik = testcase.get('file', 'Brak Danych')
                        linia = testcase.get('line', 'Brak Danych')

                        with tag('tr', klass=status):
                            with tag('td'):
                                text(nazwa)
                            with tag('td', klass='pass' if status == 'sukces' else 'fail'):
                                text(status.capitalize())
                            with tag('td'):
                                text(czas)
                            with tag('td'):
                                text(plik)
                            with tag('td'):
                                text(linia)


    with open(output_html, 'w') as f:
        f.write(doc.getvalue())

convert_xml_to_html_polish('test_report.xml', 'raport_testow.html')
print("Raport HTML został wygenerowany jako 'raport_testow.html'")
