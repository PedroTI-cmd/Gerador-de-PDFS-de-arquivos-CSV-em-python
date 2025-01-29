import pandas as pd
import random
from faker import Faker


fake = Faker("pt_BR")


dados = []
for _ in range(20):  
    dados.append([
        fake.name(),
        fake.job(),
        round(random.uniform(2000, 10000), 2),  
        fake.city(),
        fake.date_of_birth(minimum_age=18, maximum_age=65)
    ])


df = pd.DataFrame(dados, columns=["Nome", "Profissão", "Salário", "Cidade", "Data de Nascimento"])

df.to_csv("dados_ficticios.csv", index=False, encoding="utf-8")

print("Arquivo CSV gerado com sucesso!")
