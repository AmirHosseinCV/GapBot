from .send_text import SendText
from .send_image import SendImage
from .send_audio import SendAudio
from .send_video import SendVideo
from .send_voice import SendVoice
from .send_file import SendFile


class Messages(SendText, SendImage, SendAudio, SendVideo, SendVoice, SendFile):
    pass
