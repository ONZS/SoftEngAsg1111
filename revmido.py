from mido import MidiFile

NOTE_TO_CHAR = {i + 60: chr(i + 97) for i in range(26)}

def midi_to_text(filename="song.mid"):
    midi = MidiFile(filename)
    res = ""
    
    for msg in midi.tracks[0]:
        if msg.type == 'note_on':
            if msg.note in NOTE_TO_CHAR:
                res += NOTE_TO_CHAR[msg.note]
    
    return res

t = midi_to_text("song.mid")
flag = f"PETIR{{{t[:28]}}}"
print(flag)
