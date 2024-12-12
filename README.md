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

This program returns two coefficients (a,b) where a and b are finite one-dimensional arrays. For example a = [ 0.98533167 -3.94132669  5.91199003 -3.94132669  0.98533167]

##### Inputs: 
N = the order of the filter. A higher order creates a stronger, steeper filter response. 

Wn = the critical frequency. Mathematically this represents (cutoff frequency)/(Nyquist Frequency). 

btype = the type of filter, this could represent a low pass, high pass, or bandpass filter. For this code we used a low pass filter (btyper="low) and a high pass filter (btype="high")

##### Returns:
a, b where each is a one-dimensional array. These coefficients can be convolved with the original audio source or passed through another filter function

### Signal.filtfilt()
"filtfilt(b, a, x, axis=-1, padtype='odd', padlen=None, method='pad', irlen=None)" - Python Help()
Takes coefficients and returns filtered data.

Inputs: 
a, b = coefficients returned from filter function
x = the signal that will be filtered
Returns:
y = the filtered signal


# Main Functions

### High_Pass()
High_Pass(signal,order,cutoff,sample_rate)

This function takes a given signal, order, cutoff frequency, and sample rate and returns a filtered signal that passes frequencies above the cutoff frequency. The filter response depends on the order of the filer. 

Inputs:
signal = the signal to be filtered

order = the order of the filter

cutoff = the cutoff frequency. For example, if the cutoff frequency is 500 Hz, in theory, all frequencies above 500Hz will pass and all frequencies less than 500Hz will be rejected. However, we know there is no such thing as a perfect filter and if the filter order is too high we encounter the Gibbs' phenomena.

Returns: 
filtered_signal = the filtered signal after it has been passed through a high-pass filter.



