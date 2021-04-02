import datetime as dt


def before_the_concert(first, second):

    first = list(map(int, first.split('-')))
    second = list(map(int, second.split('-')))
    first = dt.date(first[0], first[1], first[2])
    second = dt.date(second[0], second[1], second[2])
    now = dt.datetime.now().date()

    if int(first.strftime("%w")) == 1 or int(first.strftime("%w")) == 3:
        first += dt.timedelta(days=1)
    if int(second.strftime("%w")) == 1 or int(second.strftime("%w")) == 3:
        second += dt.timedelta(days=1)

    return int((first - now).days), int((second - now).days)
