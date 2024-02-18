import tkinter as tk

app = tk.Tk()
times = 0
def on_btn_click():
    global times
    times += 1
    app.title = f"You have clicked this button {times} times"
    label.delete(1.0, tk.END)
    label.insert(tk.END, f"The button has been clicked {times} times")
    print(app.title)
label = tk.Text(app)
btn1 = tk.Button(app, text="Click me!", command=on_btn_click)
btn1.pack()
label.pack()
# Run the application
app.mainloop()