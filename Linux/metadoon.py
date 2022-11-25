#encoding-utf-8
#importando bibliotecas
import os
from typing import Any
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
#importando widgets da biblioteca tkinter:
from tkinter import *
from tkinter import filedialog, Frame
from tkinter import ttk
from tkinter import messagebox
#setando variavel para o caminho do arquivo atual
nome_diretorio = os.path.dirname(__file__)

messagebox.showinfo("BEM VINDO AO METADDOON",
                    "Este é um pipeline chamado Metadoon, voltado para tratamento de dados de 16S. \nO metadoon conta com uma interface grafica.\n Aproveite! ")
# criando listas de DataBases para exibição no comboboxes:
_LIST_db = ["RDP training set v18 (21k seqs.). RDP license terms.",
            "RDP training set v16 (13k seqs.). RDP license terms.",
            "RDP training set with species names;(not recommended);(can species be predicted?).",
            "Greengenes v13.5 (1.2M seqs.). Greengenes license terms. (not recommended)",
            "SILVA v123 (1.6M seqs.). SILVA license terms. (not recommended)",
            "SILVA v123 LTP named isolate subset (12k seqs.) .SILVA license terms", "Usar um banco de dados proprio..."]
#Padrões de definição de exibição
metainfo = Tk()
monitor_height = metainfo.winfo_screenheight()
monitor_width = metainfo.winfo_screenwidth()
pipeH = round(monitor_height * 80/100)
pipeW = round(monitor_width * 40/100)
metainfo.title("Metadoon")
metainfo.geometry(f"{pipeW}x{pipeH}")
metainfo.resizable(False, False)
metainfo.configure(background="gray")
timeday = datetime.now().strftime('%d-%m-%y %H:%M:%S')
# icone do programa
metainfo.iconphoto(False, PhotoImage(file=fr'{nome_diretorio}/_icon.png'))
# criando frames para posicionamento de widgets:
frame = Frame(metainfo, borderwidth=2, relief="solid")
frame.pack(fill = BOTH, expand = True)
# frames secundarias
# 1
l_frame1 = Frame(metainfo, borderwidth=1, relief="raised")
l_frame1.pack(fill = BOTH, expand = True)
# 2
l_frame2 = Frame(metainfo, borderwidth=1, relief="raised")
l_frame2.pack(fill = BOTH, expand = True)
# 3
l_frame3 = Frame(metainfo, borderwidth=1, relief="raised")
l_frame3.pack(fill = BOTH, expand = True)
# 4
l_frame4 = Frame(metainfo, borderwidth=1, relief="raised")
l_frame4.pack(fill = BOTH, expand = True)
# 5
l_frame5 = Frame(metainfo, borderwidth=1, relief="raised")
l_frame5.pack(fill = BOTH, expand = True)
# 6
l_frame6 = Frame(metainfo, borderwidth=1, relief="raised")
l_frame6.pack(fill = BOTH, expand = True)

# crianco comboboxes
CB_DB = ttk.Combobox(l_frame6, values=_LIST_db)
CB_DB.place(x=200, y=20, width=390, height=20)
# caixas de dialogos:
# 1
en_miss = Entry(l_frame1, bd=2, font=("Calibri", 9), justify=CENTER)
en_miss.place(width=50, height=20, x=325, y=0)
# 2
en_pctid = Entry(l_frame1, bd=2, font=("Calibri", 9), justify=CENTER)
en_pctid.place(width=50, height=20, x=550, y=0)
# 3
en_MEE = Entry(l_frame2, bd=2, font=("Calibri", 9), justify=CENTER)
en_MEE.place(width=50, height=20, x=425, y=0)
# 4
en_name_project = Entry(frame, bd=2, font=("Calibri", 9), justify=CENTER)
en_name_project.place(width=250, height=30, x=425, y=50)
name: list[Any] = []
# objetos/dicionarios
filed = StringVar()
filed.set("Diretorio de trabalho atual...")


# funções:
#função para setar nome de arquivos de saída
def atach():
    name_ = en_name_project.get()
    name.append(name_)
    messagebox.showinfo("!", "Esse sera o nome da pasta com seus arquivos de saida...")
    print(name)


# funções visualizadoras
def vis1():
    os.system(fr"gio open {nome_diretorio}/Metarquivos/Mesclados/_merged.fq")


def vis2():
    os.system(fr"gio open {nome_diretorio}/Metarquivos/Filtro_de_qualidade/_filtered.fa")


