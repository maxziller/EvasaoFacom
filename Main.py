import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib as mpl
import datetime
import pandas

def TabelaEntradaESaida (matriculaAlunos, titulo, anoinicio=2004, anofinal=2019):
    anos = []
    jubilamentos = []
    desistencias = []
    transferencias = []
    sucessos = []
    entradas = []
    for i in range(anofinal - anoinicio + 1):
        anos.append (anoinicio + i)
        jubilamentos.append(0)
        desistencias.append(0)
        transferencias.append(0)
        sucessos.append(0)
        entradas.append(0)
    for e in matriculaAlunos.keys():
        est = matriculaAlunos[e]
        if ( (est.ano_evasao != '') and (est.ano_evasao != None) and (est.ano_evasao >= anoinicio) and (est.ano_evasao <= anofinal+1)):
            y = est.ano_evasao - anoinicio - 1
            if est.forma_evasao ==  "Jubilamento":
                jubilamentos[y] += 1
            elif est.forma_evasao == "Desistência":
                desistencias[y] += 1
            elif est.forma_evasao == "Transferência":     
                transferencias[y] += 1
            elif est.forma_evasao == "Sucesso":
                sucessos[y] += 1
        if ( (est.ano_ingresso != '') and (est.ano_ingresso != None) and (est.ano_ingresso >= anoinicio) and (est.ano_ingresso <= anofinal+1)):
            y = est.ano_ingresso - anoinicio - 1
            entradas[y] += 1

    jacumulado = 0
    dacumulado = 0
    tacumulado = 0
    sacumulado = 0
    eacumulado = 0
    print("\\section{"+titulo+"}")
    print("\\begin{center}")
    print("\\caption{"+titulo+" em quantidade}")
    print("\\begin{tabular}{ c c c c c c }")
    print('Ano letivo & Entradas & Formaturas & Desistências & Jubilamentos & Transferências \\\\\n\\hline') 
    for i in range(len(anos)):
        jacumulado += jubilamentos[i]
        dacumulado += desistencias[i]
        tacumulado += transferencias[i]
        sacumulado += sucessos[i]
        eacumulado += entradas[i]
        print( str(anos[i]) + " & " + str(entradas[i]) + " & " + str(sucessos[i]) + " & " + str(desistencias[i]) + " & " + str(jubilamentos[i]) + " & " + str(transferencias[i]) + "\\\\")
    print ("\\hline\nAcumulado & "+str(eacumulado) + " & " + str(sacumulado) + " & " + str(dacumulado) + " & " + str(jacumulado) + " & " + str(tacumulado) + "\\\\")
    print ("Percentual & 100\\% & " + "{:.2f}".format( float(sacumulado/eacumulado) * 100) + "\\% & " +  "{:.2f}".format( float(dacumulado/eacumulado)* 100) + "\\% & " +  "{:.2f}".format( float(jacumulado/eacumulado)* 100) + "\\% & " +  "{:.2f}".format( float(tacumulado/eacumulado) * 100) + "\\% \\\\"  )    
    print("\\hline")
    print("\\end{tabular}")
    print("\\end{center}")
    print("Fonte: Base de dados da UFU")
    print("\\break")


    

def GraficoEntradaESaida (matriculaAlunos, titulo, anoinicio=2004, anofinal=2019):
    primeirodia = datetime.date(year = anoinicio, day = 1, month = 1)
    ultimodia = datetime.date(year = anofinal, day = 31, month = 12)
    tempo = ultimodia - primeirodia
    quantidade = tempo.days
    datas = []
    jubilamentos = []
    desistencias = []
    transferencias = []
    sucessos = []
    entradas = []
    qtos_no_comeco = 0
    for e in matriculaAlunos.keys():
        est = matriculaAlunos[e]
        
        if ((est.dt_evasao != '') and (est.dt_evasao != None) and (est.dt_evasao.year <= anofinal) and (est.dt_evasao.year >= anoinicio)):
            if est.forma_evasao ==  "Jubilamento":
                jubilamentos.append(est.dt_evasao)
            elif est.forma_evasao == "Desistência":
                desistencias.append(est.dt_evasao)
            elif est.forma_evasao == "Transferência":
                transferencias.append(est.dt_evasao)
            elif est.forma_evasao == "Sucesso":
                sucessos.append(est.dt_evasao)
        if ((est.dt_ingresso != '') and (est.dt_ingresso != None) and  (est.dt_ingresso.year >= anoinicio) and (est.dt_ingresso.year <= anofinal) ):
            entradas.append(est.dt_ingresso)
        elif ((est.dt_evasao != '') and (est.dt_evasao != None) and (est.dt_ingresso != '') and (est.dt_ingresso != None) and (est.dt_ingresso.year < anoinicio) and (est.dt_evasao.year >= anoinicio)):
            qtos_no_comeco += 1
    jubilamentos.sort()
    auxj = 0
    qtddj = 0
    diaj = []
    desistencias.sort()
    auxd = 0
    qtddd = 0
    diad = []
    transferencias.sort()
    auxt = 0
    qtddt = 0
    diat = []
    sucessos.sort()
    auxs = 0
    qtdds = 0
    dias = []
    entradas.sort()
    auxe = 0
    qtdde = qtos_no_comeco
    dia = primeirodia
    diae = []
    j = 1
    for i in range(quantidade):
        dia += pandas.to_timedelta(1,unit = 'D')
        datas.append(dia)
        while ((auxe < len(entradas)) and (entradas[auxe] <= dia)):
            auxe += 1
            qtdde += 1
        while ((auxj < len(jubilamentos)) and (jubilamentos[auxj] <= dia)):
            auxj += 1
            qtddj += 1
            qtdde -= 1
        while ((auxd < len(desistencias)) and (desistencias[auxd] <= dia)):
            auxd += 1
            qtddd += 1
            qtdde -= 1
        while ((auxs < len(sucessos)) and (sucessos[auxs] <= dia)):
            auxs += 1
            qtdds += 1
            qtdde -= 1
        while ((auxt < len(transferencias)) and (transferencias[auxt] <= dia)):
            auxt += 1
            qtddt += 1
            qtdde -= 1
        diae.append(qtdde)
        diaj.append(qtddj)
        diad.append(qtddd)
        dias.append(qtdds)
        diat.append(qtddt)

    plt.plot([],[], color = "gray", label = "Matriculados")
    plt.plot([],[], color = "red", label = "Desistentes")
    plt.plot([],[], color = "orange", label = "Jubilados")
    plt.plot([],[], color = "blue", label = "Formados")
    plt.plot([],[], color = "yellow", label = "Transferidos")
    plt.legend(loc="upper left")

    plt.xlabel("Dias")
    plt.ylabel("Quantidade de alunos")
    plt.title("Entrada e saída acumulada de alunos do curso de "+titulo)
    plt.stackplot(datas,dias,diat,diaj,diad,diae, colors=["blue","yellow","orange","red","gray"])
    
    plt.show()


def SucessoDisciplinas(matriculasComponentes,aulas):
    #Gráfico X = Carga Horária, Y = Porcentagem de aprovação

    aprovacoes = dict()

    for mat in matriculasComponentes.keys():
        m = matriculasComponentes[mat]
        turma = aulas[m.ID_Turma]
        chave = (turma.Cod_Disciplina,m.ch_cumprida)
        if (chave not in aprovacoes.keys()):
            aprovacoes[chave] = [0,0]
        if (m.situacao == "Sucesso"):
            aprovacoes[chave][0] += 1
        elif (m.situacao == "Fracasso"):
            aprovacoes[chave][1] += 1

    coordx = []
    coordy = []
    for a in aprovacoes.keys():
        coordx.append(a[1])
        if (aprovacoes[a][1] == 0):
            coordy.append(1)
        else:
            coordy.append( float(aprovacoes[a][0]/(aprovacoes[a][0]+aprovacoes[a][1])))

    plt.title("Aprovações, em porcentagem, por carga horária da turma")
    plt.xlabel("Carga horária")
    plt.ylabel("Percentual de aprovação")
    plt.scatter(coordx,coordy, c = "blue")

    plt.show()

class pessoa:
    def __init__(self,cpf, evasao, dt_evasao, cod_curso, versao_curric):
        self.cpf = cpf
        self.carga_horaria = 0
        self.evasao = evasao
        self.dt_evasao = dt_evasao
        self.carga_horaria_aprovada = 0
        self.qtdd_componentes_aprovados = 0
        self.cod_curso = cod_curso
        self.versao_curric = versao_curric

    def add_versao(self,versao):
        self.versao_curric = versao

