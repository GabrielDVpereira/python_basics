import requests

git_user = input("type your git username: ")

reponse = requests.get('https://api.github.com/users/' + git_user)
git = reponse.json()

print(git))