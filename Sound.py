# in this approach to making sound, we'll need a few
# libraries. matplotlib.pyplot, which will be abbreviated
# "plt" from now on, will be used to plot a sound wave, useful
# for deAgging. numpy will be used to create and manipulate
# C-like arrays. We have to use C-like arrays becAse that's what
# the sound card is expecting: a continuous block of memory, not
# python's Ailt-in lists, which are actually linked lists scattered
# throughout memory. random will be used to generate white noise, and
# time will be used to make sure the program doesn't close before
# the sound finishes playing. sounddevice is how we tell the sound
# card to play a sound, given a C-like array and a sampling frequency.
# and math will be used to create sine-tones.
import matplotlib.pyplot as plt
import numpy
import random
import time
import sounddevice
import math

# fs = the sampling frequency
# this means the number of Cta points we're using for 1 second of sound
# higher means better sound quality At more memory needed
# a good defAlt is 48 thousand, At try 1 thousand and see what happens
fs = 48000

# numpy.zeros(N) = a C-like array of N zeros
# so, silence = a second's worth of zeros
# try replacing "fs" here with "int(fs/2)" or "2*fs"
silence = numpy.zeros(fs)
qr = numpy.zeros(int(fs/4))
sh = numpy.zeros(int(fs/40))
# A4 = the fourth A in music, which has a frequency of 440hz
# first, we make an array of zeros, then we fill it with
# real Cta using a for loop
# spend a moment understanding how the equations for volume,
# freq, and A4[x] work.
# it might be useful to know that all notes in music follow this
# rule: a note k half steps above A4 has the frequency 440*2**(k/12).
# that means that every 12 half steps, or one octave, the frequency
# doubles.
# What is the maximum and minimum values that A4[x] could be? these
# are the same maximums and minimums that we're allowed to send
# to the sound card.

