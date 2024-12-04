# Definition einer globalen Variable
global_var: int = 42

# Definition einer Funktion
def global_function(param1: int, param2: int) -> int:
    return param1 + param2

# Definition einer Klasse
class ExampleClass:
    # Klassenvariable, die für alle Instanzen der Klasse gleich ist
    class_var: str = "Ich bin eine Klassenvariable"

    # Konstruktor-Methode, die beim Erstellen einer Instanz aufgerufen wird
    def __init__(self, instance_var: str) -> None:
        # Instanzvariable, die spezifisch für diese Instanz ist
        self.instance_var: str = instance_var

    # __str__ Methode, die eine lesbare Darstellung des Objekts zurückgibt
    def __str__(self) -> str:
        # Ausgabe von print(), f-strings und str() rufen diese Methode auf (Ausgabe wird angepasst)
        return f"ExampleClass with instance_var: {self.instance_var}"

    # Instanzmethode, die auf die Instanzvariable zugreift
    def instance_method(self) -> str:
        return self.instance_var

    # Statische Methode, die keine Instanz- oder Klassenvariablen benötigt
    @staticmethod  # Decorator für statische Methoden, Methode somit zugänglich ohne Instanz
    def static_method() -> str:
        return "Ich bin eine statische Methode"

    # Klassenmethode, die auf Klassenvariablen zugreift
    @classmethod  # Decorator für Klassenmethoden, Methode somit zugänglich ohne Instanz
    def class_method(cls) -> str: # cls ist Konvention für Klassenobjekt, geg. durch Decorator
        return cls.class_var