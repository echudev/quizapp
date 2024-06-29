from tkinter import ttk, StringVar

class ProfileView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent
        self.parent.title('Quizapp - Perfil')   
        # defino variables de estado 
        self.username = StringVar()
        self.partidas_jugadas = StringVar()
        self.mejor_puntaje = StringVar()
        self.username.set(self.parent.user_controller.get_user())
        self.partidas_jugadas.set(self.parent.user_controller.get_partidas_jugadas())
        self.mejor_puntaje.set(self.parent.user_controller.get_mejor_puntaje())

        profile_container = ttk.LabelFrame(self, text='Mis Datos')
        username_frame = ttk.Frame(profile_container)
        username_label = ttk.Label(username_frame, text="Nombre de usuario:", font=("Arial", 14))
        username = ttk.Label(username_frame, textvariable=self.username, font=("Arial", 20), foreground="lightgreen")
        username_label.pack(padx=5, side="left")
        username.pack(padx=5, side="left")
        username_frame.pack(pady=5, padx=15)
        
        partidas_jugadas_frame = ttk.Frame(profile_container)
        partidas_jugadas_label = ttk.Label(partidas_jugadas_frame, text="Partidas jugadas:", font=("Arial", 14))
        partidas_jugadas = ttk.Label(partidas_jugadas_frame, textvariable=self.partidas_jugadas, font=("Arial", 20), foreground="lightgreen")
        partidas_jugadas_label.pack(padx=5, side="left")
        partidas_jugadas.pack(padx=5, side="left")
        partidas_jugadas_frame.pack(pady=5, padx=15)

        mejor_puntaje_frame = ttk.Frame(profile_container)
        mejor_puntaje_label = ttk.Label(mejor_puntaje_frame, text="Mejor puntaje:", font=("Arial", 14))
        mejor_puntaje = ttk.Label(mejor_puntaje_frame, textvariable=self.mejor_puntaje, font=("Arial", 20), foreground="lightgreen")
        mejor_puntaje_label.pack(padx=5, side="left")
        mejor_puntaje.pack(padx=5, side="left")
        mejor_puntaje_frame.pack(pady=5, padx=15)
        profile_container.pack(padx=20, pady=30)

        buttons_frame = ttk.Frame(self)
        historial_button = ttk.Button(buttons_frame, text="Historial", padding=(20, 10), command = self.ver_historial)
        play_again_button = ttk.Button(buttons_frame, text="Volver", padding=(20, 10), command = self.volver)
        historial_button.pack(padx=20, pady=10)
        play_again_button.pack(padx=20, pady=10)
        buttons_frame.pack(pady=40)
    
    
    def volver(self):
        self.parent.show_frame('IntroView')

    def ver_historial(self):
        self.parent.show_frame('ScoreTableView')