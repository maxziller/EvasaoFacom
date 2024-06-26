import datetime

class DocenteAula:
    def __init__ (self,linha):
        att = linha.split(",")
        self.Cod_Disciplina = att[0] #Código da disciplina no sistema
        self.Nome_Disciplina = att[1] #Nome da disciplina no sistema
        self.Cod_Turma = att[2] #Código da turma
        self.Vagas_Oferecidas = int(att[3]) #Quantidade de vagas oferecidas
        self.Cod_Curso = att[4] #Código do curso
        self.Nome_Curso = att[5] #Nome do curso
        self.Codnome_Curso  = att[6] #Nome do curso
        self.ID_Turma  = att[7] #ID da turma aberta
        self.Descricao  = att[8] #Semestre letivo
        self.Ano  = int(att[9]) #Ano letivo
        self.Matricula  = att[10] #Um número que não identifiquei
        self.Nome_Docente = att[11] #Nome do docente a dar a aula
        #self.hash_nome = hash(self.Nome_Docente)
        self.hash_nome = fazhash(self.Nome_Docente)
        if (att[12] == ''):
            self.Dt_Admissao_Cargo = ''
        else:
            self.Dt_Admissao_Cargo = datetime.datetime.strptime(att[12],'%d/%m/%Y').date() #Data de admissão do docente
        self.Titulacao = att[13] #Titulação do docente
        self.Lotacao = att[14] #Faculdade na qual o docente está lotado
        self.Siglateorica = att[15] #Preenchido apenas se a aula tiver carga teórica
        self.Siglapratica = att[16] #Preenchido apenas se a aula tiver carga prática
        self.Vagas_Ocupadas = att[17] #Quantidade de cadeiras ocupadas por alunos
        self.Papeldocente = att[18] #Todos que estão preenchidos estão com 'coordenador', outros estão vazios e não entendi
        self.Email = att[19] #Informação pessoal a ser descartada

