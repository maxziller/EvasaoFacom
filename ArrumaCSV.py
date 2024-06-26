import os
import hashlib


def fazhash(string):
    result = hashlib.md5(string.encode())
    return result.hexdigest()
        

def tiraaspas(line):
    linha = line
    aspa1 = linha.find('"')
    if (aspa1 >= 0):
            aspa2 = linha[aspa1 + 1:].find('"') + aspa1
            palavra = linha[aspa1:aspa2+2]
            novo = palavra.replace('"','')
            novo = novo.replace(',','~')
            novo = novo.replace(';','~')
            linha = linha.replace(palavra,novo)
            return linha
    else:
        return linha


def limpalinha(line):
    linha = line.strip()
    linha = tiraaspas(linha)
    linha = linha.replace('"','')
    linha = linha.replace('"','')
    linha = linha.replace("'","")
    #linha = linha.replace(",","','")
    linha = linha.replace(",'',",",,")
    linha = linha.replace(",' ',",",,")
    return linha

pathHistoricos = 'C:/Users/Max Ziller/OneDrive/Documents/TCC/Históricos/'
pathAlunos = 'C:/Users/Max Ziller/OneDrive/Documents/TCC/Discentes/'
pathAulas = 'C:/Users/Max Ziller/OneDrive/Documents/TCC/Docentes que ofertaram as disciplinas/'
pathGrades = 'C:/Users/Max Ziller/OneDrive/Documents/TCC/Períodos/'
pathRequis = 'C:/Users/Max Ziller/OneDrive/Documents/TCC/Pré-requisitos/'
exec(open("Classes.py").read())

historicos = []
alunos = []
professores = []
prerequis = []

for file in (os.listdir(pathRequis)):

    primeira = True
    with open(pathRequis+file, 'r', encoding="utf8") as f:
        
        for line in f:
            linha = leLinha(line)
            novo = PreRequisito(linha[0],linha[1],linha[2],linha[3])
            if novo not in prerequis:
                prerequis.append(novo)
        
    f.close()

for file in (os.listdir(pathHistoricos)):

    primeira = True
    with open(pathHistoricos+file, 'r', encoding="utf8") as f:
        
        for line in f:
            if primeira:
                primeira = False
                titulo = line.strip()
                linha = titulo
                
            else:
                anterior = linha
                linha = limpalinha(line)
                novo = Historico(linha)     
                historicos.append(novo)
        
    f.close()

for file in (os.listdir(pathAulas)):

    i = 0
    primeira = True
    with open(pathAulas+file, 'r', encoding="utf8") as f:
        
        for line in f:
            i += 1
            if primeira:
                primeira = False
                titulo = line.strip()
                
            else:
                linha = limpalinha(line)
                novo = DocenteAula(linha)
                professores.append(novo)
    f.close()

for file in (os.listdir(pathAlunos)):

    primeira = True
    with open(pathAlunos+file, 'r', encoding="utf8") as f:

        for line in f:
            if primeira:
                primeira = False
                titulo = line.strip()
            else:
                linha = limpalinha(line)
                novo = DiscenteEntrada(linha)
                alunos.append(novo)

grades = dict()

for file in (os.listdir(pathGrades)):

    linha = 0
    with open(pathGrades+file, 'r', encoding="utf8") as f:
        for line in f:
            linha += 1
            if (linha == 1):
                curss = leLinha(line)[0]
            elif (linha == 2):
                campuss = leLinha(line)[0]
            elif (linha == 3):
                curriculs = leLinha(line)[0]
            else:
                t = line.strip()
                if ((len(t) > 0) and (t[0].isdigit())):
                    periodo = line.replace(":","")
                elif ('optativa' in line.lower()):
                    periodo = 'Optativa'
                elif(len(t)>0):
                    l = t.split('-',1)
                    codigo = l[0].replace(" ","")
                    codigo = codigo.upper()
                    grades[curss,campuss,curriculs,codigo] = periodo.strip().lower()
        
    f.close()


def compareperiodo(periodo1,periodo2):
    periodos = ["Ano","1° Per. Esp.","2° Per. Esp.","1° Semestre","2° Semestre"]
    if (periodos.index(periodo1) > periodos.index(periodo2)):
        return True
    else:
        False

