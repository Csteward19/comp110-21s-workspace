"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730404260"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    result = days_to_target(population, doses, doses_per_day, target)
    date: str = future_date(result)
    target1 = str(target)
    print('We will reach', target1 + '% vaccination', 'in', result, 'days, which falls on', date, '.')


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """The Original."""
    days_left = float(((population * (target / 100)) - (doses / 2)) / (doses_per_day / 2))
    rounded_days_left: int = round(days_left)
    return rounded_days_left
    
    
def future_date(time_left: int) -> str:
    """Gauging time till goal accomplished."""
    today: datetime = datetime.today()
    x_days: timedelta = timedelta(time_left)
    future: datetime = today + x_days
    f = future.strftime("%B %d, %Y")
    return f


if __name__ == "__main__":
    main()
