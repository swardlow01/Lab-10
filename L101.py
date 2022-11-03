#the authors' names are Cadyn and Sarah
g = dict()
g = {"c": True, "a": "awesome", "d": 3, "y":3.14, "n": False}

def my_get_method(key, default):
    if key in g:
        print(g[key])
    else:
        print(default)

my_get_method("c", 7)
my_get_method("z", "cool")
my_get_method("d", "amazing")



#class = {"Holly": "Skrip", "Danielle": "Hongell", "Christina": "Shadid", "Julia": "Bub", "Adrianne": "Verstraete", "Ellen": "Kevin", "Julia": "Schutz", "Cody": "Brown", "Amanda": "Miloserny", "Catherine", "Doherty", "Kaylen": "Nyhuis", "Brenna": "Kieft", "Emily": "Rusch", "Britney": "Salazar", "Margaret":"Dunn", "Camryn": "Hurley", "Isabela": "Guthrie Beckstrom", "Cadyn": "Reger", "Haley": "Greene", "Sarah": "Wardlow", "Najmeh": "Salehi"}
