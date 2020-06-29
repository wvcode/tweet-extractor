import csv as c
import datetime
import os
import re

import typer


def match_dates(data):
    regex = r"\D*(\d{2}\/\d{2}\/\d{4})\w*"
    matches = re.finditer(regex, data, re.MULTILINE)
    for x, i in enumerate(matches):
        if x == 0:
            start_date = i[1]
        else:
            end_date = i[1]
    return start_date, end_date


def match_equipamento(data):
    regex = r"\D*(EPTC-[0-9]*)\s\-\s(.*)"
    matches = re.finditer(regex, data.replace(',', ''), re.MULTILINE)
    for x, i in enumerate(matches):
        cod_equip = i[1]
        end_equip = i[2]
    return cod_equip, end_equip


def main(arquivo: str):
    dados = []
    fonte = 'dados_transito/'
    with open(os.path.join(fonte, arquivo), 'r', encoding='utf-8') as fr:
        rows = c.reader(fr, delimiter=',')
        i = 1
        for line in rows:
            if 'Intervalo' in line[0]:
                start_date, end_date = match_dates(line[0])
                start_date_arr = start_date.split('/')
                date_start = datetime.date(
                    int(start_date_arr[2]), int(start_date_arr[1]), int(start_date_arr[0]))
            elif 'Equipamento' in line[0]:
                cod_equip, end_equip = match_equipamento(line[0])
            else:
                if ':' in line[0]:
                    sd = date_start
                    for idx, item in enumerate(line):
                        if idx > 0 and idx < (len(line)-1):
                            rec = {'data': sd,
                                   'equipamento': cod_equip,
                                   'endereco': end_equip,
                                   'horario': line[0],
                                   'transito': item
                                   }
                            dados.append(rec)
                            sd = sd + datetime.timedelta(days=1)

        with open(arquivo, 'w', encoding='utf-8', newline='') as fw:
            cw = c.DictWriter(
                fw, fieldnames=['data', 'equipamento', 'endereco', 'horario', 'transito'])
            cw.writerows(dados)


# =================================================================================================
# Main Routine
# =================================================================================================
if __name__ == "__main__":
    typer.run(main)
