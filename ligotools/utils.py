import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.io.wavfile import write

def whiten(strain, psd, dt):
    Nt = len(strain)
    freqs = np.fft.rfftfreq(Nt, dt)
    hf = np.fft.rfft(strain)
    white_hf = hf / (np.sqrt(psd / (dt * 2.0)))
    white_ht = np.fft.irfft(white_hf, n=Nt)
    return white_ht

def write_wavfile(filename, fs, data):
    scaled = np.int16(data / np.max(np.abs(data)) * 32767)
    write(filename, fs, scaled)

def reqshift(data, fshift=100, sample_rate=4096):
    x = np.arange(len(data))
    shifted = data * np.exp(1j * 2 * np.pi * fshift * x / sample_rate)
    return np.real(shifted)

def plot_psd(time, strain, label):
    fs = 1.0 / (time[1] - time[0])
    freq, psd = welch(strain, fs=fs, nperseg=fs//2)
    plt.loglog(freq, psd, label=label)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Spectral Density (strain^2/Hz)')
    plt.legend()
    plt.grid(True)
    return freq, psd
