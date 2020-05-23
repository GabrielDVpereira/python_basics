animals = {
  "vertebrado": {
    "ave":{
      "carnivoro": "aguia",
      "onivoro": "pomba"
    },
    "mamifero": {
      "onivoro": "homem",
      "herbivoro": "vaca"
    }
  },
  "invertebrado":{
    "inseto":{
      "hematofago": "pulga",
      "herbivoro": "lagarta"
    },
    "anelideo":{
      "hematofago": "sangessuga",
      "onivoro": "minhoca"
    }
  }
}

print(animals[input()][input()][input()])