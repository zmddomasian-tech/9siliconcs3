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


