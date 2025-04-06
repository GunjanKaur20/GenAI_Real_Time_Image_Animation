from moviepy.editor import VideoFileClip

# Load the GIF file
clip = VideoFileClip("inputs/driving.gif")

# Convert and save as MP4
clip.write_videofile("inputs/driving.mp4", codec="libx264")
