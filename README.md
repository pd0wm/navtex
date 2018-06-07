# Navtex
Navtex (Navigational Telex) is a way to broadcast (weather) information to ships. This repository contains an IPython notebook to receive such messages.

Navtex is broadcasted at 518 kHz, and is modulated using FSK (frequency-shift keying). This is de-modulated using a simple PLL (phased locked loop). After the signal is demodulated the bits can be extracted. Navtex consists of 7 bit symbols, with no start or stop bits. The only way to separate symbols is using the phasing sequence at the start of each message. Each 7 bit symbol consist of exactly four 1s and three 0s. The alphabet is chosen in such a way that each symbol has at least a hamming distance of two.

A Navtex broadcast consist of two streams broadcasting the same information, but shifted a few symbols. In this way when reception is disrupted, the complete message can still be received. At the start of each message both stream are sending a special phasing symbol, which can be used to synchronize the symbol timing in the receiver.

The receiver implemented in this notebook is just a proof of concept and does not use any error recovery. Therefore improving the performance should be pretty easy.

Information about the exact implementation is scarce, but a lot of information can be found on this website: https://arachnoid.com/JNX/
