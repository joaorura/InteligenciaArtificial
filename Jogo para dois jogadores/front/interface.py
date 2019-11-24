from tkinter import *
from tkinter import messagebox
from back.game import Game
from PIL import Image, ImageTk

from back.ia.main import Problem


class Interface:
    def __init__(self):
        self.master = Tk()
        self.master.title('Jogo da Velha')
        self.master.geometry('800x600')
        self.master.wm_iconbitmap('front/data/images/icone.ico')

        self.header = [Frame(self.master), False]
        self.body = [Frame(self.master), False]
        self.footer = [Frame(self.master), False]

    def _construct_header(self):
        pass

    def _construct_game(self, funct):
        self.body[0].pack()
        self.body[1] = True
        self.board = []
        aux_0 = Frame(self.body[0])
        aux_0.pack(pady=50)

        for i in range(0, 3):
            aux_1 = Frame(aux_0)
            aux_1.pack(side='top')
            board_line = []

            for j in range(0, 3):
                aux_2 = StringVar(value=' ')
                board_line.append(aux_2)

                aux_2 = Button(aux_1, textvariable=aux_2, command=funct((i, j), aux_2),
                               justify=CENTER, font='size: 60', width=5)
                aux_2.pack(side='left')

            self.board.append(board_line)

    def _construct_menu(self, funct):
        self.body[0].pack()

        aux = Image.open('front/data/images/background.png')
        aux = ImageTk.PhotoImage(aux)
        frame = Label(self.body[0], image=aux, width=800, justify='center')
        frame.pack()

        aux = Label(frame, text='Jogo da Velha', font='size: 50', pady=70, justify='center')
        aux.pack()

        aux = Label(frame, text='Novo Jogo', font='size: 30', pady=30, justify='center')
        aux.pack()

        aux = Button(frame, text='P vs P', font='size: 15', pady=10, justify='center', command=funct[0])
        aux.pack()

        aux = Button(frame, text='P vs C', font='size: 15', pady=10, command=funct[1])
        aux.pack()

        self.body[1] = True

    def _construct_body(self, type_body, funct):
        if self.body[1]:
            self._destruct_body()

        if type_body == 0:
            self._construct_game(funct)
        elif type_body == 1:
            self._construct_menu(funct)
        else:
            raise ValueError

    def _destruct_body(self):
        self.body[0].destroy()
        self.body.clear()
        self.body = [Frame(self.master), False]

    def _construct_footer(self):
        pass

    def construct_interface(self, **kwargs):
        self._construct_header()
        self._construct_body(kwargs['type_body'], kwargs['funct'])
        self._construct_footer()

    def run(self):
        self.master.mainloop()


class InGame:
    def __init__(self, interface=Interface()):
        self.interface = interface
        self.game = None
        self.menu_funct = (self.start_game('pvp'), self.start_game('pvc'))

    def _init_menu(self):
        self.interface.construct_interface(type_body=1, funct=self.menu_funct)

    def _init_game(self):
        if self.game is not None:
            del self.game

        self.game = Game()

        self.interface.construct_interface(type_body=0, funct=self.play)

    def win(self, winner):
        if winner is not None:
            if winner == -1:
                messagebox.showinfo('Error', 'A posicão já foi ocupada!')
                return -1
            if winner == 2:
                message = 'Empate'
            else:
                message = f'O player {self.game.names[winner]} ganhou a partida.'

            messagebox.showinfo('Fim do Jogo', message)
            self._init_menu()

    def _execute_play(self, pos, string_var):
        if self.game.make_play(pos) == -1:
            return -1
        else:
            if self.game.board[pos[0]][pos[1]] == 0:
                string_var.set('X')
            else:
                string_var.set('O')

        return self.game.check()[0]

    def play(self, pos, string_var):
        def func():
            aux = self._execute_play(pos, string_var)
            if aux is not None:
                if self.win(aux) == -1:
                    return
            else:
                if self.game.type == 1:
                    problem = Problem(self.game, 2)
                    new_pos = problem.get_solution()
                    new_string_var = self.interface.board[new_pos[0]][new_pos[1]]
                    aux = self._execute_play(new_pos, new_string_var)

                    if aux is not None:
                        self.win(aux)
        return func

    def start_game(self, game_type):
        if game_type != 'pvp' and game_type != 'pvc':
            raise ValueError

        def func():
            self._init_game()
            if game_type == 'pvp':
                self.game.type = 0
            elif game_type == 'pvc':
                self.game.type = 1

        return func

    def run(self):
        self._init_menu()
        self.interface.run()
