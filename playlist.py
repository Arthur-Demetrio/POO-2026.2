from datetime import datetime, timedelta


def formatar_tempo(td):
    """Formata um timedelta como HH:MM:SS."""
    total = int(td.total_seconds())
    h, resto = divmod(total, 3600)
    m, s = divmod(resto, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


# ======================================================================
class Musica:
    def __init__(self, i, t, art, alb, d):
        self.__id = i
        self.__titulo = t
        self.__artista = art
        self.__album = alb
        self.__duracao = d

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_artista(self):
        return self.__artista

    def get_album(self):
        return self.__album

    def get_duracao(self):
        return self.__duracao

    def set_id(self, i):
        self.__id = i

    def set_titulo(self, t):
        self.__titulo = t

    def set_artista(self, art):
        self.__artista = art

    def set_album(self, alb):
        self.__album = alb

    def set_duracao(self, d):
        self.__duracao = d

    def __str__(self):
        return (f"ID: {self.__id} | Título: {self.__titulo} | Artista: {self.__artista} | "
                f"Álbum: {self.__album} | Duração: {formatar_tempo(self.__duracao)}")


# ======================================================================
class PlayList:
    def __init__(self, i, n, d):
        self.__id = i
        self.__nome = n
        self.__descricao = d
        self.__musicas = []  # atributo extra: músicas da playlist (para o tempo total)

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def set_id(self, i):
        self.__id = i

    def set_nome(self, n):
        self.__nome = n

    def set_descricao(self, d):
        self.__descricao = d

    def AdicionarMusica(self, musica):
        self.__musicas.append(musica)

    def RemoverMusica(self, musica):
        if musica in self.__musicas:
            self.__musicas.remove(musica)

    def TempoTotal(self):
        total = timedelta(0)
        for m in self.__musicas:
            total += m.get_duracao()
        return total

    def __str__(self):
        return (f"ID: {self.__id} | Nome: {self.__nome} | Descrição: {self.__descricao} | "
                f"Músicas: {len(self.__musicas)} | Tempo total: {formatar_tempo(self.TempoTotal())}")


# ======================================================================
class PlayListItem:
    def __init__(self, i, ip, im, d, s):
        self.__id = i
        self.__id_playlist = ip
        self.__id_musica = im
        self.__data_inclusao = d
        self.__sequencia = s

    def get_id(self):
        return self.__id

    def get_id_playlist(self):
        return self.__id_playlist

    def get_id_musica(self):
        return self.__id_musica

    def get_data_inclusao(self):
        return self.__data_inclusao

    def get_sequencia(self):
        return self.__sequencia

    def set_id(self, i):
        self.__id = i

    def set_id_playlist(self, ip):
        self.__id_playlist = ip

    def set_id_musica(self, im):
        self.__id_musica = im

    def set_data_inclusao(self, d):
        self.__data_inclusao = d

    def set_sequencia(self, s):
        self.__sequencia = s

    def __str__(self):
        return (f"ID: {self.__id} | Playlist: {self.__id_playlist} | Música: {self.__id_musica} | "
                f"Incluída em: {self.__data_inclusao.strftime('%d/%m/%Y %H:%M')} | "
                f"Sequência: {self.__sequencia}")


# ======================================================================
class UI:
    def __init__(self):
        self.__playlists = []
        self.__musicas = []
        self.__itens = []
        self.__prox_playlist = 1
        self.__prox_musica = 1
        self.__prox_item = 1

    # ---------- utilidades ----------
    @staticmethod
    def __ler_inteiro(msg):
        try:
            return int(input(msg))
        except ValueError:
            return None

    @staticmethod
    def __ler_duracao(msg, padrao=None):
        while True:
            txt = input(msg).strip()
            if txt == "" and padrao is not None:
                return padrao
            try:
                partes = [int(p) for p in txt.split(":")]
                if len(partes) == 2:
                    partes = [0] + partes
                if len(partes) != 3 or any(p < 0 for p in partes):
                    raise ValueError
                td = timedelta(hours=partes[0], minutes=partes[1], seconds=partes[2])
                if td.total_seconds() > 0:
                    return td
                print("A duração deve ser maior que zero.")
            except ValueError:
                print("Duração inválida. Use mm:ss ou hh:mm:ss.")

    @staticmethod
    def __ler_texto(msg, padrao=None):
        txt = input(msg).strip()
        return padrao if (txt == "" and padrao is not None) else txt

    def __buscar_playlist(self, id):
        return next((p for p in self.__playlists if p.get_id() == id), None)

    def __buscar_musica(self, id):
        return next((m for m in self.__musicas if m.get_id() == id), None)

    def __buscar_item(self, id):
        return next((i for i in self.__itens if i.get_id() == id), None)

    def __itens_da_playlist(self, id_playlist):
        itens = [i for i in self.__itens if i.get_id_playlist() == id_playlist]
        return sorted(itens, key=lambda i: i.get_sequencia())

    def __renumerar(self, id_playlist):
        for n, item in enumerate(self.__itens_da_playlist(id_playlist), start=1):
            item.set_sequencia(n)

    # ---------- menus ----------
    def Main(self):
        op = -1
        while op != 0:
            op = self.Menu()
            if op == 1:
                self.__menu_crud("PLAYLISTS", self.InserirPlaylist, self.ListarPlaylists,
                                 self.AtualizarPlaylist, self.ExcluirPlaylist)
            elif op == 2:
                self.__menu_crud("MÚSICAS", self.InserirMusica, self.ListarMusicas,
                                 self.AtualizarMusica, self.ExcluirMusica)
            elif op == 3:
                self.__menu_crud("ITENS DA PLAYLIST", self.InserirItem, self.ListarItens,
                                 self.AtualizarItem, self.ExcluirItem)
            elif op == 0:
                print("Até logo!")
            else:
                print("Opção inválida.")

    def Menu(self):
        print("\n===== PLAYLIST =====")
        print("1 - Playlists")
        print("2 - Músicas")
        print("3 - Itens da playlist")
        print("0 - Sair")
        op = self.__ler_inteiro("Opção: ")
        return op if op is not None else -1

    def __menu_crud(self, titulo, inserir, listar, atualizar, excluir):
        while True:
            print(f"\n--- {titulo} ---")
            print("1 - Inserir")
            print("2 - Listar")
            print("3 - Atualizar")
            print("4 - Excluir")
            print("0 - Voltar")
            op = self.__ler_inteiro("Opção: ")
            if op == 1:
                inserir()
            elif op == 2:
                listar()
            elif op == 3:
                atualizar()
            elif op == 4:
                excluir()
            elif op == 0:
                return
            else:
                print("Opção inválida.")

    # ---------- playlists ----------
    def InserirPlaylist(self):
        nome = self.__ler_texto("Nome: ")
        desc = self.__ler_texto("Descrição: ")
        self.__playlists.append(PlayList(self.__prox_playlist, nome, desc))
        print(f"Playlist {self.__prox_playlist} inserida!")
        self.__prox_playlist += 1

    def ListarPlaylists(self):
        if not self.__playlists:
            print("Nenhuma playlist cadastrada.")
        for p in self.__playlists:
            print(p)

    def AtualizarPlaylist(self):
        p = self.__buscar_playlist(self.__ler_inteiro("Id da playlist: "))
        if p is None:
            print("Playlist não encontrada.")
            return
        print("(Enter mantém o valor atual)")
        p.set_nome(self.__ler_texto(f"Nome [{p.get_nome()}]: ", p.get_nome()))
        p.set_descricao(self.__ler_texto(f"Descrição [{p.get_descricao()}]: ", p.get_descricao()))
        print("Playlist atualizada!")

    def ExcluirPlaylist(self):
        p = self.__buscar_playlist(self.__ler_inteiro("Id da playlist: "))
        if p is None:
            print("Playlist não encontrada.")
            return
        self.__itens = [i for i in self.__itens if i.get_id_playlist() != p.get_id()]
        self.__playlists.remove(p)
        print("Playlist excluída (e seus itens também)!")

    # ---------- músicas ----------
    def InserirMusica(self):
        titulo = self.__ler_texto("Título: ")
        artista = self.__ler_texto("Artista: ")
        album = self.__ler_texto("Álbum: ")
        duracao = self.__ler_duracao("Duração (mm:ss): ")
        self.__musicas.append(Musica(self.__prox_musica, titulo, artista, album, duracao))
        print(f"Música {self.__prox_musica} inserida!")
        self.__prox_musica += 1

    def ListarMusicas(self):
        if not self.__musicas:
            print("Nenhuma música cadastrada.")
        for m in self.__musicas:
            print(m)

    def AtualizarMusica(self):
        m = self.__buscar_musica(self.__ler_inteiro("Id da música: "))
        if m is None:
            print("Música não encontrada.")
            return
        print("(Enter mantém o valor atual)")
        m.set_titulo(self.__ler_texto(f"Título [{m.get_titulo()}]: ", m.get_titulo()))
        m.set_artista(self.__ler_texto(f"Artista [{m.get_artista()}]: ", m.get_artista()))
        m.set_album(self.__ler_texto(f"Álbum [{m.get_album()}]: ", m.get_album()))
        m.set_duracao(self.__ler_duracao("Duração (mm:ss): ", m.get_duracao()))
        print("Música atualizada!")

    def ExcluirMusica(self):
        m = self.__buscar_musica(self.__ler_inteiro("Id da música: "))
        if m is None:
            print("Música não encontrada.")
            return
        # remove a música das playlists onde ela aparece
        for item in [i for i in self.__itens if i.get_id_musica() == m.get_id()]:
            p = self.__buscar_playlist(item.get_id_playlist())
            if p:
                p.RemoverMusica(m)
            self.__itens.remove(item)
            self.__renumerar(item.get_id_playlist())
        self.__musicas.remove(m)
        print("Música excluída (e removida das playlists)!")

    # ---------- itens da playlist ----------
    def InserirItem(self):
        p = self.__buscar_playlist(self.__ler_inteiro("Id da playlist: "))
        if p is None:
            print("Playlist não encontrada.")
            return
        m = self.__buscar_musica(self.__ler_inteiro("Id da música: "))
        if m is None:
            print("Música não encontrada.")
            return
        sequencia = len(self.__itens_da_playlist(p.get_id())) + 1
        item = PlayListItem(self.__prox_item, p.get_id(), m.get_id(), datetime.now(), sequencia)
        self.__itens.append(item)
        p.AdicionarMusica(m)
        print(f"'{m.get_titulo()}' adicionada à playlist '{p.get_nome()}' (posição {sequencia})!")
        self.__prox_item += 1

    def ListarItens(self):
        p = self.__buscar_playlist(self.__ler_inteiro("Id da playlist: "))
        if p is None:
            print("Playlist não encontrada.")
            return
        print(p)
        itens = self.__itens_da_playlist(p.get_id())
        if not itens:
            print("Playlist vazia.")
        for item in itens:
            m = self.__buscar_musica(item.get_id_musica())
            print(f"  {item}")
            print(f"     -> {m.get_titulo()} - {m.get_artista()} ({formatar_tempo(m.get_duracao())})")

    def AtualizarItem(self):
        item = self.__buscar_item(self.__ler_inteiro("Id do item: "))
        if item is None:
            print("Item não encontrado.")
            return
        print(item)
        nova = self.__ler_inteiro("Nova sequência (Enter mantém): ")
        if nova is None:
            print("Nada alterado.")
            return
        itens = self.__itens_da_playlist(item.get_id_playlist())
        nova = max(1, min(nova, len(itens)))
        # reposiciona o item e renumera os demais
        itens.remove(item)
        itens.insert(nova - 1, item)
        for n, i in enumerate(itens, start=1):
            i.set_sequencia(n)
        print("Item atualizado!")

    def ExcluirItem(self):
        item = self.__buscar_item(self.__ler_inteiro("Id do item: "))
        if item is None:
            print("Item não encontrado.")
            return
        p = self.__buscar_playlist(item.get_id_playlist())
        m = self.__buscar_musica(item.get_id_musica())
        if p and m:
            p.RemoverMusica(m)
        self.__itens.remove(item)
        self.__renumerar(item.get_id_playlist())
        print("Item removido da playlist!")


if __name__ == "__main__":
    UI().Main()
