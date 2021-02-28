"""A Buzzfeed Quiz To Determine What Game of Thrones House You Are."""
from random import randint

def main() -> None:
    """The initial inputs for quiz"""
    global whitewalker
    whitewalker = "\U0001F976"
    global wolf
    wolf = "\U0001F43A"
    global lion
    lion = "\U0001F981"
    global fish
    fish = "\U0001F41F"
    global kraken
    kraken = "\U0001F419"
    global rose
    rose = "\U0001F33A"
    global sun 
    sun = "\U00002600"
    global dragon
    dragon = "\U0001F409"
    greet()
    global points
    points = 0
    color()
    print(points)
    if points != 0:
        points = weather(points)
        print(points)
    if points != 0:
        points = weapon(points)
        print(points)
    print(total_points())

    

def greet() -> None:
    """Greetings young one."""
    global player
    player = str(input("Hello! So you'd like to know what Game of Thrones house you'd be, what is your name? "))
    return None
    

def color()-> None:
    """Asseses favorite color banner."""
    global points
    fave_color: str = str(input(player + ", what color is best: red, green, orange, blue, gold, silver, iron, or leave? "))
    if fave_color == "red":
        points = 5
    else:
        if fave_color == "green":
            points = 6
        else: 
            if fave_color == "orange":
                points = 7
            else:
                if fave_color == "blue":
                    points = 8
                else: 
                    if fave_color == "gold":
                        points = 9
                    else:
                        if fave_color == "silver":
                            points = 11
                        else: 
                            if fave_color == "iron":
                                points = 13
                            else:
                                if fave_color == "leave":
                                    points = 0



def weather(current_points: int)-> int:
    """Assesses weather preference."""
    best_weather: str = str(input(player + " ,what is the best climate?: cold, hot, warm, mild, or leave? "))
    if best_weather == "cold":
        return current_points * 143
    else:
        if best_weather == "hot":
            return current_points * 7
        else: 
            if best_weather == "warm":
                return current_points * 54
            else:
                if best_weather == "mild":
                    return current_points * 40
                else:
                    if best_weather == "leave":
                        return current_points * 0
    return 1000


def weapon(current_points: int) -> int:
    """Assesses participant's preffered weapon in combat."""
    best_weapon: str = str(input(player + ", what is your choice of weapon?: ship, sword, dagger, spear, dragon, or leave? "))
    if best_weapon == "ship":
        return current_points * 26
    else: 
        if best_weapon == "sword":
            return current_points * 264
        else:
            if best_weapon == "dagger":
                return current_points * 18
            else:
                if best_weapon == "spear":
                    return current_points * 21
                else: 
                    if best_weapon == "dragon":
                        return current_points * 20
                    else: 
                        if best_weapon == "leave":
                            return current_points * 0
    return 1000


def total_points() -> str:
    total = points
    if total == 0:
        return f"You are a Whitewalker. {whitewalker}"
    else:
        if total % 5 == 0:
            return f"You are from House Targaeryan. {dragon}"
        else:
            if total % 6 == 0:
                return f"You are from House Tyrell. {rose}"
            else:
                if total % 7 == 0:
                    return f"You are from House Martell. {sun}"
                else:
                    if total % 8 == 0:
                        return f"You are from House Tully. {fish}"
                    else:
                        if total % 9 == 0:
                            return f"You are from House Lannister. {lion}"
                        else:
                            if total % 11 == 0:
                                return f"You are from House Stark. {wolf}"
                            else:
                                if total % 13 == 0:
                                    return f"You are from House Greyjoy. {kraken}"
                                
                                
    return "hi"





















if __name__ == "__main__":
    main()