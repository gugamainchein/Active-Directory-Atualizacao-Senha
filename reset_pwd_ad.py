#!/usr/bin/python

# Importando bibliotecas
import ldap3
import getpass

# Definindo as configurações do servidor de AD
BASEDN = "OU=Usuarios,OU=Corpflex,DC=nm,DC=local"

# Definindo as variáveis de usuário
IP_AD = input('IP do Domínio: ')
DOMINIO = input('Domínio (ex.: nm, local, etc...): ')
USER = input('Usuário: ')
CURREENTPWD = getpass.getpass('Senha atual: ')
NEWPWD = getpass.getpass('Nova senha: ')

# Criando um filtro de busca
SEARCHFILTER = '(&(|(userPrincipalName='+USER+')(samaccountname=' + \
    USER+')(mail='+USER+'))(objectClass=person))'

# Variável de busca
USER_DN = ""

# Realizando a conexão com o servidor LDAP
conn = ldap3.Connection(ldap3.Server('LDAP://' + IP_AD + ':389'),
                        auto_bind=True,
                        user="{}\\{}".format(DOMINIO, USER),
                        password=CURREENTPWD)

# Iniciando a conexão
conn.start_tls()

# Printando os resultados achados
conn.search(search_base=BASEDN,
            search_filter=SEARCHFILTER,
            search_scope=ldap3.SUBTREE,
            attributes=['cn', 'givenName'],
            paged_size=5)

# Percorrendo a consulta
for entry in conn.response:
    if entry.get("dn") and entry.get("attributes"):
        if entry.get("attributes"):
            USER_DN = entry.get("dn")

# Modificando a senha
reset_pass = conn.extend.microsoft.modify_password(
    USER_DN, NEWPWD, CURREENTPWD)

# Printando o resultado booleano
print(reset_pass)
