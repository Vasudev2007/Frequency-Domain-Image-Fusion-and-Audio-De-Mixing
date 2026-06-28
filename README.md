# Frequency-Domain Image Fusion and Audio De-Mixing

An engineering and research notebook exploring advanced signal processing techniques applied to image and audio data. 

This repository documents the mathematical foundations, algorithm design, and implementation of:
1. **Frequency-Domain Image Fusion:** Combining images using 2D Fourier Transforms.
2. **Audio De-Mixing:** Isolating and filtering overlapping frequency bands in complex audio signals.

## Project Philosophy

This project is structured as an **Engineering Notebook**. The workflow emphasizes theoretical understanding backed by practical implementation. Each module tells a complete engineering story:

`Problem Definition` → `Signal Analysis` → `Frequency-Domain Processing` → `Results` → `Conclusion`

---

## Technical Stack & Concepts

- **Core Languages & Libraries:** Python, NumPy, SciPy, Matplotlib, Pillow
- **Mathematics & Signal Processing:** 
  - Fast Fourier Transform (1D and 2D FFT)
  - Spectral Analysis (Magnitude and Phase Spectra)
  - Digital Filter Design (Butterworth, Low-pass, High-pass)
  - Frequency Masking and Signal Reconstruction

---

## Directory Structure

```text
├── audio_demixing/
│   ├── data/          # Raw audio files (e.g., mixtures)
│   ├── notebook/      # Engineering notebooks for audio analysis
│   └── results/       # Filtered and de-mixed audio outputs
├── image_fusion/
│   ├── data/          # Source images
│   ├── notebook/      # Engineering notebooks for 2D FFT image fusion
│   └── results/       # Fused image outputs
├── reports/           # Formal PDF and DOCX submissions
├── archive/           # Exploratory notebooks and tutorials
└── requirements.txt   # Python dependencies
```

---

## Module 1: Image Fusion in the Frequency Domain

**Goal:** Blend high-frequency details of one image with the low-frequency structure of another to create a composite image.

### Workflow:
1. **Spatial to Frequency Domain:** Apply 2D FFT to both source images to extract their magnitude and phase spectra.
2. **Spectral Manipulation:** 
   - Apply a Low-Pass Filter (LPF) to Image A (retaining structural contours).
   - Apply a High-Pass Filter (HPF) to Image B (retaining fine details/edges).
3. **Fusion & Reconstruction:** Combine the filtered spectra and apply the Inverse 2D FFT to reconstruct the spatial image.

---

## Module 2: Audio De-Mixing and Filtering

**Goal:** Isolate specific instruments or frequencies from a mixed audio track (e.g., removing background noise or isolating a piccolo from a mixed track).

### Workflow:
1. **Time to Frequency Domain:** Read the audio file and apply a 1D FFT to analyze the frequency spectrum.
2. **Filter Design:** Design digital filters (e.g., Butterworth low-pass filter) with precise cutoff frequencies derived from the spectral analysis.
3. **Frequency Masking:** Apply the filter to the signal's spectrum in the frequency domain.
4. **Reconstruction:** Apply the Inverse 1D FFT to generate the filtered time-domain audio signal.

---

## Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Notebooks

1. Clone the repository.
2. Launch Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook
   ```
3. Navigate to `image_fusion/notebook/` or `audio_demixing/notebook/` to explore the analytical workflows.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
