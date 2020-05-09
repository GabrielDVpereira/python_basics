import requests

git_user = input("type your git username: ")

reponse = requests.get('https://api.github.com/users/' + git_user)
git = reponse.json()

username = git['login']; 
repos = git['public_repos']

print("Your git username: " + username)
print("The number of repos you have " + str(repos))