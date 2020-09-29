# Active Directory -> Reset de Senha

## Sobre o projeto

Este é um projeto desenvolvido para estudo, onde, por meio da execução de um script Python, é possível resetar sua senha do AD.

O método escolhido para realizar este reset é coletando as informações atuais do AD e as credenciais do usuário. A partir desses dados, ele pode atualizar sua senha para a que desejar.

## Arquitetura do projeto

* Linguagem: Python
* Biblioteca: ldap3

## Pré-requisitos para rodar o código

Para rodar este desenvolvimento com sucesso, você só precisa seguir os passos abaixo:
* Ter o Python instalado na máquina;
* Passar sua base de domínios para a variável " BASEDN ", do arquivo .py, ou torná-la uma variável que irá receber dados digitados pelo usuário, por meio do método " input('Base de Domínios: ') ";
* Instalar a biblioteca ldap3 em um ambiente virtual: " pip install ldap3 ".

## Contatos

Segue abaixo meus contatos para sugestões, dúvidas ou feedbacks:

* E-mail: gustavomainchein@outlook.com
* Linkedin: <a href="www.linkedin.com/in/gustavosantos14/">linkedin/gustavomainchein</a>
* Instagram: <a href="www.instagram.com/gugamainchein/">instagram.com/gugamainchein/</a>