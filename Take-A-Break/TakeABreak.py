import time
import webbrowser
total_breaks = 3
break_count = 0
while ( break_count < total_breaks ):
    print time.ctime()
    time.sleep(50)
    webbrowser.open_new( "https://www.youtube.com/watch?v=PT2_F-1esPk" )
    break_count = break_count + 1
