import csv as c
import os

import typer


def main(file_name: str):
    dados = []
    fonte = 'dados_transito_processados/'

    for arquivo in os.listdir(fonte):
        with open(os.path.join(fonte, arquivo), 'r', encoding='utf-8') as fr:
            cr = c.DictReader(
                fr, fieldnames=['data', 'equipamento', 'endereco', 'horario', 'volume'])
            next(cr)
            for line in cr:
                dados.append(line)

    with open(file_name, 'w', encoding='utf-8', newline='') as fw:
        cw = c.DictWriter(
            fw, fieldnames=['data', 'equipamento', 'endereco', 'horario', 'volume'])
        cw.writeheader()
        cw.writerows(dados)


# =================================================================================================
# Main Routine
# =================================================================================================
if __name__ == "__main__":
    typer.run(main)
