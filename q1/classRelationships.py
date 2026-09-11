
class Song:

  def __init__(self, title, artist, duration):
    self.title = title
    self.artist = artist
    self.duration = duration  
    self.is_playing = False
    self.is_paused = False
    self.current_time = 0
    self.repeat_mode = False

  def play(self):
    if self.is_playing and not self.is_paused:
      print(f"'{self.title}' is already playing.")
      return

    if self.is_paused:
      self.is_paused = False
      print(f"Resumed '{self.title}' from {self.current_time}s.")
    else:
      self.is_playing = True
      self.is_paused = False
      print(f"Playing '{self.title}' by {self.artist}.")

  def pause(self):
    if not self.is_playing or self.is_paused:
      print(f"'{self.title}' is not currently playing.")
      return

    self.is_paused = True
    print(f"Paused '{self.title}' at {self.current_time}s.")

  def set_playback(self, seconds):
    if 0 <= seconds <= self.duration:
      self.current_time = seconds
      print(f"Playback moved to {self.current_time}s.")
    else:
      print("Invalid playback time.")

  def toggle_repeat(self):
    self.repeat_mode = not self.repeat_mode
    status = "ON" if self.repeat_mode else "OFF"
    print(f"Repeat mode is now {status}.")

  def update_playback(self, seconds_passed):
    if self.is_playing and not self.is_paused:
      self.current_time += seconds_passed
      if self.current_time >= self.duration:
        if self.repeat_mode:
          self.current_time = 0
          print(f"Repeating '{self.title}'.")
        else:
          self.current_time = self.duration
          self.is_playing = False
          print(f"Finished playing '{self.title}'.")

class Playlist:
    
    def __init__(self, name: str):
        self.name = name
        self.tracks = []
        
    def add_song(self, song: Song):
        if isinstance(song, Song):
            self.tracks.append(song)
            print(f"Added {song.title} to '{self.name}'.")
            return True
        print("Error: Only instances of the Song class can be added.")
        return False

    def remove_song(self, title: str):
        for song in self.tracks:
            if song.title.lower() == title.lower():
                self.tracks.remove(song)
                print(f"Removed '{song.title}' from '{self.name}'.")
                return True
        print(f"Song '{title}' not found in '{self.name}'.")
        return False

    def get_total_duration(self):
        total_seconds = sum(song.duration for song in self.tracks)
        seconds = total_seconds 
        return f"{seconds}s"

    def display_playlist(self):
        print(f"\n--- Playlist: {self.name} ---")
        if not self.tracks:
            print("  [No songs in this playlist]")
            return
        
        for index, song in enumerate(self.tracks, start=1):
            print(f"{index}. {song}")
        print(f"Total Runtime: {self.get_total_duration()}\n")
