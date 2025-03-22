-- Prova PYIA - SQL II 
-- [PYIA-A16] Crie uma tabela chamada Produtos que contenha quatro colunas: ProdutoID, NomeProduto, Quantidade e Preco. A coluna ProdutoID deve ser um identificador único para cada produto, a coluna NomeProduto deve armazenar o nome do produto, a coluna Quantidade deve indicar a quantidade disponível do produto, e a coluna Preco deve representar o preço do produto. Após criar a tabela, insira três registros diferentes, cada um representando um produto distinto, incluindo valores específicos para ProdutoID, NomeProduto, Quantidade e Preco.

CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    NomeProduto VARCHAR(100) NOT NULL,
    Quantidade INT NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL
);

INSERT INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco) VALUES
(20, 'Mouse', 50, 19.00),
(33, 'Teclado', 30, 45.00),
(47, 'Fone', 20, 39.99);
