import win32com.client

import os

os.environ['PATH'] += ';D:\AutoCad\AutoCAD 2022\Acad.exe'


def main():
    acad = win32com.client.Dispatch("AutoCAD.Application.27")
    doc = acad.Documents.Open("D:\AutoCad\Arquivos\Teste1.dwg")


    modelspace = doc.ModelSpacez


    line = modelspace.AddLine((0, 0), (10, 10))


    line.color = 2


    doc.Save()
    doc.Close()
