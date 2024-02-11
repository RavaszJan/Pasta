# Pasta
class Pasta:
    def __init__(self):
        self.pastas = []

    def add_pasta(self, pasta):
        self.pastas.append(pasta)

    def __str__(self):
        return "\n".join(self.pastas)


class Prisady:
    def __init__(self, ):
        self.prisady = Pasta()

    def add_cestoviny_pasta(self):
        self.prisady.add_pasta("Cestoviny: Spagety", )
        return self

    def add_omacka_pasta(self):
        self.prisady.add_pasta("Omacka:Bolonska  ", )
        return self

    def add_topping_pasta(self):
        self.prisady.add_pasta("Topping:Parmezan ", )
        return self

    def add_dressing_pasta(self):
        self.prisady.add_pasta("Dressing:Kecup ", )
        return self

    def build(self):
        return self.prisady


prisady = Prisady()
pasta1 = prisady.add_cestoviny_pasta().add_omacka_pasta().add_topping_pasta().add_dressing_pasta().build()

print(pasta1)
print()

# pasta2=prisady.add_cestoviny_pasta().add_omacka_pasta().build()
# print(pasta2)


