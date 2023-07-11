""" blabla """


RATES = {
    "USDEUR" : 0.85,
    "GBPEUR" : 1.13,
    "CHFEUR" : 0.86,
    "EURGBP" : 0.885
}


def convert(amount, currency):
    """ blabla """

    if RATES.get( amount[1] + currency , "toto") is not "toto":
        amount_ = round(amount[0] * RATES.get( amount[1] + currency))
        return amount_