class DiscenteEntrada:
    def __init__(self,linha):
        att = linha.split(",")
        self.Sequencia_geral = int(att[0]) #ID autogerada. Desprezar.
        self.Sequencia_curso = int(att[1]) #ID autogerada. Desprezar.
        self.id_pessoa = att[3] #Outra ID. Desprezar.
        self.matr_aluno = att[3]
        #print(self.matr_aluno)
        #self.hash_matricula = hash(self.matr_aluno.strip())
        self.hash_matricula = fazhash(self.matr_aluno)
        self.Login = att[4] #Um número de matrícula que já foi ligado à pessoa. Talvez dê pra aproveitar algo, mas não tem um padrão sobre qual número de matrícula é (se primeiro, se o atual)
        self.Nome_Pessoa = att[5] #Nome do aluno. Anonimizar.
        #self.hash_nome = hash(self.Nome_Pessoa)
        self.hash_nome = fazhash(self.Nome_Pessoa)
        self.CPF = att[6] #CPF da pessoa. Anonimizar.
        #self.hash_cpf = hash(self.CPF)
        self.hash_cpf = fazhash(self.CPF)
        if (self.hash_cpf == 0):
            #self.hash_cpf = hash ( self.Nome_Pessoa + att[10])
            self.hash_cpf = fazhash(self.Nome_Pessoa)
        self.Sexo = att[7] #Char se a pessoa é homem ou mulher
        if (att[8] == ''):
            self.Dt_Nascimento = ''
        else:
            self.Dt_Nascimento = datetime.datetime.strptime(att[8],'%d/%m/%Y').date() #Data de nascimento do estudante
        self.Estado_Civil = att[9] #Informação sobre o estudante
        self.Naturalidade = att[10] #Informação sobre o estudante
        self.Naturalidade_UF = att[11] #Informação sobre o estudante
        self.Nacionalidade = att[12].strip() #Informação sobre o estudante
        self.Email = att[13] #Dado pessoal não útil para o cálculo. Retirar.
        self.Cod_Curso = att[14] #Código do curso no sistema
        if (att[15] == '1097a' or att[15] == '1097A'):
            self.Num_Versao = '1097'
        else:
            self.Num_Versao = att[15] #Número da versão do currículo. Talvez seja útil.
        self.Situacao_Versao = att[16] #Se o currículo está ativo agora ou não
        self.Curso = att[17] #Novamente o curso, dessa vez o nome
        self.Ingresso = att[18] #Descrição completa do ano e semestre do ingresso
        self.Ano_Ingresso = int(att[19]) #Informação muito relevante
        self.Periodo_Ingresso = att[20] #Informação muito relevante
        self.Forma_Ingresso = att[21] #Informação muito relevante
        if (att[22] == ''):
            self.Dt_Ingresso = ''
        else:
            self.Dt_Ingresso = datetime.datetime.strptime(att[22],'%d/%m/%Y').date() #Data exata do ingresso da pessoa. Dá pra usar pra calcular se houve atraso no calendário, talvez?
        self.Evasao = att[23] #Ano e semestre de evasão.
        if (att[24] == ''):
            self.Ano_Evasao = ''
        else:
            self.Ano_Evasao = int(att[24]) #Ano da evasão
        self.Periodo_Evasao = att[25] #Semestre da evasão
        self.Forma_Evasao = att[26] #Forma da evasão
        if (att[27] == ''):
            self.Dt_Evasao = ''
        else:
            self.Dt_Evasao = datetime.datetime.strptime(att[27],'%d/%m/%Y').date() #Data da evasão
        if (att[28] == ''):
            self.Dt_Conclusao = ''
        else:
            self.Dt_Conclusao = datetime.datetime.strptime(att[28],'%d/%m/%Y').date() #Data da conclusão, vazia se o estudante não concluiu
        if (att[29] == ''):
            self.Dt_Colacao = ''
        else:
            self.Dt_Colacao = datetime.datetime.strptime(att[29],'%d/%m/%Y').date() #Data da colação, vazia se o estudante não colou grau
        if (att[30] == ''):
            self.Data_Nascimento = ''
        else:
            self.Data_Nascimento = datetime.datetime.strptime(att[30],'%d/%m/%Y').date() #Data de nascimento de novo, informação redundante
        self.Campus = att[31] #Campus onde estuda, informação não tão relevante


