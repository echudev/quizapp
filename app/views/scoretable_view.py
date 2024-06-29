import tkinter as tk
from tkinter import ttk

class ScoreTableView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent
        self.parent.title('Quizapp - Historial de partidas')

        self.data = self.parent.user_controller.get_historial_partidas()
        self.show_table()
               

    def show_table(self):
        print(self.data)
        # creo un contenedor para la tabla y el scrollbar
        container = ttk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)

        # creo un Treeview con columnas
        self.tree = ttk.Treeview(container, columns=('fecha', 'hora', 'puntaje'), show='headings')
        
        # encabezados de las columnas
        self.tree.heading('fecha', text='Fecha')
        self.tree.heading('hora', text='Hora')
        self.tree.heading('puntaje', text='Puntaje')
        
        # ancho de columnas
        self.tree.column('fecha', width=100, anchor='center')
        self.tree.column('hora', width=100, anchor='center')
        self.tree.column('puntaje', width=100, anchor='center')

        # creo el Scrollbar vertical
        scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # pack del Treeview y el Scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
          
        # agrego datos en el Treeview
        for item in self.data:
            self.tree.insert('', tk.END, values=item)
    
        goback_button = ttk.Button(self, text="Volver", padding=(20, 10), command = self.volver)
        goback_button.pack(pady=20)
    
    
    def volver(self):
        self.parent.show_frame('ProfileView')
