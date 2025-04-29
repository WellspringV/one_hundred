

import csv


def figny(row, pull_ups, squats_1, push_ups, squats_2):
        pull_ups_ = int(row.get(pull_ups))*4
        squats_1_ = int(row.get(squats_1))*4
        push_ups_ = int(row.get(push_ups))*4
        squats_2_ = int(row.get(squats_2))*4
        return pull_ups_, squats_1_, push_ups_, squats_2_



def dict_sotka_stat(name_file):
    users_stat = []
    with open(name_file) as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            users_stat.append(row)
        return users_stat
    

def sum_sotka_stat(dict_stat):
    sum_stat = {}
    for row in dict_stat:
        username = row['username']
        if username not in sum_stat:
            sum_stat[username] = [0, 0, 0, 0]
        pull_ups, squats_1, push_ups, squats_2 = figny(row, 'pull_ups', 'squats_1', 'push_ups', 'squats_2')
        sum_stat[username][0] += pull_ups
       
        sum_stat[username][1] += squats_1
        sum_stat[username][2] += push_ups
        sum_stat[username][3] += squats_2
    return sum_stat

def render_stat_of_the_day(dict_stat):
    strok = '-' * 70
    sum_stat = sum_sotka_stat(dict_stat)
    TEMPLATE = [
        f"{'Дата':^6}|{'Денис':^20}|{'Виталик':^20}|{'Тима':^20}|\n",
    ]
    stat = {}
    for row in dict_stat:
        username = row['username']
        pull_ups, squats_1, push_ups, squats_2 = figny(row, 'pull_ups', 'squats_1', 'push_ups', 'squats_2')
        stat.update({username: [pull_ups, squats_1, push_ups, squats_2]})
        if len(stat) == 3:
            date = row['date']
            Denerk = str(stat['Denerk'])[1:-1]
            wellspringweather = str(stat['wellspringweather'])
            Kron3583 = str(stat['Kron3583'])[1:-1]
            TEMPLATE.append(f"{date:^6}|{Denerk:^20}|{wellspringweather:^20}|{Kron3583:^20}|\n")
            stat = {}
    Denerk = str(sum_stat['Denerk'])[1:-1]
    wellspringweather = str(sum_stat['wellspringweather'])
    Kron3583 = str(sum_stat['Kron3583'])[1:-1]
    TEMPLATE.append(f"{'Всего':^6}|{Denerk:^20}|{wellspringweather:^20}|{Kron3583:^20}|\n")
    return f'{strok}\n'.join(TEMPLATE)
    
    
print(render_stat_of_the_day(dict_sotka_stat('stat.csv')))
