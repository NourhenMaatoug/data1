'''
Created on 13‏/04‏/2024

@author: norhe
'''

if __name__ == '__main__':
    pass
from git import Repo

def cloner_repo(url, chemin_destination):
  Repo.clone_from(url, chemin_destination)

# Exemple d'utilisation
url_repo = "https://github.com/user/repo.git"
chemin_destination = "C:\Users\norhe\pfaa"
cloner_repo(url_repo, chemin_destination)