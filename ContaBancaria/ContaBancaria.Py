//---------------------------------------------#
//                                             #
//  Nome: Miguel Fernandes Santos              #
//  Projeto: Conta bancaria.                   #
//  Data: 30/10/2021                           #
//                                             #
//---------------------------------------------#

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ContaBancaria
{
    class Program
    {
        static void Main(string[] args)
        {

            // função para adicionar valor a sua conta:
            double Adicionar(double valor, double saldo)
            {

                //  adiciona saldo:
                saldo = saldo + valor;

                return saldo;

            }

            // função para retornar o valor do credito que vc possue direito:
            double[] SeuCredito(double Salario)
            {

                // Cria um vetor com 3 valores:
                double[] dados = new double[3];

                // Credito de 50% a mais:
                dados[0] = ((Salario / 100) * 50) + Salario;

                // Credito de 75% a mais:
                dados[1] = ((Salario / 100) * 75) + Salario;

                // Credito de 100% a mais:
                dados[2] = ((Salario / 100) * 100) + Salario;

                return dados;

            }

            // função para pedir credito:
            double[] Credito(double valor, double credito, double saldo, double divida)
            {

                // Cria uma lista com 3 valores:
                double[] dados = new double[3];

                // Se seu credito for menor que o valor que vc deseja retirar:
                if (valor > credito)
                {

                    Console.WriteLine("\nInfelizmente seu credito é menor que o necessario!!!");
                    return dados;

                }

                // Indice 0 é o saldo atual + o credito:
                dados[0] = valor;
                // indice 1 é o valor de credito que tem que pagar:
                dados[1] = divida + valor;
                // indice 2 é o valor de credito que vc ainda possui:
                dados[2] = credito - valor;

                return dados;

            }

            // função para descobrir se o que foi digitado é um numero:
            double converter(string value)
            {
                // declara a variavel retorno:
                double retorno = 0;

                // Vai tentar converter o valor passado para float:
                try
                {

                    retorno = Convert.ToDouble(value);

                }
                catch // se nao der certo retorna 0:
                {

                    Console.WriteLine("\nO valor inserido anteriormente não é um numero!!!!!");
                    return 0;

                }

                return retorno;

            }

            // função para retirar o dinheiro:
            double Retirar(double valor, double saldo)
            {

                // Se o saldo for menor que o valor a retirar:
                if (saldo < valor)
                {

                    Console.WriteLine("Infelizmente o valor que deseja retirar é maior que o seu saldo atual.");
                    return saldo;

                }
                else
                {

                    saldo = saldo - valor;

                }

                return saldo;
            }

            // Adiciona no historico de transaçoes:
            string Historico(string palavra, double valor)
            {

                // Pega a data Atual:
                string data = DateTime.Now.ToString("dd-MM-yyyy");
                //  Declara a variavel frase:
                string frase = "";

                // A variavel frase recebe a data mais o tipo de movimento mais o valor:
                frase = data + " - Foi " + palavra + " um valor de " + Convert.ToString(valor);

                return frase;

            }

            // função para gerar arquivo txt do extrato na mesma pasta que o arquivo:
            void Extrato(Dictionary<string, double> valores, string Nome, List<string> extrato)
            {

                // Pega a data atual:
                string data = DateTime.Now.ToString("dd-MM-yyyy");

                // Pega a quantidade total de valores no historico:
                int tamanho = valores.Count();

                // Escreve no documento a data atual:
                Console.WriteLine("\n\nData atual: " + data + "\n");
                // Escreve no documento o nome:
                Console.WriteLine("Nome: " + Nome + "\n");
                // Escreve no documento o Saldo atual:
                Console.WriteLine("Saldo Atual: " + Convert.ToString(valores["Saldo"]) + "\n");
                // Escreve no documento o Credito atual:
                Console.WriteLine("Credito Atual: " + Convert.ToString(valores["Credito"]) + "\n");
                // Escreve no documento o credito a pagar atual:
                Console.WriteLine("Credito a pagar: " + Convert.ToString(valores["CreditoPagar"]) + "\n");

                // Se existir algo no historico:
                if (tamanho > 0)
                {

                    Console.WriteLine("\n\n---------- HISTORICO ---------\n");

                    // escrever cada uma das informaçoes do historico:
                    foreach (string item in extrato)
                    {

                        Console.WriteLine(item + "\n");

                    }

                }

            }

            // Declara uma lista do historico de transações:
            List<string> historico = new List<string>();
            // Declara uma variavel para o nome:
            string nome = "";
            // Declara um vetor para as 3 opções de credito:
            double[] opcoes;

            // Dicionario das variaveis da pessoa:
            Dictionary<string, double> Pessoa = new Dictionary<string, double>()
            {

                {"Salario", 0 },
                {"Menu", 0 },

            };

            // Dicionario das variaveis que seram usadas na conta:
            Dictionary<string, double> Dados = new Dictionary<string, double>()
            {

                {"Saldo", 5000 },
                {"Credito", 0 },
                {"CreditoPagar", 0 },
                {"AuxiliarRetirar", 0 },
                {"AuxiliarCOlocar", 0 },
                {"Menu", 0 }

            };

            Console.WriteLine("---------- Cadastro Pessoal ---------");

            // Faz a leitura do nome:
            Console.WriteLine("Por favor, insira seu Nome: ");
            nome = Console.ReadLine();

            // Faz a leitura do salario:
            while (Pessoa["Salario"] <= 0)
            {

                // Faz a leitura do seu salario ate ser maior que 0:
                Console.WriteLine("\n\nPor favor insira seu Salario: ");
                Pessoa["Salario"] = converter(Console.ReadLine());

            }

            // Chama a função que descobre o seu credito:
            opcoes = SeuCredito(Pessoa["Salario"]);

            // laço que obriga o usuario a digitar uma das opções:
            while (Pessoa["Menu"] < 1 || Pessoa["Menu"] > 3)
            {

                // Mostra as opções de credito:
                Console.WriteLine("\nBaseado em seu salario você tem direito a creditos de: \n");
                // Mostra 50% a mais:
                Console.WriteLine(" 1 - " + Convert.ToString(opcoes[0]));
                // Mostra 75% a mais:
                Console.WriteLine(" 2 - " + Convert.ToString(opcoes[1]));
                // Mostra 100% a mais:
                Console.WriteLine(" 3 - " + Convert.ToString(opcoes[2]));
                
                // Pergunta qual das opções o usuario quer:
                Console.WriteLine("Qual das opões acima você deseja?");
                Pessoa["Menu"] = converter(Console.ReadLine());
            
                if (Pessoa["Menu"] == 1)
                {

                    // Escolheu a primeira opção:
                    Dados["Credito"] = opcoes[0];

                }
                else if (Pessoa["Menu"] == 2)
                {

                    // Escolheu a segunda opção:
                    Dados["Credito"] = opcoes[1];

                }
                else if (Pessoa["Menu"] == 3)
                {

                    // Escolheu a terceira opção:
                    Dados["Credito"] = opcoes[2];

                }
                else
                {

                    Console.WriteLine("Opção invalida!!!");

                }

            }

            // --- FIM DO CADASTRO DA PESSOA --- //

            Console.WriteLine("\n\n---------- Bem Vindo ----------");

            while(Dados["Menu"] != 5)
            {
                double[] valores;

                // Mostra o menu:
                Console.WriteLine("\n---------- MENU ----------");
                Console.WriteLine("\n 1 - Retirar\n 2 - Colocar\n 3 - Credito\n 4 - Extrato\n 5 - Sair\n");
                Console.WriteLine("\n---------- MENU ----------\n");
                
                Dados["Menu"] = 0;
                // Pergunta qual a escolha do usuario:
                Console.WriteLine("\nQual a sua escolha");
                // Faz a leitura da escolha do usuario:
                Dados["Menu"] = converter(Console.ReadLine());
                
                if(Dados["Menu"] == 1)
                {
                    // Pergunta o valor que usuario deseja:
                    Console.WriteLine("\n\nDigite o valor que deseja retirar: ");
                    // Faz a leitura e converte o valor que o usuario digitar:
                    Dados["AuxiliarRetirar"] = converter(Console.ReadLine());
                    // Chama a função retirar:
                    Dados["Saldo"] = Retirar(Dados["AuxiliarRetirar"], Dados["Saldo"]);
                    // Adiciona no historico:
                    historico.Add(Historico("Retirado", Dados["AuxiliarRetirar"]));

                }
                else if(Dados["Menu"] == 2)
                {

                    // Pergunta o valor que usuario deseja inserir:
                    Console.WriteLine("Digite o valor que deseja inserir: ");
                    // faz a leitura e converte o valor que o usuario digitar:
                    Dados["AuxiliarColocar"] = converter(Console.ReadLine());
                    // Chama a função adicionar:
                    Dados["Saldo"] = Adicionar(Dados["AuxiliarColocar"], Dados["Saldo"]);
                    // Adiciona no historico:
                    historico.Add(Historico("Adicionado", Dados["AuxiliarColocar"]));

                }
                else if(Dados["Menu"] == 3)
                {

                    // Pergunta o valor que o usuario quer de credito:
                    Console.WriteLine("Digite o valor que deseja de credito: ");
                    // Faz a leitura e converte o valor que o usuario digitar:
                    Dados["AuxiliarColocar"] = converter(Console.ReadLine());
                    // Chama a função de credito:
                    valores = Credito(Dados["AuxiliarColocar"], Dados["Credito"], Dados["Saldo"], Dados["CreditoPagar"]);
                    // O saldo recebe o valor do credito:
                    Dados["Saldo"] = Dados["Saldo"] + valores[0];
                    // O credito a pagar recebe o valor:
                    Dados["CreditoPagar"] = Dados["CreditoPagar"] + valores[1];
                    // O credito que tem direito - valor:
                    Dados["Credito"] = Dados["Credito"] - valores[2];
                    // Adiciona no historico:
                    historico.Add(Historico("adicionado um credito em", valores[0]));

                }
                else if(Dados["Menu"] == 4)
                {

                    // Cria o extrato no console:
                    Extrato(Dados, nome, historico);

                }
                else if(Dados["menu"] == 5)
                {

                    // Sai do programa:
                    Console.WriteLine("Saindo...");

                }
                else
                {

                    // Opção invalida:
                    Console.WriteLine("Opção invalida!!!!!!");

                }

            }

        }
    }
}
