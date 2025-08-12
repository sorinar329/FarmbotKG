from owlready2 import *


from src.ontology.farmbotOnto.classes  import Leaf, Factor, Crop, LeafChlorophyllConcentration
from src.ontology.farmbotOnto.classes import LeafWetness

onto = get_ontology("http://www.ease-crc.org/ont/FarmBotOntology")

with onto:
    class has_leaf_wetness(ObjectProperty):
        """Wetness of the soil"""
        domain = [Leaf]
        range = [LeafWetness]

    class has_value(DataProperty):
        """Value of the observation"""
        domain = [Factor]
        range = [float]

    class has_leaf(ObjectProperty):
        """Leaf of the plant"""
        domain = [Crop]
        range = [Leaf]

    class has_chlorophyll_concentraton(ObjectProperty):
        """Chlorophyll content of the leaf"""
        domain = [Leaf]
        range = [LeafChlorophyllConcentration]

    class has_chlorophyll_concentration_threshold(DataProperty):
        """Threshold for chlorophyll concentration"""
        domain = [Crop]
        range = [float]

    class has_plant_stress(DataProperty):
        """Plant stress level"""
        domain = [Crop]
        range = [str]

