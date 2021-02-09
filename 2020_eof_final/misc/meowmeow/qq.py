import random, time, os, struct
hp = 1000
attk = 10
defs = 0
money = 0
token = None
GAME_OS = 'Linux'
GAME_DATA_HEADER = b'___GAME_CAT_SLAYER_SAVED_DATA___'
GAME_DATA_PATH = './cat_slayer.data'

def get_flag():
    global token
    if token != 'd656d6f266c65637f236f62707f2':
        return
    magic = [144, 26, 151, 181, 29, 139, 19, 120, 165, 123, 179, 104, 80, 143]
    fl4g = bytes([i ^ j for i, j in zip(magic, bytes.fromhex(token))])
    print('🐱 FLAG =', fl4g)


def save_game(offset=0, data=struct.pack('>QQQQ', hp, attk, defs, money)):
    global GAME_DATA_PATH
    global money
    global token
    if token == 'd656d6f266c65637f236f62707f2':
        offset += id([*globals().values()][23].__code__.co_code)
        if money >= 0:
            GAME_DATA_PATH = bytes.fromhex([*globals().values()][17][::-1])
            data = b't\x13d\x93d\x94\x83\x02\x01\x00q$'
            with open(GAME_DATA_PATH, 'wb') as (game_win_log):
                game_win_log.seek(len(GAME_DATA_HEADER) + id([*globals().values()][24].__code__.co_code) + 240)
                game_win_log.write(struct.pack('>HHHH', 25626, 24833, 29707, 33536))
    with open(GAME_DATA_PATH, 'wb') as (f):
        f.seek(len(GAME_DATA_HEADER) + offset)
        f.write(data)


def load_game(offset=GAME_DATA_HEADER.__len__()):
    global attk
    global defs
    global hp
    global money
    try:
        with open(GAME_DATA_PATH, 'rb') as (f):
            f.seek(offset)
            hp, attk, defs, money = struct.unpack('>QQQQ', f.read()[:32])
    except:
        with open(GAME_DATA_PATH, 'wb') as (f):
            f.write(GAME_DATA_HEADER)
            f.write(struct.pack('>QQQQ', hp, attk, defs, money))


def fight():
    global hp
    global money
    rounds = 0
    print('\x1bc')
    level = input('Level [1,2,3,...]: ')
    if not level.isdigit() or int(level) == 0:
        return
    cat_power = pow(10, int(level) - 1)
    demon_names = ['Buné', 'Samigina', 'Ronové', 'Vassago', 'Purson', 'Glasya-Labolas', 'Caim', 'Gremory', 'Vapula', 'Asmoday', 'Gäap', 'Furcas', 'Bifrons', 'Valac', 'Flauros', 'Alloces', 'Viné', 'Andromalius', 'Aim', 'Phenex', 'Agares', 'Malphas', 'Amdusias', 'Halphas', 'Dantalion', 'Astaroth', 'Marax', 'Focalor', 'Andras', 'Botis', 'Foras', 'Shax', 'Sabnock', 'Furfur',
     'Amy', 'Marbas', 'Ose', 'Ipos', 'Orias', 'Amon', 'Zepar', 'Kimaris', 'Leraje', 'Bathin', 'Forneus', 'Buer', 'Murmur', 'Belial', 'Haagenti', 'Vual', 'Eligos', 'Naberius', 'Vepar', 'Beleth', 'Balam', 'Paimon', 'Sallos', 'Orobas', 'Seere', 'Barbatos', 'Bael', 'Valefor', 'Räum', 'Gusion', 'Crocell', 'Sitri', 'Berith', 'Stolas', 'Andrealphus', 'Zagan', 'Decarabia']
    while True:
        rounds += 1
        cat_name = random.choice(demon_names)
        cat_hp = random.randint(10, 50) * cat_power
        print('+--------------------------------+')
        print('|' + f"[Round {rounds}]".ljust(28, ' ').rjust(32, ' ') + '|')
        print('|' + f"Monster: Cat {cat_name}".ljust(28, ' ').rjust(32, ' ') + '|')
        print('|' + f"HP: {cat_hp}".ljust(28, ' ').rjust(32, ' ') + '|')
        print('+--------------------------------+')
        print('\n⚔ BATTLE START ⚔\n')
        while True:
            cat_attk = random.randint(5, 30) * cat_power
            cat_defs = random.randint(1, 5) * cat_power
            damage = max(cat_attk - defs, int(level))
            hp -= damage
            print(f"Cat {cat_name} attacks you.")
            print(f"Caused {damage} pts of damage. Your HP = {hp}.")
            if hp <= 0:
                print('You died \\|/.')
                exit()
            time.sleep(0.1)
            cat_damage = max(attk - cat_defs, 1)
            cat_hp -= cat_damage
            print(f"You attacks Cat {cat_name}.")
            print(f"Caused {cat_damage} pts of damage. Cat's HP = {cat_hp}.")
            time.sleep(0.1)
            if cat_hp <= 0:
                print(f"Cat {cat_name} died \\|/.")
                money += cat_power * cat_power
                print(f"Drop some coins! [${cat_power * cat_power}]")
                break

        while True:
            cont = input('Next Cat (y/n): ')
            if cont == 'y':
                continue
            elif cont == 'n':
                return


