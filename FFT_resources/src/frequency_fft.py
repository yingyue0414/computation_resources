#@author Y Ying
#Calculate frequency from FFT analysis of fluctuation arrays

#dependencies
import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

def frequency_fft(fluctuation, **kwargs):
    """
    Perform FFT analysis (scipy.fft) on the input fluctuation and output frequency
    versus arbitrary amplitude.
    
    Keyword arguments:
        flucatuaiton -- (double(n)) array of temporal fluctuation for FFT
    (optional)
        numStep -- (int) total number of step (default: length of fluctuation array)
        timeStep -- (double) time step size in seconds (default: 1e-6 sec)
    """
    # extract value from keyword-value pairs
    numStep = kwargs.get("numStep", len(fluctuation)) # total number of steps (data pts)
    timeStep = kwargs.get("timeStep", 1e-6) # time interval between records
    
    # perform fft
    fftResult = fft(fluctuation)
    halfNumStep = numStep // 2
    amplitudeArray = np.abs(fftResult)[:halfNumStep] * 1 / numStep #second half is only imaging of first half
    frequencyArray = (1 / timeStep) * np.linspace(0, halfNumStep - 1, halfNumStep) / numStep
    
    return amplitudeArray, frequencyArray

def generate_sample_model(timeStep = 1e-3, numStep = 500, omega = 62.8):
    """
    Generate model systems for analysis
     1. Simple sin fluctuation (sin(omega * t))
     2. Stacked fluctuation (stacked -- (1~5)*omega)
     3. Random (randn) fluctuation (omega/4 * randn)
     4. Simple sin + random (randn) fluctuation ([1] + [3] * 0.1)
     
    Return flucutations array (double(5,N))
        
    Keyword arguments:
        timeStep -- time step interval in seconds (default: 1e-6 sec)
        numStep -- total sampling steps (default: 500)
    """

    #vibration sampling constants
    samplingRate = 1/timeStep
    timeScale = np.linspace(0, timeStep * numStep, numStep)

    #fluctuation record
    fluctuations = np.zeros([5, numStep])

    #1. Simple sin fluctuation
    fluctuations[0] = np.sin(62.8 * timeScale)
    
    #2. Stacked fluctuation
    def combinedVibration(time, n = 5, omega = omega): #time in sec
        vibrationSum = 0;
        for i in range(1, n + 1):
            vibrationSum += i * np.cos(i * omega * time)
        return vibrationSum

    fluctuations[1] = combinedVibration(timeScale, 5, omega)
    
    #3. randn fluctuation
    rng = np.random.default_rng(10)
    fluctuations[2] = omega / 4 * rng.normal(size = numStep)
    
    #4. simple sin + random
    fluctuations[3] = fluctuations[0] + fluctuations[2] * 0.1

    return fluctuations, timeScale

def plot_fluctuations(fluctuations, timeScale, timeStep = 1e-3, numStep = 500, cutoff = -1):
    """
    Use frequency_fft to solve for frequencies with given fluctuations
    array. Plot both (x, t) and (frequency, amplitude).
    
    Keyword argument:
        fluctuations -- double(k,n) array for fluctuations
        timeStep -- time interval
        numStep -- total number of simulation steps
    """
    
    # initialize
    fluc_plots = [(0,0), (1,0), (2,0), (3,0)]
    fft_plots = [(0,1), (1,1), (2,1), (3,1)]

    # ploting
    fig, axs = plt.subplots(4, 2, figsize = (11, 16))
    fig.tight_layout(pad = 2.16)

    for (index, flucplot, fftplot) in zip(range(0, len(fluctuations)),fluc_plots, fft_plots):

        #fluctuation plot
        p = axs[flucplot]

        p.plot(timeScale, fluctuations[index])
        p.set(xlabel = "Time (sec)", ylabel = "Displacement")

        #fft plot
        q = axs[fftplot]

        amplitudeArray, frequencyArray = frequency_fft(fluctuations[index], timeStep = timeStep, numStep = numStep)

        if cutoff < 0:
            q.plot(frequencyArray, amplitudeArray)
        else:
            frequencyArray_cutoff = frequencyArray[frequencyArray < cutoff]
            amplitudeArray_cutoff = amplitudeArray[:len(frequencyArray_cutoff)]
            q.plot(frequencyArray_cutoff, amplitudeArray_cutoff)
        q.set(xlabel = "Frequency (Hz)", ylabel = "Arbitrary Amplitude")

    return True