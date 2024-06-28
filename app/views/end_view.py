from tkinter import ttk
from tkinter import messagebox


class EndView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent
               

        text_frame = ttk.Frame(self)
        label = ttk.Label(text_frame, text=f'Felicitaciones! llegaste al final', font=("Arial", 20))
        label.pack(pady=20, side='left')
        label_name = ttk.Label(text_frame, textvariable=self.parent.user_controller.user_model.username, font=("Arial", 20), foreground="lightgreen")
        label_name.pack(pady=20, side='left')
        text_frame.pack(pady=20, padx=20)
        
        text_frame2 = ttk.Frame(self)
        points_label = ttk.Label(text_frame2, text=f'Hiciste', font=("Arial", 14))
        points_label.pack(pady=20, side='left')
        points_label2 = ttk.Label(text_frame2, textvariable=self.parent.game_controller.model.puntaje, font=("Arial", 20), foreground="lightgreen")
        points_label2.pack(pady=20, side='left')
        points_label3 = ttk.Label(text_frame2, text=f'puntos.', font=("Arial", 14))
        points_label3.pack(pady=20, side='left')
        text_frame2.pack(pady=20, padx=20)

    
        buttons_frame = ttk.Frame(self)
        play_again_button = ttk.Button(buttons_frame, text="Jugar de nuevo", padding=(20, 10), command = lambda: print('jugad de nuevo'))
        play_again_button.pack(padx=5, side='left')
        profile_button = ttk.Button(buttons_frame, text="Mi Perfil", padding=(20, 10), command = lambda: print('mi perfil'))
        profile_button.pack(padx=5, side='left')
        logout_button = ttk.Button(buttons_frame, text="Salir", padding=(20, 10), command = lambda: print('Salir'), bootstyle="warning")
        logout_button.pack(padx=5, side='left')
        buttons_frame.pack(pady=20, padx=20)
    
    
    def volver_a_jugar(self):
        self.parent.show_frame('IntroView')

    def ver_perfil(self):
        self.parent.show_frame('PerfilView')

    def salir(self):
        messagebox.showinfo("Hasta luego!", "Gracias por jugar!")
        self.parent.show_frame('LoginView')