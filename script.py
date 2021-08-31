from tkinter import *
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube
import threading

class App:
	def __init__(self, master):
		self.master = master
		self.master.title('Youtube Video Downloader')
		self.master.maxsize(400, 464)
		self.master.minsize(400, 464)
		self.master.iconbitmap("youtube.ico")
		self.master.protocol("WM_DELETE_WINDOW", self.exit)
		self.set_up()
		self.master.mainloop()

	def exit(self):
		ask = messagebox.askyesno("Exit", "Are you sure that you want to exit?")
		if ask == 1:
			self.master.destroy()

	def clear(self):
		lis = self.master.winfo_children()
		for i in lis:
			i.destroy()

	def set_up(self):
		self.lab_url = Label(self.master, text="Enter the url: ", font=('Helvetica', 16))
		self.entry_url = Entry(self.master, font=('Helvetica', 16), width=25)
		self.lab_file_path = Label(self.master, text="Choose Filepath: ", font=('Helvetica', 16))
		self.entry_file_path = Entry(self.master, font=('Helvetica', 16), width=15)
		self.browse_btn = Button(self.master, text="Browse", activebackground="blue", activeforeground="white", font=('Helvetica', 14), width = 10, bg="blue", fg="white", command = self.browse)
		self.download_btn = Button(self.master, padx=5, pady=2.5, text="Download", activebackground="green", activeforeground="white", font=('Helvetica', 14), width = 10, bg="green", fg="white", command = self.download_video)
		self.entry_file_path.insert(0, "C:/")
		self.lab_url.place(x=50, y=50)
		self.entry_url.place(x=50, y=100)
		self.lab_file_path.place(x=50, y=150)
		self.entry_file_path.place(x=50, y=200)
		self.browse_btn.place(x=250, y=200)
		self.download_btn.place(x=50, y=250)

	def browse(self):
		self.filepath = filedialog.askdirectory(initialdir="C:/", title = "Save Video")
		self.entry_file_path.delete(0, "end")
		self.entry_file_path.insert(0, self.filepath)

	def downloading(self):
		video = self.youtube.streams.get_highest_resolution()
		video.download(self.path)

	def show_progress(self):
		self.clear()
		self.progress_title = Label(self.master, text="Downloading", font=('Helvetica', 16))
		self.progressbar = ttk.Progressbar(self.master, orient="horizontal", length=500, mode='determinate')
		self.progress_title.place(x=50, y=150)
		self.progressbar.place(x=50, y=200)


	def download_video(self):
		self.url = self.entry_url.get()
		self.youtube = YouTube(self.url)
		self.path = self.entry_file_path.get()
		self.title = self.youtube.title
		# t1 = threading.Thread(target=self.downloading)
		# t2 = threading.Thread(target=self.youtube.register_on_progress_callback(self.show_progress))
		# t2.start()
		# t1.start()

window = Tk()
downloader = App(window)