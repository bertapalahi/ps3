# ps3

In this project I implemented an interactive main. The user will be able to choose between different possibilities. The main will be the following:

[1] Convert codec & video codec comparison.

[2] Live streaming BBB.mp4, choosing the IP of the broadcast. 

So when the user clicks the first option the main will allow to choose also the codec (vp8, vp9, .h265 and av1) and the size of the video. After the video converted will show the comparison between these videos.
The second option will stream the BBB video allowing the user to choose the IP address.

Important: when you use the av1 codec, to install FFmpeg with support for libaom-av1, you should compile FFmpeg with the *--enable-libaom* option.



References:
http://trac.ffmpeg.org/wiki/Encode/AV1
