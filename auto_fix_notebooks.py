import os
import json
import subprocess

def append_cell(notebook_path, source_lines):
    if not os.path.exists(notebook_path):
        print(f"Could not find {notebook_path}")
        return
        
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    new_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source_lines
    }
    
    nb['cells'].append(new_cell)
    
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print(f"Appended static code cell to {notebook_path}")

def main():
    image_nb = "image_fusion/notebook/image.part2.ipynb"
    audio_nb = "audio_demixing/notebook/Q2.Code.ipynb"
    
    # 1. Add static cell to Image Fusion
    append_cell(image_nb, [
        "# Static example for GitHub portfolio rendering\\n",
        "frequency_mixer(low_frequency_image='cat', high_frequency_image='dog', threshold=17)"
    ])
    
    # 2. Add static cell to Audio Demixing
    append_cell(audio_nb, [
        "# Static example for GitHub portfolio rendering - Ideal Lowpass\\n",
        "apply_ideal_lowpass_filter(cutoff=1150)\\n",
        "\\n",
        "# Static example for GitHub portfolio rendering - Butterworth\\n",
        "apply_butterworth_lowpass_filter(signal=audio_signal, sampling_rate=sampling_rate, cutoff=1150, order=4)"
    ])
    
    # 3. Execute notebooks automatically
    print("\\nExecuting Notebooks... This might take 10-20 seconds to process the audio and images...")
    
    for nb in [image_nb, audio_nb]:
        if os.path.exists(nb):
            try:
                subprocess.run([
                    "jupyter", "nbconvert", 
                    "--to", "notebook", 
                    "--execute", 
                    "--inplace", 
                    nb
                ], check=True)
                print(f"Successfully executed and saved outputs for {nb}!")
            except subprocess.CalledProcessError as e:
                print(f"Failed to execute {nb}. Error: {e}")
        
if __name__ == "__main__":
    main()
