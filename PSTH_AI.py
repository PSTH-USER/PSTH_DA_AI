import datetime, random

print("There is a {}% chance that the PSTH DA is on {}".format(\
        random.getrandbits(64) % 100 ,\
        datetime.date.today() + datetime.timedelta(days=1)))
