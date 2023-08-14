import os
import subprocess
import whisper
from whisper.utils import write_srt



def transcribe_and_burn_subtitles(input_video_path):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio
    result = model.transcribe(input_video_path)

    # Create temporary SRT file path
    base_name = os.path.basename(input_video_path)
    video_dir = os.path.dirname(input_video_path)
    name_without_ext = os.path.splitext(base_name)[0]
    srt_path = os.path.join(video_dir, f'{name_without_ext}.srt')
    output_video_path = os.path.join(video_dir, f'{name_without_ext}_subtitles.mp4')
    abs_input = os.path.abspath(input_video_path)
    abs_srt = os.path.abspath(srt_path)
    abs_srt_ffmpeg = abs_srt[0] + "\\\:" + abs_srt[2:].replace("\\", "\\\\\\\\")

    # Write the transcriptions to the SRT file
    with open(srt_path, "w", encoding="utf-8") as srt_file:
        write_srt(result["segments"], file=srt_file)

    # # Burn the subtitles onto the video
    command = [
        'ffmpeg',
        '-i', abs_input,
        '-vf', f"subtitles={abs_srt_ffmpeg}",
        '-c:v', 'libx264',
        '-crf', '18',
        '-c:a', 'aac',
        output_video_path
    ]
    subprocess.run(command)

    # Remove the original video and SRT file
    os.remove(input_video_path)
    os.remove(srt_path)

    # Return the path to the new video with subtitles
    return output_video_path