def vis3():
    os.system(fr"gio open {nome_diretorio}/Metarquivos/Leituras_unicas/_uniques.fa")


def vis4():
    os.system(fr"gio open {nome_diretorio}/Metarquivos/Geracao_de_otus/_otus.fa")


def vis5():
    os.system(fr"gio open {nome_diretorio}/Metarquivos/Tabela_de_OTU/_otutable.tsv")


def vis6():
    os.system(fr"gio open {nome_diretorio}/Metarquivos/XVI_S_DB/_taxonomy.csv")


# funcoes de execucao:
#BASH-PYTHON;
def sel():
    global filed_
    filed.set(filedialog.askdirectory())
    filed_ = filed.get()
    print(filed_)
    os.system(fr'cp {filed_}/*.fastq {nome_diretorio}/Sample ')
    messagebox.showinfo("METADDOON:",
                        "Essa é a pasta de onde seus arquivos fasta/fafstq foram retirados...\n Posteriormente você podera salvar seus arquivos nela...")

#FUNCOES PARA EXECUCAO DE COMANDOS USEARCH

def merge():
    progress1['value'] += 5
    progress1['value'] += 5
    n1 = en_miss.get()
    progress1['value'] += 5
    progress1['value'] += 5
    n2 = en_pctid.get()
    progress1['value'] += 50
    progress1['value'] += 5
    os.system(
        fr'./_Usearch -fastq_mergepairs ./Sample/*_R1*.fastq -fastq_maxdiffs {n1} -fastq_pctid {n2} -fastqout ./Metarquivos/Mesclados/_merged.fq -relabel @')
    progress1['value'] += 5
    progress1['value'] += 5
    progress1['value'] += 5
    progress1['value'] += 5
    progress1['value'] += 5
    messagebox.showinfo("METADDOON:", "Arquivos fastq/fasta mesclados com sucesso...")


def quali():
    n1 = en_MEE.get()
    progress2['value'] += 10
    progress2['value'] += 10
    progress2['value'] += 10
    os.system \
        (fr'./_Usearch -fastq_filter ./Metarquivos/Mesclados/_merged.fq -fastq_maxee {n1} -fastaout ./Metarquivos/Filtro_de_qualidade/_filtered.fa')

    progress2['value'] += 10
    progress2['value'] += 10
    progress2['value'] += 10
    progress2['value'] += 10
    progress2['value'] += 10
    progress2['value'] += 10
    progress2['value'] += 10
    progress2['value'] += 10
    messagebox.showinfo("METADDOON:", "Arquivos filtrados com sucesso...")


def uniq():
    os.system \
        (fr'./_Usearch -fastx_uniques ./Metarquivos/Filtro_de_qualidade/_filtered.fa -fastaout ./Metarquivos/Leituras_unicas/_uniques.fa -relabel uniq -sizeout')
    progress3['value'] += 10
    progress3['value'] += 10
    progress3['value'] += 10
    progress3['value'] += 10
    progress3['value'] += 10
    progress3['value'] += 10
    progress3['value'] += 5
    progress3['value'] += 5
    progress3['value'] += 10
    progress3['value'] += 10
    progress3['value'] += 10
    messagebox.showinfo("METADDOON:", "Arquivo de sequencias unicas armazenado com sucesso...")


def otus():
    os.system \
        (fr'./_Usearch -cluster_otus ./Metarquivos/Leituras_unicas/_uniques.fa -minsize 2 -otus ./Metarquivos/Geracao_de_otus/_otus.fa -relabel otu')
    progress4['value'] += 10
    progress4['value'] += 10
    progress4['value'] += 10
    progress4['value'] += 10
    progress4['value'] += 10
    progress4['value'] += 10
    progress4['value'] += 10
    progress4['value'] += 10
    progress4['value'] += 10
    progress4['value'] += 10
    messagebox.showinfo("METADDOON:", "Verificação de OTUS feita com sucesso...")