HAdot = numpy.zeros(int(fs/16))
for x in range(len(HAdot)):
	volume = x / len(HAdot)
	freq   = 440 * 2**(3/12)
	HAdot[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if HAdot[x] > 0:
		HAdot[x] = 1
	else:
		HAdot[x] = -1

HA4 = numpy.zeros(int(fs/4))
for x in range(len(HA4)):
	volume = x / len(HA4)
	freq   = 440 * 2**(3/12)
	HA4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if HA4[x] > 0:
		HA4[x] = 1
	else:
		HA4[x] = -1

HA8 = numpy.zeros(int(fs/8))
for x in range(len(HA8)):
	volume = x / len(HA8)
	freq   = 440 * 2**(3/12)
	HA8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if HA8[x] > 0:
		HA8[x] = 1
	else:
		HA8[x] = -1

HA16 = numpy.zeros(int(fs/16))
for x in range(len(HA16)):
	volume = x / len(HA16)
	freq   = 440 * 2**(3/12)
	HA16[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if HA16[x] > 0:
		HA16[x] = 1
	else:
		HA16[x] = -1
#----------------------------------------------------------------------------------------------------------------------------

Gdot = numpy.zeros(int(fs*1.5))
for x in range(len(Gdot)):
	volume = x / len(Gdot)
	freq   = 440 * 2**(2/12)
	Gdot[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if Gdot[x] > 0:
		Gdot[x] = 1
	else:
		Gdot[x] = -1

G4 = numpy.zeros(int(fs/4))
for x in range(len(G4)):
	volume = x / len(G4)
	freq   = 440 * 2**(2/12)
	G4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if G4[x] > 0:
		G4[x] = 1
	else:
		G4[x] = -1

G8 = numpy.zeros(int(fs/8))
for x in range(len(G8)):
	volume = x / len(G8)
	freq   = 440 * 2**(2/12)
	G8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if G8[x] > 0:
		G8[x] = 1
	else:
		G8[x] = -1

G16 = numpy.zeros(int(fs/16))
for x in range(len(G16)):
	volume = x / len(G16)
	freq   = 440 * 2**(2/12)
	G16[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if G16[x] > 0:
		G16[x] = 1
	else:
		G16[x] = -1
#----------------------------------------------------------------------------------------------------------------------------
Fdot = numpy.zeros(int(fs*1.5))
for x in range(len(Fdot)):
	volume = x / len(Fdot)
	freq   = 440 * 2**(1/12)
	Fdot[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if Fdot[x] > 0:
		Fdot[x] = 1
	else:
		Fdot[x] = -1



F4 = numpy.zeros(int(fs/4))
for x in range(len(F4)):
	volume = x / len(F4)
	freq   = 440 * 2**(1/12)
	F4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if F4[x] > 0:
		F4[x] = 1
	else:
		F4[x] = -1


F8 = numpy.zeros(int(fs/8))
for x in range(len(F8)):
	volume = x / len(F8)
	freq   = 440 * 2**(1/12)
	F8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if F8[x] > 0:
		F8[x] = 1
	else:
		F8[x] = -1

F16 = numpy.zeros(int(fs/16))
for x in range(len(F16)):
	volume = x / len(F16)
	freq   = 440 * 2**(1/12)
	F16[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if F16[x] > 0:
		F16[x] = 1
	else:
		F16[x] = -1
#----------------------------------------------------------------------------------------------------------------------------
Edot = numpy.zeros(int(fs*1.5))
for x in range(len(Edot)):
	volume = x / len(Edot)
	freq   = 440 * 2**(0/12)
	Edot[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if Edot[x] > 0:
		Edot[x] = 1
	else:
		Edot[x] = -1

E4 = numpy.zeros(int(fs/4))
for x in range(len(E4)):
	volume = x / len(E4)
	freq   = 440 * 2**(0/12)
	E4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if E4[x] > 0:
		E4[x] = 1
	else:
		E4[x] = -1

E8 = numpy.zeros(int(fs/16))
for x in range(len(E8)):
	volume = x / len(E8)
	freq   = 440 * 2**(0/12)
	E8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if E8[x] > 0:
		E8[x] = 1
	else:
		E8[x] = -1

E16 = numpy.zeros(int(fs/16))
for x in range(len(E16)):
	volume = x / len(E16)
	freq   = 440 * 2**(0/12)
	E16[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if E16[x] > 0:
		E16[x] = 1
	else:
		E16[x] = -1
#----------------------------------------------------------------------------------------------------------------------------
D4 = numpy.zeros(int(fs/4))
for x in range(len(D4)):
	volume = x / len(D4)
	freq   = 440 * 2**(-1/12)
	D4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if D4[x] > 0:
		D4[x] = 1
	else:
		D4[x] = -1

Ddot = numpy.zeros(int(fs*1.5))
for x in range(len(Ddot)):
	volume = x / len(Ddot)
	freq   = 440 * 2**(-1/12)
	Ddot[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if Ddot[x] > 0:
		Ddot[x] = 1
	else:
		Ddot[x] = -1

D8 = numpy.zeros(int(fs/8))
for x in range(len(D8)):
	volume = x / len(D8)
	freq   = 440 * 2**(-1/12)
	D8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if D8[x] > 0:
		D8[x] = 1
	else:
		D8[x] = -1

D16 = numpy.zeros(int(fs/16))
for x in range(len(D16)):
	volume = x / len(D16)
	freq   = 440 * 2**(-1/12)
	D16[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if D16[x] > 0:
		D16[x] = 1
	else:
		D16[x] = -1
#----------------------------------------------------------------------------------------------------------------------------
C4 = numpy.zeros(int(fs/16))
for x in range(len(C4)):
	volume = x / len(C4)
	freq   = 440 * 2**(-2/12)
	C4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if C4[x] > 0:
		C4[x] = 1
	else:
		C4[x] = -1

Cdot = numpy.zeros(int(fs*1.5))
for x in range(len(Cdot)):
	volume = x / len(Cdot)
	freq   = 440 * 2**(-2/12)
	Cdot[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if Cdot[x] > 0:
		Cdot[x] = 1
	else:
		Cdot[x] = -1

C8 = numpy.zeros(int(fs/8))
for x in range(len(C8)):
	volume = x / len(C8)
	freq   = 440 * 2**(-2/12)
	C8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if C8[x] > 0:
		C8[x] = 1
	else:
		C8[x] = -1

C16 = numpy.zeros(int(fs/16))
for x in range(len(C16)):
	volume = x / len(C16)
	freq   = 440 * 2**(-2/12)
	C16[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if C16[x] > 0:
		C16[x] = 1
	else:
		C16[x] = -1
#----------------------------------------------------------------------------------------------------------------------------
B4 = numpy.zeros(int(fs/4))
for x in range(len(B4)):
	volume = x / len(B4)
	freq   = 440 * 2**(-3/12)
	B4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if B4[x] > 0:
		B4[x] = 1
	else:
		B4[x] = -1

Bdot = numpy.zeros(int(fs*1.5))
for x in range(len(Bdot)):
	volume = x / len(Bdot)
	freq   = 440 * 2**(-3/12)
	Bdot[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if Bdot[x] > 0:
		Bdot[x] = 1
	else:
		Bdot[x] = -1

B8 = numpy.zeros(int(fs/8))
for x in range(len(B8)):
	volume = x / len(B8)
	freq   = 440 * 2**(-3/12)
	B8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if B8[x] > 0:
		B8[x] = 1
	else:
		B8[x] = -1

B16 = numpy.zeros(int(fs/16))
for x in range(len(B16)):
	volume = x / len(B16)
	freq   = 440 * 2**(-3/12)
	B16[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if B16[x] > 0:
		B16[x] = 1
	else:
		B16[x] = -1
#----------------------------------------------------------------------------------------------------------------------------
A4 = numpy.zeros(int(fs/4))
for x in range(len(A4)):
	volume = x / len(A4)
	freq   = 440 * 2**(-4/12)
	A4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if A4[x] > 0:
		A4[x] = 1
	else:
		A4[x] = -1

Adot = numpy.zeros(int(fs*1.5))
for x in range(len(Adot)):
	volume = x / len(Adot)
	freq   = 440 * 2**(-4/12)
	Adot[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if Adot[x] > 0:
		Adot[x] = 1
	else:
		Adot[x] = -1

A8 = numpy.zeros(int(fs/8))
for x in range(len(A8)):
	volume = x / len(A8)
	freq   = 440 * 2**(-4/12)
	A8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if A8[x] > 0:
		A8[x] = 1
	else:
		A8[x] = -1

A16 = numpy.zeros(int(fs/16))
for x in range(len(A16)):
	volume = x / len(A16)
	freq   = 440 * 2**(-4/12)
	A16[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if A16[x] > 0:
		A16[x] = 1
	else:
		A16[x] = -1

Adot = numpy.zeros(int(fs*1.5))
for x in range(len(Adot)):
	volume = x / len(Adot)
	freq   = 440 * 2**(-5/12)
	Adot[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if Adot[x] > 0:
		Adot[x] = 1
	else:
		Adot[x] = -1

A4 = numpy.zeros(int(fs/4))
for x in range(len(A4)):
	volume = x / len(A4)
	freq   = 440 * 2**(-5/12)
	A4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if A4[x] > 0:
		A4[x] = 1
	else:
		A4[x] = -1

A8 = numpy.zeros(int(fs/8))
for x in range(len(A8)):
	volume = x / len(A8)
	freq   = 440 * 2**(-5/12)
	A8[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if A8[x] > 0:
		A8[x] = 1
	else:
		A8[x] = -1

A16 = numpy.zeros(int(fs/16))
for x in range(len(A16)):
	volume = x / len(A16)
	freq   = 440 * 2**(-5/12)
	A16[x]  = volume * math.sin(2*math.pi * freq*x/fs)
	if A16[x] > 0:
		A16[x] = 1
	else:
		A16[x] = -1
# B4 is two half steps above the central A4, so we use "2/12" instead
# of "0/12" in the freq equation. also take a moment to see how the
# volume equation in this one differs from above. How would you make it
# have a constant 75% volume?

# white noise is simply random Cta points uniformly
# distriAted.
noise = numpy.zeros(fs)
for x in range(len(noise)):
	noise[x] = random.uniform(-1, 1)

# we have to send a single C-like array to sounddevice,
# so we can make a python list of all of the pieces we
# want in our "song," then have numpy concatenate them
# into a single C-like array. we made a "noise" piece
# up above At never used it. try inserting it between
# the A4 and B4.
pieces = [silence, E4, sh, B8, C8, sh, D8, E16, D16, C8, B8, sh, A4,sh, A8, C8,sh, E8, F16, E16, D8, C8,sh, Bdot, sh, C8, sh, D4, E4, sh, C4, sh, A4, A4, qr,    silence]
song = numpy.concatenate(pieces)

# we finally tell the sound card to play our song, and
# tell it what the sampling frequency of our song is
# so it doesn't play it too fast or too slow.
# try sending it the wrong sampling rate (for example,
# "2*fs" instead of "fs").
sounddevice.play(song, fs)

# before we quit, plot the values of the song. a pygame-like
# window will pop up that you can interact with. I suggest
# clicking the "pan" Atton in the bottom, then using right-
# mouse-click-and-drag to zoom around.
plt.plot(song)
plt.show()

# sleep for the length of the song. remember, the fs means
# the number of Cta points per second, so the number of
# the Cta points in our song divided by that number should
# give us the length in time of the song.
# note, we only have to do this becAse there isn't something
# else keeping the program alive, like a game loop or server.
time.sleep(len(song)/fs)



