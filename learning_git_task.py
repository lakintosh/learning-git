
zakupy = {
    "Netto": ["Woda", "Ziemniaki", "Warzywa"],
    "Żabka": ["Pączki", "Kawa"]
    }

for key, value in zakupy.items():
    print("Idę do " + key.upper() + ", kupuję tu następujące rzeczy: " + str(value).upper())

sum = (len(zakupy["Netto"]) + len(zakupy["Żabka"]))

print("W sumie kupuję " + str(sum) + " produktów.")

#Zmiany dokonane przez innego programistę.

print("Teraz samodzielnie wykonuję zadanie. ")
print("Powtarzam zadanie.")
