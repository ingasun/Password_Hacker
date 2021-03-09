hat_wieviel = int(input())
so_viel_gibt_es = int(input())
prozent_erreicht = (hat_wieviel * 100) // so_viel_gibt_es

if prozent_erreicht >= 90:
    print('A')
elif prozent_erreicht >= 80:
    print('B')
elif prozent_erreicht >= 70:
    print('C')
elif prozent_erreicht >= 60:
    print('D')
else:
    print('F')