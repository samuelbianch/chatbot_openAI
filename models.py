class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Samuel Bianch", "samuelbianch", "123")
usuario2 = Usuario("Administrador", "admin", "123")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2}