def otutable():
    os.system \
        (fr'./_Usearch -usearch_global ./Metarquivos/Mesclados/_merged.fq  -db ./Metarquivos/Geracao_de_otus/_otus.fa -strand plus -id 0.97 -otutabout ./Metarquivos/Tabela_de_OTU/_otutable.txt')
    progress5['value'] += 10
    progress5['value'] += 10
    progress5['value'] += 10
    os.system(
        "cd ./Metarquivos/Tabela_de_OTU/ | cp ./Metarquivos/Tabela_de_OTU/_otutable.txt ./Metarquivos/Tabela_de_OTU/_otutable.tsv")
    progress5['value'] += 10
    progress5['value'] += 10
    progress5['value'] += 10
    progress5['value'] += 10
    os.system(
        "cd ./Metarquivos/Alpha D/ | cp ./Metarquivos/Alpha D/alpha_chao_BP.txt ./Metarquivos/Alpha D/alpha_chao_BP.tsv")
    progress5['value'] += 10
    os.system("cd ./Metarquivos/Alpha D/ | cp ./Metarquivos/Alpha D/alpha.txt ./Metarquivos/Alpha D/alpha.tsv")
    progress5['value'] += 10
    os.system(fr"Rscript {nome_diretorio}/CHAO1.R")
    os.system(fr"Rscript {nome_diretorio}/SHANNON.R")
    os.system(fr"Rscript {nome_diretorio}/Ace.R")
    os.system(fr"Rscript {nome_diretorio}/SIMPSON.R")
    os.system(fr"Rscript {nome_diretorio}/RIQUEZA.R")
    os.system(fr"Rscript {nome_diretorio}/INV_SIMPSON.R")
    os.system(fr"Rscript {nome_diretorio}/taxax.R")
    progress5['value'] += 10
    messagebox.showinfo("METADDOON:", "Tabela de Otus gerada com sucesso...")


def otu16s():
    xvis_db = CB_DB.get()
    if xvis_db == _LIST_db[0]:
        os.system(
            fr'./_Usearch -nbc_tax ./Metarquivos/Geracao_de_otus/_otus.fa -db ./REF_DATA/1.fa -strand plus -tabbedout ./Metarquivos/XVI_S_DB/_taxonomy.csv')
    if xvis_db == _LIST_db[1]:
        os.system(
            fr'./_Usearch -nbc_tax ./Metarquivos/Geracao_de_otus/_otus.fa -db ./REF_DATA/2.fa -strand plus -tabbedout ./Metarquivos/XVI_S_DB/_taxonomy.csv')
    if xvis_db == _LIST_db[2]:
        os.system(
            fr'./_Usearch -nbc_tax ./Metarquivos/Geracao_de_otus/_otus.fa -db ./REF_DATA/3.fa -strand plus -tabbedout ./Metarquivos/XVI_S_DB/_taxonomy.csv')
    if xvis_db == _LIST_db[3]:
        os.system(
            fr'./_Usearch -nbc_tax ./Metarquivos/Geracao_de_otus/_otus.fa -db ./REF_DATA/4.fa -strand plus -tabbedout ./Metarquivos/XVI_S_DB/_taxonomy.csv')
    if xvis_db == _LIST_db[4]:
        os.system(
            fr'./_Usearch -nbc_tax ./Metarquivos/Geracao_de_otus/_otus.fa -db ./REF_DATA/5.fa -strand plus -tabbedout ./Metarquivos/XVI_S_DB/_taxonomy.csv')
    if xvis_db == _LIST_db[5]:
        os.system(
            fr'./_Usearch -nbc_tax ./Metarquivos/Geracao_de_otus/_otus.fa -db ./REF_DATA/6.fa -strand plus -tabbedout ./Metarquivos/XVI_S_DB/_taxonomy.csv')
    if xvis_db == _LIST_db[6]:
        db_file_path = filedialog.askopenfilename()
        os.system(
            fr'./_Usearch -nbc_tax ./Metarquivos/Geracao_de_otus/_otus.fa -db {db_file_path} -strand plus -tabbedout ./Metarquivos/XVI_S_DB/_taxonomy.csv')
    progress6['value'] += 10

    progress6['value'] += 10
    progress6['value'] += 10
    progress6['value'] += 10
    progress6['value'] += 10
    progress6['value'] += 50
    messagebox.showinfo("METADDOON:", "Base de dados verificada...")



