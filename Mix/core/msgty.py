# outdated code :( don't bother reading this shit

from enum import IntEnum, unique


@unique
class Types(IntEnum):
    TEXT = 1
    DOCUMENT = 2
    PHOTO = 3
    VIDEO = 4
    STICKER = 5
    AUDIO = 6
    VOICE = 7
    VIDEO_NOTE = 8
    ANIMATION = 9
    ANIMATED_STICKER = 10
    CONTACT = 11


def ReplyCheck(m):
    reply_id = None
    if m.reply_to_message:
        reply_id = m.reply_to_message.id
    elif not m.from_user.is_self:
        reply_id = m.id
    return reply_id


def get_note_type(m):
    """Get type of note."""
    if len(m.text.split()) <= 1:
        return None, None, None, None

    data_type = None
    content = None
    raw_text = m.text.markdown if m.text else m.caption.markdown
    args = raw_text.split(None, 2)
    note_name = args[1]

    if len(args) >= 3:
        text = args[2]
        data_type = Types.TEXT

    elif m.reply_to_message:
        if m.reply_to_message.text:
            text = m.reply_to_message.text.markdown
        elif m.reply_to_message.caption:
            text = m.reply_to_message.caption.markdown
        else:
            text = ""

        if len(args) >= 2 and m.reply_to_message.text:  # not caption, text
            data_type = Types.TEXT

        elif m.reply_to_message.sticker:
            content = m.reply_to_message.sticker.file_id
            data_type = Types.STICKER

        elif m.reply_to_message.document:
            if m.reply_to_message.document.mime_type in [
                "application/x-bad-tgsticker",
                "application/x-tgsticker",
            ]:
                data_type = Types.ANIMATED_STICKER
            else:
                data_type = Types.DOCUMENT
            content = m.reply_to_message.document.file_id

        elif m.reply_to_message.photo:
            content = m.reply_to_message.photo.file_id  # last elem = best quality
            data_type = Types.PHOTO

        elif m.reply_to_message.audio:
            content = m.reply_to_message.audio.file_id
            data_type = Types.AUDIO

        elif m.reply_to_message.voice:
            content = m.reply_to_message.voice.file_id
            data_type = Types.VOICE

        elif m.reply_to_message.video:
            content = m.reply_to_message.video.file_id
            data_type = Types.VIDEO

        elif m.reply_to_message.video_note:
            content = m.reply_to_message.video_note.file_id
            data_type = Types.VIDEO_NOTE

        elif m.reply_to_message.animation:
            content = m.reply_to_message.animation.file_id
            data_type = Types.ANIMATION

    else:
        return None, None, None, None

    return note_name, text, data_type, content


def get_wlcm_type(m):
    """Get wlcm type."""
    data_type = None
    content = None
    raw_text = m.text.markdown if m.text else m.caption.markdown
    args = raw_text.split(None, 1)

    if not m.reply_to_message and m.text and len(m.text.strip().split()) >= 2:
        content = None
        text = m.text.markdown.split(None, 1)[1]
        data_type = Types.TEXT

    elif m.reply_to_message:
        if m.reply_to_message.text:
            text = m.reply_to_message.text.markdown
        elif m.reply_to_message.caption:
            text = m.reply_to_message.caption.markdown
        else:
            text = ""

        if len(args) >= 1 and m.reply_to_message.text:  # not caption, text
            data_type = Types.TEXT

        elif m.reply_to_message.document:
            data_type = Types.DOCUMENT
            content = m.reply_to_message.document.file_id

        elif m.reply_to_message.photo:
            content = m.reply_to_message.photo.file_id  # last elem = best quality
            data_type = Types.PHOTO

        elif m.reply_to_message.audio:
            content = m.reply_to_message.audio.file_id
            data_type = Types.AUDIO

        elif m.reply_to_message.voice:
            content = m.reply_to_message.voice.file_id
            data_type = Types.VOICE

        elif m.reply_to_message.video:
            content = m.reply_to_message.video.file_id
            data_type = Types.VIDEO

        elif m.reply_to_message.video_note:
            content = m.reply_to_message.video_note.file_id
            data_type = Types.VIDEO_NOTE

        elif m.reply_to_message.animation:
            content = m.reply_to_message.animation.file_id
            data_type = Types.ANIMATION

    else:
        text = None
        data_type = None
        content = None

    return text, data_type, content


