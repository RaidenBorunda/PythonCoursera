from ldap3 import Server, Connection, RESTARTABLE, SYNC
from getpass import getpass


serverName = 'LDAP://dt-ad03.dt.lan:389/OU=_BETA Azure AD Connect,OU=Users,OU=Dermtech,DC=dt,DC=lan'

domainName = 'dt.lan'

userName = input('Username: ')
password = getpass('Password: ')
base = 'OU=_BETA Azure AD Connect,OU=Users,OU=Dermtech,DC=dt,DC=lan'
hostPort = serverName.split('/')[2]
newUserName = userName.replace('.', ' ')
connUserName = "CN="+newUserName

server = Server('dt.lan', port=389)
# user=connUserName+
conn = Connection(server, read_only=True, user=connUserName+',OU=Admin,OU=_BETA Azure AD Connect,OU=Users,OU=Dermtech,DC=dt,DC=lan', password=password, auto_bind=False) #, client_strategy=SYNC)
conn.open()
conn.bind()

conn.search(base, '(objectclass=person)', attributes=['displayName', 'mail','sAMAccountName'])

for i in conn.entries:
    if i.sAMAccountName.values and i.displayName.values and i.mail.values:
        print ('USER = {0} : {1} : {2}'.format(i.sAMAccountName.values[0], i.displayName.values[0], i.mail.values[0]))
    else:
        print('USER = Missing some values')
