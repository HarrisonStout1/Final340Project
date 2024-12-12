# Final340Project
The repo should include a README on the main page outlining:

The general/topic and challenge the code addresses
A list of any required dependencies and additional programs
The main programs written to analyze the data
A tutorial/walkthrough of how to operate the code
A sample of results from the analysis
Any limitations on running the program
A brief discussion of future results.

# Problem:
In many real applications of audio recording, we experience unwanted background noise that we want to remove. Thus, our challenge was to implement a filter that would remove background noise and emphasize the freqeuencies associated with the human voice.

# Additional Programs:
For this code we used a few important programs.

### Signal.Butter()
"butter(N, Wn, btype='low', analog=False, output='ba', fs=None)" - Python Help()

This program returns two coefficients (a,b) where a and b are finite one-dimensional arrays. 

##### Inputs: 
N = the order of the filter. A higher order creates a stronger, steeper filter response. 

Wn = the critical frequency. Mathematically this represents (cutoff frequency)/(Nyquist Frequency). 

btype = the type of filter, this could represent a low pass, high pass, or bandpass filter. For this code, we used a low pass filter (btyper="low) and a high pass filter (btype="high")

##### Returns:
a, b where each is a one-dimensional array. These coefficients can be convolved with the original audio source or passed through another filter function

### Signal.filtfilt()
"filtfilt(b, a, x, axis=-1, padtype='odd', padlen=None, method='pad', irlen=None)" - Python Help()

Takes coefficients and returns filtered data.

##### Inputs: 
a, b = coefficients returned from filter function

x = the signal that will be filtered

##### Returns:
y = the filtered signal

## iirnotch()
iirnotch(w0, Q, fs)

This filter removes a specified frequency from a signal. The limitation of this filter is that it only removes one frequency, therefore, if the noise is a varying frequency this filter becomes substantially less effective.


##### Inputs:
w0 = frequency to be removed from the signal

Q = quality, this is similar to order and represents the strength of the filter

fs = the sample rate

##### Returns:
Filtered signal with frequency removed. 


# Main Functions

### High_Pass()
High_Pass(signal,order,cutoff,sample_rate)

This function takes a given signal, order, cutoff frequency, and sample rate and returns a filtered signal that passes frequencies above the cutoff frequency. The filter response depends on the order of the filer. 

##### Inputs:
signal = the signal to be filtered

order = the order of the filter

cutoff = the cutoff frequency. For example, if the cutoff frequency is 500 Hz, in theory, all frequencies above 500Hz will pass and all frequencies less than 500Hz will be rejected. However, we know there is no such thing as a perfect filter and if the filter order is too high we encounter the Gibbs' phenomena.

##### Returns: 
filtered_signal = the filtered signal after it has been passed through a high-pass filter.

### Low_Pass()
High_Pass(signal,order,cutoff,sample_rate)

This function takes a given signal, order, cutoff frequency, and sample rate and returns a filtered signal that passes frequencies above the cutoff frequency. The filter response depends on the order of the filer. 

##### Inputs:
signal = the signal to be filtered

order = the order of the filter

cutoff = the cutoff frequency. For example, if the cutoff frequency is 500 Hz, in theory, all frequencies below 500Hz will pass and all frequencies greater than 500Hz will be rejected. However, we know there is no such thing as a perfect filter and if the filter order is too high we encounter the Gibbs' phenomena.

##### Returns: 
filtered_signal = the filtered signal after it has been passed through a low-pass filter.

### Band_Pass()
BandPass(signal,order,low_cutoff,high_cutoff,sample_rate)

This function takes a given signal, order, cutoff frequency, and sample rate and returns a filtered signal that passes frequencies in the accepted frequency range. The filter response depends on the order of the filer. 

##### Inputs:
signal = the signal to be filtered

order = the order of the filter

low_cutoff =low cutoff that passes frequencies below cutoff

high_cutoff = high cutoff that passes frequencies above cutoff

##### Returns: 
filtered_signal = the filtered signal after it has been passed through a band-pass filter.

### Notch_Filter()
NotchFilter(signal, frequency, sample_rate, Q)

This function takes a given signal, quality, target frequency, and sample rate and returns a filtered signal that passes frequencies in the accepted frequency range. The filter response depends on the order of the filer. 

##### Inputs:
signal = the signal to be filtered

Q = the quality of the filter, this is similar to the order

frequency = this is the frequency to be removed

##### Returns: 
filtered_signal = the filtered signal after it has been passed through a notch filter.


### Generate_test_data()
Generate_test_data(f_start, f_stop, f_step, sample_rate)

This function will generate a signal that's the sum of cosine waves of specified frequencies.

##### Inputs:
f_start = the starting frequency 

f_stop = stopping frequency

f_step = the distance between each frequency 

sample_rate = sample rate of the signal

##### Returns: 
sample_signal = signal of mixed frequencies

### Plot_Signal()
Plot_Signal(signal, sample_rate, title)

This function plots a given signal vs time. The graph is amplitude vs. time. 

##### Inputs:
signal = signal to be plotted

sample_rate = sample rate of the signal

title = title of plot

##### Returns: 
No return just plots graph

### Plot_FFT()
Plot_FFT(signal,sample_rate,title,x_max)

This function plots the Fast Fourier Transform of a given signal. This plot is Power vs. Frequency. 
##### Inputs:
signal = signal to be plotted

sample_rate = sample rate of the signal

title = title of plot

x_max = maximum x-value in plot

##### Returns: 
No return just plots graph


# Code Walkthrough
First, we used Generate_test_data() to generate a sample signal. We set 
f_start = 1

f_stop = 600

f_step = 10

sample_rate = 50000 

This means the sample signal would have frequencies from {1,11,21,...,591}.

![Raw Signal](https://github.com/user-attachments/assets/df5e7725-cd01-4422-8076-21cc8771bea5)

Above we can see the raw signal we generated. We then applied a high pass filter to our sample data with an order of 4 and a cutoff frequency of 90 Hz. We then plotted the Fast Fourier Transform (FFT) of our data after it had been passed through the high pass filter.











