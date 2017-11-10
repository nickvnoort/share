def standaardprijs(afstandkm):
    prijs = 0
    if afstandkm > 50:
        prijs = 15 + (afstandkm-50)*0.60
    elif afstandkm > 0:
        prijs = 0.80*afstandkm
    else:
        prijs = 0
    return prijs


def ritprijs(leeftijd, weekendrit, afstandkm):
    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = standaardprijs(afstandkm) * 0.65
        else:
            prijs = standaardprijs(afstandkm) * 0.60
    else:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = standaardprijs(afstandkm) * 0.70
        else:
            prijs = standaardprijs(afstandkm)

    return '€ ' + str(round(prijs,2))


print(ritprijs(eval(input("Leeftijd: ")), eval(input("Weekendrit? ")), eval(input("Afstand in km: "))))


