import sqlite3 as sql

# Criar a conexão com o banco de dados (ou criar o banco se não existir)
con = sql.connect('db_brisa.db')
cur = con.cursor()

# Criar a tabela com os campos
cur.execute('DROP TABLE IF EXISTS tb_adm')

sql_adm = '''CREATE TABLE "tb_adm" (
    "id_usuario" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome_usuario" VARCHAR(200) NOT NULL,
    "cpf" VARCHAR(11) NOT NULL,
    "email" VARCHAR(150) UNIQUE NOT NULL,
    "senha_hash" VARCHAR(255) NOT NULL,
    "funcao" VARCHAR(100),
    "status" BOOLEAN DEFAULT TRUE
)'''

cur.execute(sql_adm)

cur.execute('DROP TABLE IF EXISTS tb_cliente')

sql_cliente = '''CREATE TABLE "tb_cliente" (
    "id_cliente" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome" VARCHAR(200) NOT NULL,
    "cpf_cnpj" VARCHAR(20) NOT NULL UNIQUE,
    "email" VARCHAR(150) UNIQUE NOT NULL,
    "telefone" VARCHAR(20) NOT NULL,
    "endereco" VARCHAR(200) NOT NULL,
    "cep" VARCHAR(8) NOT NULL,
    "cidade" VARCHAR(100) NOT NULL,
    "estado" VARCHAR(200) NOT NULL,
    "numero" VARCHAR(200) NOT NULL,
    "complemento" VARCHAR(200) NOT NULL,
    "data_festa" DATE NOT NULL,
    "qtd_convidados" INTEGER NOT NULL,
    "observacoes" TEXT
)'''

cur.execute(sql_cliente)

cur.execute('DROP TABLE IF EXISTS tb_funcionario')

sql_funcionario = '''CREATE TABLE "tb_funcionario" (
    "id_funcionario" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome" TEXT NOT NULL,
    "cpf" VARCHAR(11) NOT NULL UNIQUE,
    "email" VARCHAR(150) NOT NULL UNIQUE,
    "telefone" VARCHAR(20) NOT NULL,
    "endereco" TEXT NOT NULL,
    "cep" VARCHAR(8) NOT NULL,
    "cidade" TEXT NOT NULL,
    "estado" TEXT NOT NULL,
    "numero" TEXT NOT NULL,
    "complemento" TEXT,
    "cargo" TEXT NOT NULL,
    "salario" REAL NOT NULL,
    "tipo_contrato" TEXT NOT NULL,
    "disponibilidade" TEXT NOT NULL,
    "habilidades" TEXT NOT NULL,
    "tamanho_camisa" TEXT NOT NULL,
    "observacoes" TEXT
)'''

cur.execute(sql_funcionario)

cur.execute('DROP TABLE IF EXISTS tb_servico')

sql_servico = '''CREATE TABLE "tb_servico" (
    "id_servico" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome_servico" VARCHAR(200) NOT NULL,
    "descricao" TEXT NOT NULL,
    "valor" REAL NOT NULL,
    "status" BOOLEAN DEFAULT TRUE,
    "tipo_servico" VARCHAR(100) NOT NULL,
    "tipo_evento" VARCHAR(100) NOT NULL,
    "capacidade" INTEGER,
    "custo_unit" DECIMAL(10,2)
)'''

cur.execute(sql_servico)

cur.execute('DROP TABLE IF EXISTS tb_evento')

sql_evento = '''CREATE TABLE "tb_evento" (
    "id_evento" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome_evento" VARCHAR(200) NOT NULL,
    "tipo_evento" VARCHAR(100) NOT NULL,
    "id_cliente" INTEGER NOT NULL,
    "data_evento" DATE NOT NULL,
    "hora_inicio" TIME NOT NULL,
    "hora_fim" TIME NOT NULL,
    "local_evento" VARCHAR(200) NOT NULL,
    "orcamento_inicial" REAL NOT NULL,
    "orcamento_final" REAL NOT NULL,
    "status_pagamento" BOOLEAN DEFAULT FALSE,
    "custos_adicionais" REAL,
    "valor_lucro_liquido" REAL,
    "feedback_cliente" TEXT,
    FOREIGN KEY (id_cliente) REFERENCES tb_cliente(id_cliente)
)'''

cur.execute(sql_evento)

cur.execute('DROP TABLE IF EXISTS tb_contrato')

sql_contrato = '''CREATE TABLE "tb_contrato" (
    "id_contrato" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_cliente" INTEGER NOT NULL,
    "id_evento" INTEGER NOT NULL,
    "id_servico" INTEGER NOT NULL,
    "data_contrato" DATE NOT NULL,
    "valor_total" REAL NOT NULL,
    "valor_por_convidado" REAL NOT NULL,
    "sinal_reserva" REAL NOT NULL,
    "condicoes_pagamento" TEXT,
    "observacoes" TEXT,
    "politicas_cancelamento" TEXT,
    "status_contrato" BOOLEAN DEFAULT TRUE,
    "disponibilidade" BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_cliente) REFERENCES tb_cliente(id_cliente),
    FOREIGN KEY (id_evento) REFERENCES tb_evento(id_evento),
    FOREIGN KEY (id_servico) REFERENCES tb_servico(id_servico)
)'''

cur.execute(sql_contrato)

cur.execute('DROP TABLE IF EXISTS tb_orcamento')

sql_orcamento = '''CREATE TABLE "tb_orcamento" (
    "id_orcamento" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome" VARCHAR(200) NOT NULL,
    "email" VARCHAR(150) UNIQUE NOT NULL,
    "telefone" VARCHAR(20) NOT NULL,
    "tipo_evento" VARCHAR(100) NOT NULL,
    "data_evento" DATE NOT NULL,
    "qtd_convidados" INTEGER NOT NULL,
    "horario_evento" TIME NOT NULL,
    "servicos_solicitados" TEXT,
    "observacoes" TEXT
)'''

cur.execute(sql_orcamento)

cur.execute('DROP TABLE IF EXISTS tb_evento_realizado')

sql_evento_realizado = '''CREATE TABLE "tb_evento_realizado" (
    "id_evento" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_contrato" INTEGER NOT NULL,
    "id_cliente" INTEGER NOT NULL,
    "tipo_evento" VARCHAR(100) NOT NULL,
    "data_evento" DATE NOT NULL,
    "qtd_convidados" INTEGER NOT NULL,
    "tema_festa" VARCHAR(200),
    "servicos_utilizados" TEXT,
    "funcionarios_envolvidos" TEXT,
    "avaliacao_cliente" REAL,
    "custo_total" REAL DEFAULT 0,
    "lucro_liquido" REAL DEFAULT 0,
    "problemas_ocorridos" TEXT,
    "elogios_destaques" TEXT,
    "responsavel_evento" TEXT,
    "status_evento" TEXT DEFAULT 'PENDENTE',
    "data_registro" DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_contrato) REFERENCES tb_contrato(id_contrato),
    FOREIGN KEY (id_cliente) REFERENCES tb_cliente(id_cliente)
)'''

cur.execute(sql_evento_realizado)

# Salvar as alterações e fechar a conexão
con.commit()
con.close()
