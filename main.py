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
		self.clear()
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
		self.video.download(self.path)

	def set_up_progress_bar(self):
		self.clear()
		self.progress_title = Label(self.master, text="Downloading", font=('Helvetica', 16))
		self.progressbar = ttk.Progressbar(self.master, orient="horizontal", length=300, mode='determinate')
		self.progress_title.place(x=50, y=150)
		self.progressbar.place(x=50, y=200)

	def show_progress(self, stream, data, byte):
		self.progressbar['value'] = 100 - ((byte/self.max_file_size) * 100)


	def download_finished(self, stream, filepath):
		messagebox.showinfo("Download Finshed", "Download has been completed! The file " + self.title + " is successfully stored in " + self.path)
		self.set_up()
		self.url = None;
		self.youtube = None;
		self.path = None;
		self.title = None;
		self.video = None;
		self.max_file_size = None;



	def download_video(self):
		self.url = self.entry_url.get()
		try:
			self.youtube = YouTube(self.url, on_progress_callback=self.show_progress, on_complete_callback=self.download_finished)
			self.path = self.entry_file_path.get()
			self.title = self.youtube.title
			self.video = self.youtube.streams.get_highest_resolution()
			self.max_file_size = self.video.filesize
			self.set_up_progress_bar()
			messagebox.showinfo("Starting Download", "Download will soon start please wait!")
			t1 = threading.Thread(target=self.downloading)
			t1.start()
		except:
			messagebox.showinfo("Error!", "An error occured due to the video not being available or due to internet connnection! Please check your connection or check the video link and try again later!")
			self.set_up()
			self.url = None;
			self.youtube = None;
			self.path = None;
			self.title = None;
			self.video = None;
			self.max_file_size = None;
			return

window = Tk()
downloader = App(window)