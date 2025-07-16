input.onSound(DetectedSound.Loud, function () {
    작동_시작 += 1
})
let 작동_시작 = 0
input.setSoundThreshold(SoundThreshold.Loud, 250)
music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.InBackground)
basic.forever(function () {
    if (작동_시작 == 1) {
        basic.pause(1000)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.JumpUp), music.PlaybackMode.InBackground)
        basic.pause(2000)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.JumpDown), music.PlaybackMode.InBackground)
    }
})
