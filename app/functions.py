import subprocess
import sys
import shutil
import os
from lip_sync.settings import upload_video_path, result_dir, BASE_DIR


def f(face_file_path, audio_file_path):
    # if result_dir.exists():
    #     shutil.rmtree(result_dir)
    # os.mkdir(result_dir)

    # ffmpeg -i lip_sync_1_aud.mp4 -ab 160k -ac 2 -ar 44100 -vn lip_sync_1_aud.wav
    subprocess.run(['ffmpeg', '-i', str(audio_file_path),
                    '-ab', '160k', '-ac', '2', '-ar', '44100', '-vn',
                    str(upload_video_path / 'audio.wav')], capture_output=False)

    # cd Wav2Lip && python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face "/content/lip_sync_1_face.mp4" --audio "/content/lip_sync_1_aud.wav"
    os.chdir(BASE_DIR / 'Wav2Lip')
    subprocess.run(['python', 'inference.py', '--checkpoint_path',
                    'checkpoints/wav2lip_gan.pth', '--face',
                    str(face_file_path), '--audio', str(audio_file_path), '--outfile', str(result_dir / 'result.mp4')],
                   capture_output=False)

    return 'done!'
