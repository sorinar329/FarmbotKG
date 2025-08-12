from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/FarmBotOntology")

with onto:
    class Action(Thing):
        """An action concept"""
        pass

    class MovingAction(Action):
        """A moving action concept"""
        pass

    class WateringAction(Action):
        """A watering action concept"""
        pass

    class SeedingAction(Action):
        """A seeding action concept"""
        pass

    class Crop(Thing):
        """A crop concept"""
        pass

    class Tomato(Crop):
        """A tomato crop concept"""
        pass

    class Corn(Crop):
        """A corn crop concept"""
        pass

    class Factor(Thing):
        """A factor concept"""
        pass

    class EnvironmentalFactor(Factor):
        """An environmental factor concept"""
        pass

    class AirHumidity(EnvironmentalFactor):
        """An air humidity concept"""
        pass

    class SoilMoisture(EnvironmentalFactor):
        """A soil moisture concept"""
        pass

    class AirTemperature(EnvironmentalFactor):
        """An air temperature concept"""
        pass

    class SoilCompaction(EnvironmentalFactor):
        """A soil compaction concept"""
        pass

    class soilPH(EnvironmentalFactor):
        """A soil pH concept"""
        pass

    class soilSalinity(EnvironmentalFactor):
        """A soil salinity concept"""
        pass

    class soilTemperature(EnvironmentalFactor):
        """A soil temperature concept"""
        pass

    class PlantFactor(Factor):
        """A plant factor concept"""
        pass

    class LeafChlorophyllConcentration(PlantFactor):
        """A leaf chlorophyll concentration concept"""
        pass

    class LeafStomatalClosure(PlantFactor):
        """A leaf stomatal closure concept"""
        pass

    class LeafTemperature(PlantFactor):
        """A leaf temperature concept"""
        pass

    class LeafWetness(PlantFactor):
        """A leaf wetness concept"""
        pass

    class Sensor(Thing):
        """A sensor concept"""
        pass

    class Camera(Sensor):
        """A camera sensor concept"""
        pass

    class HyperSpectralCamera(Camera):
        """A hyperspectral camera sensor concept"""
        pass

    class RGBDCamera(Camera):
        """An RGBD camera sensor concept"""
        pass

    class stereoDepth(Camera):
        """A stereo camera sensor concept"""
        pass

    class ThermalCamera(Camera):
        """A thermal camera sensor concept"""
        pass

    class Leaf(Thing):
        """A leaf concept"""
        pass

    class Threshold(Thing):
        """A threshold concept"""
        pass
