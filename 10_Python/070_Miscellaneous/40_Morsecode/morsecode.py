# Morsecode library

import time
from machine import Pin

# Ganimede.E12 default LED
LED = Pin(16, Pin.OUT)

# Morsecode lookup-table
CODE = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
    'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.',
    'O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
    'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
    '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
    '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
    '.':'.-.-.-',
    ',':'--..--',
    '?':'..--..',
    '/':'--..-.',
    '@':'.--.-.',
    ' ':' ',
}

# Morse class
class Morse:
    def __init__ (self, on_cbk = LED.on, off_cbk = LED.off, tdot = 0.1):
        # Values for time delays
        self.tdot = tdot
        self.tdash = tdot * 3
        self.tspace = tdot * 2
        self.tword = tdot * 6        
        self.on = on_cbk
        self.off = off_cbk
            
    def _flash (self, t):
        self.on()
        time.sleep(t)
        self.off()
        return

    def send (self, msg):
        self.off()        
        for l in msg:
            c = CODE.get(l.upper())
            for e in c:
                # Dot
                if e == ".":
                    self._flash(self.tdot)
                    time.sleep(self.tdot)
                # Dash
                if e == "-":
                    self._flash(self.tdash)
                    time.sleep(self.tdot)
                # Space
                if e == " ":
                    time.sleep(self.tword)
            # Delay between characters        
            time.sleep(self.tword)                
        self.off()  
