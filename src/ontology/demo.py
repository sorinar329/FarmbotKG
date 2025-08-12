from farmbotOnto import onto
from farmbotOnto.classes import Crop, Leaf, LeafChlorophyllConcentration
from farmbotOnto.properties import has_leaf, has_chlorophyll_concentraton, has_chlorophyll_concentration_threshold, has_plant_stress


with onto:
    crop1 = Crop("tomato")
    leaf1 = Leaf("leaf1")
    leaf_chlorophyll_concentration = LeafChlorophyllConcentration("chlorophyll1")

    crop1.has_leaf = [leaf1]
    crop1.has_chlorophyll_concentration_threshold = [0.5]

    leaf1.has_chlorophyll_concentraton = [leaf_chlorophyll_concentration]
    leaf_chlorophyll_concentration.has_value = [0.6]

    print(f"Crop: {crop1.name}")
    print(f"Leaf: {leaf1.name}")
    print(f"Chlorophyll Concentration: {leaf_chlorophyll_concentration.has_value}")
    print(f"Chlorophyll Concentration Threshold: {crop1.has_chlorophyll_concentration_threshold}")

    if leaf_chlorophyll_concentration.has_value > crop1.has_chlorophyll_concentration_threshold:
        crop1.has_plant_stress = ["High"]
        print("Chlorophyll concentration is above the threshold, indicating potential plant stress.")



# Save the ontology with the new data
onto_path = "/home/sorin/dev/FarmbotKG/ressources/farmbotOnto.owl"
onto.save(file=onto_path, format="rdfxml")