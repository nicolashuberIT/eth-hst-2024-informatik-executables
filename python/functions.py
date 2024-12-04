#########################
# Wie in B7 gezeigt
#########################

global_var = 20                             # globale Variable

def my_function(number_a, number_b=2):
    global global_var                       # Schreibzugriff auf globale Variable erlauben
    global_var = number_b                   # globale Variable überschreiben
    return number_a                         # Rückgabewert

print(f"{my_function(5)}, {global_var}")    # >>> 5, 2 (Funktionsaufruf mit number_a = 5 und number_b mit default 2)

#########################
# ANHANG FÜR TESTS
#########################

def get_global_var():
    global global_var
    return global_var

def set_global_var(value):
    global global_var
    global_var = value