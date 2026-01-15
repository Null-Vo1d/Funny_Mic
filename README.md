# Funny_Mic
A way to recreate Funny Mic in python


First run soundlist.bat or alternativly 'python soundlist.py' in terminal

that will give you something like this:

>1 Voicemeeter Out B1 (VB-Audio Vo, MME (8 in, 0 out)
2 Voicemeeter Out A2 (VB-Audio Vo, MME (8 in, 0 out)
3 Voicemeeter Out A1 (VB-Audio Vo, MME (8 in, 0 out)
4 Voicemeeter Out A3 (VB-Audio Vo, MME (8 in, 0 out)
5 Voicemeeter Out B2 (VB-Audio Vo, MME (8 in, 0 out)
6 Voicemeeter Out A4 (VB-Audio Vo, MME (8 in, 0 out)
7 CABLE Output (VB-Audio Virtual , MME (8 in, 0 out)
8 Voicemeeter Out B3 (VB-Audio Vo, MME (8 in, 0 out)
9 Voicemeeter Out A5 (VB-Audio Vo, MME (8 in, 0 out)
10 Microphone Array (Voice.ai Audi, MME (2 in, 0 out)
11 Microphone (Voicemod Virtual Au, MME (2 in, 0 out)
12 Microsoft Sound Mapper - Output, MME (0 in, 2 out)
<13 Voicemeeter AUX Input (VB-Audio, MME (0 in, 8 out)
14 Voicemeeter In 2 (VB-Audio Voic, MME (0 in, 8 out)
15 Line (Voicemod Virtual Audio De, MME (0 in, 2 out)
16 Voicemeeter In 4 (VB-Audio Voic, MME (0 in, 8 out)
17 Realtek Digital Output (Realtek, MME (0 in, 2 out)


the two with the arrows are the selected input and output of windows.

Find the number of what you want to use, in my case 1 is the input and 17 is the output.

Taking these numbers head into the funny.py file in any editor(including note pad) and change the 'device=(in, out)' to your respective numbers.

At this point just run the script in either the funny.bat or terminal 'python funny.py' and press f9 to activate!

if you want to change the keybind head to the KEYBIND = 'f9' line and change f9 to your new keybind
