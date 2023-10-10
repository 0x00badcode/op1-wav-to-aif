import os
import sys
from pydub import AudioSegment

def convert_wav_to_aif(src_folder, dest_folder):
    for subdir, dirs, files in os.walk(src_folder):
        for file in files:
            if file.endswith(".wav"):
                wav_path = os.path.join(subdir, file)
                rel_path = os.path.relpath(wav_path, src_folder)
                dest_subdir = os.path.join(dest_folder, os.path.dirname(rel_path))
                os.makedirs(dest_subdir, exist_ok=True)
                dest_path = os.path.join(dest_subdir, os.path.splitext(os.path.basename(file))[0] + ".aif")
                print(f"Converting {wav_path} to {dest_path}")
                sound = AudioSegment.from_wav(wav_path)
                sound = sound.set_channels(2).set_frame_rate(44100).set_sample_width(2)
                sound.export(dest_path, format="aiff")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py [source_folder] [destination_folder]")
        sys.exit(1)

    src_folder = sys.argv[1]
    dest_folder = sys.argv[2]
    convert_wav_to_aif(src_folder, dest_folder)