class cursoporcento:
    def __init__(self,cod_curso,versao_curric):
        self.cod_curso = cod_curso
        self.versao_curric = versao_curric
        self.atividades = []
        self.ch_total = 0
        
        
def SucessoTempoEstudante(matriculasComponentes,matriculasAlunos,estudantes,componentesCurriculares,aulas):
    #Eixo X = Carga horária, Eixo Y = Porcentagem do curso completo ao evadir
    pessoas = dict()
    cursosporcento = dict()
    for e in matriculasAlunos.keys():
        cpf = matriculasAlunos[e].cpf
        if (cpf in pessoas.keys()):
            if (not isinstance(matriculasAlunos[e].dt_evasao,datetime.date) or not isinstance(pessoas[cpf].dt_evasao,datetime.date)):
                pessoas[cpf].dt_evasao = ''
                pessoas[cpf].evasao = 'Cursando'
            elif (matriculasAlunos[e].dt_evasao > pessoas[cpf].dt_evasao):
                pessoas[cpf].dt_evasao = matriculasAlunos[e].dt_evasao
                pessoas[cpf].evasao = matriculasAlunos[e].forma_evasao
        else:
            novo = pessoa(cpf, matriculasAlunos[e].forma_evasao, matriculasAlunos[e].dt_evasao, matriculasAlunos[e].curso, matriculasAlunos[e].versao_curric)
            pessoas[cpf] = novo

    for comp in componentesCurriculares.keys():
        c = componentesCurriculares[comp]
        chave = (c.cod_curso,c.versao_curric)
        if ( (chave in cursosporcento.keys()) and (c.cod_ativ not in cursosporcento[chave].atividades) and (c.descr_estrutura == "Obrigatória")) :
            cursosporcento[chave].atividades.append(c.cod_ativ)
            cursosporcento[chave].ch_total += c.ch_prevista
        elif ( (chave not in cursosporcento.keys() and (c.descr_estrutura == "Obrigatória"))):
            cursosporcento[chave] = cursoporcento(c.cod_curso,c.versao_curric)
            cursosporcento[chave].atividades.append(c.cod_ativ)
            cursosporcento[chave].ch_total += c.ch_prevista
            

    for registro in matriculasComponentes.keys():
        r = matriculasComponentes[registro]
        matr = r.estudante
        cpf = matriculasAlunos[matr].cpf
        if (isinstance(r.ch_cumprida,int)):
            pessoas[cpf].carga_horaria += r.ch_cumprida
            if r.situacao == "Sucesso":
                pessoas[cpf].qtdd_componentes_aprovados += 1
                pessoas[cpf].carga_horaria_aprovada += r.ch_cumprida
                aula = aulas[r.ID_Turma]
                chave = (aula.Cod_Disciplina,pessoas[cpf].versao_curric, pessoas[cpf].cod_curso)
                if (chave in componentesCurriculares.keys()):
                    ch_p = componentesCurriculares[chave].ch_prevista
                    if ( (pessoas[cpf].cod_curso,pessoas[cpf].versao_curric) in cursosporcento.keys() and (aula.Cod_Disciplina not in cursosporcento[pessoas[cpf].cod_curso,pessoas[cpf].versao_curric].atividades)):
                        curso = pessoas[cpf].cod_curso
                        versao = matriculasAlunos[matr].versao_curric
                        if (curso,versao) in cursosporcento.keys():
                            cursosporcento[curso,versao].atividades.append(aula.Cod_Disciplina)
                            cursosporcento[curso,versao].ch_total += ch_p

    mx, my = [], []
    dx, dy = [], []
    jx, jy = [], []
    sx, sy = [], []
    tx, ty = [], []



    for cpf in pessoas.keys():
        if (cpf != ''):
            p = pessoas[cpf]
            x = p.carga_horaria
            y = p.qtdd_componentes_aprovados
            if (p.evasao == "Jubilamento"):
                jx.append(x)
                jy.append(y)
            elif (p.evasao == "Desistência"):
                dx.append(x)
                dy.append(y)
            elif (p.evasao == "Transferência"):
                tx.append(x)
                ty.append(y)
            elif (p.evasao == "Sucesso"):
                sx.append(x)
                sy.append(y)
            #elif (p.evasao == "Cursando"):
                #mx.append(x)
                #my.append(y)
 

    #plt.plot([],[], color = "gray", label = "Matriculados")
    plt.plot([],[], color = "red", label = "Desistentes")
    plt.plot([],[], color = "orange", label = "Jubilados")
    plt.plot([],[], color = "blue", label = "Formados")
    plt.plot([],[], color = "yellow", label = "Transferidos")
    plt.legend(loc="upper left")

    #plt.scatter(mx,my, c = "gray")
    plt.scatter(dx,dy, c = "red")
    plt.scatter(jx,jy, c = "orange")
    plt.scatter(sx,sy, c = "blue")
    plt.scatter(tx,ty, c = "yellow")

    plt.title("Sucesso dos estudantes de acordo com carga horária cursada")
    plt.xlabel("Carga horária total cursada")
    plt.ylabel("Quantidade de componentes curriculares aprovados")

    plt.show()


class ps:
    def __init__(self,curso,nome,ano,semestre,vagas,candidatos):
        self.curso = curso
        self.nome = nome
        self.ano = ano
        self.semestre = semestre
        self.concorrencia = float(candidatos)/float(vagas)
        #if (self.concorrencia < float(1)):
        #    self.concorrencia = float(1)
        self.cursando = 0
        self.desistente = 0
        self.jubilado = 0
        self.formado = 0
        self.transferido = 0

    def totalsaida(self):
        total = self.desistente + self.jubilado + self.formado + self.transferido
        return total

    def porcentojubilado(self):
        total = self.totalsaida()
        pc = float(self.jubilado)/total
        return pc

    def porcentodesistente(self):
        total = self.totalsaida()
        pc = float(self.desistente)/total
        return pc

    def porcentotransferido(self):
        total = self.totalsaida()
        pc = float(self.transferido)/total
        return pc

    def porcentoformado(self):
        total = self.totalsaida()
        pc = float(self.formado)/total
        return pc
    

def SucessoConcorrência(candidatosVagas, matriculasAlunos):
    #Eixo X = Concorrência, Eixo Y = Taxa de sucesso
    pss = dict()
    x = []
    y = []
    for cv in candidatosVagas.keys():
        c = candidatosVagas[cv]
        if (c.modalidade_cota == 'A'):
            novo = ps(c.cod_curso,c.nome_ps,c.ano_ingresso,c.semestre_ingresso,c.vagas,c.candidatos)
            pss[c.cod_curso,c.nome_ps,int(c.ano_ingresso),c.semestre_ingresso] = novo

    for est in matriculasAlunos.keys():
        e = matriculasAlunos[est]
        chave = (e.curso,e.forma_ingresso,e.ano_ingresso,e.periodo_ingresso)
        if (chave in pss.keys()):
            if (e.forma_evasao == "Jubilamento"):
                pss[chave].jubilado += 1
            elif (e.forma_evasao == "Desistência"):
                pss[chave].desistente += 1
            elif (e.forma_evasao == "Transferência"):
                pss[chave].transferido += 1
            elif (e.forma_evasao == "Sucesso"):
                pss[chave].formado += 1
            elif (e.forma_evasao == "Cursando"):
                pss[chave].cursando += 1

    print("\\begin{center}\n\\caption{Taxa de sucesso dos estudantes por processo seletivo}")
    print("\\begin{tabular}{ c c c c c c c }\nProcesso Seletivo & Curso & Ano & Semestre & Total de estudantes & Concorrência (candidatos/vaga) & Formados\\\\\n\\hline")
    for pskey in pss.keys():
        p = pss[pskey]
        totalest = p.cursando + p.desistente + p.jubilado + p.formado + p.transferido
        if (totalest > 0):
            txsucesso =(float(p.formado)/(totalest)) * 100
            y.append(txsucesso)
            x.append(p.concorrencia)
            print(p.nome +" & "+ p.curso +" & "+ p.ano +" & "+ p.semestre +" & "+ str(totalest) +" & "+ "%.4f" %p.concorrencia +" & "+ str(p.formado) + "\\\\")
    print("\\hline\n\\end{tabular}\n\\end{center}\nFonte: Base de dados da UFU")

    plt.title("Sucesso dos estudantes de acordo com concorrência")
    plt.xlabel("Concorrência (candidatos/vaga)")
    plt.ylabel("Taxa de formatura dos aprovados (em %)")
    plt.scatter(x,y, c = "blue")

    plt.show()




