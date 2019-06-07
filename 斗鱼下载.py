
import os
import _thread as thread


m3u8_address = []

path = "D:\Downloads\\"""


def get_command(address, name, path, thread):
    command = "ffmpeg -threads "+thread+" -i "+"\""+address+"\""+" -c copy -y -bsf:a aac_adtstoasc "+"\""+path+name+".mp4"+"\""
    return command


def call_command(command):
    os.system(command)


while True:
    new_address = input("Input m3u8 adress:")
    if new_address == "finish":
        break
    else:
        m3u8_address.append(new_address)

for i in range(len(m3u8_address)):
    command = get_command(m3u8_address[i], "No_"+str(i), path, str(i))
    try:
        thread.start_new_thread( call_command, (command, ) )
    except:
        print("Error: unable to start thread")