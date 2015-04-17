#!/usr/bin/env python

"""
Class describing implementation of a SN universe describing the types of SN in the universe, the abundances of each type of SN, and the distribution of subtypes/parameters of each type of SN. To allow for convenient usage in multiple application situations (eg. where the population of galaxies is known or where it is not), it should be possible to describe such a universe in terms of the galaxies present (giving environmental properties) or on the average, with no knowledge of galaxies but through a rate. 

In practice the class is specified by the following attributes and methods:

    atrributes:
        SNModel: Physically this is a phenomenological model of SN such as\
            the SALT2 model. In practice, this could point to an SNCosmo Model\
            object.
    methods:
        SNdists: This specifies how the parameters of SNModel described above
            are distributed.

"""
import sncosmo
import numpy as np
import Sources



class TypeInfo(object):
      """docstring for TypeInfo"""
      def __init__(self, model, pdf):
          super(TypeInfo, self).__init__()
          self.model = model
          self._pdf=pdf

class TSSUniverse (object):

    def __init__(self, start_mjd, end_mjd, seed):
        self._types=types  = [ 'SN II-pec','SN IIL','SN IIL/P', 'SN IIP', \
            'SN IIn', 'SN Ia', 'SN Ib', 'SN Ib/c', 'SN Ic']

        self._start_mjd = start_mjd
        self._end_mjd = end_mjd
        self._seed = seed

        self.typeinfo=dict()
        for t in self._types:
            self.typeinfo[t]=TypeInfo(Sources.registry_sources_as_models(t,
                subclassName="sncosmo.TimeSeriesSource"), np.random.normal(-19.3, 0.3))

    def sneByGalaxies(self,galaxies):
        #for each type determine wehther there is a 
        pass

    def sneBySNType(self,sntype):
        pass

    @property
    def seed(self):
        return self._seed
    def reset_model(self, seed, z):
        self._seed = seed
        self.set_z(z) 
        return self.get_SNparams()

    @property 
    def z(self):
        return self._z

    def set_z(self,z ):
        self._z = z
        self.snIaModel.set(z=z)
    @property
    def ra(self):
        return self._ra 

    def get_SNparams(self):

        hundredyear = 100*365.0
        np.random.seed(self.seed)
        t0 = np.random.uniform(-hundredyear/2.0, hundredyear/2.0)
        c = np.random.normal(0., 0.3)
        x1 = np.random.normal(0., 1.0)
        mabs = np.random.normal(-19.3, 0.3)
        self.snIaModel.set(z=self.z, c=c, x1=x1)
        self.snIaModel.set_source_peakabsmag(mabs, 'bessellb', 'ab')
        x0 = self.snIaModel.get('x0')

        return np.array([t0, x0, x1, c])


if __name__ == "__main__":
    dum =  TSSUniverse(0,365.25*10,0)