def SucessoMetodoEntrada( matriculasAlunos):
    #Eixo X = Processos Seletivos, Eixo Y = Taxa de sucesso
    pss = dict()
    x = []
    y = []

    for est in matriculasAlunos.keys():
        e = matriculasAlunos[est]
        chave = e.forma_ingresso
        if (chave not in pss.keys()):
            novo = ps('', chave, '', '', 1, 1)
            pss[chave] = novo
        if (e.forma_evasao == "Jubilamento"):
            pss[chave].jubilado += 1
        elif (e.forma_evasao == "Desistência"):
            pss[chave].desistente += 1
        elif (e.forma_evasao == "Transferência"):
            pss[chave].transferido += 1
        elif (e.forma_evasao == "Sucesso"):
            pss[chave].formado += 1
        elif (e.forma_evasao == "Cursando"):
            pss[chave].cursando += 1

    jubilados = []
    desistentes = []
    transferidos = []
    formados = []
    nomes = []

    totalj = 0
    totald = 0
    totalt = 0
    totalf = 0

    print("\\begin{center}\n\\caption{Taxa de sucesso dos estudantes por processo seletivo}")
    print("\\begin{tabular}{ c c c c c c }\nProcesso Seletivo & Desistentes & Jubilados & Transferidos & Formados & Sucesso (em %)\\\\\n\\hline")
    for pskey in pss.keys():
        p = pss[pskey]
        totalest = p.desistente + p.jubilado + p.formado + p.transferido
        nomes.append(p.nome)
        jubilados.append(p.jubilado)
        desistentes.append(p.desistente)
        formados.append(p.formado)
        transferidos.append(p.transferido)
        totalj += p.jubilado
        totald += p.desistente
        totalt += p.transferido
        totalf += p.formado
        if (totalest > 0):
            txsucesso =(float(p.formado)/(totalest)) * 100
            print(p.nome +" & "+ str(p.desistente) +" & "+ str(p.jubilado) +" & "+ str(p.transferido) +" & "+ str(p.formado) +" & "+ "%.4f" %txsucesso + "\\\\")
    print("Total & "+ str(totald) +" & "+ str(totalj) +" & "+ str(totalt) +" & "+ str(totalf) +" & "+ "%.4f" %( float( totalf*100/(totald + totalj + totalt + totalf) )) + "\\\\")
    print("\\hline\n\\end{tabular}\n\\end{center}\nFonte: Base de dados da UFU")

    barWidth = 0.1
    plt.figure(figsize=(12,5))
    barras = []
    r1 = np.arange(4)
    barras.append(r1)
    for i in range (len(pss) - 1):
        r = [x + barWidth for x in barras[i]]
        barras.append(r)

    relevantes = ['Vestibular', 'SISU', 'PAAES', 'Port. Dipl. Curso Sup', 'PAIES']
    transferencias = ['Transferência Facultativa', 'Transferência', 'Transferência Interna','Mobilidade Acadêmica', 'Transfer. Ex-Officio', 'Mobilidade Internacional']

    transj = 0
    transd = 0
    transt = 0
    transf = 0
    results = dict()

    for i in pss.keys():
        p = pss[i]
        total = p.jubilado + p.desistente + p.transferido + p.formado
        if p.nome in transferencias:
            transj += p.jubilado
            transd += p.desistente
            transt += p.transferido
            transf += p.formado
        if p.nome in relevantes:
            results[p.nome] = [float(p.desistente*100/total),float(p.transferido*100/total),float(p.jubilado*100/total),float(p.formado*100/total)]
    total = transj + transd + transt + transf
    results["Transferências"] = [float(transd*100/total),float(transt*100/total),float(transj*100/total),float(transf*100/total)]
    fins = ["Desistência","Transferência","Jubilamento","Formatura"]
    quantosfins = dict()
    for f in fins:
        quantosfins[f] = []
  
    for i in results.keys():
        quantosfins["Desistência"].append(results[i][0])
        quantosfins["Transferência"].append(results[i][1])
        quantosfins["Jubilamento"].append(results[i][2])
        quantosfins["Formatura"].append(results[i][3])

    plt.bar(results.keys(),quantosfins["Desistência"], label = "Desistência")
    plt.bar(results.keys(),quantosfins["Transferência"], bottom = quantosfins["Desistência"], label = "Transferência")
    baixo = []
    for i in range(len(quantosfins["Desistência"])):
        baixo.append(quantosfins["Desistência"][i] + quantosfins["Transferência"][i])
    plt.bar(results.keys(),quantosfins["Jubilamento"], bottom = baixo, label = "Jubilamento")
    for i in range(len(quantosfins["Desistência"])):
        baixo[i] += quantosfins["Jubilamento"][i]
    plt.bar(results.keys(),quantosfins["Formatura"], bottom = baixo, label = "Formatura")
   
    plt.title("Sucesso dos estudantes de acordo com método de ingresso")
    plt.xlabel("Processos Seletivos")
    plt.legend(fins)
    plt.ylabel("Situação dos ex-alunos (em %)")
    plt.show()



def SucessoGenero(matriculasAlunos,estudantes):
    evasoes = ["Sucesso", "Cursando","Jubilamento", "Desistência", "Transferência"]
    homem = [0,0,0,0,0]
    mulher = [0,0,0,0,0]
    sobrevivenciah = []
    sobrevivenciam = []

    for matr in matriculasAlunos.keys():
        resultado = matriculasAlunos[matr].forma_evasao
        cpf = matriculasAlunos[matr].cpf
        indice = evasoes.index(resultado)
        genero = estudantes[cpf].genero
        if (genero == 'M'):
            homem[indice] += 1
        elif (genero == 'F'):
            mulher[indice] += 1

    indice = evasoes.index("Cursando")
    del evasoes[indice]
    del mulher[indice]
    del homem[indice]
    evasoes[0] = "Formatura"

    print("\\begin{table}\n\\begin{center}\n\\caption{Taxa de sucesso dos estudantes por gênero}")
    print("\\begin{tabular}{ c c c }\nForma de saida & Homens & Mulheres\\\\\n\\hline")
    for i in range(len(homem)):
        print( evasoes[i] + " & " + str(homem[i]) + " & " + str(mulher[i]) + " \\\\")
    print("\\hline\n\\end{tabular}\n\\end{center}\nFonte: Base de dados da UFU\n\\end{table}")

    plt.title("Forma de saída dos estudantes do sexo masculino")
    plt.pie(homem, labels = evasoes,autopct='%.1f%%', startangle=90)
    #plt.title("Forma de saída dos estudantes do sexo feminino")
    #plt.pie(mulher, labels = evasoes,autopct='%.1f%%', startangle=90)

    

    plt.show()

def contasemestres(dias, tipo = "fracassos"):
    semestres = []
    for i in range(25):
        semestres.append(0)

    total = 0
    certos = 0
    narisca = 0

    for dia in dias:    
            
        qt = dia.days
        if (qt < 0):
            qt = 0
        i = qt % 365
        sem = int(qt/365)*2
        if (i > 183):
            sem += 1
        if (tipo == "sucessos"):
            total += 1
            if sem <= 8:
                certos += 1
            elif sem <= 12:
                narisca += 1
        try:
            semestres[sem]+=1
        except:
            semestres[-1]+= 1

    if (tipo == "sucessos"):
        print("Total de alunos formados = "+str(total))
        print("Total de alunos formados no prazo = "+str(certos))
        print("Total de alunos formados na risca = "+str(narisca))

    return semestres
    
        
