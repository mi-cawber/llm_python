import tkinter as tk
from tkinter import font

def show_motivational_phrase():
    # Create the main window
    window = tk.Tk()
    window.title("Daily Motivation")
    
    # Set the window size and position it in center of screen
    window_width = 400
    window_height = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    # Add some style
    window.configure(bg='#f0f0f0')
    
    # Your motivational phrase
    phrase = "Believe you can and you're halfway there."
    
    # Create a custom font
    custom_font = font.Font(family="Helvetica", size=14, weight="bold")
    
    # Create and place the label with the phrase
    label = tk.Label(
        window, 
        text=phrase,
        font=custom_font,
        bg='#f0f0f0',
        fg='#333333',
        wraplength=350
    )
    label.pack(expand=True)
    
    # Start the main loop
    window.mainloop()

# Run the function
show_motivational_phrase()