componentesCurriculares = dict() #Feito
matriculasComponentes = dict()
cursos = dict() #Feito
estudantes = dict() #Feito
matriculasAluno = dict()  #Feito
aulas = dict()#Feito
docentes = dict() #Feito
dispensas = dict() #Feito

for aluno in alunos:
    if (aluno.hash_cpf not in estudantes.keys()):
        novo = Estudante(aluno.hash_nome, aluno.hash_cpf, aluno.Sexo, aluno.Dt_Nascimento.strftime('%d/%m/%Y'), aluno.Estado_Civil, aluno.Naturalidade, aluno.Naturalidade_UF, aluno.Nacionalidade)
        estudantes[aluno.hash_cpf] = novo
    tirado = ["Cancelamento de Matrícula - Mandado Segurança","Cancelamento por indeferimento de renda","Jubilamento"]
    saiu = ["Abandono","Desistente","Desistente Oficial","Desligamento","Desligamento Convênio","Falecimento","Ingressante/Não Compareceu"]
    formou = ["Formado"]
    buscando = ["Mobilidade Acadêmica","Transferência Interna","Transferido"]
    cursando = ["Aluno com Vínculo"]
    evasao = aluno.Forma_Evasao
    if (evasao in tirado):
        ev = "Jubilamento"
    elif (evasao in saiu):
        ev = "Desistência"
    elif (evasao in formou):
        ev = "Sucesso"
    elif (evasao in buscando):
        ev = "Transferência"
    else:
        ev = "Cursando"
    novo = MatriculaAluno(aluno.hash_matricula,aluno.hash_cpf,aluno.Cod_Curso,aluno.Dt_Ingresso,aluno.Ano_Ingresso,aluno.Periodo_Ingresso,aluno.Forma_Ingresso,ev,aluno.Dt_Evasao,aluno.Ano_Evasao,aluno.Periodo_Evasao,aluno.Dt_Conclusao,aluno.Dt_Colacao)
    matriculasAluno[aluno.hash_matricula] = novo
    if (aluno.Cod_Curso not in cursos.keys()):
        if ((aluno.Curso == 'Graduação em Sistemas de Informação: Bacharelado - Noturno') or (aluno.Curso == 'Graduação em Sistemas de Informação: Bacharelado - Integral - Monte Carmelo')):
            grad = 'Sistemas de Informação'
        else:
            grad = 'Ciência da Computação'
        novo = Curso(aluno.Cod_Curso,grad,aluno.Campus)
        cursos[aluno.Cod_Curso] = novo
    

for aula in professores:
    novo = Aula(aula.ID_Turma, aula.Cod_Disciplina, aula.Cod_Curso, aula.Nome_Docente, aula.Cod_Turma, aula.Vagas_Oferecidas, aula.Descricao, aula.Ano, aula.Vagas_Ocupadas, aula.Siglateorica, aula.Siglapratica)
    aulas[aula.ID_Turma] = novo
    if (aula.hash_nome not in docentes.keys()):
        instituto = aula.Lotacao
        if (instituto == "Diretoria de Processamento de Dados"):
            instituto = "Faculdade de Computação"
        elif (instituto == "Graduação em Sistemas de Informação: Bacharelado - Noturno"):
            instituto = "Faculdade de Computação"
        elif (instituto == "Coordenação do Curso de Graduação em Ciência da Computação"):
            instituto = "Faculdade de Computação"
        elif (instituto == "Coordenação do Curso de Graduação em Matemática"):
            instituto = "Faculdade de Matemática"
        elif (instituto == "Coordenação do Programa de Pós-Graduação em Ciência da Computação"):
            instituto = "Faculdade de Computação"
        novo = Docente(aula.hash_nome, aula.Dt_Admissao_Cargo, aula.Titulacao, aula.Lotacao)
        if(aula.hash_nome != '0'):
            docentes[novo.nome] = novo


aulasporhorario = dict()


for unid in aulas.keys():
    classe = aulas[unid]
    chave = (classe.Cod_Disciplina,classe.Ano,classe.Semestre)
    if chave in aulasporhorario.keys():
        aulasporhorario[chave].append(unid)
    else:
        lista = []
        lista.append(unid)
        aulasporhorario[chave] = lista

