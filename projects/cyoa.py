"""A Buzzfeed Quiz To Determine What Game of Thrones House You Are."""
from random import randint

def main() -> None:
    """The initial inputs for quiz"""
    global points
    points: int = color() * weather() * weapon()
    print(greet())
    

def greet() -> None:
    """Greetings young one."""
    player: str = str(input("Hello! So you'd like to know what Game of Thrones house you'd be, what is your name?"))
    return None
    

def color(favorite: int)-> int:
    """Asseses favorite color banner."""
    fave_color: str = str(input("What is best: red, green, orange, blue, gold, silver, iron, or leave?"))
    if fave_color == "red":
        return 5
    else:
        if fave_color == "green":
            return 6
        else: 
            if fave_color == "orange":
                return 7
            else:
                if fave_color == "blue":
                    return 8
                else: 
                    if fave_color == "gold":
                        return 9
                    else:
                        if fave_color == "silver":
                            return 11
                        else: 
                            if fave_color == "iron":
                                return 13
                            else:
                                if fave_color == "leave":
                                    return 0
    return favorite


def weather(climate: int)-> int:
    """Assesses weather preference."""
    best_weather: str = str(input("What is the best climate?: cold, hot, warm, mild, or leave"))
    if best_weather == "cold":
        return 143
    else:
        if best_weather == "hot":
            return 7
        else: 
            if best_weather == "warm":
                return 54
            else:
                if best_weather == "mild":
                    return 40
                else:
                    if best_weather == "leave":
                        return 0
    return climate


def weapon(choice: int) -> int:
    """Assesses participant's preffered weapon in combat."""
    best_weapon: str = str(input("What is your choice of weapon?: ship, sword, dagger, spear, dragon, or leave"))
    if best_weapon == "ship":
        return 26
    else: 
        if best_weapon == "sword":
            return 264
        else:
            if best_weapon == "dagger":
                return 18
            else:
                if best_weapon == "spear":
                    return 21
                else: 
                    if best_weapon == "dragon":
                        return 20
                    else: 
                        if best_weapon == "leave":
                            return 0
    return choice




















if __name__ == "__main__":
    main()