from django.shortcuts import render
from .forms import FileForm
import os
import shutil
from .functions import f
from lip_sync.settings import upload_video_path, result_dir


# Create your views here.
def home_view(request):
    if upload_video_path.exists():
        shutil.rmtree(upload_video_path)
    os.mkdir(upload_video_path)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            face_file_path = upload_video_path / request.FILES['face'].name
            audio_file_path = upload_video_path / request.FILES['audio'].name
            print('_' * 10, f(face_file_path, audio_file_path))
            return render(request, 'home.html', {'form': form, 'download': True})
    form = FileForm()
    return render(request, 'home.html', {'form': form})

# import mimetypes
#
# def download_file(request):
#     # fill these variables with real values
#     filename = 'result.mp4'
#     fl_path = str(result_dir / filename)
#     fl = open(fl_path, 'r')
#     # mime_type, _ = mimetypes.guess_type(fl_path)
#     response = HttpResponse(fl, content_type='video/mp4')
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     return response

# TODO: create a download button, clicking which download the files