for au in aulasporhorario.keys():
    l = aulasporhorario[au]
    if (len(l) < 2):
        professor = aulas[l[0]].professor
    else:
        professor = aulas[l[0]]
        for fessor in l:
            if professor != aulas[fessor].professor:
                professor = ''
    for t in aulasporhorario[au]:
        turma = aulas[t]
        turma.LocaProfessor(professor)


materias = ["Complementação de Estudos","Disciplinas utilizadas para Aproveitamento","Núcleo de Formação Básica","Núcleo de Formação Gerencial","Núcleo de Formação Humanística e Complementar","Núcleo de Formação Tecnológica","Obrigatórias"]
optativas = ["Disciplina(s) de Outro(s) Currículo(s) do Curso","Disciplina(s) de Outro(s) Curso(s)","Optativa","Optativas","Optativas do Núcleo de Ciências Exatas","Optativas do Núcleo de Ciências Sociais"]
atividadesextra = ["Atividades Complementares","Atividades Curriculares de Extensão"]
situacoesacad = ["Situação Academica","Situação Acadêmica"]
for hist in historicos:
    if hist.hash_matricula not in matriculasAluno.keys():
        if (hist.cod_curso == '1452BI'):
            versao = '2012-1'
        else:
            versao = '2022-2'
        ingresso = datetime.datetime(2023, 2, 27)
        novamatr = MatriculaAluno(hist.hash_matricula,hist.hash_matricula,hist.cod_curso,ingresso,'2022','2° Semestre','','','','','','','',versao)
        matriculasAluno[hist.hash_matricula] = novamatr
        novapes = Estudante(hist.hash_matricula,hist.hash_nome,'','','','','','')
        estudantes[hist.hash_matricula] = novapes
    else:
        if (hist.num_versao != ''):
            matriculasAluno[hist.hash_matricula].add_versao(hist.num_versao)
    if hist.descr_estrutura in materias:
        tipo = "Obrigatória"
    elif hist.descr_estrutura in optativas:
        tipo = "Optativa"
    elif hist.descr_estrutura in atividadesextra:
        tipo = "Atividade extra-curricular"
    elif hist.descr_estrutura in situacoesacad:
        tipo = "Situação Acadêmica"
    else:
        tipo = hist.descr_estrutura
    if 'trancamento ' in hist.nome_ativ_curric.lower():
        tipo = "Situação Acadêmica"

    curss = hist.nome_curso_diploma.replace("Graduação em ","")
    if ('monte' in hist.descr_versao.lower()):
        campss = 'Campus Monte Carmelo'
    else:
        campss = 'Campus Santa Mônica'
    if ((curss,campss,hist.num_versao,hist.cod_ativ_curric.upper()) in grades.keys()):
        periodo_ideal = grades[curss,campss,hist.num_versao,hist.cod_ativ_curric.upper()]
    else:
        periodo_ideal = None
    if (hist.cod_ativ_curric not in componentesCurriculares.keys()):
        if (hist.num_versao == '1097A' or hist.num_versao == '1097a'):
            versao = '1097'
        else:
            versao = hist.num_versao
        novo = ComponenteCurricular(hist.cod_ativ_curric,versao,hist.cod_curso,hist.nome_ativ_curric,tipo,hist.total_ch_disc,periodo_ideal)
        componentesCurriculares[hist.cod_ativ_curric, versao, hist.cod_curso] = novo
    if (hist.id_local_dispensa == '' or hist.id_local_dispensa == None):
        chave = (hist.cod_ativ_curric,int(hist.ano),hist.periodo)
        if (chave in aulasporhorario.keys()):
            l = aulasporhorario[chave]
            if (len(l) == 1):
                turma = aulas[l[0]].ID_Turma
            else:
                turma = str(hash(chave))
        else:
            turma = str(hash(chave))

        if(turma not in aulas.keys()):
            novo = Aula(turma, hist.cod_ativ_curric, hist.cod_curso, '', '', 0,hist.periodo, hist.ano, '0', '', '')
            aulas[turma] = novo
        aprovados = ["Apr. s/nt","Aprov.Freq","Aprovado","C/Aprov.","Dispensado","Eq.curric.",]
        reprovados = ["Repr. RM","Repr. s/nt","Reprovado","S/Aprov.","Sem nota","Tr. Total","Tr.Parcial"]
        cursando = ["Cursando","Matrícula","Repr.Freq.","Vínculo"]
        if (hist.situacao in aprovados):
            situ = "Sucesso"
        elif (hist.situacao in reprovados):
            situ = "Fracasso"
        else:
            situ = "Cursando"
        novo = MatriculaComponente(turma,hist.hash_matricula,situ,hist.media_final,hist.ch_total)
        matriculasComponentes[novo.ID_Turma,hist.nome_ativ_curric,hist.matr_aluno] = novo
    else:
        novo = Dispensa(hist.hash_matricula,hist.cod_ativ_curric,hist.num_versao,hist.cod_curso,hist.id_local_dispensa)
        dispensas[hist.hash_matricula,hist.cod_ativ_curric] = novo

    
