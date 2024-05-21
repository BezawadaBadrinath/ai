from pygame import mixer as mix
mix.init()
def play_song(path):
    mix.music.load(path)
    mix.music.play()
    mix.music.set_volume(1)
def control(inp):
    
    if(inp == "stop"):
        mix.music.stop()
    elif(inp == "pause"):
        mix.music.pause()
    elif(inp == "play"):
        mix.music.play()
    elif(inp=="unpause"):
        mix.music.unpause()
if  __name__=="__main__":
    print("i'm inside the sample.py")