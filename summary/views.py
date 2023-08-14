from django.shortcuts import render, redirect
from django.views.generic import View
from .models import FileUpload
from .forms import FileUploadForm
import ffmpeg
import speech_recognition as sr
import datetime as dt
from django.http import FileResponse
from django.contrib import messages
import os


class IndexView(View):
    def get(self, request, *args, **kwargs):
        form = FileUploadForm()
        return render(request, 'summary/index.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_data = FileUpload()
            upload_data.upload = form.cleaned_data['upload']
            if os.path.exists(upload_data.upload.path):
                os.remove(upload_data.upload.path)
            upload_data.save()

            now = dt.datetime.now()
            date = now.strftime('%Y%m%d%H%M%S')
            material = ffmpeg.input(upload_data.upload.path)
            material = ffmpeg.output(material, f'material{date}.wav')
            ffmpeg.run(material)
            material = f'material{date}.wav'
            info = ffmpeg.probe(material)
            duration = float(info['streams'][0]['duration'])
            split_time = 180  # 180秒（3分）ごと
            current = 0
            idx = 1
            while current < duration:
                start = current
                stream = ffmpeg.input(material, ss=start, t=split_time)
                stream = ffmpeg.output(stream, f'split{date}{idx}.wav', c='copy')
                ffmpeg.run(stream)
                idx += 1
                current += split_time
            # 文字起こし
            r = sr.Recognizer()
            num = 1
            text = ''
            while num < idx:
                with sr.AudioFile(f'split{date}{num}.wav') as source:
                    audio = r.record(source)
                text = text + r.recognize_google(audio, language='ja-JP')
                num += 1
                f = open('text.txt', 'w', encoding='UTF-8')
                f.write(text+'\n')
            f.close()

            os.remove(material)
            for i in range(1, idx):
                os.remove(f'split{date}{i}.wav')

            messages.success(request, 'txtデータを作成しました。')
            return redirect('summary:index')
        return render(request, 'summary/index.html', {
            'form': form
        })


def file_download_view(request):
    now = dt.datetime.now()
    date = now.strftime('%Y%m%d-%H%M%S')
    filename, file_path = f'{date}.txt', './text.txt'
    return FileResponse(open(file_path, "rb"), as_attachment=True, filename=filename)
