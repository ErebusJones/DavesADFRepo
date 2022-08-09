from unicodedata import name


def hi(person):
    return f"Hi, {person['name']}"


def bye(person):
    return f"Bye, {person['name']}"


def how_are_you(person):
    return f"How are you {person['name']}?"