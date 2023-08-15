import PyPDF2
import os
import time

mesclar = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print("Aqui está sua lista de arquivos.")
print(lista_arquivos)
time.sleep(2)
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        mesclar.append(f"arquivos/{arquivo}")

print("=-" * 20)
print("O seu arquivo PDF foi mesclado!")
mesclar.write("PDF Finalizado.pdf")