class Historico:
    def __init__(self,linha):
        att = linha.split(";")
        self.id = att[0]
        self.id_curso_aluno = att[1] #Não sei o que diabos é isso ainda
        self.matr_aluno = att[2] #Número de matrícula - IDENTIFICAÇÃO
        self.id_versao_curso = att[3] #Não sei o que é isso
        self.nome_pessoa = att[4] #Nome - IDENTIFICAÇÃO
        self.class_ativ_item = att[5] #Valores possíveis 1, 2, 3 e 5. Não sei o que e.
        self.id_estrutura_cur = att[6] #Não faço ideia do que é isso
        self.ano = att[7] #ano que aconteceu a aula
        self.periodo_item = att[8] #semestre que aconteceu a aula (redundante)
        self.cod_ativ_curric = att[9] #Código da matéria
        self.cod_curso = att[10] #Código do curso no sistema
        self.nome_unidade = att[11] #Nome do curso no sistema
        if (att[22] == '1097a' or att[22] == '1097A'):
            self.num_versao = '1097'
        else:
            self.num_versao = att[12] #Quando tem troca de currículo, muda isso aqui
        self.id_curric_aluno = att[13] #Cada registro tem um, não faz sentido pra mim, não sei o que e
        self.id_ativ_curric = att[14] #Código para o nome de cada matéria.
        self.media_final = att[15] #Nota do aluno
        self.situacao_item = att[16] #Se passou ou não. Agrupar isso aqui. Está em número.
        self.periodo = att[17] #Forma escrita do código de periodo_item
        self.situacao = att[18] #nome de situacao_item (se tá aprovado ou não)
        self.nome_ativ_curric = att[19] #nome da matéria. Algumas se repetem, pois se está em outra versão de currículo, tem outro código. Vai ter que separar atividade extracurricular de aula normal. Dica, nota nula separa de uma forma quase perfeita.
        self.creditos = att[20] #Não sei o que é. Não é nota.
        self.ch_total = att[21] #Carga horária. Muitas atividades extra-curriculares têm carga 0 ou pequena. Prestar atenção. 
        self.id_local_dispensa = att[22] #Código de onde dispensou, nulo quando não é dispensa
        self.conceito = att[23] #Específico, pouco aplicável, retundante pois tudo está na coluna SITUACAO
        self.id_nota = att[24] #Não sei o que é, valores 1 e 2. 2 apenas com notas nula e 0.
        self.descr_estrutura = att[25] #Fala se a matéria é obrigatória, optativa, ou atividade complementar, etc.
        self.forma_evasao = att[26] #Descrição da forma de evasão, incluindo se formado.
        self.nome_curso_diploma = att[27] #Só se é BCC ou BSI
        self.ch_minima = att[28] #Não tem a ver com a carga horária. Não me pergunte o que é, não sei.
        self.descr_versao = att[29] #Mais um jeito de dizer qual é o curso. Separa por campus. Tem dois BCC's diferentes.
        self.modalidade_item = att[30] #Todos os registros têm o número 2
        self.tipo_ativ_item = att[31] #Números de 1 a 18 ou 99, quase todos os registros com 99. Não sei o que é.
        self.total_ch_disc = att[32] #Esse e mais um registro de Carga Horária, mas por algum motivo MUITO MAIS limpo e organizado que os outros
        self.total_cr_disc = att[33] #Vai de 0 a 9 e NULL, não sei o que e
        self.ano_ingresso = att[34] #Ano de entrada, vai de 1995 a 2023
        self.periodo_ingresso = att[35] #primeiro ou segundo semestre
        self.hash_nome = fazhash(self.nome_pessoa)
        
        #self.hash_matricula = hash(self.matr_aluno.strip())
        self.hash_matricula = fazhash(self.matr_aluno)

    def DadoAnonimizado(self):
        dados = ""
        dados += self.hash_nome + ","
        dados += self.hash_matricula + ","
        dados += self.ano_ingresso + ","
        dados += self.periodo_ingresso + ","
        dados += self.ano + ","
        dados += self.periodo_item + ","
        dados += self.periodo + ","
        dados += self.cod_ativ_curric + ","
        dados += self.cod_curso + ","
        dados += self.nome_unidade + ","
        dados += self.num_versao + ","
        dados += self.id_ativ_curric + ","
        dados += self.nome_ativ_curric + ","
        dados += self.media_final + ","
        dados += self.situacao_item + ","
        dados += self.situacao + ","
        dados += self.ch_total + ","
        dados += self.id_local_dispensa + ","
        dados += self.descr_estrutura + ","
        dados += self.forma_evasao + ","
        dados += self.nome_curso_diploma + ","
        dados += self.total_ch_disc + "\n"
        return dados

class ComponenteCurricular:
    def __init__(self,cod_ativ,num_versao,cod_curso,nome_ativ,descr_estrutura,total_ch_disc,periodo_ideal):
        self.cod_ativ = cod_ativ
        if (num_versao == '1097a'):
            self.versao = '1097'
        else:
            self.versao_curric = num_versao
        self.cod_curso = cod_curso
        self.nome_ativ = nome_ativ
        self.descr_estrutura = descr_estrutura
        if (total_ch_disc == ''):
            self.ch_prevista = None
        else:
            self.ch_prevista = int(total_ch_disc)
        self.periodo_ideal = periodo_ideal

    def TextoArquivo(self):
        texto = self.cod_ativ
        texto += "," + self.versao_curric
        texto += "," + self.cod_curso
        texto += "," + self.nome_ativ
        texto += "," + self.descr_estrutura
        if (self.ch_prevista == None):
            texto += ","
        else:
            texto += "," + str(self.ch_prevista)
        if (self.periodo_ideal == None):
            texto += ","
        else:
            texto += "," + self.periodo_ideal
        return texto

