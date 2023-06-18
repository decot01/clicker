import customtkinter
import json

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def save_settings():
    with open("settingsclicker.txt", "w") as f:
        settings = {
            "slider_value": slider_1.get(),
            "entry_text": entry_1.get(),
        }
        json.dump(settings, f)

def load_settings():
    try:
        with open("settingsclicker.txt", "r") as f:
            settings = json.load(f)
            slider_1.set(settings["slider_value"])
            entry_1.insert(0, settings["entry_text"])
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass

app = customtkinter.CTk()
app.geometry("400x350")
app.title("clicker")

def slider_callback(value):
    progressbar_1.set(value)

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
label_1.pack(pady=10, padx=10)

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=10, padx=10)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=10, padx=10)
slider_1.set(0.5)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="bind1:")
entry_1.pack(pady=10, padx=10)

button_save = customtkinter.CTkButton(master=frame_1,text="Сохранить", command=save_settings)
button_save.pack(pady=10, padx=10)

button_load = customtkinter.CTkButton(master=frame_1,text="Загрузить", command=load_settings)
button_load.pack(pady=10, padx=10)

app.mainloop()
