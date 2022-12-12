#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import time


def get_poezd():
    name = input("Название пункта назначения? ")
    no = input("Номер поезда? ")
    time_str = input("Введите время отправления (чч:мм)\n")
    t = time.asctime(time.strptime(time_str, "%H:%M"))[11:-5]
    return {
        "name": name,
        "no": no,
        "t": t,
    }


def list(poezd):
    line = "+-{}-+-{}-+-{}-+".format(
        "-" * 10,
        "-" * 20,
        "-" * 8,
    )
    print(line)
    print("| {:^10} | {:^20} | {:^8} |".format(" No ", "Название", "Время"))
    print(line)

    for idx, po in enumerate(poezd, 1):
        print(
            "| {:>10} | {:<20} | {"
            "} |".format(po.get("no", ""), po.get("name", ""), po.get("t", ""))
        )
    print(line)


def select(poezd):
    count = 0
    nom = input("Введите номер поезда: ")
    for idx, po in enumerate(poezd, 1):
        if po["no"] == str(nom):
            print(
                "Название пункта: ",
                po["name"],
                "\nВремя отправления: ",
                po.get("t", ""),
            )
            count += 1

    if count == 0:
        print("Поезда с таким номером нет")


def save_poezd(file_name, poezd):
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(poezd, fout, ensure_ascii=False, indent=4)


def load_poezd(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def help():
    print("Список команд:\n")
    print("add - добавить поезд;")
    print("list - вывести список поездов;")
    print("select <номер> - запросить поезд по номеру;")
    print("load - загрузить данные из файла;")
    print("save - сохранить данные в файл;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def main():
    poezd = []

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            po = get_poezd()
            poezd.append(po)
            if len(poezd) > 1:
                poezd.sort(key=lambda item: item.get("no", ""))

        elif command == "list":
            list(poezd)

        elif command == ("select"):
            select(poezd)

        elif command == "help":
            help()

        elif command.startswith("save "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            save_poezd(file_name, poezd)

        elif command.startswith("load "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            poezd = load_poezd(file_name)

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()
