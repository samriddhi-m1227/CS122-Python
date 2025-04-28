import tkinter as tk 
from tkinter import ttk
import time
import random 

start_time = None #need this for later 

#5 sentences 
sentences = [
    "Traveling to different countries helps you learn about new cultures, traditions, and ways of life you have never seen before.",
    "A healthy lifestyle requires consistent exercise, balanced nutrition, and maintaining a positive outlook toward daily challenges.",
    "The invention of the internet completely changed how people communicate, access information, and build connections globally.",
    "Reading a wide variety of books can expand your imagination, critical thinking abilities, and improve your communication skills.",
    "Building strong habits early in your academic journey will make learning easier and help you succeed in your future career goals."
]
random_sentence=random.choice(sentences) #choose a random sentence


#Initialize window 
root=tk.Tk()
root.title('Typing Practice App')
root.geometry('700x400')

#Label for random sentence
sentence_label=tk.StringVar()
sentence_label.set(random_sentence)#display a new random sentence 

label1 = ttk.Label(root, textvariable=sentence_label, font=("Arial", 16)) 
label1.pack(padx=20, pady=20) 


#Entry Box for user to type
entry = tk.Text(root,font=('Arial', 16), height=4, width=80)
entry.pack(padx=10, pady=10)


#Label showing time remaining 
time_label=tk.StringVar()
time_label.set('Time Remaining')

label2 = ttk.Label(root, textvariable=time_label, font=("Arial", 16)) 
label2.pack(padx=20, pady=20) 


#Functions:

def start_timer(event):
    """
    starts timer on the first key press.
    If the timer is already running, nothing happens.
    Calls update_timer() to update the remaining time and display it 
    """
    global start_time
    if start_time is None: #only starts if the timer is not currently running 
        start_time=time.time() #current time 
        update_timer()


def check_text(event):
    """
    Checks the user's typed text after each key release.
    If the typed text exactly matches the random sentence,
    the typing test is finished early by calling finish_test().
    """
    typed_text = entry.get("1.0", 'end-1c').strip()  # Remove extra newlines/spaces for clarity
    if typed_text == random_sentence:  # Compare exactly the two strings
        finish_test()


def update_timer():
    """
    Updates the time remaining every second.
    If 60 seconds have passed, automatically finishes the test.
    Uses root.after() to schedule the next timer update.
    """
    global start_time
    if start_time:
        elapsed = int(time.time() - start_time)  # how many seconds passed
        remaining = 60 - elapsed                 # how many seconds left
        if remaining >= 0:
            time_label.set(f"Time Remaining: {remaining}")  
            root.after(1000, update_timer)  # wait one second and call update_timer again
        else:
            finish_test()  # if the time is up, end the test


def finish_test():
    """
    Ends the typing test session.
    Calculates the elapsed time and determines if the user's text exactly matches the random sentence.
    Shows a modal popup with the time taken and exact match status,
    then closes the application window.
    """
    end_time = time.time()
    elapsed = end_time - start_time

    typed_text = entry.get("1.0", 'end-1c').strip()
    exact_match = typed_text == random_sentence

    if not exact_match and elapsed > 60:
        elapsed = 60 # shows 60 seconds exactly if the user timed out 

    from tkinter import messagebox
    messagebox.showinfo("Test Finished",
                        f"Time Taken: {elapsed:.2f} seconds\nExact Match: {exact_match}")
    root.destroy()


#binding the events
entry.bind("<KeyPress>", start_timer) 
entry.bind("<KeyRelease>", check_text)

#run the app
root.mainloop()

