from datetime import datetime


def calculate_champion_health(champion, date_string_intervals):
    '''
    calculate amount of health remained for a champion
    at the end of day

    @param champion - type of the champion (e.g. 'Wizard', 'human')
    @param date_string_intervals - list of date intervals strings
        when a champion passing the gate (e.g. ['XXXX-XX-XX XX:XX'])

    '''
    total_damage = 0
    for i, date_string in enumerate(date_string_intervals):
        date = datetime.strptime(date_string, "%Y-%m-%d %H:%M")
        try:
            date_next = datetime.strptime(date_string_intervals[i+1], "%Y-%m-%d %H:%M")
        except IndexError:
            date_next = date

        next_damage = calculate_damage_taken(date, champion)

        interval = (date_next - date).total_seconds()

        if (interval >= 3600 or i == len(date_string_intervals) -1):
            total_damage += next_damage

    return total_damage


def calculate_damage_taken(date, champion):
    if (holly_day(date) or invincible_champion(champion)):
        return 0
    # "Janna" demon of Wind spawned
    if (date.hour == 6 and date.minute >= 0 and date.minute <= 29):
        return 7
    # "Tiamat" goddess of Oceans spawned
    elif (date.hour == 6 and date.minute >= 30 and date.minute <= 59):
        return 18
    # "Mithra" goddess of sun spawned
    elif (date.hour == 7 and date.minute >= 0 and date.minute <= 59):
        return 25
    # "Warwick" God of war spawned
    elif (date.hour == 8 and date.minute >= 0 and date.minute <= 29):
        return 18
    # "Kalista" demon of agony spawned
    elif (date.hour >= 8 and date.hour <= 14 and date.minute >= 30 and date.minute <= 59):
        return 7
    # "Ahri" goddess of wisdom spawned
    elif (date.hour == 15 and date.minute >= 0 and date.minute <= 29):
        return 13
    # "Brand" god of fire spawned
    elif (date.hour == 15 and date.minute >= 0 or date.hour == 16 and date.minute <= 59):
        return 25
    # "Rumble" god of lightning spawned
    elif (date.hour == 17 and date.minute >= 0 and date.minute <= 59):
        return 18
    # "Skarner" the scorpion demon spawned
    elif (date.hour >= 18 and date.hour <= 19 and date.minute >= 0 and date.minute <= 59):
        return 7
    # "Luna" The goddess of the moon spawned
    elif (date.hour == 20 and date.minute <=59):
        return 13
    else:
        return 0

def holly_day(date):
    # Tuesday and Thursday are the only holly days
    if date.weekday() == 1 or date.weekday() == 3:
        return True
    else:
        return False

def invincible_champion(champion):
    if champion == 'Wizard':
        return True
    if champion == 'Spirit':
        return True
    if champion == 'Human' or champion == 'Giant' or champion == 'Vampire':
        return False

if __name__ == '__main__':
    # Champions initial health
    init_health = {'Human': 100, 'Wizard': 100, 'Spirit': 100, 'Giant': 150, 'Vampire': 110}
    date = ["2018-04-16 06:12", "2018-04-18 13:11", "2018-04-28 8:11"]
    for champion in init_health:
        total_damage = calculate_champion_health(champion, date)
        life_left = init_health[champion] - total_damage
        if life_left <= 0:
            print("{} is Dead".format(champion))
        else:
            print("{} has {}HP left ".format(champion, life_left))
