-- Prova PYIA - SQL III
-- [PYIA-A17] Crie uma tabela chamada Estoque que contenha as seguintes colunas: EstoqueID, ProdutoID, FornecedorID, Quantidade e DataEntrada. A coluna EstoqueID deve ser um identificador único para cada registro no estoque. A coluna ProdutoID deve referenciar o identificador do produto correspondente na tabela de produtos, e a coluna FornecedorID deve referenciar o identificador do fornecedor na tabela de fornecedores, ambas atuando como chaves estrangeiras para estabelecer a relação com outras tabelas. A coluna Quantidade deve indicar a quantidade de produtos recebidos, e a coluna DataEntrada deve armazenar a data em que os produtos entraram no estoque. Para criar esta tabela e garantir as referências corretas, é necessário definir as chaves estrangeiras para ProdutoID e FornecedorID.
-- Após a criação da tabela, você pode utilizar operações de banco de dados como FULL OUTER JOIN para combinar informações de diferentes tabelas, GROUP BY para agrupar dados com base em uma ou mais colunas, e ALTER TABLE para modificar a estrutura da tabela, como adicionar ou alterar colunas.

CREATE TABLE Estoque (
    EstoqueID INT PRIMARY KEY,
    ProdutoID INT,
    FornecedorID INT,
    Quantidade INT NOT NULL,
    DataEntrada DATE NOT NULL,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID)
);

CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
    NomeProduto VARCHAR(100) NOT NULL,
    Quantidade INT NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Fornecedores (
    FornecedorID INT PRIMARY KEY AUTO_INCREMENT,
    NomeFornecedor VARCHAR(100) NOT NULL,
    Contato VARCHAR(100),
    Telefone VARCHAR(15)
);

-- EXEMPLO DE FULL OUTER JOIN:
SELECT * FROM Estoque
FULL OUTER JOIN Produtos ON Estoque.ProdutoID = Produtos.ProdutoID
FULL OUTER JOIN Fornecedores ON Estoque.FornecedorID = Fornecedores.FornecedorID;

-- EXEMPLO DE GROUP BY
SELECT FornecedorID, SUM(Quantidade) AS TotalQuantidade
FROM Estoque
GROUP BY FornecedorID;

-- EXEMPLO DE ALTER TABLE
ALTER TABLE Estoque
ADD Observacoes VARCHAR(255);