def graficoSobrevivencia(matriculasAlunos):
    jubilamentos = []
    desistencias = []
    sucessos = []
    transferencias = []
    current = 0
    total = len(matriculasAlunos)
    for matr in matriculasAlunos.keys():
        m = matriculasAlunos[matr]
        if (m.dt_evasao != '' and m.dt_ingresso != '' and m.cpf != ''):
            tempo = m.dt_evasao - m.dt_ingresso
            if (m.forma_evasao == "Jubilamento"):
                jubilamentos.append(tempo)
            elif (m.forma_evasao == "Desistência"):
                desistencias.append(tempo)
            elif (m.forma_evasao == "Transferência"):
                transferencias.append(tempo)
            elif (m.forma_evasao == "Sucesso"):
                sucessos.append(tempo)
            else:
                total -= 1
        else:
            total -= 1

    jubila = contasemestres(jubilamentos)
    desiste = contasemestres(desistencias)
    sucede = contasemestres(sucessos, tipo = "sucessos")
    trans = contasemestres(transferencias)

    sobrevive = []
    semestres = []
    for i in range(25):
        semestres.append(i)
        if (i > 0):
            sobrevive.append(sobrevive[i-1])
        else:
            sobrevive.append(total)
        sobrevive[i] -= (jubila[i] + desiste[i] + sucede[i] + trans[i])

    porcentovivo = []
    for elem in sobrevive:
        pcvv = 100 * float(elem / total)
        porcentovivo.append(pcvv)

    fig,ax = plt. subplots ()
    
    ax.plot(semestres,jubila, label = "Jubilamentos", marker = ".", color = "orange")
    ax.plot(semestres,desiste, label = "Desistências", marker = "v", color = "red")
    ax.plot(semestres,trans, label = "Transferências", marker = "^", color = "yellow")
    ax.plot(semestres,sucede, label = "Formaturas", marker = "*", color = "blue")
    plt.xticks(semestres)
    ax.set_xlabel("Semestres letivos após o ingresso")
    ax.set_ylabel("Quantidade de estudantes")

    #ax2 = ax.twinx()
    #ax2.plot(semestres,porcentovivo,linewidth = 2, label = "Matriculados", color = "gray")
    #ax2.set_ylabel('Percentual de alunos ainda matriculados', color = "gray")

    
    plt.title("Saídas de estudantes por semestres letivos a partir da matrícula")
    ax.legend()
    plt.show()    


class materia:
    def __init__(self,nome,tipo):
        self.nome = nome
        self.aprovados = 0
        self.reprovados = 0
        self.tipo = tipo
        self.estudantes = dict()
        self.reprovevade = 0
        self.aprovevade = 0

    def porcentevade(self):
        pct = 100 - (100 * float(self.reprovevade / self.reprovados))
        return pct

    def aprovamasevade(self):
        pct = 100 - (100 * float(self.aprovevade / self.aprovados))
        return pct

    def porcentagem(self):
        pct = 100 * float(self.aprovados / (self.aprovados + self.reprovados))
        return pct

    def contaReprovacoes(self):
        reprovacoes = [0,0,0,0,0,0,0,0]
        for est in self.estudantes.keys():
            e = self.estudantes[est]
            reprovacoes[e[3]] += 1
        return reprovacoes
            

    def contaMatricula(self,matriculaComponente,Turma,matriculasAlunos):
        ano = int(Turma.Ano)
        semestre = Turma.Semestre
        sucesso = matriculaComponente.situacao
        if (matriculaComponente.estudante not in self.estudantes):
            if sucesso == "Sucesso":
                evasao = matriculasAlunos[matriculaComponente.estudante].forma_evasao
                if (evasao != "Sucesso"):
                    self.aprovevade += 1
                self.aprovados += 1
                i = 0
                self.estudantes[matriculaComponente.estudante] = (ano,semestre,sucesso,i)
            elif sucesso == "Fracasso":
                self.reprovados += 1
                i = 1
                self.estudantes[matriculaComponente.estudante] = (ano,semestre,sucesso,i)
                evasao = matriculasAlunos[matriculaComponente.estudante].forma_evasao
                if (evasao != "Sucesso"):
                    self.reprovevade += 1
        else:
            holdon = self.estudantes[matriculaComponente.estudante]
            if (ano < holdon[0] or (ano == holdon[0] and int(semestre[0]) > int(holdon[1][0]))):
                reprovacoes = self.estudantes[matriculaComponente.estudante][3]
                if holdon[2] == "Sucesso":
                    self.estudantes[matriculaComponente.estudante] = (ano,semestre,sucesso,reprovacoes)
                    self.aprovados -= 1
                    self.reprovados += 1
                    evasao = matriculasAlunos[matriculaComponente.estudante].forma_evasao
                    if (evasao != "Sucesso"):
                        self.reprovevade += 1
                        self.aprovevade += 1
                elif holdon[2] == "Fracasso":
                    i = reprovacoes + 1
                    self.estudantes[matriculaComponente.estudante] = (holdon[0],holdon[1],holdon[2],i)

            