# Organizando os dados:
REPORT_FINAL = []
def drawn():
    # objetos para dados:
    ace = fr'{nome_diretorio}/Metarquivos/Graficos/ace.png'
    chao = fr'{nome_diretorio}/Metarquivos/Graficos/CHAO.png'
    inv_simp = fr'{nome_diretorio}/Metarquivos/Graficos/INV_SIMPSON.png'
    simpson = fr'{nome_diretorio}/Metarquivos/Graficos/Simpson.png'
    ric = fr'{nome_diretorio}/Metarquivos/Graficos/RIQUEZA.png'
    shannon = fr'{nome_diretorio}/Metarquivos/Graficos/Shannon.png'
    tax = fr'{nome_diretorio}/Metarquivos/Graficos/TAX.png'
    #reproduzindo report final (EN)
    cnv = canvas.Canvas(fr"{nome_diretorio}/Report/{name}_Final_Report_EN.pdf", pagesize=A4)
    cnv.drawString(10, 830, f'Data/Time: {timeday}')
    cnv.drawString(10, 810, f'Final report:')
    cnv.drawString(400, 830, f'Richness')
    cnv.drawImage(ric, 320, 730, width=200, height=100)
    cnv.drawString(400, 722, f'Shannon')
    cnv.drawImage(shannon, 320, 620, width=200, height=100)
    cnv.drawString(300, 610, f'\t Shannon - Species diversity is usually ')
    cnv.drawString(300, 595, f'described by an index, such as Shannon’s Index(H).')
    cnv.drawString(300, 580, f'The greater the Shannon indices, the higher')
    cnv.drawString(300, 565, f'the diversity of the sample.')
    cnv.drawString(10, 785, f'\t Richness - Species richness is simply')
    cnv.drawString(10, 770, f'the number of species in a community.')
    cnv.drawString(10, 755, f'Species diversity is more complex, and')
    cnv.drawString(10, 740, f'includes a measure of the number of ')
    cnv.drawString(10, 725, f'species in a community and a measure')
    cnv.drawString(10, 710, f'of the abundance of each species.')
    cnv.drawString(10, 695, f'\t Diversity - It is important to consider')
    cnv.drawString(10, 680, f'that just a greater number of species does not')
    cnv.drawString(10, 665, f'mean that an environment has the greatest ')
    cnv.drawString(10, 650, f'diversity, as it is necessary to consider')
    cnv.drawString(10, 635, f' the taxonomy. Example:')
    cnv.drawString(10, 620, f'Environment A has 5 species of the same genus,')
    cnv.drawString(10, 605, f'while environment B has 4 species of different')
    cnv.drawString(10, 590, f'phyla. Environment B is more diverse and ')
    cnv.drawString(10, 575, f'environment A has greater richness.')
    cnv.drawString(0, 560,  f'-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
    cnv.drawString(150, 545, f'Ace')
    cnv.drawImage(ace, 30, 420, width=250, height=120)
    cnv.drawString(150, 405, f'Chao1')
    cnv.drawImage(chao,30, 280, width=250, height=120)
    cnv.drawString(440, 545, f'Simpson')
    cnv.drawImage(simpson, 320, 420, width=250, height=120)
    cnv.drawString(420, 405, f'Inverse Simpson')
    cnv.drawImage(inv_simp, 320, 280, width=250, height=120)
    cnv.drawString(10, 270, f'\t Ace - The greater the Ace index, the higher the expected species richness of the microbiome')
    cnv.drawString(10, 255, f'\t Chao - The greater the Chao1 index, the higher the expected species richness of the microbiome')
    cnv.drawString(10, 240, f'\t Simpson - The smaller the Simpson index, the higher the diversity of the sample.')
    cnv.drawString(10, 225, f'\t Inv.Simpson - The greater the index, the higher the diversity of the microbiome.')
    cnv.drawString(495, 0, f'Metadoon-Pipeline')
    cnv.save()
    #reproduzindo report final (PT-BR)
    cnv1 = canvas.Canvas(fr"{nome_diretorio}/Report/{name}_Report_Final_PT.pdf", pagesize=A4)
    cnv1.drawString(10, 830, f'Data/Hora: {timeday}')
    cnv1.drawString(10, 810, f'Report final:')
    cnv1.drawString(400, 830, f'Riqueza')
    cnv1.drawImage(ric, 320, 730, width=200, height=100)
    cnv1.drawString(400, 722, f'Shannon')
    cnv1.drawImage(shannon, 320, 620, width=200, height=100)
    cnv1.drawString(300, 610, f'\t Shannon - A diversidade de espécies é geralmente ')
    cnv1.drawString(300, 595, f'descrita por um índice, como o Índice (H) de Shannon')
    cnv1.drawString(300, 580, f'Quanto maiores os índices de Shannon')
    cnv1.drawString(300, 565, f',maior a diversidade da amostra.')
    cnv1.drawString(10, 785, f'\t Riqueza - A riqueza de espécies é simplesmente')
    cnv1.drawString(10, 770, f'o número de espécies em uma comunidade.')
    cnv1.drawString(10, 755, f'A diversidade de espécies é mais complexa e ')
    cnv1.drawString(10, 740, f'inclui uma medida do número de')
    cnv1.drawString(10, 725, f'espécies em uma comunidade e a medida ')
    cnv1.drawString(10, 710, f'da abundância de cada espécie.')
    cnv1.drawString(10, 695, f'\t Diversidade - É importante considerar ')
    cnv1.drawString(10, 680, f'que apenas um número maior de espécies não')
    cnv1.drawString(10, 665, f'significa que um ambiente tenha a maior')
    cnv1.drawString(10, 650, f'diversidade, pois é necessário considerar')
    cnv1.drawString(10, 635, f'a taxonomia. Exemplo: ')
    cnv1.drawString(10, 620, f'O Ambiente A possui 5 espécies do mesmo gênero,')
    cnv1.drawString(10, 605, f'enquanto o Ambiente B possui 4 espécies de filos ')
    cnv1.drawString(10, 590, f' diferentes. O Ambiente B é mais diversificado e o ')
    cnv1.drawString(10, 575, f'Ambiente A tem maior riqueza.')
    cnv1.drawString(0, 560,  f'-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
    cnv1.drawString(150, 545, f'Ace')
    cnv1.drawImage(ace, 30, 420, width=250, height=120)
    cnv1.drawString(150, 405, f'Chao1')
    cnv1.drawImage(chao,30, 280, width=250, height=120)
    cnv1.drawString(440, 545, f'Simpson')
    cnv1.drawImage(simpson, 320, 420, width=250, height=120)
    cnv1.drawString(420, 405, f'Inverse Simpson')
    cnv1.drawImage(inv_simp, 320, 280, width=250, height=120)
    cnv1.drawString(10, 270, f'\t Ace - Quanto maior o índice Ace, maior a riqueza de espécies esperada do microbioma.')
    cnv1.drawString(10, 255, f'\t Chao - Quanto maior o índices de Chao1, maior a riqueza de espécies esperada do microbioma.')
    cnv1.drawString(10, 240, f'\t Simpson - Quanto menor o índice Simpson, maior a diversidade da amostra.')
    cnv1.drawString(10, 225, f'\t Inv.Simpson - Quanto maior o índice, maior a diversidade da amostra.')
    cnv1.drawString(495, 0, f'Metadoon-Pipeline')
    cnv1.save()
    # reproduzindo GRAFICO DE FILOS
    cnv2 = canvas.Canvas(fr"{nome_diretorio}/Report/{name}_TAX_OTUs.pdf", pagesize=A4)
    cnv2.drawString(10, 830, f'Data/Hora-Date/Time: {timeday}')
    cnv2.drawString(10, 810, f'Report final:')
    cnv2.drawString(400, 830, f'TAX:')
    cnv2.drawImage(tax, 0, 10, width=625, height=850)
    cnv2.save()
    messagebox.showinfo("!", "Arquivo gerado com sucesso")
    return 0
def abrir_report_final():
    os.system(fr'open {nome_diretorio}/Report/{name}_Report_Final_PT.pdf')
    os.system(fr'open {nome_diretorio}/Report/{name}_Final_Report_EN.pdf')
    os.system(fr'open {nome_diretorio}/Report/{name}_TAX_OTUs.pdf')
def salvar_final():
    path_final_salvamento = filedialog.askdirectory()
    os.system(fr'mkdir {path_final_salvamento}/{name}')
    os.system(fr'cp -r {nome_diretorio}/Metarquivos {path_final_salvamento}/{name}')
    os.system(fr'cp -r {nome_diretorio}/Report {path_final_salvamento}/{name}')

    messagebox.showinfo("✔✔✔", "Se você não abortou o processo, seus arquivos foram salvos em uma pasta e essa pasta foi copiada para o diretorio que você especificou.")
# botões de execucao de funcoes
# 1
btn1 = Button(frame, text="Selecionar Pasta", command=sel, borderwidth=2, relief="raised")
btn1.place(x=0, y=10)
# 2
btn2 = Button(l_frame1, text="Mesclar Pares", command=merge, borderwidth=2, relief="raised")
btn2.place(x=0, y=0)
# 3
btn3 = Button(l_frame2, text="Filtragem de Qualidade", command=quali, borderwidth=2, relief="raised")
btn3.place(x=0, y=0)
# 4
btn4 = Button(l_frame3, text="Busca de Leituras Unicas", command=uniq, borderwidth=2, relief="raised")
btn4.place(x=0, y=0)
# 5
btn5 = Button(l_frame4, text="Agrupamento de OTU's", command=otus, borderwidth=2, relief="raised")
btn5.place(x=0, y=0)
# 6
btn6 = Button(l_frame5, text="Tabela de OTU's", command=otutable, borderwidth=2, relief="raised")
btn6.place(x=0, y=0)
# 7
btn7 = Button(l_frame6, text="Alinhamento com 16s-DB", command=otu16s, borderwidth=2, relief="raised")
btn7.place(x=0, y=0, width=200, height=50)
# 8
btn8 = Button(frame, text="Associar", command=atach, borderwidth=2, relief="raised")
btn8.place(x=590, y=75)

# label
# 1
lab_banco = Label(l_frame6, text="Banco de Dados:")
lab_banco.place(x=200, y=5, width="", height=10)
# 2
lab_missmatches = Label(l_frame1, text="Missmatches no alinhamento:")
lab_missmatches.place(x=120, y=0)
# 3
lab_pctid = Label(l_frame1, text="Minimo %id do alinhamento:")
lab_pctid.place(x=375, y=0)
# 4
lab_maxe = Label(l_frame2, text="Intervalo Maximo de Erro Esperado:")
lab_maxe.place(x=190, y=0)

# botão visualizar
# 1 mesclar
btn_vis1 = Button(l_frame1, text="Visualizar", command=vis1, borderwidth=2, relief="raised")
btn_vis1.place(x=625, y=40)
# 2 filtragem
btn_vis2 = Button(l_frame2, text="Visualizar", command=vis2, borderwidth=2, relief="raised")
btn_vis2.place(x=625, y=40)
# 3 busca de leituras unicas
btn_vis3 = Button(l_frame3, text="Visualizar", command=vis3, borderwidth=2, relief="raised")
btn_vis3.place(x=625, y=40)
# 4 agrupamento de otus
btn_vis4 = Button(l_frame4, text="Visualizar", command=vis4, borderwidth=2, relief="raised")
btn_vis4.place(x=625, y=40)
# 5 tabela de otus
btn_vis5 = Button(l_frame5, text="Visualizar", command=vis5, borderwidth=2, relief="raised")
btn_vis5.place(x=625, y=40)
# 6 alinhamento com 16s db
btn_vis6 = Button(l_frame6, text="Visualizar", command=vis6, borderwidth=2, relief="raised")
btn_vis6.place(x=625, y=40)

# local de exibição de diretorio:
# 1 diretorio
lfile = Label(frame, bg="green", textvariable=filed)
lfile.place(x=10, y=60)
# 2 caixa de dialogo para nomear arquivos finais
infoba = Label(frame, text="Qual seu local de coleta:", bg="white", fg="black")
infoba.place(x=427, y=35)

# barras de progresso
# 1 mesclar
progress1 = ttk.Progressbar(l_frame1, orient=HORIZONTAL, length=550, mode='determinate')
progress1.place(x=20, y=40)
# 2 filtragem
progress2 = ttk.Progressbar(l_frame2, orient=HORIZONTAL, length=550, mode='determinate')
progress2.place(x=20, y=40)
# 3 busca de leituras unicas
progress3 = ttk.Progressbar(l_frame3, orient=HORIZONTAL, length=550, mode='determinate')
progress3.place(x=20, y=40)
# 4 agrupamento de otus
progress4 = ttk.Progressbar(l_frame4, orient=HORIZONTAL, length=550, mode='determinate')
progress4.place(x=20, y=40)
# 5 tabela de otus
progress5 = ttk.Progressbar(l_frame5, orient=HORIZONTAL, length=550, mode='determinate')
progress5.place(x=20, y=40)
# 6 alinhamento com 16s db
progress6 = ttk.Progressbar(l_frame6, orient=HORIZONTAL, length=550, mode='determinate')
progress6.place(x=20, y=60)
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
#Botões de interacao com resultados
#0 gerar report final:
bt_00 = Button(l_frame6, text="Gerar Report Final", command=drawn, borderwidth=1, relief="raised")
bt_00.place(x=10, y=90)
#1 visualizar reports finais
bt_01 = Button(l_frame6, text="Visualizar", command=abrir_report_final, borderwidth=1, relief="raised")
bt_01.place(x=350, y=90)
#2 salvar os resultados
bt_02 = Button(l_frame6, text="Salvar", command=salvar_final, borderwidth=1, relief="raised")
bt_02.place(x=600, y=90)
metainfo.mainloop()
