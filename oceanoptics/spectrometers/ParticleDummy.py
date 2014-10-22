__author__ = 'sei'


from oceanoptics.base import OceanOpticsBase as _OOBase
import numpy as np
import time
import PIStage
#----------------------------------------------------------


class ParticleDummy(_OOBase):

    def __init__(self,stage=None,particles=[[10,10],]):
        self._integration_time = 1000
        self._particles = particles
        self._stage = stage
        print 'ParticleDummy class initialized'

    def __gaussian(self, x, mu, sig):
        return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
        #return (1/(np.sqrt(2*np.pi)*sig)) * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

    def __gaussian2d(self, x, y, mu_x, mu_y, FWHM):
        sig = FWHM/2.3548
        #return (1/(2*np.pi*np.power(sig,2.))) * np.exp(-( np.power(x - mu_x, 2.) + np.power(y - mu_y, 2.) ) / (2 * np.power(sig, 2.)))
        return np.exp(-( np.power(x - mu_x, 2.) + np.power(y - mu_y, 2.) ) / (2 * np.power(sig, 2.)))


    def _calc_spectrum(self):
        spectrum = np.random.random_integers(2400, 2600, (1024))
        spectrum = np.array(spectrum, dtype=np.float)
        spectrum = spectrum + 300*self.__gaussian(self.wavelengths(),512,60)
        spectrum = np.array(spectrum, dtype=np.uint16)
        return spectrum

    def _calc_particle_spectrum(self):
        spectrum = np.random.random_integers(2400, 2600, (1024))

        for pos in self._particles:
            x, y, z = self._stage.pos()
            int = self.__gaussian2d(x,y,pos[0],pos[1],1)
            spectrum += 300*int*self.__gaussian(self.wavelengths(),512,60)

        spectrum = np.array(spectrum, dtype=np.uint16)
        return spectrum


    def _request_spectrum(self):
        time.sleep(float(self._integration_time)/1000000)
        if self._stage is None: return self._calc_spectrum()
        else : return self._calc_particle_spectrum()

    def intensities(self, raw=False, only_valid_pixels=True,
                    correct_nonlinearity=True, correct_darkcounts=True,
                    correct_saturation=True):
        data =  self._request_spectrum()
        data = np.array(data, dtype=np.float)
        return data

    def wavelengths(self, only_valid_pixels=True):
        return np.linspace(200, 900, num=1024)

    def integration_time(self, time_us=None):
        self._integration_time = time_us
        return self._integration_time
