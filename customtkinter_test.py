import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import os



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x500")
        self.title("multithread uploader and downloader")

        container = ctk.CTkFrame(master=self)
        container.pack(fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for i in (MainFrame, UploadFrame, UploadedFilesFrame, HelpFrame, CreditsFrame):
            name = i.__name__
            frame = i(parent=container, controller=self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        
        current_frame: ctk.CTkFrame = None

        self.show_frame("MainFrame")
    
    def show_frame(self, name: str):
        frame: ctk.CTkFrame = self.frames[name]
        self.current_frame = frame
        frame.tkraise()



class MainFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame, controller: App):
        super().__init__(master=parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        frame1 = ctk.CTkFrame(master=self)
        frame1.grid(
            row=0
        )

        title = ctk.CTkLabel(
            master=frame1,
            text="MULTITHREADED DRIVE STIMULATOR",
            font=('Arial',30),
        )
        title.pack(
            padx=16, pady=16,
            expand = True
        )

        frame2 = ctk.CTkFrame(master=self)
        frame2.grid(
            row=1,
            padx=16,
            sticky="nsew"
        )
        frame2.grid_columnconfigure(0, weight=1)

        upload_button = ctk.CTkButton(
            master=frame2,
            text="UPLOAD",
            font=('Arial',16),
            image=ctk.CTkImage(
                light_image=Image.open("images\cloud-upload.png"),
                size=(32,32)
            ),
            command=lambda: controller.show_frame("UploadFrame")
        )
        upload_button.grid(
            row=0,
            padx=16, pady=16,
            sticky="nsew"
        )

        download_button = ctk.CTkButton(
            master=frame2,
            text="DOWNLOAD",
            font=('Arial',16),
            image=ctk.CTkImage(
                light_image=Image.open("images\cloud-download.png"),
                size=(32,32)
            ),
            command=lambda: controller.show_frame("UploadedFilesFrame")
        )
        download_button.grid(
            row=1,
            padx=16, pady=16,
            sticky="nsew"
        )

        frame3 = ctk.CTkFrame(master=self)
        frame3.grid(
            row=2,
            padx=16, pady=16,
            sticky="nsew"
        )
        frame3.grid_columnconfigure(0, weight=1)
        frame3.grid_columnconfigure(1, weight=1)

        credits_button = ctk.CTkButton(
            master=frame3,
            text="HELP",
            font=('Arial',16),
            command=lambda: controller.show_frame("HelpFrame")
        )
        credits_button.grid(
            padx=16,
            pady=16
        )

        credits_button = ctk.CTkButton(
            master=frame3,
            text="CREDITS",
            font=('Arial',16),
            command=lambda: controller.show_frame("CreditsFrame")
        )
        credits_button.grid(
            row=0, column=1,
            padx=16,
            pady=16
        )



class UploadFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame, controller: App):
        super().__init__(master=parent)

        return_button = ctk.CTkButton(
            master=self,
            text="",
            width=1,
            image=ctk.CTkImage(
                light_image=Image.open("images\\return.png"),
                size=(32,32)
            ),
            command=lambda: controller.show_frame("MainFrame")
        )
        return_button.pack(
            padx=16, pady=16,
            anchor="w"
        )

        frame = ctk.CTkFrame(master=self)
        frame.pack(
            padx=16, pady=16,
            fill="both",
            expand=True
        )
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        frame2 = ctk.CTkFrame(
            master=frame,
            fg_color="transparent"
        )
        frame2.grid(sticky="ew")
        frame2.grid_rowconfigure(0, weight=1)
        frame2.grid_rowconfigure(1, weight=1)
        frame2.grid_columnconfigure(0, weight=1)

        choose_file_frame = ctk.CTkFrame(master=frame2)
        choose_file_frame.grid(sticky="ew")
        choose_file_frame.grid_columnconfigure(0, weight=0)
        choose_file_frame.grid_columnconfigure(1, weight=1)

        choose_file_button = ctk.CTkButton(
            master=choose_file_frame,
            text="Choose a File",
            font=('Arial',16),
            command=self.open_file_dialog
        )
        choose_file_button.grid(padx=16)

        self.file_label = ctk.CTkLabel(master=choose_file_frame, text="No file selected", width=20)
        self.file_label.grid(pady=16, row=0, column=1)

        upload_button = ctk.CTkButton(master=frame2, text="Upload", font=('Arial',16))
        upload_button.grid(row=1, padx=16, sticky="w")

        #upload_title1 = ctk.CTkLabel(master=frame2, text="UPLOAD FILE", font=('Roboto',40))
        #upload_title1.grid(padx = 1, pady=1, sticky="nsew", row=0, column=0)
    
    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=(("All files", "*.*"), ("Text files", "*.txt"), ("Image files", "*.jpg *.png"), ("PDF files", "*.pdf"), ("Word files", "*.docx"))
        )
        if file_path:
            self.file_label.configure(text=f"Selected file: {self.truncate_text(text=os.path.basename(file_path), max_length=32)}")
    
    def truncate_text(self, text, max_length):
            if len(text) > max_length:
                return text[:max_length-3] + "..."
            return text



class UploadedFilesFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame, controller: App):
        super().__init__(master=parent)

        return_button = ctk.CTkButton(
            master=self,
            text="",
            width=1,
            image=ctk.CTkImage(
                light_image=Image.open("images\\return.png"),
                size=(32,32)
            ),
            command=lambda: controller.show_frame("MainFrame")
        )
        return_button.pack(
            padx=16, pady=16,
            anchor="w"
        )

        scrollable_frame = ctk.CTkScrollableFrame(master=self)
        scrollable_frame.pack(
            padx=16, pady=16,
            fill="both", expand=True
        )

        label = ctk.CTkLabel(master=scrollable_frame, text="no files")
        label.pack(
            fill="both", expand=True
        )



class HelpFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame, controller: App):
        super().__init__(master=parent)



class CreditsFrame(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame, controller: App):
        super().__init__(master=parent)



if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    
    app = App()
    app.mainloop()