def reprovaDisciplina(matriculasComponentes, aulas, componentesCurriculares,matriculasAlunos):
    materias = dict()
    tipos = []
    retorno = []

    for matr in matriculasComponentes.keys():
        m = matriculasComponentes[matr]
        aula = aulas[m.ID_Turma]
        cod_disc = aula.Cod_Disciplina
        cod_curso = aula.Cod_Curso
        chave = (cod_disc,cod_curso)
        disciplina = componentesCurriculares[chave].nome_ativ.replace("~",",")
        if (disciplina == "Administração 1"):
            disciplina = "Administração de Empresas 1"
        elif (disciplina == "Administração 2"):
            disciplina = "Administração de Empresas 2"
        elif (disciplina == "Algoritmos e Estruturas de Dados 1"):
            disciplina = "Estrutura de Dados 1"
        elif (disciplina == "Algoritmos e Estruturas de Dados 2"):
            disciplina = "Estrutura de Dados 2"
        elif (disciplina == "Análise de Algoritmos 1"):
            disciplina = "Análise de Algoritmos"
        elif (disciplina == "Arquitetura de Computadores 1"):
            disciplina = "Arquitetura e Organização de Computadores 1"
        elif (disciplina == "Cálculo Diferencial e Integral II"):
            disciplina = "Cálculo Diferencial e Integral 2"
        elif (disciplina == "Empreendedores em Informática"):
            disciplina = "Empreendedorismo em Informática"
        elif ((disciplina == "Matemática para a Ciência da Computação") or (disciplina == "Matemática para Ciência da Computação 1")):
            disciplina = "Matemática para Ciência da Computação"
        elif (disciplina == "Microprocessadores 1"):
            disciplina = "Microprocessadores"
        elif (disciplina == "Organização de Computadores 1"):
            disciplina = "Arquitetura e Organização de Computadores 1"
        elif (disciplina == "Organização de Computadores 2"):
            disciplina = "Arquitetura e Organização de Computadores 2"
        elif (disciplina == "Organização de Computadores 2"):
            disciplina = "Arquitetura e Organização de Computadores"
        elif (disciplina == "Organização de Computadores 2"):
            disciplina = "Arquitetura e Organização de Computadores"
        elif (disciplina == "Trabalho de Conclusão de Curso I"):
            disciplina = "Trabalho de Conclusão de Curso 1"
        elif (disciplina == "Trabalho de Conclusão de Curso II"):
            disciplina = "Trabalho de Conclusão de Curso 2"
        elif (disciplina == "Tópicos Especiais de Engenharia de Software: Interação Humano Computador"):
            disciplina = "Interação Humano-Computador"
        elif (disciplina == "Tópicos Especiais de Inteligência Artificial: Inteligência Artificial Aplicados aos Negócios"):
            disciplina = "Inteligência Artificial Aplicada aos Negócios"
        elif (disciplina == "Tópicos Especiais em Computação 1 - Programação Orientada a Objetos 2"):
            disciplina = "Programação Orientada a Objetos 2"
        elif (disciplina == "Tópicos Especiais em Computação 1 - Sistemas de Recuperação da Informação"):
            disciplina = "Organização e Recuperação da Informação"
        elif (disciplina == "Tópicos Especiais em Computação 1: Álgebra Linear"):
            disciplina = "Álgebra Linear"
        elif (disciplina == "Programação lógica"):
            disciplina = "Programação Lógica"
        elif (disciplina == "Tópicos Especiais em Computação II: Resolução de Problemas Algoritmos"):
            disciplina = "Resolução de Problemas"
        elif (disciplina == "Tópicos Especiais em Computação I: Matemática Básica"):
            disciplina = "Tópicos Especiais em Computação 1: Matemática Básica"
        elif (disciplina == "Tópicos Especiais em Computação 2: Resolução de Problemas e Soluções Algorítmicas"):
            disciplina = "Resolução de Problemas"
        elif (disciplina == "Estruturas de Dados 1"):
            disciplina = "Estrutura de Dados 1"
        elif (disciplina == "Estruturas de Dados 2"):
            disciplina = "Estrutura de Dados 2"
        elif (disciplina == "Organização e Arquitetura de Computadores"):
            disciplina = "Arquitetura e Organização de Computadores"
        elif (disciplina == "Máquinas Seqüenciais"):
            disciplina = "Máquinas Sequenciais"
        elif (disciplina == "Teoria dos Grafos 1"):
            disciplina = "Teoria dos Grafos"
        elif (disciplina == "Teoria da Computação 1"):
            disciplina = "Teoria da Computação"
        descr = componentesCurriculares[chave].descr_estrutura
        if descr not in tipos:
            tipos.append(descr)
        if ( disciplina not in materias.keys()):
            novo = materia(disciplina, descr)
            materias[disciplina] = novo
        materias[disciplina].contaMatricula(m,aula,matriculasAlunos)

    chaves = list(materias.keys())
    chaves.sort()

    i = 0
    #print("\\begin{table}\n\\begin{center}\n\\caption{Aprovações dos estudantes na primeira tentativa por disciplina}")
    #print("\\begin{tabular}{ c c c c }\nDisciplina & Aprovados & Reprovados & Porcentagem de aprovação\\\\\n\\hline")
    #for k in chaves:
    #    m = materias[k]
    #    if ( ((m.tipo == "Obrigatória") or (m.tipo == "Optativa")) and (m.aprovados + m.reprovados > 10)):
    #        i += 1
    #        if (i % 36 == 35):
    #            print("\\hline\n\\end{tabular}")
    #            print("\\begin{table}\nDisciplina & Aprovados & Reprovados & Porcentagem de aprovação\\\\")
    #        retorno.append( m.porcentagem())
    #        print(m.nome + " & " + str(m.aprovados) + " & " + str(m.reprovados) + " & " + "{:.2f}".format(m.porcentagem()) + "\\\\")
    #print("\\hline\n\\end{tabular}\n\\end{center}\nFonte: Base de dados da UFU\n\\end{table}")

    disciplinasfoco = []

    discperiodos = []
    discperiodos.append('Lógica para Ciência da Computação 1','1° período')
    discperiodos.append('Programação Funcional','1° período')
    discperiodos.append('Matemática para Ciência da Computação 1','1° período')
    discperiodos.append('Introdução à Ciência da Computação','1° período')
    discperiodos.append('Cálculo Diferencial e Integral 1','1° período')
    discperiodos.append('Geometria Analítica','1° período')
    discperiodos.append('Empreendedorismo em Informática','1° período')
    discperiodos.append('Cálculo Diferencial e Integral 1','1° período')
    discperiodos.append('Geometria Analítica e Álgebra Linear','1° período')
    discperiodos.append('Programação Procedimental','1° período')
    discperiodos.append('Introdução à Ciência da Computação','1° período')
    discperiodos.append('Lógica para Computação','1° período')
    discperiodos.append('Empreendedorismo em Informática','1° período')
    discperiodos.append('Introdução à Programação de Computadores','1° período')
    discperiodos.append('Introdução aos Sistemas de Informação','1° período')
    discperiodos.append('Programação Funcional','1° período')
    discperiodos.append('Lógica para Computação','1° período')
    discperiodos.append('Empreendedorismo em Informática','1º período')
    discperiodos.append('Cálculo Diferencial e Integral 1','1º período')
    discperiodos.append('Geometria Analítica e Álgebra Linear','1º período')
    discperiodos.append('Programação Procedimental','1º período')
    discperiodos.append('Introdução à Ciência da Computação','1º período')
    discperiodos.append('Lógica para Computação','1º período')
    discperiodos.append('Introdução à Ciência da Computação','1º período')
    discperiodos.append('Programação Procedimental','1º período')
    discperiodos.append('Cálculo Diferencial e Integral I','1º período')
    discperiodos.append('Geometria Analítica e Álgebra Linear','1º período')
    discperiodos.append('Lógica para Computação','1º período')
    discperiodos.append('Empreendedorismo em Informática','1º período')
    discperiodos.append('Introdução à Programação de Computadores','1º período')
    discperiodos.append('Introdução aos Sistemas de Informação','1º período')
    discperiodos.append('Lógica para Computação','1º período')
    discperiodos.append('Matemática 1','1º período')
    discperiodos.append('Algoritmos e Programação I','1º período')
    discperiodos.append('Introdução aos Sistemas de Informação','1º período')
    discperiodos.append('Matemática Discreta','1º período')
    discperiodos.append('Lógica para Computação','1º período')
    discperiodos.append('Profissão em Sistemas de Informação','1º período')
    discperiodos.append('Fundamentos de Marketing','1º período')
    discperiodos.append('Introdução à Programação de Computadores','1º período')
    discperiodos.append('Empreendedorismo em Informática','1º período')
    discperiodos.append('Introdução aos Sistemas de Informação','1º período')
    discperiodos.append('Programação Funcional','1º período')
    discperiodos.append('Lógica para Computação','1º período')
    discperiodos.append('Contabilidade e Análise de Demonstrativos Financeiros','1º período')
    discperiodos.append('Informática e Sociedade','1º período')
    discperiodos.append('Algoritmos e Programação I','1º período')
    discperiodos.append('Introdução aos Sistemas de Informação','1º período')
    discperiodos.append('Lógica para Computação','1º período')
    discperiodos.append('Máquinas Seqüenciais','2° período')
    discperiodos.append('Programação lógica','2° período')
    discperiodos.append('Lógica para Ciência da Computação 2','2° período')
    discperiodos.append('Programação Procedimental','2° período')
    discperiodos.append('Álgebra Linear','2° período')
    discperiodos.append('Cálculo Diferencial e Integral 2','2° período')
    discperiodos.append('Profissão em Computação e Informática','2° período')
    discperiodos.append('Matemática para a Ciência da Computação','2° período')
    discperiodos.append('Programação Lógica','2° período')
    discperiodos.append('Sistemas Digitais','2° período')
    discperiodos.append('Cálculo Diferencial e Integral 2','2° período')
    discperiodos.append('Estrutura de Dados 1','2° período')
    discperiodos.append('Matemática 1','2° período')
    discperiodos.append('Sistemas Digitais','2° período')
    discperiodos.append('Profissão em Sistemas de Informação','2° período')
    discperiodos.append('Programação Lógica','2° período')
    discperiodos.append('Sistemas Digitais','2º período')
    discperiodos.append('Profissão em Computação e Informática','2º período')
    discperiodos.append('Matemática para a Ciência da Computação','2º período')
    discperiodos.append('Algoritmos e Estruturas de Dados 1','2º período')
    discperiodos.append('Cálculo Diferencial e Integral 2','2º período')
    discperiodos.append('Programação Lógica','2º período')
    discperiodos.append('Empreendedorismo em Informática','2º período')
    discperiodos.append('Programação Funcional','2º período')
    discperiodos.append('Cálculo Diferencial e Integral II','2º período')
    discperiodos.append('Profissão em Sistemas de Informação','2º período')
    discperiodos.append('Sistemas Digitais','2º período')
    discperiodos.append('Programação Orientada a Objetos 1','2º período')
    discperiodos.append('Matemática para Ciência da Computação','2º período')
    discperiodos.append('Estrutura de Dados 1','2º período')
    discperiodos.append('Gestão Empresarial','2º período')
    discperiodos.append('Algoritmos e Programação II','2º período')
    discperiodos.append('Sistemas Digitais','2º período')
    discperiodos.append('Cálculo Diferencial e Integral','2º período')
    discperiodos.append('Gestão Empresarial','2º período')
    discperiodos.append('Fundamentos da Economia','2º período')
    discperiodos.append('Sistemas Digitais','2º período')
    discperiodos.append('Algoritmos e Estruturas de Dados I','2º período')
    discperiodos.append('Matemática para Ciência da Computação','2º período')
    discperiodos.append('Matemática 1','2º período')
    discperiodos.append('Sistemas Digitais','2º período')
    discperiodos.append('Estrutura de Dados 1','2º período')
    discperiodos.append('Profissão em Sistemas de Informação','2º período')
    discperiodos.append('Programação Lógica','2º período')
    discperiodos.append('Algoritmos e Programação II','2º período')
    discperiodos.append('Fundamentos de Marketing','2º período')
    discperiodos.append('Gestão Empresarial','2º período')
    discperiodos.append('Cálculo I','2º período')
    discperiodos.append('Cálculo Numérico','3° período')
    discperiodos.append('Organização de Computadores 1','3° período')
    discperiodos.append('Programação Orientada a Objetos','3° período')
    discperiodos.append('Cálculo Diferencial e Integral 3','3° período')
    discperiodos.append('Estrutura de Dados 1','3° período')
    discperiodos.append('Gerenciamento de Banco de Dados 1','3° período')
    discperiodos.append('Programação Funcional','3° período')
    discperiodos.append('Algoritmos e Estruturas de Dados 1','3° período')
    discperiodos.append('Estatística','3° período')
    discperiodos.append('Cálculo Diferencial e Integral 3','3° período')
    discperiodos.append('Programação Orientada a Objetos 1','3° período')
    discperiodos.append('Arquitetura e Organização de Computadores 1','3° período')
    discperiodos.append('Matemática 2','3° período')
    discperiodos.append('Arquitetura e Organização de Computadores','3° período')
    discperiodos.append('Matemática para Ciência da Computação','3° período')
    discperiodos.append('Programação Orientada a Objetos 1','3° período')
    discperiodos.append('Estrutura de Dados 2','3° período')
    discperiodos.append('Matemática Financeira e Análise de Investimentos','3° período')
    discperiodos.append('Algoritmos e Estruturas de Dados 2','3º período')
    discperiodos.append('Programação Orientada a Objetos 1','3º período')
    discperiodos.append('Arquitetura e Organização de Computadores 1','3º período')
    discperiodos.append('Estatística','3º período')
    discperiodos.append('Cálculo Diferencial e Integral 3','3º período')
    discperiodos.append('Programação Funcional','3º período')
    discperiodos.append('Cálculo Numérico','3º período')
    discperiodos.append('Álgebra Linear','3º período')
    discperiodos.append('Estrutura de Dados 2','3º período')
    discperiodos.append('Arquitetura e Organização de Computadores','3º período')
    discperiodos.append('Programação para Internet I','3º período')
    discperiodos.append('Programação Orientada a Objetos 2','3º período')
    discperiodos.append('Banco de Dados 1','3º período')
    discperiodos.append('Estrutura de Dados I','3º período')
    discperiodos.append('Arquitetura e Organização de Computadores','3º período')
    discperiodos.append('Banco de Dados I','3º período')
    discperiodos.append('Fundamentos de Engenharia de Software','3º período')
    discperiodos.append('Programação Orientada a Objetos I','3º período')
    discperiodos.append('Estatística','3º período')
    discperiodos.append('Arquitetura e Organização de Computadores','3º período')
    discperiodos.append('Cálculo Diferencial e Integral III','3º período')
    discperiodos.append('Programação Orientada a Objetos','3º período')
    discperiodos.append('Algoritmos e Estruturas de Dados II','3º período')
    discperiodos.append('Matemática 2','3º período')
    discperiodos.append('Programação Orientada a Objetos 1','3º período')
    discperiodos.append('Estrutura de Dados 2','3º período')
    discperiodos.append('Arquitetura e Organização de Computadores','3º período')
    discperiodos.append('Matemática para Ciência da Computação','3º período')
    discperiodos.append('Álgebra Linear','3º período')
    discperiodos.append('Estatística','4° período')
    discperiodos.append('Estruturas de Dados 2','4° período')
    discperiodos.append('Linguagens Formais e Autômatos','4° período')
    discperiodos.append('Teoria dos Grafos 1','4° período')
    discperiodos.append('Organização de Computadores 2','4° período')
    discperiodos.append('Gerenciamento de Banco de Dados 2','4° período')
    discperiodos.append('Algoritmos e Estruturas de Dados 2','4° período')
    discperiodos.append('Teoria dos Grafos','4° período')
    discperiodos.append('Sistemas de Banco de Dados','4° período')
    discperiodos.append('Linguagens Formais e Autômatos','4° período')
    discperiodos.append('Sistemas Operacionais','4° período')
    discperiodos.append('Arquitetura e Organização de Computadores 2','4° período')
    discperiodos.append('Sistemas Operacionais 1','4° período')
    discperiodos.append('Programação para Internet','4° período')
    discperiodos.append('Estatística','4° período')
    discperiodos.append('Sistemas Operacionais','4° período')
    discperiodos.append('Programação Orientada a Objetos 2','4° período')
    discperiodos.append('Banco de Dados 1','4° período')
    discperiodos.append('Estatística Computacional','4º período')
    discperiodos.append('Teoria dos Grafos','4º período')
    discperiodos.append('Sistemas de Banco de Dados','4º período')
    discperiodos.append('Linguagens Formais e Autômatos','4º período')
    discperiodos.append('Sistemas Operacionais','4º período')
    discperiodos.append('Arquitetura e Organização de Computadores 2','4º período')
    discperiodos.append('Estatística','4º período')
    discperiodos.append('Estatística','4º período')
    discperiodos.append('Sistemas Operacionais','4º período')
    discperiodos.append('Programação para Internet II','4º período')
    discperiodos.append('Banco de Dados 2','4º período')
    discperiodos.append('Programação para Dispositivos Móveis','4º período')
    discperiodos.append('Modelagem de Software','4º período')
    discperiodos.append('Sistemas Operacionais','4º período')
    discperiodos.append('Programação para Web I','4º período')
    discperiodos.append('Programação Orientada a Objetos II','4º período')
    discperiodos.append('Princípios e Padrões de Projeto','4º período')
    discperiodos.append('Programação Lógica','4º período')
    discperiodos.append('Teoria dos Grafos','4º período')
    discperiodos.append('Sistemas Operacionais','4º período')
    discperiodos.append('Sistemas de Banco de Dados','4º período')
    discperiodos.append('Estatística','4º período')
    discperiodos.append('Programação para Internet','4º período')
    discperiodos.append('Banco de Dados 1','4º período')
    discperiodos.append('Programação Orientada a Objetos 2','4º período')
    discperiodos.append('Sistemas Operacionais','4º período')
    
    for c in componentesCurriculares.keys():
        if (componentesCurriculares[c].periodo_ideal in periodosfoco):
            disciplinasfoco.append(componentesCurriculares[c].nome_ativ)
            
    #disciplinasfoco = ["Arquitetura e Organização de Computadores","Cálculo Diferencial e Integral 1","Cálculo Diferencial e Integral 2","Cálculo Diferencial e Integral 3","Cálculo Numérico","Estatística","Estatística Computacional","Estrutura de Dados 1","Estrutura de Dados 2","Geometria Analítica","Geometria Analítica e Álgebra Linear","Introdução à Programação de Computadores","Linguagens Formais e Autômatos","Lógica para Computação","Matemática 1","Matemática 2","Matemática para Ciência da Computação","Programação Funcional","Programação Lógica","Programação Orientada a Objetos","Programação Orientada a Objetos 1","Programação Procedimental","Sistemas Digitais","Sistemas Operacionais","Álgebra Linear"]
    #print("\\begin{table}\n\\begin{center}\n\\caption{Reprovações por aluno por disciplina}")
    #print("\begin{tabular}{ P{0.4\textwidth} P{0.1\textwidth} P{0.2\textwidth} P{0.2\textwidth} }\nDisciplina & Média de reprovações & Taxa de sucesso no curso dos reprovados& Taxa de sucesso no curso dos aprovados na primeira tentativa\\\\\n\\hline")
    for k in disciplinasfoco:
        rep = (materias[k].contaReprovacoes())
        print(k + " & " + "{:.2f}".format(float( (rep[1]+2*rep[2]+3*rep[3]+4*rep[4]+5*rep[5]+6*rep[6]+7*rep[7])/(rep[1]+rep[2]+rep[3]+rep[4]+rep[5]+rep[6]+rep[7]) )) + " & " +  "{:.2f}".format(materias[k].porcentevade()) + " & " +  "{:.2f}".format(materias[k].aprovamasevade()) +" \\\\")
    #print("\\hline\n\\end{tabular}\n\\end{center}\nFonte: Base de dados da UFU\n\\end{table}")
    retorno.sort()
    return retorno

