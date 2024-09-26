from ihk_noten_berechnung import berechne_prozent
from ihk_noten_berechnung import ermittle_note
import pytest

def test_berechne_prozent__gesamt_min():
    #Arrange
    erreicht = 0
    gesamt = 6
    soll_wert = 0

    #Act
    ist_wert = berechne_prozent(erreicht, gesamt)

    #Assert
    assert ist_wert == soll_wert
    
def test_berechne_prozent__erreicht_min():
    #Arrange
    erreicht = 0
    gesamt = 6
    soll_wert = 0

    #Act
    ist_wert = berechne_prozent(erreicht, gesamt)

    #Assert
    assert ist_wert == soll_wert

def test_berechne_prozent__erreicht_equal_to_gesamt():
    #Arrange
    erreicht = 6
    gesamt = 6
    soll_wert = 100

    #Act
    ist_wert = berechne_prozent(erreicht, gesamt)

    #Assert
    assert ist_wert == soll_wert

def test_berechne_prozent__ergebnis_ist_gerundet():
    #Arrange
    erreicht = 15
    gesamt = 86
    soll_wert = 17

    #Act
    ist_wert = berechne_prozent(erreicht, gesamt)

    #Assert
    assert ist_wert == soll_wert

def test_berechne_prozent__gesamt_under_min():
    #Arrange
    erreicht = 0
    gesamt = 5

    #Act
    with pytest.raises(ValueError):  
        berechne_prozent(erreicht, gesamt)

def test_berechne_prozent__erreicht_under_min():
    #Arrange
    erreicht = -1
    gesamt = 6

    #Act
    with pytest.raises(ValueError):  
        berechne_prozent(erreicht, gesamt)

def test_berechne_prozent__erreicht_over_gesamt():
    #Arrange
    erreicht = 7
    gesamt = 6

    #Act
    with pytest.raises(ValueError):  
        berechne_prozent(erreicht, gesamt)        

def test_berechne_prozent__gesamt_text():
    #Arrange
    erreicht = 0
    gesamt = "text"

    #Act
    with pytest.raises(TypeError):  
        berechne_prozent(erreicht, gesamt)

def test_berechne_prozent__erreicht_text():
    #Arrange
    erreicht = "text"
    gesamt = 6

    #Act
    with pytest.raises(TypeError):  
        berechne_prozent(erreicht, gesamt)



def test_ermittle_note__prozent_ungenuegend_untere_grenze():
    #Arrange
    prozent = 0
    soll_wert = "ungenügend"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_ungenuegend_obere_grenze():
    #Arrange
    prozent = 29
    soll_wert = "ungenügend"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_mangelhaft_untere_grenze():
    #Arrange
    prozent = 30
    soll_wert = "mangelhaft"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_mangelhaft_obere_grenze():
    #Arrange
    prozent = 49
    soll_wert = "mangelhaft"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_ausreichend_untere_grenze():
    #Arrange
    prozent = 50
    soll_wert = "ausreichend"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_ausreichend_obere_grenze():
    #Arrange
    prozent = 66
    soll_wert = "ausreichend"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_befriedigend_untere_grenze():
    #Arrange
    prozent = 67
    soll_wert = "befriedigend"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_befriedigend_obere_grenze():
    #Arrange
    prozent = 80
    soll_wert = "befriedigend"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_gut_untere_grenze():
    #Arrange
    prozent = 81
    soll_wert = "gut"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_gut_obtere_grenze():
    #Arrange
    prozent = 91
    soll_wert = "gut"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_sehr_gut_untere_grenze():
    #Arrange
    prozent = 92
    soll_wert = "sehr gut"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_sehr_gut_obere_grenze():
    #Arrange
    prozent = 100
    soll_wert = "sehr gut"

    #Act
    ist_wert = ermittle_note(prozent)

    #Assert
    assert ist_wert == soll_wert

def test_ermittle_note__prozent_under_min():
    #Arrange
    prozent = -1

    #Act
    with pytest.raises(ValueError):  
        ermittle_note(prozent)

def test_ermittle_note__prozent_over_max():
    #Arrange
    prozent = 101

    #Act
    with pytest.raises(ValueError):  
        ermittle_note(prozent)

def test_ermittle_note__prozent_text():
    #Arrange
    prozent = "text"

    #Act
    with pytest.raises(TypeError):  
        ermittle_note(prozent)