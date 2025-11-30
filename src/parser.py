import re

def parser(line: str) -> list:
    """
    Функция для парсинга команды
    :param line: строка команды в формате "<функция> <список> <пременная>"
    :return: список из команды, спика сортировки и пременной
    """
    func = re.search(r"^\S+\s*", line)
    line = re.sub(r"^\S+\s*","", line)
    number = re.findall(r"\s*\d+$|\s*\d+\.\d+$|\s*\S+\"$", line)
    line = re.sub(r"\s*\d+$|\s*\d+\.\d+$|\s*\S+\"$","", line)
    end_ls = [func.group().strip()]
    
    if len(line) != 0:
        line = line[1:-1]
        line = line.split(",")
        ls_sort = []
        for i in line:
            i = i.strip()
            try:
                a = float(i)
                if "." in i:
                    ls_sort.append(float(i))
                else:
                    ls_sort.append(int(i))
            except:
                if '"' in i:
                    i = i[1:-1]
                    ls_sort.append(i)
                elif i != '':
                    ls_sort.append(i)
        end_ls.append(ls_sort)
    if len(number)!= 0:
        if "." in number[0]:
            num = float(number[0].strip())
        elif '"' in number[0]:
            num = number[0].strip()[1:-1]
        else:
            num = int(number[0].strip())
        end_ls.append(num)

    return end_ls

