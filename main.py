def on_sound_loud():
    global 작동_시작
    작동_시작 += 1
input.on_sound(DetectedSound.LOUD, on_sound_loud)

작동_시작 = 0
input.set_sound_threshold(SoundThreshold.LOUD, 250)
music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
    music.PlaybackMode.IN_BACKGROUND)

def on_forever():
    if 작동_시작 == 1:
        basic.pause(1000)
        music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
            music.PlaybackMode.IN_BACKGROUND)
        basic.pause(2000)
        music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_DOWN),
            music.PlaybackMode.IN_BACKGROUND)
basic.forever(on_forever)

def on_forever2():
    if 작동_시작 == 1:
        basic.show_leds("""
            # . # . .
            # # # # #
            . . # . #
            . # . # #
            . # . . .
            """)
        basic.show_leds("""
            . . # . #
            # # # # #
            # . # . .
            # # . # .
            . . . # .
            """)
        basic.show_leds("""
            # . # . #
            . # # # .
            . . # . .
            . # . # .
            . # . # .
            """)
basic.forever(on_forever2)
