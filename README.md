# Wav2Lip-Django
This program is a wrapper around the [Wav2Lip](https://github.com/Rudrabha/Wav2Lip "Wav2Lip") algorithm. It uses Django to create a simple GUI.

[![sample](https://github.com/utkarsh-21st/Wav2Lip-Django/blob/master/sample/sample.png "sample")](https://github.com/utkarsh-21st/Wav2Lip-Django/blob/master/sample/sample.png "sample")

### Setup
- Make sure you have your GPU enabled
- Create a new virtual environment, clone the project and cd into it.
- Install dependencies
```shell
pip install -r requirements.txt
```
```shell
wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "Wav2Lip/face_detection/detection/sfd/s3fd.pth"
```
- Download [wav2lip_gan.pth](https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/onedrive.aspx?originalPath=aHR0cHM6Ly9paWl0YXBoeWQtbXkuc2hhcmVwb2ludC5jb20vOnU6L2cvcGVyc29uYWwvcmFkcmFiaGFfbV9yZXNlYXJjaF9paWl0X2FjX2luL0Vkakk3YlpsZ0FwTXFzVm9FVVVYcExzQnhxWGJuNXo4VlRtb3hwNTVZTkRjSUE%5FcnRpbWU9ZjUwR0FfQWgyVWc&id=%2Fpersonal%2Fradrabha%5Fm%5Fresearch%5Fiiit%5Fac%5Fin%2FDocuments%2FWav2Lip%5FModels "wav2lip_gan.pth")
to the `Wav2Lip/checkpoints` directory


### How to run?
```python
python manage.py runserver
```


