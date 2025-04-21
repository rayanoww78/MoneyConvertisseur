import requests
def moneyConverter(Money,devise,devise_cible):
    url = requests.get(f"https://v6.exchangerate-api.com/v6/9c6608f162fe1db6fc281eec/latest/{devise}")
    TC = url.json()
    taux = TC['conversion_rates'][devise_cible]
    if taux is not None:
        argent = Money * taux
    else:
        return("La devise que vous avez écrit(e) n'existe pas")

    return argent

"""url = requests.get("https://v6.exchangerate-api.com/v6/9c6608f162fe1db6fc281eec/latest/USD")
r = url.json()
t = r['conversion_rates']["AMD"]
m = 15*t
print(m)
"""
print(moneyConverter(10,"EUR","USD"))