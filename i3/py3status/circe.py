import os


NCHAR = 3
CMD = 'emacsclient --eval \"(mapcar \'message tracking-buffers)\"'

def get_channels(res):
    """Get channels from the system pipe response"""
    return [c.strip('"') for c in res.rstrip().strip('()').split(' ')]
n
class Py3status:

    def circe(self):
        res = os.popen(CMD).read()
        channels = get_channels(res)
        if len(channels) == 1 and channels[0] == 'nil':
            full_text = ""
        else:
            full_text = ""
            for i,c in enumerate(channels):
                full_text += c[:NCHAR]
                if i!=len(channels)-1:
                    full_text += ' '
        return {
            'full_text': full_text,
            'color': self.py3.COLOR_LOW
        }
