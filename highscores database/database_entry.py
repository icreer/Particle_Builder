import tkinter as tk

import high_scores

HighScores = high_scores.HighScores()

class Main():
    def __init__(self,root):
        self.root = root
        clear_button = tk.Button(self.root,text="Clear",command=self.clear)
        clear_button.grid(row=3,column=4)
        
        user_entry_label = tk.Label(self.root,text="New Score User:")
        user_entry_label.grid(row=1,column=1)

        self.user_entry = tk.Entry(self.root)
        self.user_entry.grid(row=1,column=2)

        score_entry_label = tk.Label(self.root,text="New Score Amount: ")
        score_entry_label.grid(row=2,column=1)

        self.score_entry = tk.Entry(self.root)
        self.score_entry.grid(row=2,column=2)

        add_score_button = tk.Button(self.root,text="Add Score",command=self.add_score)
        add_score_button.grid(row=3,column=2)

    def clear(self):
        HighScores.clear_top_ten()
    
    def add_score(self):
        HighScores.update_top_ten(int(self.score_entry.get()),self.user_entry.get())


root = tk.Tk()
main = Main(root)
main.root.mainloop()