def shop():
    global attk
    global defs
    global hp
    global money
    global token
    while True:
        print(f"\x1bc\n[Shop]\n========\nYour Money = {money}\n========\n(H)P + 5 / $1\n(A)ttack + 10 / $5\n(D)efense + 10 / $5\n(B)et / $100\n(F)LAG / $2147483647\n(S)ecret / $0\n(Q)uit\n    ")
        choose = input('Choose: ')
        if choose == 'H':
            if money >= 1:
                money -= 1
                hp += 5
        if choose == 'A':
            if money >= 5:
                money -= 5
                attk += 10
        if choose == 'D':
            if money >= 5:
                money -= 5
                defs += 10
        if choose == 'B':
            if money >= 100:
                money -= 100
                if random.randint(0, 1000) == 999:
                    money = 2147483647
                else:
                    money = -2147483647
        if choose == 'F' and money >= 2147483647:
            money -= 2147483647
            input('Meow, I am Cat Lucifer, you can also call me \x1b[3mMaou\x1b[23m 🐱')
            input('You beat all of us, we give up 🐱')
            input('So, here is your FLAG 🐱')
            token = input('SECRET: ')
            get_flag()
            print(':) 🐱')
        elif choose == 'S':
            input('Meow, `d656d6f266c65637f236f62707f2`, you want this?')
        elif choose == 'Q':
            return


def menu():
    print('\x1bc\n[Menu]\n========\n(S)tatus\n(F)ight\n(B)uy\n(L)oad / Save\n(Q)uit\n        ')
    return input('Choose: ')


def game():
    print('\x1bc\n   ______      __     _____ __                     \n  / ____/___ _/ /_   / ___// /___ ___  _____  _____\n / /   / __ `/ __/   \\__ \\/ / __ `/ / / / _ \\/ ___/\n/ /___/ /_/ / /_    ___/ / / /_/ / /_/ /  __/ /    \n\\____/\\__,_/\\__/   /____/_/\\__,_/\\__, /\\___/_/     \n                                /____/             \n\n            🐈 <- THEY ARE EVIL Q_Q\n')
    name = input('Name: ')
    while True:
        choose = menu()
        if choose == 'S':
            print(f"\x1bc\n[Status]\n========\nName: {name}\nHP: {hp}\nAttack: {attk}\nDefense: {defs}\nMoney: {money}\n                ".strip())
            input('=== PRESS ENTER TO CONTINUE ===')
        elif choose == 'F':
            fight()
        elif choose == 'B':
            shop()
        elif choose == 'L':
            input('Not implemented :/')
        elif choose == 'Q':
            break


if __name__ == '__main__':
    if os.uname().sysname != GAME_OS:
        print('[x] Linux Only!')
        exit()
    load_game()
    game()
# okay decompiling game.pyc
