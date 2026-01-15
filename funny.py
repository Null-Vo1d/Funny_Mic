import numpy as np
import sounddevice as sd
import keyboard
from scipy.signal import butter, lfilter

def maximum_pain(x):
    drive = 100.0 #This is the one you can change for the biggest effect.
    clip_threshold = 0.5  #minimum sound level, everything will be this loud, quickly leads to non-understandability
    fold_threshold = 0.9

    y = x * drive
    y = np.clip(y, -clip_threshold, clip_threshold)

    #wavefold
    folded = np.abs(y)
    folded = np.mod(folded + fold_threshold, fold_threshold * 2) - fold_threshold
    y = folded * np.sign(y)

    y = np.tanh(y * 2.5)
    return y


def lowpass(signal, cutoff, fs):
    b, a = butter(4, cutoff / (fs / 2), btype='low')
    return lfilter(b, a, signal)


effect_enabled = False

def toggle():
    global effect_enabled
    effect_enabled = not effect_enabled
    print("Maximum Pain:", "ON" if effect_enabled else "OFF")

KEYBIND = 'f9' #change this to change the keybind, ex 'a' '9' 'alt' 'alt+m'

keyboard.add_hotkey(KEYBIND, toggle) 



fs = 44100

def audio_callback(indata, outdata, frames, time, status):
    global effect_enabled

    x = indata[:, 0]

    if effect_enabled:
        y = maximum_pain(x)
        y = lowpass(y, cutoff=6000, fs=fs)
    else:
        y = x

    outdata[:, 0] = y


with sd.Stream(
    samplerate=fs,
    blocksize=256,
    dtype="float32",
    channels=1,
    callback=audio_callback,
    device=(in, out), #This is the one you have to change, the first spot it the input the last is the output
):
    print("Running... Press F9 to toggle distortion")
    keyboard.wait()