path = "C:/Users/Max Ziller/OneDrive/Documents/TCC/Dados/"

fileC = open(path+"componentesCurriculares.csv", "w", encoding="utf8")
fileC.write("cod_ativ,versao_curric,cod_curso,nome_ativ,descr_estrutura,ch_prevista,periodo_ideal\n")
for c in componentesCurriculares.keys():
    fileC.write(componentesCurriculares[c].TextoArquivo())
    fileC.write("\n")
fileC.close()

fileC = open(path+"matriculasComponentes.csv", "w", encoding="utf8")
fileC.write("ID_Turma,estudante,situacao,media_final,ch_cumprida\n")
for c in matriculasComponentes.keys():
    fileC.write(matriculasComponentes[c].TextoArquivo())
    fileC.write("\n")
fileC.close()

fileC = open(path+"cursos.csv", "w", encoding="utf8")
fileC.write("cod_curso,nome_curso,campus,turno\n")
for c in cursos.keys():
    fileC.write(cursos[c].TextoArquivo())
    fileC.write("\n")
fileC.close()

fileC = open(path+"aulas.csv", "w", encoding="utf8")
fileC.write("ID_Turma, Cod_Disciplina, Cod_Curso, Professor, Cod_Turma, Vagas_Oferecidas, Semestre, Ano, Vagas_Ocupadas, Siglateorica, Siglapratica\n")
for c in aulas.keys():
    fileC.write(aulas[c].TextoArquivo())
    fileC.write("\n")
fileC.close()

fileC = open(path+"estudantes.csv", "w", encoding="utf8")
fileC.write("hash_cpf, hash_nome, genero, dt_nascimento, estado_civil, naturalidade, naturalidade_uf, nacionalidade\n")
for c in estudantes.keys():
    fileC.write(estudantes[c].TextoArquivoEstudante())
    fileC.write("\n")
fileC.close()

fileC = open(path+"dispensas.csv", "w", encoding="utf8")
fileC.write("estudante,id_ativ,versao_curric,cod_curso,local_dispensa\n")
for c in dispensas.keys():
    fileC.write(dispensas[c].TextoArquivo())
    fileC.write("\n")
fileC.close()

fileC = open(path+"matriculasAluno.csv", "w", encoding="utf8")
fileC.write("hash_matricula,hash_cpf,curso,dt_ingresso,ano_ingresso,periodo_ingresso,forma_ingresso,forma_evasao,dt_evasao,ano_evasao,periodo_evasao,dt_conclusao,dt_colacao,versao_curric\n")
for c in matriculasAluno.keys():
    fileC.write(matriculasAluno[c].TextoArquivo())
    fileC.write("\n")
fileC.close()

fileC = open(path+"docentes.csv", "w", encoding="utf8")
fileC.write("hash_nome, dt_admissao_cargo, titulacao, lotacao\n")
for c in docentes.keys():
    textoa = docentes[c].TextoArquivo()
    textob = textoa.replace(',','')
    if (textob != ''):
        fileC.write(textoa)
        fileC.write("\n")
fileC.close()

fileP = open(path+"prerequisitos.csv", "w", encoding="utf8")
fileP.write("cod_ativ, pre_requisito, versao_curric, cod_curso\n")
for c in prerequis:
    fileP.write(c.TextoArquivo())
    fileP.write("\n")
fileP.close()

