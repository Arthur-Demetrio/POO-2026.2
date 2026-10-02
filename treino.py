from datetime import datetime, timedelta


def formatar_tempo(td):
    """Formata um timedelta como HH:MM:SS."""
    total = int(td.total_seconds())
    h, resto = divmod(total, 3600)
    m, s = divmod(resto, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


class Treino:
    def __init__(self, id, dt, ds, t):
        self.__id = id
        self.__data = dt
        self.__distancia = ds
        self.__tempo = t

    # ---------- get ----------
    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo

    # ---------- set ----------
    def set_id(self, id):
        self.__id = id

    def set_data(self, dt):
        self.__data = dt

    def set_distancia(self, ds):
        self.__distancia = ds

    def set_tempo(self, t):
        self.__tempo = t

    # ---------- métodos ----------
    def Pace(self):
        """Tempo médio gasto por quilômetro (timedelta)."""
        if self.__distancia <= 0:
            return timedelta(0)
        segundos = self.__tempo.total_seconds() / self.__distancia
        return timedelta(seconds=round(segundos))

    def __str__(self):
        pace = int(self.Pace().total_seconds())
        pm, ps = divmod(pace, 60)
        return (f"ID: {self.__id} | Data: {self.__data.strftime('%d/%m/%Y')} | "
                f"Distância: {self.__distancia:.2f} km | "
                f"Tempo: {formatar_tempo(self.__tempo)} | "
                f"Pace: {pm:02d}:{ps:02d} min/km")


class TreinoUI:
    def __init__(self):
        self.__treinos = []
        self.__proximo_id = 1

    # ---------- leitura de dados ----------
    @staticmethod
    def __ler_data(msg, padrao=None):
        while True:
            txt = input(msg).strip()
            if txt == "" and padrao is not None:
                return padrao
            try:
                return datetime.strptime(txt, "%d/%m/%Y")
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")

    @staticmethod
    def __ler_distancia(msg, padrao=None):
        while True:
            txt = input(msg).strip().replace(",", ".")
            if txt == "" and padrao is not None:
                return padrao
            try:
                valor = float(txt)
                if valor > 0:
                    return valor
                print("A distância deve ser maior que zero.")
            except ValueError:
                print("Valor inválido.")

    @staticmethod
    def __ler_tempo(msg, padrao=None):
        while True:
            txt = input(msg).strip()
            if txt == "" and padrao is not None:
                return padrao
            try:
                partes = [int(p) for p in txt.split(":")]
                if len(partes) == 2:       # mm:ss
                    partes = [0] + partes
                if len(partes) != 3 or any(p < 0 for p in partes):
                    raise ValueError
                h, m, s = partes
                td = timedelta(hours=h, minutes=m, seconds=s)
                if td.total_seconds() > 0:
                    return td
                print("O tempo deve ser maior que zero.")
            except ValueError:
                print("Tempo inválido. Use hh:mm:ss ou mm:ss.")

    @staticmethod
    def __ler_inteiro(msg):
        try:
            return int(input(msg))
        except ValueError:
            return None

    def __buscar(self, id):
        for t in self.__treinos:
            if t.get_id() == id:
                return t
        return None

    # ---------- operações ----------
    def Main(self):
        op = 0
        while op != 7:
            op = self.Menu()
            if op == 1:
                self.Inserir()
            elif op == 2:
                self.Listar()
            elif op == 3:
                self.Listar_Id()
            elif op == 4:
                self.Atualizar()
            elif op == 5:
                self.Excluir()
            elif op == 6:
                self.MaisRapido()
            elif op == 7:
                print("Até logo!")
            else:
                print("Opção inválida.")

    def Menu(self):
        print("\n===== TREINOS =====")
        print("1 - Inserir treino")
        print("2 - Listar todos os treinos")
        print("3 - Listar treino por id")
        print("4 - Atualizar treino")
        print("5 - Excluir treino")
        print("6 - Treino mais rápido")
        print("7 - Sair")
        op = self.__ler_inteiro("Opção: ")
        return op if op is not None else 0

    def Inserir(self):
        print("\n--- Inserir treino ---")
        dt = self.__ler_data("Data (dd/mm/aaaa): ")
        ds = self.__ler_distancia("Distância (km): ")
        t = self.__ler_tempo("Tempo (hh:mm:ss ou mm:ss): ")
        self.__treinos.append(Treino(self.__proximo_id, dt, ds, t))
        print(f"Treino {self.__proximo_id} inserido com sucesso!")
        self.__proximo_id += 1

    def Listar(self):
        print("\n--- Lista de treinos ---")
        if not self.__treinos:
            print("Nenhum treino cadastrado.")
            return
        for t in self.__treinos:
            print(t)

    def Listar_Id(self):
        id = self.__ler_inteiro("Id do treino: ")
        t = self.__buscar(id)
        print(t if t else "Treino não encontrado.")

    def Atualizar(self):
        id = self.__ler_inteiro("Id do treino a atualizar: ")
        t = self.__buscar(id)
        if t is None:
            print("Treino não encontrado.")
            return
        print("Treino atual:", t)
        print("(Pressione Enter para manter o valor atual)")
        t.set_data(self.__ler_data("Nova data (dd/mm/aaaa): ", t.get_data()))
        t.set_distancia(self.__ler_distancia("Nova distância (km): ", t.get_distancia()))
        t.set_tempo(self.__ler_tempo("Novo tempo (hh:mm:ss ou mm:ss): ", t.get_tempo()))
        print("Treino atualizado!")

    def Excluir(self):
        id = self.__ler_inteiro("Id do treino a excluir: ")
        t = self.__buscar(id)
        if t is None:
            print("Treino não encontrado.")
            return
        self.__treinos.remove(t)
        print("Treino excluído!")

    def MaisRapido(self):
        if not self.__treinos:
            print("Nenhum treino cadastrado.")
            return
        melhor = min(self.__treinos, key=lambda t: t.Pace())
        print("\nTreino mais rápido (menor pace):")
        print(melhor)


if __name__ == "__main__":
    TreinoUI().Main()
