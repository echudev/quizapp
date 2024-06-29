from tkinter import ttk

class ProfileView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent
               
        username_frame = ttk.Frame(self)
        username_label = ttk.Label(username_frame, text="Nombre de usuario:", font=("Arial", 14))
        username_label.pack(pady=10, padx=5, side="left")
        username = ttk.Label(username_frame, textvariable=self.parent.user_controller.user_model.username, font=("Arial", 20), foreground="lightgreen")
        username.pack(pady=10, padx=5, side="left")
        username_frame.pack(pady=10)
        
        partidas_jugadas_frame = ttk.Frame(self)
        partidas_jugadas_label = ttk.Label(partidas_jugadas_frame, text="Partidas jugadas:", font=("Arial", 14))
        partidas_jugadas_label.pack(pady=10, padx=5, side="left")
        partidas_jugadas = ttk.Label(partidas_jugadas_frame, textvariable=self.parent.user_controller.user_model.partidas_jugadas, font=("Arial", 20), foreground="lightgreen")
        partidas_jugadas.pack(pady=10, padx=5, side="left")
        partidas_jugadas_frame.pack(pady=10)

        mejor_puntaje_frame = ttk.Frame(self)
        mejor_puntaje_label = ttk.Label(mejor_puntaje_frame, text="Mejor puntaje:", font=("Arial", 14))
        mejor_puntaje_label.pack(pady=10, padx=5, side="left")
        mejor_puntaje = ttk.Label(mejor_puntaje_frame, textvariable=self.parent.user_controller.user_model.mejor_puntaje, font=("Arial", 20), foreground="lightgreen")
        mejor_puntaje.pack(pady=10, padx=5, side="left")
        mejor_puntaje_frame.pack(pady=10)

        historial_button = ttk.Button(self, text="Historial", padding=(20, 10), command = self.ver_historial)
        historial_button.pack(padx=10, pady=10)
    
        play_again_button = ttk.Button(self, text="Volver", padding=(20, 10), command = self.volver)
        play_again_button.pack(padx=10, pady=10)
    
    
    def volver(self):
        self.parent.show_frame('IntroView')

    def ver_historial(self):
        self.parent.show_frame('ScoreTableView')