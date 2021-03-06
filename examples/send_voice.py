from gapbot import Gap  # import library;
from platform import system

app = Gap(bot_token='your_bot_token')  # instance of Main Class;
# if you need use bot parameters you must set bot_token;

if __name__ == '__main__':  # If you are running this module as the main program;
    target_id = 000000  # whose to be send text to him;
    if system().lower() == 'windows':  # Windows users
        voice_path = r'C:\Users\GapUser\Gap.ogg'
    else:  # Gnu/linux users and others (not windows)
        voice_path = r'/home/GapUser/Gap.ogg'
    app.send_video(
        chat_id=target_id,
        path=voice_path,
        caption='Gap Caption'
    )

# https://developer.gap.im/doc/botplatform#method-send-voice