def leComponentes(arquivo):
    componentes = dict()
    f = open(arquivo, mode="r", encoding="utf8")
    primeira = True
    for line in f:
        if (primeira):
            primeira = False
        else:
            linha = leLinha(line)
            if (linha[5] == 'None'):
                l2 = ''
            else:
                l2 = linha[5]
            if (linha[6] == 'None'):
                l6 = ''
            else:
                l6 = linha[6]
            novo = ComponenteCurricular(linha[0],linha[1],linha[2],linha[3],linha[4],l2,l6)
            componentes[linha[0],linha[2]] = novo
    return componentes
    
class MatriculaComponente:
    def __init__(self,ID_Turma,estudante,situacao,media_final,ch_cumprida):
        self.ID_Turma = ID_Turma
        self.estudante = estudante
        self.situacao = situacao
        if (media_final == ''):
            self.media_final = None
        else:
            self.media_final = int(media_final)
        if (ch_cumprida == ''):
            self.ch_cumprida = None
        else:
            self.ch_cumprida = int(float(ch_cumprida))

    def TextoArquivo(self):
        texto = str(self.ID_Turma)
        texto += "," + str(self.estudante)
        texto += "," + self.situacao
        texto += ","
        if (self.media_final != None):
            texto += str(self.media_final)
        texto += "," 
        if (self.media_final != None):
            texto += str(self.ch_cumprida)
        return texto

def leMatriculasComponentes(arquivo):
    matriculas = dict()
    f = open(arquivo, mode="r", encoding="utf8")
    primeira = True
    for line in f:
        if (primeira):
            primeira = False
        else:
            linha = leLinha(line)
            #print(linha)
            if (linha[3] == 'None'):
                l4 = ''
            else:
                l4 = linha[3]
            if (linha[4] == 'None'):
                l5 = ''
            else:
                l5 = linha[4]
            novo = MatriculaComponente(linha[0],linha[1],linha[2],l4,l5)
            matriculas[linha[0],linha[1],linha[2]] = novo
    return matriculas

class Curso:
    def __init__(self,cod_curso,nome_curso,campus):
        self.cod_curso = cod_curso
        self.nome_curso = nome_curso
        self.campus = campus
        if ("monte" in campus.lower()):
            self.turno = "Integral"
        elif ("sistema" in nome_curso.lower()):
            self.turno = "Noturno"
        else:
            self.turno = "Integral"

    def TextoArquivo(self):
        texto = self.cod_curso
        texto += "," + self.nome_curso
        texto += "," + self.campus
        texto += "," + self.turno
        return texto

def leCursos(arquivo):
    cursos = dict()
    f = open(arquivo, mode="r", encoding="utf8")
    primeira = True
    for line in f:
        if (primeira):
            primeira = False
        else:
            linha = leLinha(line)
            novo = Curso(linha[0],linha[1],linha[2])
            cursos[linha[0]] = novo
    return cursos

