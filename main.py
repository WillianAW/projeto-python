from pyautocad import Autocad, APoint
from pyautocad import ACAD
import win32com.client
import pyautogui


import os

os.environ['PATH'] += ';D:\AutoCad\AutoCAD 2022\Acad.exe'

def main():
    # Open AutoCAD application
    acad = win32com.client.Dispatch("AutoCAD.Application.36")

    # Make AutoCAD window visible
    acad.Visible = True

    # Create a new document
    doc = acad.Documents.Add()

    # Create a new line object
    line = doc.ModelSpace.AddLine((0, 0), (10, 10))
    line()
    # Save and close the document
    doc.SaveAs("D:\AutoCad\arquivos\treinamento.dwg")
    doc.Close()

main()


