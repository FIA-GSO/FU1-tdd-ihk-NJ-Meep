def berechne_prozent(erreichte_punkte:int, gesamte_punkte:int)->int:
    if(not isinstance(erreichte_punkte, int) and isinstance(gesamte_punkte, int)):
        raise TypeError
    if(erreichte_punkte < 0 or gesamte_punkte < 6 or erreichte_punkte > gesamte_punkte):
        raise ValueError
    prozent = 100 / gesamte_punkte * erreichte_punkte
    return int(prozent)

def ermittle_note(prozent:int)->str:
    if(not isinstance(prozent, int)):
        raise TypeError
    if(prozent < 0 or prozent > 100):
        raise ValueError
    
    if(prozent < 30):
        return "ungenügend"
    if(prozent < 50):
        return "mangelhaft"
    if(prozent < 67):
        return "ausreichend"
    if(prozent < 81):
        return "befriedigend"
    if(prozent < 92):
        return "gut"
    else:
        return "sehr gut"