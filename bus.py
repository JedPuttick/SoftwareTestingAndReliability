def ticket_price(person):
    if person.age < 3 or person.age >= 65:
        return 0
    elif person.age < 19 and person.occupation == "student":
        return 2
    return 4
