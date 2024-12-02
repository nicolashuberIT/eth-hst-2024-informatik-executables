from src.ExampleClass import global_var                               # global_var aus ExampleClass.py importieren
from src.ExampleClass import global_function                          # example_function aus ExampleClass.py importieren
from src.ExampleClass import ExampleClass as EC                       # ExampleClass aus ExampleClass.py importieren mit Alias

class_instance = EC("Ich bin eine Instanzvariable")                   # Instanzierung der Klasse
function_result: int = global_function(3, 4)                          # Zugriff auf globale Funktion
instance_result: str = class_instance.instance_method()               # Zugriff auf Instanzmethode
static_result: str = EC.static_method()                               # Zugriff auf statische Methode ohne Instanz der Klasse
class_result: str = EC.class_method()                                 # Zugriff auf Klasenmethode ohne Instanz der Klasse

print(f"Objektbeschreibung: {class_instance}")                        # Ausgabe der Objektbeschreibung (Aufruf der __str__ Methode)
print(f"Globale Variable: {global_var}")
print(f"Funktionsresultat: {function_result}")
print(f"Instanzmethodenresultat: {instance_result}")
print(f"Statische Methodenresultat: {static_result}")
print(f"Klassenmethodenresultat: {class_result}")
