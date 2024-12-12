# -*- coding: utf-8 -*-

## Import every thing ever
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import math
import wave
import scipy
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from scipy.signal import butter, filtfilt, iirnotch
from scipy.io.wavfile import write
from scipy.signal import butter, freqz

def High_Pass(signal,order,cutoff,sample_rate):
    a,b = scipy.signal.butter(order,cutoff/(sample_rate/2),btype='high') # Magic coefficients
    filtered_signal = scipy.signal.filtfilt(a, b, signal)  # Apply Filter
    return filtered_signal

def Low_Pass(signal, order, cutoff, sample_rate):
    a, b = scipy.signal.butter(order, cutoff / (sample_rate / 2), btype='low')  # Magic coefficients
    filtered_signal = scipy.signal.filtfilt(a, b, signal)  # Apply Filter
    return filtered_signal


def BandPass(signal, order, low_cutoff, high_cutoff, sample_rate):
    a_high, b_high = scipy.signal.butter(order, high_cutoff / (sample_rate / 2), btype='high')  # Magic coefficients
    a_low, b_low = scipy.signal.butter(order, low_cutoff / (sample_rate / 2), btype='low')  # Magic coefficients
    filtered_signal_high = scipy.signal.filtfilt(a_high, b_high, signal)  # Apply High Pass Filter
    filtered_signal_low = scipy.signal.filtfilt(a_low, b_low, filtered_signal_high)  # Apply Filter
    filtered_signal_band = scipy.signal.filtfilt(a_low, b_low, filtered_signal_high)  # Apply Filter
    return filtered_signal_band # This is now the bandpass filtered data

def NotchFilter(signal, frequency, sample_rate, Q=30):
    # Design the notch filter
    B, A = iirnotch(frequency, Q, sample_rate)
    # Apply the filter to the signal
    filtered_data_Notch = scipy.signal.filtfilt(B, A, signal)
    return filtered_data_Notch


def Generate_test_data(f_start, f_stop, f_step, sample_rate):
    A = np.arange(f_start, f_stop, f_step)
    sample_signal = 0
    t = np.arange(0, 1, 1 / sample_rate)
    for frequency in A:
        sample_signal += np.cos(2 * np.pi * frequency * t)
    return sample_signal

def Plot_Signal(signal, sample_rate, title):
    N = len(signal)
    t = np.arange(0, N, 1)
    plt.plot(t, signal)
    plt.xlabel("Time [S]")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.show()

def Plot_FFT(signal,sample_rate,title,x_max):
    # Plot FFT of Bandpass Pass Filter
    N = len(signal)
    y_band = fft(signal)
    x_band = fftfreq(N, 1 / sample_rate)
    plt.title(title)
    plt.ylabel("Power")
    plt.xlabel("Frequency [Hz]")
    plt.xlim(0,x_max)
    plt.plot(x_band, np.abs(y_band))
    plt.show()
# Change to Enable Plotting

Plotting = True

## Generate A Sample Signal
f_start = 1
f_stop = 600
f_step = 10
sample_rate = 50000
sample_data = Generate_test_data(f_start, f_stop, f_step, sample_rate)

if Plotting == True:
    # Plot FFT of Sample Signal
    N = len(sample_data)
    sample_xfft= fftfreq(N, 1 / sample_rate)
    sample_yfft = fft(sample_data)
    plt.ylabel("Power")
    plt.xlabel("Frequency [Hz]")
    plt.xlim(0,f_stop)
    plt.plot(sample_xfft, np.abs(sample_yfft))
    plt.title("FFT of Raw Signal")
    plt.show()

# Filter Signal with High Pass Filter
high_order = 4
high_cutoff = 20
filtered_data_high = High_Pass(sample_data, high_order, high_cutoff, sample_rate)


