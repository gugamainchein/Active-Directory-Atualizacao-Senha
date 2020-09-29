# Active Directory -> Atualização de Senha

## Sobre o projeto

Este é um projeto desenvolvido para estudo, onde, por meio da execução de um script Python, é possível atualizar sua senha do AD.

O método escolhido para realizar esta atualização é coletando as informações atuais do AD e as credenciais do usuário. A partir desses dados, ele pode escolher uma nova senha de sua preferência.

## Arquitetura do projeto

* Linguagem: Python
* Biblioteca: ldap3

## Pré-requisitos para rodar o código

Para rodar este desenvolvimento com sucesso, você só precisa seguir os passos abaixo:
* Ter o Python instalado na máquina;
* Passar sua base de domínios para a variável " BASEDN ", do arquivo .py, ou torná-la uma variável que irá receber dados digitados pelo usuário, por meio do método " input('Base de Domínios: ') ";
* Instalar a biblioteca ldap3 em um ambiente virtual Python (ou na própria máquina): " pip install ldap3 ".

## Observação

A maioria dos AD's possuem políticas que restrigem algumas ações relacionadas à atualização de senha. Por isso, recomendo que você consulte as regras que o(s) da sua empresa segue(m).

## Contatos

Segue abaixo meus contatos para sugestões, dúvidas ou feedbacks:

* E-mail: gustavomainchein@outlook.com
* Linkedin: <a href="www.linkedin.com/in/gustavosantos14/">linkedin/gustavomainchein</a>
* Instagram: <a href="www.instagram.com/gugamainchein/">instagram.com/gugamainchein/</a>
