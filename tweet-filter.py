# -*- coding: utf-8 -*-
''' Tweet-Filter
        A script to filter tweets related to
        COVID-19 quarantine/isolation protocol to generate a timeline
'''

import csv
from typing import List

import typer


def main(words: List[str], file_name: str):
    count_total = 0
    count_found = 0
    results = []
    with open(file_name, 'r', encoding='utf-8') as fw:
        csvR = csv.DictReader(
            fw, fieldnames=["date", "text", "id"], dialect="excel")
        for item in csvR:
            count_total += 1
            for word in words:
                if word in item['text']:
                    count_found += 1
                    results.append(item)
                    break

    if count_found > 0:
        print(f"Total: {count_total} - Encontrados: {count_found}")
        with open('filtered_data.csv', 'w', encoding='utf-8') as fw:
            csvW = csv.DictWriter(
                fw, fieldnames=["date", "text", "id"], dialect="excel")
            csvW.writeheader()
            csvW.writerows(results)


# =================================================================================================
# Main Routine
# =================================================================================================
if __name__ == "__main__":
    typer.run(main)
