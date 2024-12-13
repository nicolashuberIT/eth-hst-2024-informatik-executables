#########################
# Wie in B1 gezeigt
#########################

# Grundlegende Datentypen

is_boolean: bool = True  # Wahrheitswert
num_integer: int = 2  # Ganzzahl
num_float: float = 3.1  # Gleitkommazahl
txt_string: str = "x"  # Zeichenkette

# Datentyp testen

print(type(is_boolean))  # >>> 'bool'

# Datentyp explizit verändern

to_int = int(num_float)  # 3.1 wird zu 3
to_float = float(num_integer)  # 2 wird zu 2.0
to_str = str(num_float)  # 3.1 wird zu "3.1"

# String-Konkatenierung

txt_concat = txt_string + "y"  # wird zu xy

# Sequenzielle Datenstrukturen

is_list = [0, 0, 0]  # veränderbare Liste
is_tupel = (0, 0, 0)  # unveränderbare Liste (Tupel)
is_dictionary = {"gelb": 19, "grün": 20}  # assoziative Liste  # strings als keys

# Ausgabe

print(is_boolean)  # >>> True
print(num_integer)  # >>> 2
print(num_float)  # >>> 3.1
print(txt_string)  # >>> "x"

print(to_int)  # >>> 3
print(to_float)  # >>> 2.0
print(to_str)  # >>> "3.1"

print(txt_concat)  # >>> "xy"

print(is_list)  # >>> [0, 0, 0]
print(is_tupel)  # >>> (0, 0, 0)
print(is_dictionary)  # >>> {'gelb': 19, 'grün': 20}
