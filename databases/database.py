databases = (
    'https://github.com/danielmiessler/SecLists/blob/master/Passwords/xato-net-10-million-passwords.txt?raw=true',
    'https://github.com/danielmiessler/SecLists/raw/master/Passwords/unkown-azul.txt',
    'https://github.com/danielmiessler/SecLists/raw/master/Passwords/twitter-banned.txt',
    'https://github.com/danielmiessler/SecLists/raw/master/Passwords/richelieu-french-top5000.txt',
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/probable-v2-top207.txt',
    'https://github.com/danielmiessler/SecLists/blob/master/Passwords/probable-v2-top12000.txt',
    'https://github.com/danielmiessler/SecLists/raw/master/Passwords/probable-v2-top12000.txt',
    'https://github.com/danielmiessler/SecLists/blob/master/Passwords/openwall.net-all.txt?raw=true',
    'https://github.com/danielmiessler/SecLists/blob/master/Passwords/mssql-passwords-nansh0u-guardicore.txt?raw=true',
    'https://github.com/danielmiessler/SecLists/raw/master/Passwords/german_misc.txt',
    'https://github.com/danielmiessler/SecLists/blob/master/Passwords/dutch_wordlist?raw=true',
    'https://github.com/danielmiessler/SecLists/raw/master/Passwords/darkweb2017-top10000.txt',
    'https://github.com/danielmiessler/SecLists/blob/master/Passwords/darkc0de.txt?raw=true',
    'https://github.com/danielmiessler/SecLists/raw/master/Passwords/cirt-default-passwords.txt',
    'https://github.com/danielmiessler/SecLists/blob/master/Passwords/bt4-password.txt?raw=true',
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/UserPassCombo-Jay.txt',
    'https://github.com/danielmiessler/SecLists/blob/master/Passwords/SCRABBLE-hackerhouse.tgz?raw=true',
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Most-Popular-Letter-Passes.txt',
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Keyboard-Combinations.txt',
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou-75.txt',
    'https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/honeynet2.txt?raw=true',
)

if __name__ == "__main__":
    f = open('databases.txt', 'w')
    for i in databases:
        f.write(i + '\n')
