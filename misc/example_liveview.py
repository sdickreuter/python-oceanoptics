#!/usr/bin/env python
""" File:           example_liveview.py
    Author:         Andreas Poehlmann
    Last change:    2013/02/27

    Liveview example
"""


if __name__ == '__main__':

    import OceanOptics
    
    from gi.repository import Gtk, GLib
    from itertools import cycle


    class mpl:
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

    class DynamicPlotter(Gtk.Window):

        def __init__(self, sampleinterval=0.01, size=(1000,500), raw=False):
            # Gtk stuff
            #Gtk.Window.__init__(self, title='OceanOptics USB2000+ Spectrum')
            self._window_title = 'OceanOptics QE65000 Spectrum'
            Gtk.Window.__init__(self, title= self._window_title)
            self.connect("destroy", lambda x : Gtk.main_quit())
            self.set_default_size(*size)
            # Data stuff
            self._interval = int(sampleinterval*1000)
            #self.spec = OceanOptics.USB2000()
            self.spec = OceanOptics.QE65000()
            self.wl, self.sp = self.spec.acquire_spectrum()
            self.raw = bool(raw)
            # MPL stuff
            self.figure = mpl.Figure()
            self.ax = self.figure.add_subplot(1, 1, 1)
            self.ax.grid(True)
            self.canvas = mpl.FigureCanvas(self.figure)
            self.line, = self.ax.plot(self.wl, self.sp)
            # Gtk stuff
            self.add(self.canvas)
            self.canvas.show()
            self.show_all()

        def updateplot(self):
            if self.raw:
                self.sp = self.spec._request_spectrum()
            else:
                _, self.sp = self.spec.acquire_spectrum()
            self.line.set_ydata(self.sp)
            self.ax.relim()
            self.ax.autoscale_view(False, False, True)
            self.canvas.draw()
            self._update_title()
            return True

        def _update_title(self, _suff=cycle('/|\-')):
            self.set_title('%s %s' % (self._window_title, next(_suff)))
            return True  # continue updates

        def run(self):
            GLib.timeout_add(self._interval, self.updateplot )
            Gtk.main()

    import sys
    if sys.argv[1:] == ['--raw']:
        raw=True
    else:
        raw=False

    m = DynamicPlotter(sampleinterval=0.05, raw=raw)
    m.run()

