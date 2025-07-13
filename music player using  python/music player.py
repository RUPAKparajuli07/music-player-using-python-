
        # Initialize Pygame mixer
        pygame.mixer.init()
        
        # Track list
        self.track_list = []
        self.current_track_index = 0
        
        # Create UI components
        self.track_label = tk.Label(root, text="\nTrack: ", font=("Times New Roman", 30), fg="red", bg="black")
        self.track_label.pack(anchor="center")
        
        self.duration_label = tk.Label(root, text="\nDuration: ", font=("Times New Roman", 30), fg="red", bg="black")
        self.duration_label.pack(anchor="center")
        
        self.time_label = tk.Label(root, text="\nTime: ", font=("Times New Roman", 30), fg="red", bg="black")
        self.time_label.pack(anchor="center")
        
        self.controls_frame = tk.Frame(root)
        self.controls_frame.pack(pady=10, anchor="center")
        
        self.previous_button = tk.Button(self.controls_frame, text="\n<< Previous", font=("Times New Roman", 30), fg="red", bg="black", command=self.play_previous)
        self.previous_button.pack(side=tk.LEFT)
        
        self.play_button = tk.Button(self.controls_frame, text="\nPlay", font=("Times New Roman", 30), fg="red", bg="black", command=self.select_and_play)
        self.play_button.pack(side=tk.LEFT)
        
        self.next_button = tk.Button(self.controls_frame, text="\nNext >>", font=("Times New Roman", 30), fg="red", bg="black", command=self.play_next)
        self.next_button.pack(side=tk.LEFT)
        
        # Load tracks from a directory
        self.load_tracks()
        
        # Set initial track
        if self.track_list:
            self.set_track(self.track_list[0])
        
        # Add music quote
        self.quote_label = tk.Label(root, text=" 'Music is the soundtrack of life'", font=("Times New Roman", 40), fg="orange", bg="black")
        self.quote_label.place(relx=0.5, rely=1.0, anchor="s")
    
    def load_tracks(self):
        # Replace the path below with the actual path to your music directory
        directory = "C:/Users/paraj/Music"
        
        for file in os.listdir(directory):
            if file.endswith(".mp3"):
                self.track_list.append(os.path.join(directory, file))
    
    def set_track(self, track_path):
        self.current_track_index = self.track_list.index(track_path)
        pygame.mixer.music.load(track_path)
        self.track_label["text"] = "Track: " + os.path.basename(track_path)
        
        # Get duration and update duration label
        audio = MP3(track_path)
        duration = self.format_time(audio.info.length)
        self.duration_label["text"] = "Duration: " + duration
    
    def play_pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.play_button["text"] = "Play"
        else:
            pygame.mixer.music.unpause()
            self.play_button["text"] = "Pause"
    
    def play_previous(self):
        if self.current_track_index > 0:
            self.current_track_index -= 1
            self.set_track(self.track_list[self.current_track_index])
            pygame.mixer.music.play()
    
    def play_next(self):
        if self.current_track_index < len(self.track_list) - 1:
            self.current_track_index += 1
            self.set_track(self.track_list[self.current_track_index])
            pygame.mixer.music.play()

    def select_and_play(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.track_list = [file_path]
            self.set_track(file_path)
            pygame.mixer.music.play()
    
    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def update_time(self):
        if pygame.mixer.music.get_busy():
            current_time = pygame.mixer.music.get_pos() / 1000
            current_time_str = self.format_time(current_time)
            self.time_label["text"] = "Time: " + current_time_str
        
        self.root.after(1000, self.update_time)
    
# Create the main window
root = tk.Tk()
root.geometry("400x400")
root.configure(bg="black")

# Center the window on the screen
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth()/2 - window_width/2)
position_down = int(root.winfo_screenheight()/2 - window_height/2)
root.geometry(f"+{position_right}+{position_down}")

# Create an instance of the MusicPlayer class
music_player = MusicPlayer(root)

# Start updating the current playing time
music_player.update_time()

# Start the main event loop
root.mainloop()
