# WAV to AIFF Converter for OP-1

## Overview
This Python script is crafted specifically for users of the Teenage Engineering OP-1 Synthesizer, facilitating the seamless conversion of audio files from `.wav` format to `.aiff` (AIFF) format.

- **Maintain Folder Structure**: This code will maintain the folder structure of the original folder, so it's useful to keep packs organized.
- **Batch Conversion**: Convert all `.wav` files in the specified folder (and sub-folders) without manual intervention.
- **Parameter Setting**: All resultant `.aif` files are adjusted to 16-bit, stereo, and 44100Hz, ensuring compatibility with the OP-1.

## Prerequisites
- **Python**: Ensure that Python (3.6 or later) is installed on your machine. 
- **Pydub**: Install the `pydub` library for handling audio format conversion.

    You can install it using pip:
    ```bash
    pip install pydub
    ```
- **FFmpeg**: The `pydub` library leverages `ffmpeg` for audio format conversion. Therefore, ensure `ffmpeg` is installed and available in your system's PATH.
    - **Windows**: Download and install FFmpeg from [the FFmpeg official website](https://ffmpeg.org/download.html). Add the bin folder to your system PATH.
    - **macOS**: You can install FFmpeg using Homebrew with the command:
      ```bash
      brew install ffmpeg
      ```
    - **Linux**: Use your distribution’s package manager. For Ubuntu/Debian, you might run:
      ```bash
      sudo apt-get install ffmpeg
      ```
  
## Usage
### Basic Command Line Usage
Navigate to the directory containing the script using the terminal and type:
```bash
python3 wav-to-aif.py [source_folder] [destination_folder]
```

`source_folder`: The path to the folder containing the `.wav` files you wish to convert.    
`destination_folder`: The path where you'd like the converted `.aif` files (with structure) to be saved. (you need to have it created already)

### example
```bash
python3 wav-to-aif.py /path/to/wav/files /path/to/save/converted/files
```


## Notes

Ensure the destination folder is either non-existent or empty to avoid file overwriting.
Ensure you have the necessary permissions for reading and writing to the involved directories.
Always verify the conversion by checking one or two resultant files in your OP-1 to ensure they meet your expectations.

## Contribution

Feel free to fork this repository and enhance the code. Pull requests with improvements and bug fixes are always welcome.