if Plotting == True:
    # Plot FFT of High Pass Filter
    N = len(filtered_data_high)
    y_high = fft(filtered_data_high)
    x_high = fftfreq(N, 1 / sample_rate)
    plt.title(f"FFT of High Pass Filter {high_cutoff} [Hz]")
    plt.ylabel("Power")
    plt.xlabel("Frequency [Hz]")
    plt.axvline(x=high_cutoff,color="r")
    plt.xlim(0,600)
    plt.plot(x_high, np.abs(y_high))
    plt.show()


# Filter Signal with Low Pass Filter
low_order = 4
low_cutoff = 3000
filtered_data_low = Low_Pass(sample_data, low_order, low_cutoff, sample_rate)

if Plotting == True:
    # Plot FFT of Low Pass Filter
    N = len(filtered_data_low)
    y_low = fft(filtered_data_low)
    x_low = fftfreq(N, 1 / sample_rate)
    plt.title(f"FFT of Low Pass Filter {low_cutoff} [Hz]")
    plt.ylabel("Power")
    plt.xlabel("Frequency [Hz]")
    plt.axvline(x=low_cutoff,color="r")
    plt.xlim(0,600)
    plt.plot(x_low, np.abs(y_low))
    plt.show()


# Create Bandpass Filter
filtered_data_band = BandPass(sample_data,4,3400,50,sample_rate)

if Plotting == True:
    # Plot FFT of Bandpass Pass Filter
    N = len(filtered_data_band)
    y_band = fft(filtered_data_band)
    x_band = fftfreq(N, 1 / sample_rate)
    plt.title(f"FFT of Band Pass Filter {high_cutoff}-{low_cutoff} [Hz]")
    plt.ylabel("Power")
    plt.xlabel("Frequency [Hz]")
    plt.axvline(x=low_cutoff,color="r")
    plt.axvline(x=high_cutoff,color="r")
    plt.xlim(0,600)
    plt.plot(x_band, np.abs(y_band))
    plt.show()


## Now Plot Original Audio File

raw_combinded_path = r"C:\Users\cprla\Downloads\audio soften.wav"
combinded_sample_rate , combinded_wav = wavfile.read(raw_combinded_path)
combinded_wav = combinded_wav[:,0] # Just grab the first column

if Plotting == True:
    Plot_Signal(combinded_wav,combinded_sample_rate,"Raw Test 1 Amplitidue vs. Time")

    # Plot FFT of Bandpass Pass Filter
    N = len(combinded_wav)
    y_band = fft(combinded_wav)
    x_band = fftfreq(N, 1 / combinded_sample_rate)
    plt.title(f"FFT of Raw Test 1 Audio {high_cutoff}-{low_cutoff} [Hz]")
    plt.ylabel("Power")
    plt.xlabel("Frequency [Hz]")
    plt.axvline(x=low_cutoff,color="r")
    plt.axvline(x=high_cutoff,color="r")
    plt.xlim(0,3100)
    plt.plot(x_band, np.abs(y_band))
    plt.show()

combined_bandpass = BandPass(combinded_wav,4,low_cutoff,high_cutoff,combinded_sample_rate)

signal = combined_bandpass
frequency = 1000
filtered_data_notch = NotchFilter(signal, frequency, combinded_sample_rate, Q=30)

if Plotting == True:
    # Plot FFT of Bandpass Pass Filter
    N = len(filtered_data_notch)
    y_band = fft(filtered_data_notch)
    x_band = fftfreq(N, 1 / combinded_sample_rate)
    plt.title(f"FFT of Band Pass Filter Test 1 Audio {high_cutoff}-{low_cutoff} [Hz]")
    plt.ylabel("Power")
    plt.xlabel("Frequency [Hz]")
    plt.axvline(x=low_cutoff,color="r")
    plt.axvline(x=high_cutoff,color="r")
    plt.xlim(0,3100)
    plt.plot(x_band, np.abs(y_band))
    plt.show()

output_path = r"C:\Users\cprla\Downloads\pleasework.wav"
write(output_path, combinded_sample_rate, np.int16(filtered_data_notch / np.max(np.abs(filtered_data_notch)) * 32767))


#Plot_FFT(combined_bandpass,combinded_sample_rate,"PLot new",1200)

