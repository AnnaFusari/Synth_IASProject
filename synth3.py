from pyo import *

class Oscillator(PyoObject):
    """
    Oscillator
    :Parent: :py:class:'PyoObject'

    :Args:
        f: int object
            Frequency of oscillator
        ratio: float object optional
            Factor that raise or decrease the frequency ratio between modulator frequency and carrier frequency.
            Default to 0.5
        modulator: int or PyoObject
            Frequency modulator
            0 means no modulation
            Default to 0
        mulindex: float object
            Factor that raise or decrease the mul attribute of oscillator, Sine or LFO
            Default to 300
        tipooscillatore: int object
            Factor that set the type of oscillator.
            0 means LFO
            1 means Sine
            Default to 1
    
    """
    def __init__(self, f, ratio=0.5, modulatore=0, mulindex=300., tipooscillatore=1):
        """
        __init__(self, f, ratio=0.5, modulatore=0, mulindex=300., tipooscillatore=1):
            Initialize self.

        """
        # Call superclass (PyoObject)
        super().__init__()

        #define and inizialize frequency modulator signal and instance attributes
        if tipooscillatore==1:
            self._f=f
            self._mulindex=mulindex
            self._ratio=ratio
            self._modulatore=modulatore
            self._freqO=self._f=self._f+self._modulatore
            self._osc=Sine(freq=self._freqO*self._ratio, mul=self._mulindex)
        else:
            self._f=f
            self._mulindex=mulindex
            self._ratio=ratio
            self._modulatore=modulatore
            self._freqO=self._f=self._f+self._modulatore
            self._osc=LFO(freq=self._freqO*self._ratio, mul=self._mulindex)

        # Define output seen by outside world: self._base_objs
        # Returned by getBaseObjects() method
        self._base_objs = self._osc.getBaseObjects()

    def ctrl(self, map_list=None, title=None, wxnoserver=False):
        """
        def ctrl(self, map_list=None, title=None, wxnoserver=False):
            Opens a sliders window to control the parameters of the object.

        """
        self._osc.ctrl()
        self._map_list=[SLMap(0., 20., "lin", "ratio", self._ratio, res="float"),
                        SLMap(0., 1000., "lin", "mulindex", self._mulindex, res="float")]
        super().ctrl(self._map_list, title, wxnoserver)

    def play(self):
        return super().play()

    def stop(self): 
        return super().stop()

    def out(self):
        return super().out()

    def setF(self, x):
        """
        Replace the `f` attribute.

        :Args:

            x : int object
                New `f` attribute.

        """
        self._f = x
        self._osc.freq=x*self._ratio

    def setMulindex(self, x):
        """
        Replace the `mulindex` attribute.

        :Args:

            x : float object
                New `mulindex` attribute.

        """
        self._mulindex = x
        self._osc.mul=x

    def setRatio(self, x):
        """
        Replace the `ratio` attribute.

        :Args:

            x : int object
                New `ratio` attribute.

        """
        self._ratio = x
        self._osc.freq=self._freqO*x


    @property
    def f(self):
        """int or PyoObject. Frequency of oscillator"""
        return self._f
    @f.setter
    def f(self, x):
        self.setF(x)

    @property
    def ratio(self):
        """float or PyoObject. Ratio between modulator frequency and carrier frequency."""
        return self._ratio
    @ratio.setter
    def ratio(self, x):
        self.setRatio(x)

    @property
    def mulindex(self):
        """float or PyoObject. Factor that raise or decrease the mul attribute of oscillator, Sine or LFO."""
        return self._mulindex
    @mulindex.setter
    def mulindex(self, x):
        self.setMulindex(x)

    

class MySynth(PyoObject):
    """
    Synth FM produced by a carrier signal and 2, 3 or 4 modulator signals.
    MySynth
    :Parent: :py:class:'PyoObject'

    :Args:
        tiposynth: int object:
            Set the number of modulator signals
            Default to 1 means 2 modulator signals
            2 means 3 modulator signals
            3 means 4 modulator signals

    >>> s = Server().boot()
    >>> s.start()
    >>> synth=MySynth(1).out()
    >>> synth.ctrl()
    >>> Scope(synth)
    >>> s.gui(locals())

    """

    def __init__(self, tiposynth=1):
        """
        __init__(self, tiposynth=1):
            Initialize self.

        """

        super().__init__()

        #From a MIDI device, takes the notes
        notes = Notein(poly=6, scale=1)
        notes.keyboard()

        #Define frequncy and amplitude of carrier signal from notes taken from MIDI device
        self._freqcarrier=notes["pitch"]
        self._ampcarrier=Port(notes["velocity"], risetime=0.005, falltime=0.2)
       
        # Define and initialize instance attributes
        self._tiposynth=tiposynth

        # Define modulator signals using Oscillator class
        if tiposynth == 1:
            self._osc1=Oscillator(self._freqcarrier, tipooscillatore=0)
            self._osc2=Oscillator(self._freqcarrier, tipooscillatore=0)
        if tiposynth == 2:
            self._osc3=Oscillator(100, tipooscillatore=1)
            self._osc1=Oscillator(self._freqcarrier, self._osc3, tipooscillatore=0)
            self._osc2=Oscillator(self._freqcarrier, tipooscillatore=0)
        if tiposynth == 3:
            self._osc3=Oscillator(100, tipooscillatore=1)
            self._osc4=Oscillator(400, tipooscillatore=1)
            self._osc1=Oscillator(self._freqcarrier, modulatore=self._osc3, tipooscillatore=0)
            self._osc2=Oscillator(self._freqcarrier, modulatore=self._osc4, tipooscillatore=0)

        # Define the carrier signal (Sine)
        self._carrier=Sine(freq=self._freqcarrier+self._osc1+self._osc2, mul=self._ampcarrier)

        # Pan the carrier signal on 2 channel.
        self._carrierPan=Pan(self._carrier, outs=2, pan=0.5, spread=0.5)

        self._base_objs = self._carrierPan.getBaseObjects()

    def ctrl(self, map_list=None, title=None, wxnoserver=False):
        """
        def ctrl(self, map_list=None, title=None, wxnoserver=False):
            Opens sliders window to control the parameters of the object.
            It uses ctrl method from Oscillator class.

        """
        if self._tiposynth == 1:
            self._osc1.ctrl(title="osc1")
            self._osc2.ctrl(title="osc2")
        if self._tiposynth == 2:
            self._osc1.ctrl(title="osc1")
            self._osc2.ctrl(title="osc2")
            self._osc3.ctrl(title="osc3")
        if self._tiposynth == 3:
            self._osc1.ctrl(title="osc1")
            self._osc2.ctrl(title="osc2")
            self._osc3.ctrl(title="osc3")
            self._osc4.ctrl(title="osc4")

        self._ampcarrier.ctrl(title="carrier")
        
        super().ctrl(map_list, title, wxnoserver)

    def play(self):
        return super().play()
    
    def stop(self):
        return super().stop()
    
    def out(self):
        return super().out()



if __name__ == "__main__":

    s = Server().boot()
    s.start()
    s.amp = 0.1
    #synth=MySynth(1).out()
    synth=MySynth(2).out()
    #synth=MySynth(3).out()
    synth.ctrl()
    Scope(synth)
    s.gui(locals())

    

    

    
