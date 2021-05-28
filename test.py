import subprocess
import sys
import os
from lip_sync.settings import upload_video_path


def f(face_file_path, audio_file_path):
    # os.remove(upload_video_path / 'audio.wav')
    subprocess.run(['ffmpeg', '-i', str(audio_file_path),
                    '-ab', '160k', '-ac', '2', '-ar', '44100', '-vn',
                    str(upload_video_path / 'audio.wav')], capture_output=False)

    # cd Wav2Lip && python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face "/content/lip_sync_1_face.mp4" --audio "/content/lip_sync_1_aud.wav"
    os.chdir('Wav2Lip')
    subprocess.run(['python', 'inference.py', '--checkpoint_path',
                    'checkpoints/wav2lip_gan.pth', '--face',
                    str(face_file_path), '--audio', str(audio_file_path)], capture_output=False)

    # sys.stdout.buffer.write(command.stdout)
    # sys.stderr.buffer.write(command.stderr)
    # sys.exit(command.returncode)
    # print('\n\n_________', command)


face_file_path = upload_video_path / 'output1.mp4'
audio_file_path = upload_video_path / 'output2.mp4'
f(face_file_path, audio_file_path)
