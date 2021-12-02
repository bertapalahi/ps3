
import os

# ex1. Remember you have the BBB video converted
# into these? 720p, 480p, 360x240, 160x120
# Convert them into VP8, VP9, h265 & AV1.
def resize_video(video, factor):
    if factor == "1":
        f = '1280:720'
    elif factor == "2":
        f = '854:480'
    elif factor == "3":
        f = '360:240'
    elif factor == "4":
        f = '160:120'
    else:
        print("The possibles are: 1, 2, 3 or 4")

    cmd = "ffmpeg -i {} -vf scale={} resized_video.mp4".format(video, f)
    os.system(cmd)

    return "resized_video.mp4"

def ex1(video, codec): # Automatize all these tasks inside a new class in Python
    if codec == "1":
        cmd = "ffmpeg -i {} -c:v libvpx -b:v 1M -c:a libvorbis video_vp8.webm".format(video)
        os.system(cmd)
        video_encoded = "video_vp8.webm"
    elif codec == "2":
        cmd = "ffmpeg -i {} -c:v libvpx-vp9 -b:v 2M video_vp9.webm".format(video)
        os.system(cmd)
        video_encoded = "video_vp9.webm"
    elif codec == "3":
        cmd = "ffmpeg -i {} -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k video_h265.mp4".format(video)
        os.system(cmd)
        video_encoded = "video_h265.mp4"
    elif codec == "4":
        cmd = "ffmpeg -i {} -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental video_av1.mkv".format(video)
        os.system(cmd)
        video_encoded = "video_av1.mkv"
    else:
        print("The possibles are: 1, 2, 3 or 4")

    return video_encoded

# ex2. Create a script that will export 2 video
# comparision.
# Then choose 2 codecs of the 4 mentioned
# before, create the output and comment the
# differences you find there
def ex2(video1, video2):
    cmd = "ffplay -f lavfi 'movie={}[a];movie={}[b]; [a][b]blend=all_mode=difference'".format(video1, video2)
    os.system(cmd)

# ex3. Try to achieve with FFMPEG to create a live
# streaming of the BBB Video. You should
# broadcast it into an IP address (locally of
# course) and open this IP or URL inside VLC
# Media Player.Create a script that let you choose the IP to
# broadcast the previous video
def ex3(video, host, port):
    # -i: tells ffmpeg where to pull the input stream from
    # -re: Read input at native frame rate. Mainly used to simulate a grab device.
    # -f: flv says to deliver the output stream in an flv wrapper
    # mpegts: with udp you need to be careful and use a muxer that supports 'connecting anytime'
    cmd = "ffmpeg -re -i {} -c copy -f mpegts udp://{}:{}".format(video, host, port) #this video will be streamed to the port and to the following ip
    os.system(cmd)
    cmd = "ffplay rtp://{}:{}".format(host, port) #receive the stream using VLC
    os.system(cmd)

def decide_codec():
    codec = input("Choose what codec you want to convert (1, 2, 3 or 4): \n"
                  "[1] vp8 \n"
                  "[2] vp9 \n"
                  "[3] h265 \n"
                  "[4] av1 \n"
                  "Type 1, 2, 3 or 4: ")
    return codec


# main
if __name__ == '__main__':
    video = "BBB_12s.mp4" #input video
    ip = "127.0.0.1"
    port = "1234"

    #main output to the user
    print("You almost did it! One last step. \n" 
          "What do you want to do?\n "
          "[1] Convert codec & video codec comparison \n "
          "[2] Live streaming BBB.mp4, choosing the IP of the broadcast \n ")
    option = input("Type 1 or 2: ")

    if option == "1":
        print("Let's start the codecs war...")

        factor = input("First, choose in which factor you want your video (1, 2, 3 or 4): \n"
                       "[1] 720p\n"
                       "[2] 480p \n"
                       "[3] 360x240\n"
                       "[4] 160x120\n"
                       "Type 1, 2, 3 or 4: ")

        video_resized = resize_video(video, factor)
        video_encoded1 = ex1(video_resized, decide_codec())

        print("Let's compare with another codec.")
        video_encoded2 = ex1(video_resized, decide_codec())

        #video comparison function
        ex2(video_encoded1, video_encoded2)

    elif option == "2":
        print("Video stream")
        ip = input("Choose the IP address (xxx.x.x.x): ")
        ex3(video, ip, port)
    else:
        option = input("Incorrect! Please, introduce 1 or 2")