def adicionaevasaoforma(forma_evasao,tupla):
    if (forma_evasao == "Jubilamento"):
        result = (tupla[0]+1,tupla[1],tupla[2],tupla[3])
    elif (forma_evasao == "Desistência"):
        result = (tupla[0],tupla[1]+1,tupla[2],tupla[3])
    elif (forma_evasao == "Transferência"):
        result = (tupla[0],tupla[1],tupla[2]+1,tupla[3])
    elif (forma_evasao == "Sucesso"):
        result = (tupla[0],tupla[1],tupla[2],tupla[3]+1)
    else:
        result = tupla
    return result


def SucessoIdade(estudantes,matriculasAlunos):
    idades = dict()
    for matr in matriculasAlunos.keys():
        m = matriculasAlunos[matr]
        nasc = estudantes[m.cpf].dt_nascimento
        ingresso = m.dt_ingresso
        if (ingresso != '' and nasc != ''):
            idade = ingresso - nasc
            anos = int(idade.days / 365)
            sucesso = m.forma_evasao
            if anos not in idades.keys():
                idades[anos] = (0,0,0,0)
            idades[anos] = adicionaevasaoforma(sucesso,idades[anos])

    lista = list(idades.keys())
    lista.sort()
    menor18 = [0,0,0,0]
    d18a23 = [0,0,0,0]
    d24a30 = [0,0,0,0]
    maior30 = [0,0,0,0]

    print("\\begin{table}\n\\begin{center}\n\\caption{Forma de saida do estudante por idade ao ingressar}\\label{TabelaIdade}")
    print("\\begin{tabular}{ P{0.18\\textwidth} P{0.18\\textwidth} P{0.18\\textwidth} P{0.18\\textwidth} P{0.18\\textwidth}  }\\Idade ao ingressar & Jubilamento & Desistência & Transferência & Sucesso\\\\\n\\hline")
    labels = ["Jubilamento","Desistência", "Transferência", "Sucesso"]
    
    for i in lista:
        print( str(i) + "&" + str(idades[i][0]) + "&" + str(idades[i][1]) + "&" + str(idades[i][2]) + "&" + str(idades[i][3]) + "\\\\")
        if (i < 18):
            idad = "Menor de 18 anos"
            menor18[0] += idades[i][0]
            menor18[1] += idades[i][1]
            menor18[2] += idades[i][2]
            menor18[3] += idades[i][3]
        elif (i <= 23):
            idad = "18 a 23 anos"
            d18a23[0] += idades[i][0]
            d18a23[1] += idades[i][1]
            d18a23[2] += idades[i][2]
            d18a23[3] += idades[i][3]
        elif (i <= 30):
            idad = "24 a 30 anos"
            d24a30[0] += idades[i][0]
            d24a30[1] += idades[i][1]
            d24a30[2] += idades[i][2]
            d24a30[3] += idades[i][3]
        else:
            idad = "Mais do que 30 anos"
            maior30[0] += idades[i][0]
            maior30[1] += idades[i][1]
            maior30[2] += idades[i][2]
            maior30[3] += idades[i][3]

    print("\\hline\n\\end{tabular}\n\\end{center}\nFonte: Base de dados da UFU de 2004 a 2019\n\\end{table}")       
    print(menor18)
    #plt.title("Forma de saída dos estudantes que ingressaram menores de 18 anos")
    #plt.pie(menor18, labels = labels,autopct='%.1f%%')
    #plt.title("Forma de saída dos estudantes que ingressaram com 18 a 23 anos")
    #plt.pie(d18a23, labels = labels,autopct='%.1f%%')
    #plt.title("Forma de saída dos estudantes que ingressaram com 24 a 30 anos")
    #plt.pie(d18a23, labels = labels,autopct='%.1f%%')
    plt.title("Forma de saída dos estudantes que ingressaram mais do que 30 anos")
    plt.pie(maior30, labels = labels,autopct='%.1f%%')
    plt.show()


