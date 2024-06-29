from tkinter import ttk

class EndView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent
               

        text_frame = ttk.Frame(self)
        label = ttk.Label(text_frame, text=f'Felicitaciones!', font=("Arial", 20))
        label.pack(pady=5, side='left')
        label_name = ttk.Label(text_frame, textvariable=self.parent.user_controller.user_model.username, font=("Arial", 20), foreground="lightgreen")
        label_name.pack(pady=5, side='left')
        text_frame.pack(padx=20)

        label2 = ttk.Label(self, text=f'Llegaste al final!', font=("Arial", 16))
        label2.pack(pady=10)
        
        text_frame2 = ttk.Frame(self)
        points_label = ttk.Label(text_frame2, text=f'Hiciste', font=("Arial", 20))
        points_label.pack(pady=20, side='left')
        points_label2 = ttk.Label(text_frame2, textvariable=self.parent.game_controller.model.puntaje, font=("Arial", 20), foreground="lightgreen")
        points_label2.pack(pady=20, side='left')
        points_label3 = ttk.Label(text_frame2, text=f'puntos.', font=("Arial", 20))
        points_label3.pack(pady=20, side='left')
        text_frame2.pack(pady=20, padx=20)

    
        play_again_button = ttk.Button(self, text="Volver", padding=(20, 10), command = self.volver)
        play_again_button.pack(pady=20)
    
    
    def volver(self):
        self.parent.show_frame('IntroView')
