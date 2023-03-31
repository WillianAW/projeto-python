import pyautocad

def open_autocad():
    try:
        acad = pyautocad.Autocad(create_if_not_exists=True)
        print("AutoCAD opened successfully!")
    except pyautocad.exceptions.AutomationError as e:
        print("Failed to open AutoCAD:", e)
        acad()

open_autocad()