class MatriculaAluno:
    def __init__(self,matr_aluno,cpf_aluno,curso,dt_ingresso,ano_ingresso,periodo_ingresso,forma_ingresso,forma_evasao,dt_evasao,ano_evasao,periodo_evasao,dt_conclusao,dt_colacao,versao_curric = ""):
        self.matr_aluno = matr_aluno
        self.cpf = cpf_aluno
        self.curso = curso.replace("Graduação em ","")
        if (dt_ingresso != ''):
            self.dt_ingresso = dt_ingresso
        else:
            self.dt_ingresso = ''
        self.ano_ingresso = int(ano_ingresso)
        self.periodo_ingresso = periodo_ingresso
        self.forma_ingresso = forma_ingresso.replace("Processo Seletivo: ","")
        self.dt_evasao = dt_evasao
        if ( (ano_evasao != "") and (ano_evasao != "None")):
            self.ano_evasao = int(ano_evasao)
        else:
            self.ano_evasao = None
        self.periodo_evasao = periodo_evasao
        self.forma_evasao = forma_evasao
        self.dt_evasao = dt_evasao
        self.dt_conclusao = dt_conclusao
        self.dt_colacao = dt_colacao
        if (versao_curric != ""):
            if (versao_curric.upper == '1097A'):
                self.versao_curric = '1097'
            else:
                self.versao_curric = versao_curric
        else:
            if (self.curso == '115728BN'):
                if (self.ano_ingresso >= 2016 and (self.ano_ingresso < 2022 or (self.ano_ingresso == 2022 and self.periodo_ingresso == '2° Semestre'))):
                    self.versao_curric = '2016-1'
                elif (self.ano_ingresso > 2022):
                    self.versao_curric = '2022-2'
                else:
                    self.versao_curric = '2009-1'
            elif (self.curso == '1452BI'):
                if (self.ano_ingresso < 2012 and (self.ano_ingresso == 2011 or (self.ano_ingresso == 2010 and self.periodo_ingresso == '2° Semestre'))):
                    self.versao_curric = '2010-2'
                elif (self.ano_ingresso < 2010 or (self.ano_ingresso == 2010 and self.periodo_ingresso == '1° Semestre')):
                    self.versao_curric = '1097'
                elif (self.ano_ingresso >= 2012 and ano_ingresso < 2016):
                    self.versao_curric = '2012-1'
                else:
                    self.versao_curric = '2023-1'
            else:
                if (self.ano_ingresso < 2014):
                    self.versao_curric = '2011-1'
                elif (self.ano_ingresso < 2016):
                    self.versao_curric = '2014-1'
                elif (self.ano_ingresso < 2022 or (self.ano_ingresso == 2022 and self.periodo_ingresso == '1° Semestre')):
                    self.versao_curric = '2016-1'
                else:
                    self.versao_curric = '2022-2'

    def add_versao(self,versao):
        if (versao.upper() == '1097A'):
            self.versao_curric = '1097'
        else:
            self.versao_curric = versao


    def TextoArquivo(self):
        texto = str(self.matr_aluno)
        texto += "," + str(self.cpf)
        texto += "," + self.curso
        if (self.dt_ingresso == ''):
            texto += ","
        else:
            texto += "," + self.dt_ingresso.strftime('%d/%m/%Y')
        texto += "," + str(self.ano_ingresso)
        texto += "," + self.periodo_ingresso
        texto += "," + self.forma_ingresso
        texto += "," + self.forma_evasao
        if (self.dt_evasao == ''):
            texto += ","
        else:
            texto += "," + self.dt_evasao.strftime('%d/%m/%Y')
        texto += "," + str(self.ano_evasao)
        texto += "," + self.periodo_evasao
        if (self.dt_conclusao == ''):
            texto += ","
        else:
            texto += "," + self.dt_conclusao.strftime('%d/%m/%Y')
        if (self.dt_colacao == ''):
            texto +=","
        else:
            texto += "," + self.dt_colacao.strftime('%d/%m/%Y')
        texto += "," + self.versao_curric
        return texto

def leMatriculaAluno(arquivo):
    matriculas = dict()
    f = open(arquivo, mode="r", encoding="utf8")
    primeira = True
    for line in f:
        if (primeira):
            primeira = False
        else:
            linha = leLinha(line)
            if (linha[8] == ''):
                l8 = ''
            else:
                l8 = datetime.datetime.strptime(linha[8], '%d/%m/%Y').date()
            if (linha[11] == ''):
                l11 = ''
            else:
                l11 = datetime.datetime.strptime(linha[11], '%d/%m/%Y').date()
            if (linha[12] == ''):
                l12 = ''
            else:
                l12 = datetime.datetime.strptime(linha[12], '%d/%m/%Y').date()
            if (linha[3] == ''):
                l3 = ''
            else:
                l3 = datetime.datetime.strptime(linha[3], '%d/%m/%Y').date()
            novo = MatriculaAluno(linha[0],linha[1],linha[2],l3,linha[4],linha[5],linha[6],linha[7],l8,linha[9],linha[10],l11,l12,versao_curric = linha[13])
            matriculas[linha[0]] = novo
    f.close()
    return matriculas