def SucessoReentrada(matriculasAlunos):
    cadaum = dict()
    for key in matriculasAlunos.keys():
        a = matriculasAlunos[key]
        if cpf in cadaum.keys():
            if cadaum[cpf][1] > 190:
                print (a.cpf)
            lista = cadaum[cpf][2]
            lista.append(a.forma_evasao)
            if (a.forma_evasao == "Sucesso" or cadaum[cpf][0] == "Sucesso"):
                cadaum[cpf] = ("Sucesso",cadaum[cpf][1] + 1,lista)
            elif (a.forma_evasao != "Cursando"):
                cadaum[cpf] = ("Fracasso",cadaum[cpf][1] + 1,lista)
            else:
                cadaum[cpf] = (cadaum[cpf][0], cadaum[cpf][1], lista) 
        else:
            if (a.forma_evasao == "Sucesso"):
                cadaum[cpf] = ("Sucesso",1,[a.forma_evasao])
            elif (a.forma_evasao != "Cursando"):
                cadaum[cpf] = ("Fracasso",1,[a.forma_evasao])

    print(len(cadaum))
    son = [0,0]
    for c in cadaum.keys():
        if (cadaum[c][0]== "Sucesso" and cadaum[c][1] > 1):
            son[0] += 1
        elif (cadaum[c][0]== "Fracasso" and cadaum[c][1] > 1):
            son[1] += 1
    labels = ["Sucesso","Fracasso"]
    print(son)
    plt.title("Taxa de sucesso de estudantes que entraram mais de uma vez")
    plt.pie(son, labels = labels,autopct='%.2f%%')
    plt.show()
    

def stringpct(decimal):
    f = (int(decimal*100))
    if (f == 0):
        return "0"
    f = str(f)
    f = f[:-2]+"."+f[2:]
    if f[-1] == "0":
        f = f[:-1]
    if f[-1] == "0":
        f = f[:-1]
    if f[-1] == ".":
        f = f[:-1]
    return f

class professor:
    def __init__(self,nome):
        self.nome = nome
        self.formados = 0
        self.evadidos = 0
        self.aprovados = 0
        self.reprovados = 0

    def pctevadido(self):
        if (self.evadidos + self.formados <= 0):
            return 1000
        pct = self.evadidos*100 / float(self.formados + self.evadidos)
        return pct

    def pctreprovado(self):
        if (self.reprovados + self.aprovados <= 0):
            return 1000
        pct = self.reprovados*100 / float(self.aprovados + self.reprovados)
        return pct

    def total(self):
        return (self.aprovados + self.reprovados)
    
def SucessoPorProfessor(docentes,aulas,matriculasAlunos,matriculasComponentes):
    professores = dict()
    institutos = []
    listaprofs = []
    retorno = []

    for doc in docentes.keys():
        novo = professor(doc)
        professores[doc] = novo
        if docentes[doc].lotacao not in institutos:
            institutos.append( docentes[doc].lotacao )
    for mc in matriculasComponentes.keys():
        m = matriculasComponentes[mc]
        id_turma = m.ID_Turma
        turma = aulas[id_turma]
        estudante = m.estudante
        forma_evasao = matriculasAlunos[estudante].forma_evasao
        doc = turma.professor
        if doc in professores.keys():
            prof = professores[doc]
            if (forma_evasao == "Sucesso"):
                prof.formados += 1
            elif (forma_evasao != "Cursando"):
                prof.evadidos += 1
                if m.situacao == "Sucesso":
                    prof.aprovados += 1
                elif m.situacao == "Fracasso":
                    prof.reprovados += 1

    #nomes = list(professores.keys())
    #nomes.sort()
    for prof in professores.keys():
        p = professores[prof]
        if (p.pctevadido() >= 0 and p.pctevadido()<=100 and p.pctreprovado() >= 0 and p.pctreprovado() <= 100):
            listaprofs.append(p)

    listaprofs.sort(key = lambda professor: professor.pctreprovado())
    
    for inst in institutos:
        print("------")
        print(inst)
        print("------")
        i = 0
        if inst == "Faculdade de Ciências Contábeis":
            nomeholder = "FACIC"
        elif inst == "Instituto de Economia e Relações Internacionais":
            nomeholder = "IERI"
        elif inst == "Faculdade de Gestão e Negócios":
            nomeholder = "FAGEN"
        elif inst == "Faculdade de Matemática":
            nomeholder = "FAMAT"
        elif inst == "Faculdade de Computação":
            nomeholder = "FACOM"
        else:
            nomeholder = "OUTRO"
        print("\\begin{table}\n\\begin{center}\n\\caption{Reprovações e evasão por professor - " + nomeholder + "}\\label{TabelaProf"+ nomeholder +"}")
        print("\\begin{tabular}{ P{0.3\\textwidth} P{0.25\\textwidth} P{0.25\\textwidth}  }\\nDocente & Reprovados em suas aulas (em \\%) & Evasão dentre os reprovados (em \\%) \\\\\n\\hline")
    
        for profe in listaprofs:
            prof = profe.nome
            p = professores[prof]
            d = docentes[prof]
            if (p.evadidos + p.formados > 0) and (p.reprovados + p.aprovados > 0) and (d.lotacao == inst):
                i += 1
                retorno.append(100-p.pctreprovado())
                nome = nomeholder + str(i)
                print(nome + " & " + str( p.total() ) + " & " + stringpct(p.pctreprovado()) + " & "+ stringpct(p.pctevadido()) + "\\\\")

        print("\\hline\n\\end{tabular}\n\\end{center}\nFonte: Base de dados da UFU de 2004 a 2019\n\\end{table}")
    return retorno



