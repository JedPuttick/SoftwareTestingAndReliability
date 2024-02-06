def check_speed(incident):
    fine = False
    court = False
    if incident.speed - incident.speed_limit > 0:
        fine = True
        if incident.speed - incident.speed_limit > 10:
            court = True
    return fine, court

