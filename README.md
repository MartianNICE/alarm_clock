# Alarm Clock

## Overview
This project is a simple **Alarm Clock** implemented in Python. It counts down from a specified number of seconds and plays a sound when the countdown reaches zero. The code is designed to be straightforward and demonstrates basic programming concepts such as loops, time management, and audio playback.

---

## Features
- Countdown timer with a clear and updating display.
- Plays an audio file (`ringtone.mp3`) when the timer ends.

---

## How It Works
1. **Timer Setup:** The `alarm` function takes the countdown time in seconds as input.
2. **Countdown Logic:** During the countdown, the remaining time is displayed in the format `MM:SS` (minutes:seconds).
3. **Alarm Trigger:** Once the countdown reaches zero, the alarm sound is played using the `playsound` library.

---

## Requirements
- Python 3.x
- `playsound` module for audio playback.

---

## Installation
1. Clone this repository or download the code.
2. Install the required module:
   ```bash
   pip install playsound
   ```
3. Ensure the `ringtone.mp3` file is present in the same directory as the script.

---

## Usage
1. Update the `alarm(seconds)` call in the script to set your desired countdown time (in seconds).
2. Run the script:
   ```bash
   python main.py
   ```
3. The countdown timer will start, and the alarm sound will play when the timer ends.

---

## Customization
- Replace `ringtone.mp3` with any MP3 file of your choice for a custom alarm sound.
- Adjust the countdown time by changing the argument passed to the `alarm` function.

---

## Example
```python
alarm(300)  # Sets a 5-minute timer
```

---

## Notes
- Ensure that the MP3 file path is correct if the file is not in the same directory as the script.
- Use a compatible MP3 file to avoid playback issues.

---

Happy coding! ⏰