class Aula:
    def __init__(self,ID_Turma, Cod_Disciplina, Cod_Curso, professor, Cod_Turma, Vagas_Oferecidas, Descricao, Ano, Vagas_Ocupadas, Siglateorica, Siglapratica):
        self.ID_Turma = ID_Turma
        self.Cod_Disciplina = Cod_Disciplina
        self.Cod_Curso = Cod_Curso
        if (professor == '0'):
            self.professor = None
        else:
            self.professor = professor
        self.Cod_Turma = Cod_Turma
        self.Vagas_Oferecidas = int(Vagas_Oferecidas)
        self.Semestre = Descricao
        self.Ano = int(Ano)
        self.Vagas_Ocupadas = int(Vagas_Ocupadas)
        self.Teorica = Siglateorica
        self.Pratica = Siglapratica

    def LocaProfessor(self,professor):
        self.professor = professor


    def TextoArquivo(self):
        texto = str(self.ID_Turma)
        texto += "," + self.Cod_Disciplina
        texto += "," + self.Cod_Curso
        if (self.professor == None):
            texto += ","
        else:
            texto += "," + self.professor
        texto += "," + str(self.Cod_Turma)
        texto += "," + str(self.Vagas_Oferecidas)
        texto += "," + self.Semestre
        texto += "," + str(self.Ano)
        texto += "," + str(self.Vagas_Ocupadas)
        texto += "," + self.Teorica
        texto += "," + self.Pratica
        return texto


def leAula(arquivo):
    aulas = dict()
    f = open(arquivo, mode="r", encoding="utf8")
    primeira = True
    for line in f:
        if (primeira):
            primeira = False
        else:
            linha = leLinha(line)
            if (linha[3] == ''):
                l3 = None
            else:
                l3 = linha[3]
            novo = Aula(linha[0],linha[1],linha[2],l3,linha[4],linha[5],linha[6],linha[7],linha[8],linha[9],linha[10])
            aulas[linha[0]] = novo
    f.close()
    return aulas

class Dispensa:
    def __init__(self,estudante,disciplina,versao_curric,cod_curso,dispensa):
        self.estudante = estudante
        self.disciplina = disciplina
        self.versao_curric = versao_curric
        self.cod_curso = cod_curso
        self.dispensa = dispensa

    def TextoArquivo(self):
        texto = str(self.estudante)
        texto += ","+self.disciplina
        texto += ","+self.versao_curric
        texto += ","+self.cod_curso
        texto += ","+self.dispensa
        return texto

def leDispensa(arquivo):
    dispensas = dict()
    f = open(arquivo, mode="r", encoding="utf8")
    primeira = True
    for line in f:
        if (primeira):
            primeira = False
        else:
            linha = leLinha(line)
            novo = Dispensa(linha[0],linha[1],linha[2],linha[3],linha[4])
            dispensas[linha[0],linha[1],linha[2],linha[3]] = novo
    f.close()
    return dispensas

class Estudante:
    def __init__(self, hash_nome, hash_cpf, genero, dt_nascimento, estado_civil, naturalidade, naturalidade_uf, nacionalidade):
        self.matriculas = []
        self.nome = hash_nome
        self.cpf = hash_cpf #Key
        self.genero = genero
        if (dt_nascimento != ''):
            self.dt_nascimento = datetime.datetime.strptime(dt_nascimento, '%d/%m/%Y').date()
        else:
            self.dt_nascimento = ''
        self.estado_civil = estado_civil
        self.naturalidade = naturalidade
        self.naturalidade_uf = naturalidade_uf
        self.nacionalidade = nacionalidade

    def TextoArquivoEstudante(self):
        texto = str(self.cpf)
        texto += "," + str(self.nome)
        texto += "," + self.genero
        if self.dt_nascimento != '':
            texto += "," + self.dt_nascimento.strftime('%d/%m/%Y')
        else:
            texto += ","
        texto += "," + self.estado_civil
        texto += "," + self.naturalidade
        texto += "," + self.naturalidade_uf
        texto += "," + self.nacionalidade
        return texto

    def TextoArquivoEstudanteMatricula(self):        
        for matricula in self.matriculas:
            texto += str(self.cpf) + "," + str(matricula) + "\n"
        return texto

    def AdicionaMatricula(self,matricula):
        if (matricula not in self.matriculas):
            self.matriculas.append(matricula)

