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


# Sample Analysis
First, we used Generate_test_data() to generate a sample signal. We set 
f_start = 1

f_stop = 600

f_step = 10

sample_rate = 50000 

This means the sample signal would have frequencies from {1,11,21,...,591}.

![Raw Signal](https://github.com/user-attachments/assets/df5e7725-cd01-4422-8076-21cc8771bea5)

Above, we can see the raw signal we generated. We then applied a high-pass filter to our sample data with an order of 4 and a cutoff frequency of 90 Hz. We plotted the Fast Fourier Transform (FFT) of our data after it had been passed through the high-pass filter.

![High Pass](https://github.com/user-attachments/assets/8f699ad8-d260-4d32-ad91-8d46f2403759)

We also used a low-pass filter and we can see it's independent effect on our signal.

![low pass filer](https://github.com/user-attachments/assets/d9386600-c095-4a05-b897-7a38f6ac2258)

Then we applied our high-pass filter and after applied the low-pass filter. This creates a band-pass filter. 

![Bandpass](https://github.com/user-attachments/assets/e048ae85-99af-4cd7-bfbf-7efb12e897bf)

The next part of the code reads a wav file as well as its sample rate. The sample rate for our audio signal was approximately 44000 Hz. For the first test (Test 1), we recorded Cooper speaking while Michael played a pure tone of 1000Hz. We plotted this versus time. 

![Raw audio plot](https://github.com/user-attachments/assets/1eaa4429-8136-41a0-83df-ab839956d9ae)

We then plotted the FFT of the Test 1 audio. 

![Raw fft](https://github.com/user-attachments/assets/b6202628-e277-4ebb-859c-4b01ce5fce61)

We see that the plot has a sharp spike at 1000 Hz, which is expected as the tone played was 1000Hz. Then we applied our band-pass filter and plotted the FFT of this filtered signal.

![FFT of filtered data](https://github.com/user-attachments/assets/ac680734-6b87-4efc-a48f-02f16038d423)

Here we can see that our filter succeeded in minimizing the 1000Hz tone.

# Limitations
One of the biggest limitations is that as we make our filter more restrictive (increase the order and decrease the pass band), our audio file becomes more muddled. Thus, we trade audio quality for noise reduction. Another limitation is that the notch filter only works at removing a specific frequency, thus for audio with frequency-varying noise, this method is ineffective. 

# Future Results
In the future, we would examine the effectiveness of using a finite, but large number of notch filters to remove a given range of frequencies. We would also experiment with other types of filters, as well as possibly diving into conditioning our signal by padding as well as normalizing our audio. 

# TLDR
For this project, we created a low pass filter, high pass filter, bandpass filter, and a notch filter to an audio file. This audio file was Cooper speaking with a 1000Hz tone playing in the background. We tested the different filters, modified the parameters and found that the notch filter performed the best. Thanks for a great semester.












