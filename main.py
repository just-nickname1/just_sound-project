작동_시작 = 0
input.set_sound_threshold(SoundThreshold.LOUD, 250)
music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
    music.PlaybackMode.IN_BACKGROUND)

def on_forever():
    pass
basic.forever(on_forever)