def comparaprofdisc(reprovacoesprof,reprovacoesdisc):

    y1 = reprovacoesprof
    y1.sort()
    y2 = reprovacoesdisc
    lenprof = len(reprovacoesprof)
    lendisc = len(reprovacoesdisc)
    plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
    x1 = []
    x2 = []
    for y in range(lenprof):
        x1.append(y*lendisc)
    for y in range(lendisc):
        x2.append(y*lenprof)
    
    plt.plot(x1,y1,color = "red",label = "Aprovações por professor")
    #plt.plot(x2,y2,color = "blue",label = "Aprovações por disciplina")
    #plt.title("Comparativo entre reprovações por disciplina e por docente")
    #plt.title("Disciplinas ordenadas por porcentagem de reprovação")
    plt.title("Docentes ordenados por porcentagem de reprovação")
    plt.ylabel("Reprovações (em %)")
    plt.legend()
    plt.show()


def comparasemestres(ano1,sem1,ano2,sem2):
    diferenca = ano2 - ano1
    if (sem1[0] == '1' and sem2[0] == '2'):
        diferenca += 1
    elif (sem1[0] == '2' and sem2[0] == '1'):
        diferenca -= 1
    return diferenca



def TempoParaReprovacao(matriculasComponentes,matricula,anoingresso,semestreingresso,turmas,formaevasao):

    reprovou = False

    semestrereprova = semestreingresso
    anoreprova = anoingresso + 6
    
    for k in matriculasComponentes.keys():
        if ((matriculasComponentes[k].estudante == matricula) and (matriculasComponentes[k].situacao == "Fracasso")):
            ID_Turma = matriculasComponentes[k].ID_Turma
            if not reprovou:
                reprovou = True
                semestrereprova = turmas[ID_Turma].Semestre
                anoreprova = turmas[ID_Turma].Ano
            else:
                if turmas[ID_Turma].Ano < anoreprova:
                    anoreprova = turmas[ID_Turma].Ano
                    semestrereprova = turmas[ID_Turma].Semestre
                elif turmas[ID_Turma].Semestre[0] == '1' and semestrereprova[0] == '2':
                    semestrereprova =  turmas[ID_Turma].Semestre

    primeirarep = comparasemestres(anoingresso,semestreingresso,anoreprova,semestrereprova)

    if reprovou and primeirarep >= 8:
        return 8
    elif ((not reprovou) and formaevasao == "Cursando"):
        return 11
    elif not reprovou:
        return 9
    elif primeirarep < -1:
        return 10
    elif primeirarep == -1:
        return 0
    else:
        return primeirarep
                
        
        

def SituacaoIdealdeMatricula(matriculasAlunos,matriculasComponentes,turmas):   
    primeirareprovacao = [0,0,0,0,0,0,0,0,0,0,0,0]
    labels = ["1°","2°","3°","4°","5°","6°","7°","8°","9° ou +","Formado sem reprovação","Cursando sem reprovação"]
    totalalunos = len(matriculasAlunos)
    print(totalalunos)
    for chave in matriculasAlunos.keys():
        anoingresso = int(matriculasAlunos[chave].ano_ingresso)
        semestreingresso = matriculasAlunos[chave].periodo_ingresso
        formaevasao = matriculasAlunos[chave].forma_evasao
        x = TempoParaReprovacao(matriculasComponentes,chave,anoingresso,semestreingresso,turmas,formaevasao)
        primeirareprovacao[x] += 1

    del(primeirareprovacao[10])

    print(primeirareprovacao)

    plt.bar(labels,primeirareprovacao)
    plt.title("Semestres letivos que leva um estudante a ter a primeira reprovação")
    plt.xlabel("Semestres")
    plt.ylabel("Número de estudantes")
    plt.show()
    


        
exec(open("Classes.py").read())
datapath = 'C:/Users/maxpz/OneDrive/Documents/TCC/Dados/'

aulas = leAula(datapath+"aulas.csv")
componentesCurriculares = leComponentes(datapath+"componentesCurriculares.csv")
cursos = leCursos(datapath+"cursos.csv")
dispensas = leDispensa(datapath+"dispensas.csv")
docentes = leDocente(datapath+"docentes.csv")
estudantes = leEstudante(datapath+"estudantes.csv")
matriculasAlunos = leMatriculaAluno(datapath+"matriculasAluno.csv")
matriculasComponentes = leMatriculasComponentes(datapath+"matriculasComponentes.csv")
prerequisitos = lePreRequisito(datapath+"prerequisitos.csv")
cotas = leCotas(datapath + "ModalidadesCotas.csv")
candidatosVagas = leProcessoSeletivo(datapath + "CandidatosVaga.csv")

anoinicial = 2004
anofinal = 2019

m = dict()
for matr in matriculasAlunos.keys():
    aluno = matriculasAlunos[matr]
    if (aluno.ano_ingresso >= anoinicial-4 and isinstance(aluno.ano_evasao,int) and aluno.ano_evasao<=anofinal):
        m[matr] = aluno
        

c = dict()
for matr in matriculasComponentes.keys():
    if matriculasComponentes[matr].estudante in m:
        c[matr] = matriculasComponentes[matr]


print(len(estudantes))

#SituacaoIdealdeMatricula(matriculasAlunos,matriculasComponentes,aulas)

#reprovacoesprof = SucessoPorProfessor(docentes,aulas,m,c)


#SucessoReentrada(m)

#SucessoIdade(estudantes,m)

    
#reprovacoesdisc = reprovaDisciplina(c, aulas, componentesCurriculares,matriculasAlunos)



#graficoSobrevivencia(m)


#SucessoGenero(m,estudantes)


#SucessoMetodoEntrada( m)

#SucessoConcorrência(candidatosVagas, matriculasAlunos)


#versoes = []
#for matricula in matriculasAlunos.keys():
#    m = matriculasAlunos[matricula]
#    curso = m.curso
#    versao = m.versao_curric
#    tupla = (curso,versao)
#    if (tupla not in versoes):
#        versoes.append(tupla)

#for ver in versoes:
#    print (ver)




#SucessoTempoEstudante(matriculasComponentes,matriculasAlunos,estudantes,componentesCurriculares,aulas)






#Sucesso por disciplina e carga horária
#m = dict()
#for matr in matriculasComponentes.keys():
#    mat = matriculasComponentes[matr]
#    turma = aulas[mat.ID_Turma]
#    for c in componentesCurriculares.keys():
#        cc = componentesCurriculares[c]
#        if (cc.cod_ativ == turma.Cod_Disciplina):
#            tipo_ativ = cc.descr_estrutura
#            break
#    if ( ((tipo_ativ == "Obrigatória") or (tipo_ativ == "Optativa") ) and (turma.Ano != '') and (turma.Ano >= 2004) and (turma.Ano <= 2019) and (turma.Cod_Disciplina != 'GSI085') and (turma.Cod_Disciplina != 'GBC095') and (turma.Cod_Disciplina != 'INF95') and (turma.Cod_Disciplina != 'GSI541')):
#        if (matr not in m.keys()):
#            m[matr] = []
#            m[matr] = (mat)
#SucessoDisciplinas(m,aulas)



#subgrupo = dict()
#for i in matriculasAlunos.keys():
#    m = matriculasAlunos[i]
#    if (m.curso == "1137717BI"):
#        subgrupo[i] = m


#TabelaEntradaESaida(subgrupo, "Entrada e saída acumulada de alunos do curso de Sistemas de Informação de Monte Carmelo",anoinicio=2010)
#GraficoEntradaESaida(subgrupo,"Sistemas de Informação - Monte Carmelo",anoinicio=2010)

#TabelaEntradaESaida(subgrupo, "Entrada e saída acumulada de alunos da FACOM")
#GraficoEntradaESaida(subgrupo,"FACOM")