def leEstudante(arquivo):
    estudantes = dict()
    f = open(arquivo, mode="r", encoding="utf8")
    primeira = True
    for line in f:
        if (primeira):
            primeira = False
        else:
            linha = leLinha(line)
            novo = Estudante(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7])
            estudantes[linha[0]] = novo
    f.close()
    return estudantes



def leLinha(line):
    linha = line.strip()
    linha = linha.replace(";","")
    linha = linha.split(",")
    return linha

class Docente:
    def __init__(self, hash_nome, dt_admissao_cargo, titulacao, lotacao):
        self.nome = hash_nome
        self.dt_admissao = dt_admissao_cargo
        self.titulacao = titulacao
        self.lotacao = lotacao

    def TextoArquivo(self):
        texto = str(self.nome)
        if (self.dt_admissao == ''):
            texto += ","
        else:
            texto += "," + self.dt_admissao.strftime('%d/%m/%Y')
        texto += "," + self.titulacao
        texto += "," + self.lotacao
        if ("0,,," not in texto):
            return texto
        else:
            return ''

def leDocente(arquivo):
    docentes = dict()
    f = open(arquivo, mode="r", encoding="utf8")
    primeira = True
    for line in f:
        if (primeira):
            primeira = False
        else:
            linha = leLinha(line)
            novo = Docente(linha[0],datetime.datetime.strptime(linha[1], '%d/%m/%Y').date(),linha[2],linha[3])
            docentes[linha[0]] = novo
    f.close()
    return docentes

class PreRequisito:
    def __init__(self,cod_ativ,prerequisito,versao_curric,curso):
        self.cod_ativ = cod_ativ
        self.pre_requisito = prerequisito
        self.versao_curric = versao_curric
        self.curso = curso

    def TextoArquivo(self):
        texto = self.cod_ativ
        texto += "," + self.pre_requisito
        texto += "," + self.versao_curric
        texto += "," + self.curso
        return texto

def lePreRequisito(arquivo):
    preRequisitos = []
    f = open(arquivo, mode="r", encoding="utf8")
    primeira = True
    for line in f:
        if (primeira):
            primeira = False
        else:
            linha = leLinha(line)
            novo = PreRequisito(linha[0],linha[1],linha[2],linha[3])
            preRequisitos.append(novo)
    f.close()
    return preRequisitos

class ProcessoSeletivo:
    def __init__(self,cod_curso,nome_ps,ano_ingresso,semestre_ingresso,modalidade_cota,vagas,candidatos):
        self.cod_curso = cod_curso
        self.nome_ps = nome_ps
        self.ano_ingresso = ano_ingresso
        self.semestre_ingresso = semestre_ingresso
        self.modalidade_cota = modalidade_cota
        self.vagas = int(vagas)
        self.candidatos = int(candidatos)

def leProcessoSeletivo(arquivo):
    pss = dict()
    f = open(arquivo,mode="r", encoding="utf8")
    primeira = True
    for line in f:
        if (primeira):
            primeira = False
        else:
            linha = leLinha(line)
            novo = ProcessoSeletivo(linha[0],linha[3],linha[1],linha[2],linha[6],linha[4],linha[5])
            pss[linha[0],linha[3],linha[1],linha[2],linha[6]] = novo
    return pss

class Cota:
    def __init__(self,cod_cota,nome,escola_publica,racial,economica):
        self.cod_cota = cod_cota
        self.nome = nome
        self.escola_publica = transfbool(escola_publica)
        self.racial = transfbool(racial)
        self.economica = transfbool(economica)

def transfbool(string):
    if (string.upper() == "FALSE"):
        return False
    else:
        return True

def leCotas(arquivo):
    cotes = dict()
    f = open(arquivo,mode="r", encoding="utf8")
    primeira = True
    for line in f:
        if (primeira):
            primeira = False
        else:
            linha = leLinha(line)
            novo = Cota(linha[0],linha[1],linha[2],linha[3],linha[4])
            cotes[linha[0]] = novo
    return cotes 