def get_filter_type(m):
    """Get filter type."""
    if len(m.text.split()) <= 1:
        return None, None, None

    data_type = None
    content = None
    raw_text = m.text.markdown if m.text else m.caption.markdown
    args = raw_text.split(None, 2)

    if not m.reply_to_message and m.text and len(m.text.split()) >= 3:
        content = None
        text = m.text.markdown.split(None, 2)[2]
        data_type = Types.TEXT

    elif m.reply_to_message:
        if m.reply_to_message.text:
            text = m.reply_to_message.text.markdown
        elif m.reply_to_message.caption:
            text = m.reply_to_message.caption.markdown
        else:
            text = ""

        if len(args) >= 2 and m.reply_to_message.text:  # not caption, text
            data_type = Types.TEXT

        elif m.reply_to_message.sticker:
            content = m.reply_to_message.sticker.file_id
            data_type = Types.STICKER

        elif m.reply_to_message.document:
            if m.reply_to_message.document.mime_type in [
                "application/x-bad-tgsticker",
                "application/x-tgsticker",
            ]:
                data_type = Types.ANIMATED_STICKER
            else:
                data_type = Types.DOCUMENT
            content = m.reply_to_message.document.file_id

        elif m.reply_to_message.photo:
            content = m.reply_to_message.photo.file_id  # last elem = best quality
            data_type = Types.PHOTO

        elif m.reply_to_message.audio:
            content = m.reply_to_message.audio.file_id
            data_type = Types.AUDIO

        elif m.reply_to_message.voice:
            content = m.reply_to_message.voice.file_id
            data_type = Types.VOICE

        elif m.reply_to_message.video:
            content = m.reply_to_message.video.file_id
            data_type = Types.VIDEO

        elif m.reply_to_message.video_note:
            content = m.reply_to_message.video_note.file_id
            data_type = Types.VIDEO_NOTE

        elif m.reply_to_message.animation:
            content = m.reply_to_message.animation.file_id
            data_type = Types.ANIMATION

    else:
        text = None
        data_type = None
        content = None

    return text, data_type, content


def get_file_id(msg):
    data_type = None
    content = None
    if msg.media:
        if msg.sticker:
            content = msg.sticker.file_id
            data_type = Types.STICKER

        elif msg.document:
            content = msg.document.file_id
            data_type = Types.DOCUMENT

        elif msg.photo:
            content = msg.photo.file_id
            data_type = Types.PHOTO

        elif msg.audio:
            content = msg.audio.file_id
            data_type = Types.AUDIO

        elif msg.voice:
            content = msg.voice.file_id
            data_type = Types.VOICE

        elif msg.video:
            content = msg.video.file_id
            data_type = Types.VIDEO

        elif msg.video_note:
            content = msg.video_note.file_id
            data_type = Types.VIDEO_NOTE

    return data_type, content


def get_afk_type(m):
    data_type = None
    content = None
    raw_text = m.text.markdown if m.text else m.caption.markdown
    args = raw_text.split(None, 1)

    if not m.reply_to_message and m.text and len(m.text.strip().split()) >= 2:
        content = None
        text = m.text.markdown.split(None, 1)[1]
        data_type = Types.TEXT

    elif m.reply_to_message:
        if m.reply_to_message.text:
            text = m.reply_to_message.text.markdown
        elif m.reply_to_message.caption:
            text = m.reply_to_message.caption.markdown
        else:
            text = ""

        if len(args) >= 1 and m.reply_to_message.text:  # not caption, text
            data_type = Types.TEXT

        elif m.reply_to_message.document:
            data_type = Types.DOCUMENT
            content = m.reply_to_message.document.file_id

        elif m.reply_to_message.photo:
            content = m.reply_to_message.photo.file_id  # last elem = best quality
            data_type = Types.PHOTO

        elif m.reply_to_message.audio:
            content = m.reply_to_message.audio.file_id
            data_type = Types.AUDIO

        elif m.reply_to_message.voice:
            content = m.reply_to_message.voice.file_id
            data_type = Types.VOICE

        elif m.reply_to_message.video:
            content = m.reply_to_message.video.file_id
            data_type = Types.VIDEO

        elif m.reply_to_message.video_note:
            content = m.reply_to_message.video_note.file_id
            data_type = Types.VIDEO_NOTE

        elif m.reply_to_message.animation:
            content = m.reply_to_message.animation.file_id
            data_type = Types.ANIMATION

    else:
        text = None
        data_type = None
        content = None

    return text, data_type, content
