import json


false = False
true = True
# Define the constant keys (32 properties, in exact order)

keys = [
  "atomicNumber", "symbol", "name", "atomicMass", "category",
  "group", "period", "block", "phase", "density",
  "meltingPoint", "boilingPoint", "electronegativity", "atomicRadius",
  "ionicRadius", "covalentRadius", "ionizationEnergy", "electronAffinity",
  "oxidationStates", "electronConfiguration", "standardState", "bondingType",
  "crystalStructure", "color", "discoveryYear", "discoveredBy",
  "radioactive", "naturalOccurrence", "toxicity", "uses",
  "isotopes", "naturalOrManMade", "valency", "atomicity",
  "molecularMass", "neutrons"
]
elements_names = [
  "hydrogen", "helium", "lithium", "beryllium", "boron", "carbon", "nitrogen", "oxygen", "fluorine", "neon",
  "sodium", "magnesium", "aluminium", "silicon", "phosphorus", "sulfur", "chlorine", "argon", "potassium", "calcium",
  "scandium", "titanium", "vanadium", "chromium", "manganese", "iron", "cobalt", "nickel", "copper", "zinc",
  "gallium", "germanium", "arsenic", "selenium", "bromine", "krypton", "rubidium", "strontium", "yttrium", "zirconium",
  "niobium", "molybdenum", "technetium", "ruthenium", "rhodium", "palladium", "silver", "cadmium", "indium", "tin",
  "antimony", "tellurium", "iodine", "xenon", "cesium", "barium", "lanthanum", "cerium", "praseodymium", "neodymium",
  "promethium", "samarium", "europium", "gadolinium", "terbium", "dysprosium", "holmium", "erbium", "thulium", "ytterbium",
  "lutetium", "hafnium", "tantalum", "tungsten", "rhenium", "osmium", "iridium", "platinum", "gold", "mercury",
  "thallium", "lead", "bismuth", "polonium", "astatine", "radon", "francium", "radium", "actinium", "thorium",
  "protactinium", "uranium", "neptunium", "plutonium", "americium", "curium", "berkelium", "californium", "einsteinium", "fermium",
  "mendelevium", "nobelium", "lawrencium", "rutherfordium", "dubnium", "seaborgium", "bohrium", "hassium", "meitnerium", "darmstadtium",
  "roentgenium", "copernicium", "nihonium", "flerovium", "moscovium", "livermorium", "tennessine", "oganesson", "ununennium", "unbinilium"
]


hydrogen = [
  1, "H", "Hydrogen", 1.008, "Nonmetal",
  1, 1, "s", "Gas", 0.00008988,
  14.01, 20.28, 2.20, 53,
  None, 31, 1312, 72.8,
  "+1, -1", "1s1", "Gas", "Diatomic",
  "Hexagonal", "Colorless", 1766, "Henry Cavendish",
  False, "Natural", "Non-toxic", "Fuel, ammonia production",
  3, "Natural", 1, 2,
  2.016, 0
]

helium = [
  2, "He", "Helium", 4.0026, "Noble Gas",
  18, 1, "s", "Gas", 0.0001785,
  None, 4.22, None, 31,
  None, 28, 2372.3, 0,
  "0", "1s2", "Gas", "Atomic",
  "Hexagonal", "Colorless", 1895, "Pierre Janssen, Norman Lockyer",
  False, "Natural", "Non-toxic", "Coolant, balloons",
  2, "Natural", 0, 1,
  4.0026, 2
]

lithium = [
  3, "Li", "Lithium", 6.94, "Alkali Metal",
  1, 2, "s", "Solid", 0.534,
  453.69, 1615, 0.98, 167,
  76, 128, 520.2, 59.6,
  "+1", "[He] 2s1", "Solid", "Metallic",
  "Body-centered cubic", "Silvery-white", 1817, "Johan Arfwedson",
  False, "Natural", "Low toxicity", "Batteries, ceramics",
  2, "Natural", 1, 1,
  6.94, 4
]

beryllium = [
  4, "Be", "Beryllium", 9.0122, "Alkaline Earth Metal",
  2, 2, "s", "Solid", 1.85,
  1560, 2742, 1.57, 112,
  35, 96, 899.5, 0,
  "+2", "[He] 2s2", "Solid", "Metallic",
  "Hexagonal", "Steel-gray", 1798, "Louis Nicolas Vauquelin",
  False, "Natural", "Toxic", "Aerospace materials, alloys",
  6, "Natural", 2, 1,
  9.0122, 5
]

boron = [
  5, "B", "Boron", 10.81, "Metalloid",
  13, 2, "p", "Solid", 2.34,
  2349, 4200, 2.04, 87,
  None, 84, 800.6, 26.7,
  "+3", "[He] 2s2 2p1", "Solid", "Covalent",
  "Rhombohedral", "Black", 1808, "Joseph Louis Gay-Lussac, Louis Jacques Thénard",
  False, "Natural", "Low toxicity", "Detergents, glass, semiconductors",
  2, "Natural", 3, 1,
  10.81, 6
]

carbon = [
  6, "C", "Carbon", 12.011, "Nonmetal",
  14, 2, "p", "Solid", 2.26,
  3823, 4300, 2.55, 67,
  None, 77, 1086.5, 153.9,
  "+4, +2, -4", "[He] 2s2 2p2", "Solid", "Covalent",
  "Hexagonal or cubic", "Black (graphite)", Ancient := -4000, "Unknown",
  False, "Natural", "Non-toxic", "Organic compounds, fuels, steel",
  3, "Natural", 4, 1,
  12.011, 6
]

nitrogen = [
  7, "N", "Nitrogen", 14.007, "Nonmetal",
  15, 2, "p", "Gas", 0.0012506,
  63.15, 77.36, 3.04, 56,
  None, 71, 1402.3, -6.8,
  "-3, +3, +5, +2, +4", "[He] 2s2 2p3", "Gas", "Diatomic",
  "Hexagonal", "Colorless", 1772, "Daniel Rutherford",
  False, "Natural", "Non-toxic", "Fertilizers, explosives, refrigerants",
  2, "Natural", 3, 2,
  28.014, 7
]

oxygen = [
  8, "O", "Oxygen", 15.999, "Nonmetal",
  16, 2, "p", "Gas", 0.001429,
  54.36, 90.20, 3.44, 48,
  None, 66, 1313.9, 141,
  "-2", "[He] 2s2 2p4", "Gas", "Diatomic",
  "Cubic", "Colorless", 1774, "Carl Wilhelm Scheele, Joseph Priestley",
  False, "Natural", "Non-toxic", "Breathing, combustion, oxides",
  3, "Natural", 2, 2,
  31.998, 8
]

fluorine = [
  9, "F", "Fluorine", 18.998, "Halogen",
  17, 2, "p", "Gas", 0.001696,
  53.53, 85.03, 3.98, 42,
  None, 64, 1681, 328,
  "-1", "[He] 2s2 2p5", "Gas", "Covalent",
  "Cubic", "Pale yellow", 1886, "Henri Moissan",
  False, "Natural", "Highly toxic", "Teflon, refrigerants, uranium processing",
  1, "Natural", 1, 2,
  37.996, 10
]

neon = [
  10, "Ne", "Neon", 20.180, "Noble Gas",
  18, 2, "p", "Gas", 0.0008999,
  24.56, 27.07, None, 38,
  None, 58, 2080.7, 0,
  "0", "[He] 2s2 2p6", "Gas", "Atomic",
  "Face-centered cubic", "Colorless", 1898, "Morris Travers, William Ramsay",
  False, "Natural", "Non-toxic", "Neon lights, cryogenics",
  3, "Natural", 0, 1,
  20.180, 10
]

# 11 to 20 elements (36 properties each)
sodium = [
    11, "Na", "Sodium", 22.98976928, "alkali metal", 1, 3, "s", "solid", 0.968,
    370.87, 1156, 0.93, 190, 116, 166, 495.8, 52.8, "+1", "[Ne] 3s1",
    "solid", "metallic", "body-centered cubic", "silvery white", 1807, "Humphry Davy",
    False, "abundant", "moderate", "soap making, street lights, metal refining",
    21, "natural", 1, 1, 22.99, 12
]

magnesium = [
    12, "Mg", "Magnesium", 24.305, "alkaline earth metal", 2, 3, "s", "solid", 1.738,
    923, 1363, 1.31, 145, 86, 141, 737.7, 0, "+2", "[Ne] 3s2",
    "solid", "metallic", "hexagonal close-packed", "silvery gray", 1808, "Humphry Davy",
    False, "abundant", "low", "alloys, flares, fireworks", 22, "natural", 2, 1, 24.31, 12
]

aluminium = [
    13, "Al", "Aluminium", 26.9815385, "post-transition metal", 13, 3, "p", "solid", 2.70,
    933.47, 2792, 1.61, 118, 53.5, 121, 577.5, 42.5, "+3", "[Ne] 3s2 3p1",
    "solid", "metallic", "face-centered cubic", "silvery gray", 1825, "Hans Ørsted",
    False, "abundant", "low", "aircraft, foil, cans", 22, "natural", 3, 1, 26.98, 14
]

silicon = [
    14, "Si", "Silicon", 28.085, "metalloid", 14, 3, "p", "solid", 2.3296,
    1687, 3538, 1.90, 111, 40, 111, 786.5, 134, "+4, -4", "[Ne] 3s2 3p2",
    "solid", "covalent network", "diamond cubic", "gray", 1824, "Jöns Jacob Berzelius",
    False, "abundant", "low", "electronics, glass, solar cells", 23, "natural", 4, 1, 28.09, 14
]

phosphorus = [
    15, "P", "Phosphorus", 30.973761998, "nonmetal", 15, 3, "p", "solid", 1.823,
    317.3, 553.7, 2.19, 98, 44, 107, 1011.8, 72, "-3, +3, +5", "[Ne] 3s2 3p3",
    "solid", "covalent", "orthorhombic", "white/red", 1669, "Hennig Brand",
    False, "abundant", "moderate", "fertilizers, matches", 23, "natural", 3, 4, 30.97, 16
]

sulfur = [
    16, "S", "Sulfur", 32.06, "nonmetal", 16, 3, "p", "solid", 2.07,
    388.36, 717.87, 2.58, 88, 37, 104, 999.6, 200, "-2, +2, +4, +6", "[Ne] 3s2 3p4",
    "solid", "covalent", "orthorhombic", "yellow", "ancient", "Unknown",
    False, "abundant", "low", "sulfuric acid, rubber vulcanization", 25, "natural", 2, 8, 32.06, 16
]

chlorine = [
    17, "Cl", "Chlorine", 35.45, "halogen", 17, 3, "p", "gas", 0.003214,
    171.6, 239.11, 3.16, 79, 181, 99, 1251.2, 349, "-1, +1, +3, +5, +7", "[Ne] 3s2 3p5",
    "gas", "covalent", "orthorhombic (solid form)", "yellow-green", 1774, "Carl Wilhelm Scheele",
    True, "common", "high", "disinfectant, PVC, bleach", 24, "natural", 1, 2, 35.45, 18
]

argon = [
    18, "Ar", "Argon", 39.948, "noble gas", 18, 3, "p", "gas", 0.001784,
    83.8, 87.3, 0, 71, 0, 106, 1520.6, 0, "0", "[Ne] 3s2 3p6",
    "gas", "atomic", "face-centered cubic (solid form)", "colorless", 1894, "Lord Rayleigh & William Ramsay",
    False, "abundant", "none", "shielding gas, lighting", 26, "natural", 0, 1, 39.95, 22
]

potassium = [
    19, "K", "Potassium", 39.0983, "alkali metal", 1, 4, "s", "solid", 0.862,
    336.53, 1032, 0.82, 243, 152, 203, 418.8, 48.4, "+1", "[Ar] 4s1",
    "solid", "metallic", "body-centered cubic", "silvery white", 1807, "Humphry Davy",
    False, "abundant", "moderate", "fertilizers, glass, soap", 26, "natural", 1, 1, 39.10, 20
]

calcium = [
    20, "Ca", "Calcium", 40.078, "alkaline earth metal", 2, 4, "s", "solid", 1.54,
    1115, 1757, 1.00, 194, 114, 174, 589.8, 2.37, "+2", "[Ar] 4s2",
    "solid", "metallic", "face-centered cubic", "silvery gray", 1808, "Humphry Davy",
    False, "abundant", "low", "bones, cement, alloys", 26, "natural", 2, 1, 40.08, 20
]

# 21 to 30 elements (36 properties each)

scandium = [
    21, "Sc", "Scandium", 44.955908, "transition metal", 3, 4, "d", "solid", 2.985,
    1814, 3109, 1.36, 184, 74.5, 144, 633.1, 18.1, "+3", "[Ar] 3d1 4s2",
    "solid", "metallic", "hexagonal close-packed", "silvery white", 1879, "Lars Fredrik Nilson",
    False, "rare", "low", "aerospace alloys, lamps", 25, "natural", 3, 1, 44.96, 24
]

titanium = [
    22, "Ti", "Titanium", 47.867, "transition metal", 4, 4, "d", "solid", 4.506,
    1941, 3560, 1.54, 176, 86, 136, 658.8, 7.6, "+2, +3, +4", "[Ar] 3d2 4s2",
    "solid", "metallic", "hexagonal close-packed", "silvery gray", 1791, "William Gregor",
    False, "abundant", "low", "aircraft, implants, pigments", 26, "natural", 4, 1, 47.87, 26
]

vanadium = [
    23, "V", "Vanadium", 50.9415, "transition metal", 5, 4, "d", "solid", 6.11,
    2183, 3680, 1.63, 171, 79, 125, 650.9, 50.6, "+2, +3, +4, +5", "[Ar] 3d3 4s2",
    "solid", "metallic", "body-centered cubic", "silvery gray", 1801, "Andrés Manuel del Río",
    False, "moderate", "medium", "steel alloys, catalysts", 24, "natural", 5, 1, 50.94, 28
]

chromium = [
    24, "Cr", "Chromium", 51.9961, "transition metal", 6, 4, "d", "solid", 7.19,
    2180, 2944, 1.66, 166, 80, 127, 652.9, 64.3, "+2, +3, +6", "[Ar] 3d5 4s1",
    "solid", "metallic", "body-centered cubic", "silvery metallic", 1797, "Louis Nicolas Vauquelin",
    False, "abundant", "high", "stainless steel, plating", 26, "natural", 6, 1, 52.00, 28
]

manganese = [
    25, "Mn", "Manganese", 54.938044, "transition metal", 7, 4, "d", "solid", 7.43,
    1519, 2334, 1.55, 161, 67, 119, 717.3, 0, "+2, +3, +4, +6, +7", "[Ar] 3d5 4s2",
    "solid", "metallic", "body-centered cubic", "gray-white", 1774, "Carl Wilhelm Scheele",
    False, "abundant", "medium", "steel, batteries, pigments", 25, "natural", 7, 1, 54.94, 30
]

iron = [
    26, "Fe", "Iron", 55.845, "transition metal", 8, 4, "d", "solid", 7.874,
    1811, 3134, 1.83, 156, 76, 125, 762.5, 15.7, "+2, +3", "[Ar] 3d6 4s2",
    "solid", "metallic", "body-centered cubic", "gray", "ancient", "Unknown",
    False, "abundant", "medium", "construction, blood (hemoglobin)", 26, "natural", 2, 1, 55.85, 30
]

cobalt = [
    27, "Co", "Cobalt", 58.933194, "transition metal", 9, 4, "d", "solid", 8.90,
    1768, 3200, 1.88, 152, 74.5, 126, 760.4, 63.7, "+2, +3", "[Ar] 3d7 4s2",
    "solid", "metallic", "hexagonal close-packed", "bluish-gray", 1735, "Georg Brandt",
    False, "moderate", "medium", "magnets, batteries, alloys", 27, "natural", 2, 1, 58.93, 32
]

nickel = [
    28, "Ni", "Nickel", 58.6934, "transition metal", 10, 4, "d", "solid", 8.908,
    1728, 3186, 1.91, 149, 69, 124, 737.1, 112, "+2, +3", "[Ar] 3d8 4s2",
    "solid", "metallic", "face-centered cubic", "silvery-white", 1751, "Axel Fredrik Cronstedt",
    False, "abundant", "medium", "coins, alloys, batteries", 28, "natural", 2, 1, 58.69, 31
]

copper = [
    29, "Cu", "Copper", 63.546, "transition metal", 11, 4, "d", "solid", 8.96,
    1357.77, 2835, 1.90, 145, 77, 132, 745.5, 118.4, "+1, +2", "[Ar] 3d10 4s1",
    "solid", "metallic", "face-centered cubic", "reddish-orange", "ancient", "Unknown",
    False, "abundant", "medium", "wiring, coins, electronics", 29, "natural", 2, 1, 63.55, 35
]

zinc = [
    30, "Zn", "Zinc", 65.38, "transition metal", 12, 4, "d", "solid", 7.14,
    692.68, 1180, 1.65, 142, 74, 122, 906.4, 0, "+2", "[Ar] 3d10 4s2",
    "solid", "metallic", "hexagonal close-packed", "bluish-silver", 1746, "Andreas Marggraf",
    False, "abundant", "low", "galvanization, alloys, supplements", 30, "natural", 2, 1, 65.38, 35
]

# 31 to 40 elements (36 properties each)

gallium = [
    31, "Ga", "Gallium", 69.723, "post-transition metal", 13, 4, "p", "solid", 5.91,
    302.91, 2477, 1.81, 136, 62, 122, 578.8, 28.9, "+1, +3", "[Ar] 3d10 4s2 4p1",
    "solid", "metallic", "orthorhombic", "silvery", 1875, "Paul Émile Lecoq de Boisbaudran",
    False, "rare", "low", "semiconductors, LEDs, thermometers", 31, "natural", 3, 2, 69.72, 39
]

germanium = [
    32, "Ge", "Germanium", 72.63, "metalloid", 14, 4, "p", "solid", 5.323,
    1211.4, 3106, 2.01, 125, 73, 120, 762, 118.9, "+2, +4", "[Ar] 3d10 4s2 4p2",
    "solid", "covalent network", "diamond cubic", "grayish-white", 1886, "Clemens Winkler",
    False, "rare", "low", "fiber optics, transistors", 32, "natural", 4, 1, 72.63, 41
]

arsenic = [
    33, "As", "Arsenic", 74.921595, "metalloid", 15, 4, "p", "solid", 5.776,
    1090, 887, 2.18, 114, 58, 119, 947, 78, "-3, +3, +5", "[Ar] 3d10 4s2 4p3",
    "solid", "covalent network", "rhombohedral", "gray", "ancient", "Unknown",
    True, "rare", "high", "pesticides, semiconductors", 33, "natural", 3, 4, 74.92, 42
]

selenium = [
    34, "Se", "Selenium", 78.971, "nonmetal", 16, 4, "p", "solid", 4.81,
    494, 958, 2.55, 103, 50, 116, 941, 195, "-2, +4, +6", "[Ar] 3d10 4s2 4p4",
    "solid", "covalent", "hexagonal", "gray/red", 1817, "Jöns Jacob Berzelius",
    False, "moderate", "medium", "glass coloring, electronics", 34, "natural", 2, 2, 78.97, 45
]

bromine = [
    35, "Br", "Bromine", 79.904, "halogen", 17, 4, "p", "liquid", 3.12,
    265.8, 331.9, 2.96, 94, 196, 114, 1139.9, 324.6, "-1, +1, +3, +5", "[Ar] 3d10 4s2 4p5",
    "liquid", "covalent", "orthorhombic (solid form)", "reddish-brown", 1826, "Antoine Jérôme Balard",
    True, "moderate", "high", "flame retardants, photography", 35, "natural", 1, 2, 79.90, 45
]

krypton = [
    36, "Kr", "Krypton", 83.798, "noble gas", 18, 4, "p", "gas", 0.003733,
    115.8, 119.9, 3.00, 88, 0, 110, 1350.8, 0, "0", "[Ar] 3d10 4s2 4p6",
    "gas", "atomic", "face-centered cubic (solid form)", "colorless", 1898, "William Ramsay & Morris Travers",
    False, "rare", "none", "lighting, lasers, insulation", 36, "natural", 0, 1, 83.80, 48
]

rubidium = [
    37, "Rb", "Rubidium", 85.4678, "alkali metal", 1, 5, "s", "solid", 1.532,
    312.46, 961, 0.82, 265, 166, 220, 403, 46.9, "+1", "[Kr] 5s1",
    "solid", "metallic", "body-centered cubic", "silvery white", 1861, "Robert Bunsen & Gustav Kirchhoff",
    True, "rare", "medium", "atomic clocks, research", 36, "natural", 1, 1, 85.47, 48
]

strontium = [
    38, "Sr", "Strontium", 87.62, "alkaline earth metal", 2, 5, "s", "solid", 2.64,
    1050, 1655, 0.95, 219, 132, 195, 549.5, 5.03, "+2", "[Kr] 5s2",
    "solid", "metallic", "face-centered cubic", "silvery", 1790, "Adair Crawford",
    False, "moderate", "medium", "fireworks, alloys, magnets", 36, "natural", 2, 1, 87.62, 50
]

yttrium = [
    39, "Y", "Yttrium", 88.90584, "transition metal", 3, 5, "d", "solid", 4.472,
    1799, 3618, 1.22, 212, 90, 162, 600, 29.6, "+3", "[Kr] 4d1 5s2",
    "solid", "metallic", "hexagonal close-packed", "silvery", 1794, "Johan Gadolin",
    False, "rare", "low", "phosphors, superconductors, lasers", 37, "natural", 3, 1, 88.91, 50
]

zirconium = [
    40, "Zr", "Zirconium", 91.224, "transition metal", 4, 5, "d", "solid", 6.52,
    2128, 4682, 1.33, 206, 86, 160, 640.1, 41.1, "+4", "[Kr] 4d2 5s2",
    "solid", "metallic", "hexagonal close-packed", "grayish-white", 1789, "Martin Heinrich Klaproth",
    False, "moderate", "low", "nuclear reactors, ceramics", 38, "natural", 4, 1, 91.22, 51
]

niobium = [41, "Nb", "Niobium", 92.906, "Transition Metal", 5, 5, "d", "Solid", 8.57, 2750, 5017, 1.6, 146, 70, 164, 652, 88, "5,4,3,2", "[Kr] 4d4 5s1", "Solid", "Metallic", "Body-Centered Cubic", "Gray", 1801, "Charles Hatchett", false, "Natural", "Low", "Steel alloys", 1, "Natural", 5, 1, 92.906, 52]

molybdenum = [42, "Mo", "Molybdenum", 95.95, "Transition Metal", 6, 5, "d", "Solid", 10.28, 2896, 4912, 2.16, 139, 70, 154, 684, 72, "6,5,4,3,2", "[Kr] 4d5 5s1", "Solid", "Metallic", "Body-Centered Cubic", "Gray", 1778, "Carl Wilhelm Scheele", false, "Natural", "Low", "Steel hardening", 1, "Natural", 6, 1, 95.95, 54]

technetium = [43, "Tc", "Technetium", 98, "Transition Metal", 7, 5, "d", "Solid", 11.5, 2430, 4538, 1.9, 136, 70, 147, 702, 53, "7,6,4", "[Kr] 4d5 5s2", "Solid", "Metallic", "Hexagonal", "Gray", 1937, "Emilio Segrè", true, "Synthetic", "Medium", "Medical tracers", 1, "Man-made", 7, 1, 98, 55]

ruthenium = [44, "Ru", "Ruthenium", 101.07, "Transition Metal", 8, 5, "d", "Solid", 12.37, 2334, 4150, 2.2, 134, 70, 146, 710, 101, "8,6,4,3,2,1", "[Kr] 4d7 5s1", "Solid", "Metallic", "Hexagonal", "Silvery", 1844, "Karl Ernst Claus", false, "Natural", "Low", "Electrical contacts", 1, "Natural", 8, 1, 101.07, 57]

rhodium = [45, "Rh", "Rhodium", 102.91, "Transition Metal", 9, 5, "d", "Solid", 12.41, 1964, 3695, 2.28, 134, 70, 142, 720, 110, "6,3,1", "[Kr] 4d8 5s1", "Solid", "Metallic", "Face-Centered Cubic", "Silvery-white", 1803, "William Hyde Wollaston", false, "Natural", "Low", "Catalyst, jewelry", 1, "Natural", 3, 1, 102.91, 58]

palladium = [46, "Pd", "Palladium", 106.42, "Transition Metal", 10, 5, "d", "Solid", 12.02, 1554, 2963, 2.2, 139, 70, 139, 804, 54, "4,2,0", "[Kr] 4d10", "Solid", "Metallic", "Face-Centered Cubic", "Silvery", 1803, "William Hyde Wollaston", false, "Natural", "Low", "Catalyst, hydrogen storage", 1, "Natural", 2, 1, 106.42, 60]

silver = [47, "Ag", "Silver", 107.87, "Transition Metal", 11, 5, "d", "Solid", 10.49, 961.8, 2162, 1.93, 144, 115, 145, 731, 125, "2,1", "[Kr] 4d10 5s1", "Solid", "Metallic", "Face-Centered Cubic", "Silvery-white", "Ancient", "Unknown", false, "Natural", "Low", "Jewelry, coins", 2, "Natural", 1, 1, 107.87, 61]

cadmium = [48, "Cd", "Cadmium", 112.41, "Transition Metal", 12, 5, "d", "Solid", 8.65, 321, 767, 1.69, 151, 95, 144, 868, 0, "2", "[Kr] 4d10 5s2", "Solid", "Metallic", "Hexagonal", "Silvery-blue", 1817, "Karl Hermann", false, "Natural", "High", "Batteries, pigments", 1, "Natural", 2, 1, 112.41, 64]

indium = [49, "In", "Indium", 114.82, "Post-Transition Metal", 13, 5, "p", "Solid", 7.31, 156.6, 2072, 1.78, 167, 95, 142, 558, 28, "3,2,1", "[Kr] 4d10 5s2 5p1", "Solid", "Metallic", "Tetragonal", "Silvery-gray", 1863, "Ferdinand Reich", false, "Natural", "Low", "Touchscreens, semiconductors", 1, "Natural", 3, 1, 114.82, 66]

tin = [50, "Sn", "Tin", 118.71, "Post-Transition Metal", 14, 5, "p", "Solid", 7.31, 231.9, 2602, 1.96, 145, 93, 139, 708, 107, "4,2", "[Kr] 4d10 5s2 5p2", "Solid", "Metallic", "Tetragonal", "Silvery-white", "Ancient", "Unknown", false, "Natural", "Low", "Cans, alloys", 2, "Natural", 4, 2, 118.71, 69]

antimony = [51, "Sb", "Antimony", 121.76, "Metalloid", 15, 5, "p", "Solid", 6.697, 630.6, 1587, 2.05, 133, 76, 139, 834, 103, "5,3,-3", "[Kr] 4d10 5s2 5p3", "Solid", "Metallic", "Rhombohedral", "Silvery-gray", "Ancient", "Unknown", false, "Natural", "Medium", "Flame retardants, alloys", 2, "Natural", 3, 2, 121.76, 71]

tellurium = [52, "Te", "Tellurium", 127.60, "Metalloid", 16, 5, "p", "Solid", 6.24, 449.5, 988, 2.1, 123, 221, 138, 869, 190, "6,4,-2", "[Kr] 4d10 5s2 5p4", "Solid", "Covalent", "Hexagonal", "Silvery-white", 1782, "Franz Müller von Reichenstein", false, "Natural", "Medium", "Solar panels, metallurgy", 1, "Natural", 2, 2, 127.60, 76]

iodine = [53, "I", "Iodine", 126.90, "Halogen", 17, 5, "p", "Solid", 4.93, 113.7, 184.3, 2.66, 115, 220, 133, 1008, 295, "-1,1,3,5,7", "[Kr] 4d10 5s2 5p5", "Solid", "Covalent", "Orthorhombic", "Violet", 1811, "Bernard Courtois", false, "Natural", "Medium", "Medicine, photography", 1, "Natural", 1, 2, 126.90, 74]

xenon = [54, "Xe", "Xenon", 131.29, "Noble Gas", 18, 5, "p", "Gas", 0.005887, 161.4, 165.1, "–", "–", "–", "–", 1170, "–", "0,2,4,6,8", "[Kr] 4d10 5s2 5p6", "Gas", "Van der Waals", "Face-Centered Cubic", "Colorless", 1898, "William Ramsay", false, "Natural", "Low", "Lighting, anesthesia", 9, "Natural", 0, 1, 131.29, 77]

cesium = [55, "Cs", "Cesium", 132.91, "Alkali Metal", 1, 6, "s", "Solid", 1.93, 28.4, 671, 0.79, 262, 167, 244, 376, 45, "1", "[Xe] 6s1", "Solid", "Metallic", "Body-Centered Cubic", "Gold", 1860, "Robert Bunsen", false, "Natural", "High", "Atomic clocks, photoelectric cells", 1, "Natural", 1, 1, 132.91, 78]

barium = [56, "Ba", "Barium", 137.33, "Alkaline Earth Metal", 2, 6, "s", "Solid", 3.51, 727, 1870, 0.89, 222, 135, 215, 503, 14, "2", "[Xe] 6s2", "Solid", "Metallic", "Body-Centered Cubic", "Silvery-white", 1808, "Humphry Davy", false, "Natural", "High", "X-ray imaging, glassmaking", 7, "Natural", 2, 1, 137.33, 81]

lanthanum = [57, "La", "Lanthanum", 138.91, "Lanthanide", 3, 6, "d", "Solid", 6.15, 920, 3464, 1.1, 187, 103, 207, 538, 48, "3", "[Xe] 5d1 6s2", "Solid", "Metallic", "Hexagonal", "Silvery-white", 1839, "Carl Gustaf Mosander", false, "Natural", "Low", "Optics, catalysts", 1, "Natural", 3, 2, 138.91, 82]

cerium = [58, "Ce", "Cerium", 140.12, "Lanthanide", 4, 6, "f", "Solid", 6.77, 798, 3443, 1.12, 181, 103, 204, 534, 50, "4,3", "[Xe] 4f1 5d1 6s2", "Solid", "Metallic", "Face-Centered Cubic", "Silvery", 1803, "Jöns Jakob Berzelius", false, "Natural", "Medium", "Alloys, glass polishing", 4, "Natural", 4, 2, 140.12, 82]

praseodymium = [59, "Pr", "Praseodymium", 140.91, "Lanthanide", 5, 6, "f", "Solid", 6.77, 931, 3520, 1.13, 182, 99, 203, 527, 50, "3,4", "[Xe] 4f3 6s2", "Solid", "Metallic", "Hexagonal", "Gray", 1885, "Carl Auer von Welsbach", false, "Natural", "Medium", "Magnets, glasses", 1, "Natural", 3, 2, 140.91, 82]

neodymium = [60, "Nd", "Neodymium", 144.24, "Lanthanide", 6, 6, "f", "Solid", 7.01, 1010, 3074, 1.14, 182, 99, 201, 533, 50, "3", "[Xe] 4f4 6s2", "Solid", "Metallic", "Hexagonal", "Silvery-white", 1885, "Carl Auer von Welsbach", false, "Natural", "Medium", "Magnets, lasers", 7, "Natural", 3, 2, 144.24, 84]

promethium = [61, "Pm", "Promethium", 145, "Lanthanide", 7, 6, "f", "Solid", 7.26, 1315, 3273, 1.13, 183, 99, 199, 540, 12, "3", "[Xe] 4f5 6s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1945, "Jacob A. Marinsky", true, "Synthetic", "High", "Nuclear batteries, research", 1, "Man-made", 3, 2, 145, 84]

samarium = [62, "Sm", "Samarium", 150.36, "Lanthanide", 8, 6, "f", "Solid", 7.52, 1345, 2076, 1.17, 180, 98, 198, 544, 23, "2,3", "[Xe] 4f6 6s2", "Solid", "Metallic", "Rhombohedral", "Silvery-white", 1879, "Paul Émile Lecoq de Boisbaudran", false, "Natural", "Medium", "Magnets, reactors", 7, "Natural", 3, 2, 150.36, 88]

europium = [63, "Eu", "Europium", 151.96, "Lanthanide", 9, 6, "f", "Solid", 5.24, 1099, 1802, 1.2, 199, 109, 198, 547, 11, "2,3", "[Xe] 4f7 6s2", "Solid", "Metallic", "Body-Centered Cubic", "Silvery-white", 1901, "Eugène-Anatole Demarçay", false, "Natural", "Medium", "Phosphors, electronics", 2, "Natural", 2, 2, 151.96, 89]

gadolinium = [64, "Gd", "Gadolinium", 157.25, "Lanthanide", 10, 6, "f", "Solid", 7.90, 1585, 3546, 1.2, 180, 93.8, 196, 593, 13, "3", "[Xe] 4f7 5d1 6s2", "Solid", "Metallic", "Hexagonal", "Silvery-white", 1880, "Jean Charles Galissard de Marignac", false, "Natural", "Low", "Magnets, MRI contrast", 7, "Natural", 3, 2, 157.25, 93]

terbium = [65, "Tb", "Terbium", 158.93, "Lanthanide", 11, 6, "f", "Solid", 8.23, 1629, 3503, 1.2, 177, 92.3, 194, 565, 13, "3,4", "[Xe] 4f9 6s2", "Solid", "Metallic", "Hexagonal", "Silvery-gray", 1843, "Carl Gustaf Mosander", false, "Natural", "Low", "Phosphors, magnets", 5, "Natural", 3, 2, 158.93, 94]

dysprosium = [66, "Dy", "Dysprosium", 162.50, "Lanthanide", 12, 6, "f", "Solid", 8.55, 1680, 2840, 1.22, 178, 91.2, 192, 573, 13, "3", "[Xe] 4f10 6s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1886, "Paul Émile Lecoq de Boisbaudran", false, "Natural", "Medium", "Magnets, lasers", 7, "Natural", 3, 2, 162.50, 97]

holmium = [67, "Ho", "Holmium", 164.93, "Lanthanide", 13, 6, "f", "Solid", 8.79, 1734, 2873, 1.23, 176, 90.1, 192, 581, 33, "3", "[Xe] 4f11 6s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1878, "Per Teodor Cleve", false, "Natural", "Medium", "Magnets, lasers", 6, "Natural", 3, 2, 164.93, 98]

erbium = [68, "Er", "Erbium", 167.26, "Lanthanide", 14, 6, "f", "Solid", 9.07, 1802, 3141, 1.24, 175, 89, 189, 589, 30, "3", "[Xe] 4f12 6s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1843, "Carl Gustaf Mosander", false, "Natural", "Low", "Fiber optics, lasers", 6, "Natural", 3, 2, 167.26, 99]

thulium = [69, "Tm", "Thulium", 168.93, "Lanthanide", 15, 6, "f", "Solid", 9.32, 1818, 2223, 1.25, 174, 88, 190, 597, 30, "3", "[Xe] 4f13 6s2", "Solid", "Metallic", "Hexagonal", "Silvery-gray", 1879, "Per Teodor Cleve", false, "Natural", "Low", "Lasers, X-ray sources", 2, "Natural", 3, 2, 168.93, 99]

ytterbium = [70, "Yb", "Ytterbium", 173.05, "Lanthanide", 16, 6, "f", "Solid", 6.90, 1097, 1469, 1.1, 194, 102, 187, 603, 30, "2,3", "[Xe] 4f14 6s2", "Solid", "Metallic", "Face-Centered Cubic", "Silvery-white", 1878, "Jean Charles Galissard de Marignac", false, "Natural", "Low", "Optics, alloys", 7, "Natural", 2, 2, 173.05, 103]

lutetium = [71, "Lu", "Lutetium", 174.97, "Lanthanide", 17, 6, "d", "Solid", 9.84, 1925, 3675, 1.27, 173, 86.1, 187, 523, 20, "3", "[Xe] 4f14 5d1 6s2", "Solid", "Metallic", "Hexagonal Close-Packed", "Silvery-white", 1907, "Georges Urbain", false, "Natural", "Low", "Catalysts, PET scanners", 2, "Natural", 3, 2, 174.97, 104]

hafnium = [72, "Hf", "Hafnium", 178.49, "Transition Metal", 4, 6, "d", "Solid", 13.31, 2506, 4876, 1.3, 159, 78, 175, 658.5, 0, "4", "[Xe] 4f14 5d2 6s2", "Solid", "Metallic", "Hexagonal Close-Packed", "Silvery-gray", 1923, "Dirk Coster", false, "Natural", "Low", "Nuclear control rods, alloys", 6, "Natural", 4, 2, 178.49, 106]

tantalum = [73, "Ta", "Tantalum", 180.95, "Transition Metal", 5, 6, "d", "Solid", 16.69, 3290, 5731, 1.5, 146, 72, 170, 761, 31, "5", "[Xe] 4f14 5d3 6s2", "Solid", "Metallic", "Body-Centered Cubic", "Gray", 1802, "Anders Gustaf Ekeberg", false, "Natural", "Low", "Capacitors, surgical tools", 5, "Natural", 5, 2, 180.95, 108]

tungsten = [74, "W", "Tungsten", 183.84, "Transition Metal", 6, 6, "d", "Solid", 19.25, 3695, 5828, 2.36, 139, 66, 162, 770, 78.6, "6,5,4,3,2,0,-1,-2,-4", "[Xe] 4f14 5d4 6s2", "Solid", "Metallic", "Body-Centered Cubic", "Grayish-white", 1783, "Fausto and Juan José Elhuyar", false, "Natural", "Low", "Filaments, tools", 5, "Natural", 6, 2, 183.84, 110]

rhenium = [75, "Re", "Rhenium", 186.21, "Transition Metal", 7, 6, "d", "Solid", 21.02, 3459, 5869, 1.9, 137, 63, 151, 760, 14.5, "7,6,4,2,-1", "[Xe] 4f14 5d5 6s2", "Solid", "Metallic", "Hexagonal Close-Packed", "Silvery-gray", 1925, "Masataka Ogawa", false, "Natural", "Low", "Thermocouples, alloys", 2, "Natural", 7, 2, 186.21, 111]

osmium = [76, "Os", "Osmium", 190.23, "Transition Metal", 8, 6, "d", "Solid", 22.59, 3306, 5285, 2.2, 135, 63, 144, 840, 106, "8,6,4,3,2,0,-2", "[Xe] 4f14 5d6 6s2", "Solid", "Metallic", "Hexagonal Close-Packed", "Bluish-white", 1803, "Smithson Tennant", false, "Natural", "High", "Pen tips, alloys", 7, "Natural", 8, 2, 190.23, 114]

iridium = [77, "Ir", "Iridium", 192.22, "Transition Metal", 9, 6, "d", "Solid", 22.56, 2739, 4701, 2.2, 136, 68, 141, 880, 151, "6,4,3,2,1,0,-1,-3", "[Xe] 4f14 5d7 6s2", "Solid", "Metallic", "Face-Centered Cubic", "Silvery-white", 1803, "Smithson Tennant", false, "Natural", "Medium", "Spark plugs, crucibles", 3, "Natural", 6, 2, 192.22, 115]

platinum = [78, "Pt", "Platinum", 195.08, "Transition Metal", 10, 6, "d", "Solid", 21.45, 2041, 4098, 2.28, 139, 86, 136, 870, 205, "6,5,4,3,2,0,-1,-2", "[Xe] 4f14 5d9 6s1", "Solid", "Metallic", "Face-Centered Cubic", "Silvery-white", "Ancient", "Unknown", false, "Natural", "Low", "Jewelry, catalysts", 6, "Natural", 6, 2, 195.08, 117]

gold = [79, "Au", "Gold", 196.97, "Transition Metal", 11, 6, "d", "Solid", 19.3, 1337.33, 3129, 2.54, 144, 137, 136, 890.1, 222.8, "3,1", "[Xe] 4f14 5d10 6s1", "Solid", "Metallic", "Face-Centered Cubic", "Metallic yellow", "Ancient", "Unknown", false, "Natural", "Low", "Jewelry, electronics", 3, "Natural", 3, 1, 196.97, 118]

mercury = [80, "Hg", "Mercury", 200.59, "Transition Metal", 12, 6, "d", "Liquid", 13.534, 234.32, 629.88, 2.0, 151, 119, 132, 1007.1, 0, "2,1", "[Xe] 4f14 5d10 6s2", "Liquid", "Metallic", "Rhombohedral", "Silvery", "Ancient", "Unknown", true, "Natural", "High", "Thermometers, lamps", 7, "Natural", 2, 1, 200.59, 121]

thallium = [81, "Tl", "Thallium", 204.38, "Post-transition metal", 13, 6, "p", "Solid", 11.85, 577, 1746, 1.62, 156, "Unknown", 145, 589.4, 36.4, "+1, +3", "[Xe] 4f14 5d10 6s2 6p1", "Solid", "Metallic", "Hexagonal", "Silvery gray", 1861, "William Crookes", false, "Natural", "Moderate", "Alloys, electronics", "Tl-203, Tl-205", "Natural", 3, 2, 204.38, 123]

lead = [82, "Pb", "Lead", 207.2, "Post-transition metal", 14, 6, "p", "Solid", 11.34, 600.6, 2022, 2.33, 154, "Unknown", 144, 715.6, 35.1, "+2, +4", "[Xe] 4f14 5d10 6s2 6p2", "Solid", "Metallic", "Cubic", "Bluish gray", "Ancient", "Prehistoric", false, "Natural", "Toxic", "Batteries, radiation shielding", "Pb-204, Pb-206, Pb-207, Pb-208", "Natural", 4, 1, 207.2, 125]

bismuth = [83, "Bi", "Bismuth", 208.98, "Post-transition metal", 15, 6, "p", "Solid", 9.78, 544.7, 1837, 2.02, 143, "Unknown", 146, 703, 90.9, "+3, +5", "[Xe] 4f14 5d10 6s2 6p3", "Solid", "Metallic", "Rhombohedral", "Silvery pink", 1753, "Claude Geoffroy the Younger", false, "Natural", "Low", "Cosmetics, medicines, alloys", "Bi-209", "Natural", 3, 2, 208.98, 126]

polonium = [84, "Po", "Polonium", 209, "Metalloid", 16, 6, "p", "Solid", 9.32, 527, 1235, 2.0, 135, "Unknown", 146, 812.1, 183.3, "+2, +4, +6", "[Xe] 4f14 5d10 6s2 6p4", "Solid", "Metallic", "Simple cubic", "Silvery gray", 1898, "Marie Curie", true, "Natural", "Highly toxic", "Antistatic devices, heat sources", "Po-210", "Natural", 2, 2, 209, 125]

astatine = [85, "At", "Astatine", 210, "Halogen", 17, 6, "p", "Solid", "Unknown", 575, 610, 2.2, 127, "Unknown", 140, 899.0, 270.1, "-1, +1, +3, +5, +7", "[Xe] 4f14 5d10 6s2 6p5", "Solid", "Covalent", "Orthorhombic", "Black", 1940, "Dale R. Corson", true, "Natural", "Highly toxic", "Scientific research", "At-210", "Natural", 1, 2, 210, 125]

radon = [86, "Rn", "Radon", 222, "Noble gas", 18, 6, "p", "Gas", 0.00973, 202, 211.3, "Unknown", "Unknown", "Unknown", "Unknown", 1037.0, "Unknown", "0", "[Xe] 4f14 5d10 6s2 6p6", "Gas", "Atomic", "Cubic", "Colorless", 1900, "Friedrich Dorn", true, "Natural", "Highly toxic", "Radiation research", "Rn-222", "Natural", 0, 1, 222, 136]

francium = [87, "Fr", "Francium", 223, "Alkali metal", 1, 7, "s", "Solid", "Unknown", 300, "Unknown", 0.7, 260, "Unknown", 260, 380.0, 45.5, "+1", "[Rn] 7s1", "Solid", "Metallic", "Cubic", "Silver", 1939, "Marguerite Perey", true, "Natural", "Highly toxic", "Research", "Fr-223", "Natural", 1, 1, 223, 136]

radium = [88, "Ra", "Radium", 226, "Alkaline earth metal", 2, 7, "s", "Solid", 5.5, 973, 2010, 0.9, 215, "Unknown", 221, 509.3, 9.65, "+2", "[Rn] 7s2", "Solid", "Metallic", "Cubic", "Silvery white", 1898, "Marie and Pierre Curie", true, "Natural", "Highly toxic", "Luminous paints, research", "Ra-226", "Natural", 2, 1, 226, 138]

actinium = [89, "Ac", "Actinium", 227, "Actinide", 3, 7, "f", "Solid", 10.07, 1324, 3471, 1.1, 195, "Unknown", 215, 499, 33.77, "+3", "[Rn] 6d1 7s2", "Solid", "Metallic", "Cubic", "Silvery", 1899, "André Debierne", true, "Natural", "Moderate", "Radiotherapy, research", "Ac-227", "Natural", 3, 2, 227, 138]

thorium = [90, "Th", "Thorium", 232.04, "Actinide", 4, 7, "f", "Solid", 11.72, 2115, 5061, 1.3, 180, "Unknown", 206, 587, 112, "+4", "[Rn] 6d2 7s2", "Solid", "Metallic", "Cubic", "Silvery", 1828, "Jöns Jakob Berzelius", true, "Natural", "Low", "Nuclear fuel", "Th-232", "Natural", 4, 1, 232.04, 142]

protactinium = [91, "Pa", "Protactinium", 231.04, "Actinide", 5, 7, "f", "Solid", 15.37, 1845, 4300, 1.5, 163, "–", 200, 568, 53, "+3, +4, +5", "[Rn] 5f2 6d1 7s2", "Solid", "Metallic", "Tetragonal", "Silvery gray", 1913, "Oswald Helmuth Göhring, Kasimir Fajans", true, "Natural", "Toxic", "Research, nuclear fuel", "Pa-231", "Natural", 5, 2, 231.04, 140]

uranium = [92, "U", "Uranium", 238.03, "Actinide", 6, 7, "f", "Solid", 19.1, 1405.3, 4404, 1.38, 175, "–", 196, 597.6, 50.9, "+3, +4, +5, +6", "[Rn] 5f3 6d1 7s2", "Solid", "Metallic", "Orthorhombic", "Silvery gray", 1789, "Martin Heinrich Klaproth", true, "Natural", "Highly toxic", "Nuclear fuel, weapons", "U-235, U-238", "Natural", 6, 1, 238.03, 146]

neptunium = [93, "Np", "Neptunium", 237, "Actinide", 7, 7, "f", "Solid", 20.45, 912, 4175, 1.36, 175, "–", 190, 604.5, 45.85, "+3, +4, +5, +6, +7", "[Rn] 5f4 6d1 7s2", "Solid", "Metallic", "Orthorhombic", "Silvery", 1940, "Edwin McMillan, Philip Abelson", true, "Man-made", "Highly toxic", "Nuclear research", "Np-237", "Man-made", 7, 2, 237, 144]

plutonium = [94, "Pu", "Plutonium", 244, "Actinide", 8, 7, "f", "Solid", 19.84, 913, 3505, 1.28, 175, "–", 187, 584.7, 101.3, "+3, +4, +5, +6, +7", "[Rn] 5f6 7s2", "Solid", "Metallic", "Monoclinic", "Silvery gray", 1940, "Glenn T. Seaborg", true, "Man-made", "Highly toxic", "Nuclear weapons, energy", "Pu-239, Pu-244", "Man-made", 6, 2, 244, 150]

americium = [95, "Am", "Americium", 243, "Actinide", 9, 7, "f", "Solid", 12, 1449, 2880, 1.3, 173, "–", 180, 578, 233, "+2, +3, +4, +5, +6", "[Rn] 5f7 7s2", "Solid", "Metallic", "Hexagonal", "Silvery white", 1944, "Glenn T. Seaborg", true, "Man-made", "Highly toxic", "Smoke detectors, research", "Am-241", "Man-made", 3, 2, 243, 148]

curium = [96, "Cm", "Curium", 247, "Actinide", 10, 7, "f", "Solid", 13.51, 1613, 3383, 1.3, 170, "–", 175, 581, 27.3, "+3, +4, +6", "[Rn] 5f7 6d1 7s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1944, "Glenn T. Seaborg", true, "Man-made", "Highly toxic", "Research", "Cm-244", "Man-made", 3, 2, 247, 151]

berkelium = [97, "Bk", "Berkelium", 247, "Actinide", 11, 7, "f", "Solid", 14.78, 1259, 2900, 1.3, 170, "–", 170, 601, 9.5, "+3, +4", "[Rn] 5f9 7s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1949, "Glenn T. Seaborg", true, "Man-made", "Highly toxic", "Research", "Bk-247", "Man-made", 3, 2, 247, 150]

californium = [98, "Cf", "Californium", 251, "Actinide", 12, 7, "f", "Solid", 15.1, 1173, 1743, 1.3, 170, "–", 170, 608, 10.5, "+2, +3, +4", "[Rn] 5f10 7s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1950, "Stanley Thompson, Glenn Seaborg", true, "Man-made", "Highly toxic", "Neutron source", "Cf-252", "Man-made", 3, 2, 251, 153]

einsteinium = [99, "Es", "Einsteinium", 252, "Actinide", 13, 7, "f", "Solid", 8.84, 1133, "–", 1.3, 170, "–", 170, 619, 12.3, "+2, +3", "[Rn] 5f11 7s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1952, "Albert Ghiorso", true, "Man-made", "Highly toxic", "Scientific research", "Es-253", "Man-made", 3, 2, 252, 153]

fermium = [100, "Fm", "Fermium", 257, "Actinide", 14, 7, "f", "Solid", "–", 1800, "–", 1.3, 170, "–", 170, 627, 33.96, "+2, +3", "[Rn] 5f12 7s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1952, "Albert Ghiorso", true, "Man-made", "Highly toxic", "Research", "Fm-257", "Man-made", 3, 2, 257, 157]

mendelevium = [101, "Md", "Mendelevium", 258, "Actinide", 15, 7, "f", "Solid", "–", 1100, "–", 1.3, 170, "–", 170, 635, 93.91, "+2, +3", "[Rn] 5f13 7s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1955, "Albert Ghiorso", true, "Man-made", "Highly toxic", "Scientific research", "Md-258", "Man-made", 3, 2, 258, 157]

nobelium = [102, "No", "Nobelium", 259, "Actinide", 16, 7, "f", "Solid", "–", 1100, "–", 1.3, 170, "–", 170, 642, 69.4, "+2, +3", "[Rn] 5f14 7s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1958, "Albert Ghiorso", true, "Man-made", "Highly toxic", "Scientific research", "No-259", "Man-made", 2, 2, 259, 157]

lawrencium = [103, "Lr", "Lawrencium", 266, "Actinide", 17, 7, "d", "Solid", "–", 1900, "–", 1.3, 161, "–", 160, 470, 30.04, "+3", "[Rn] 5f14 7s2 7p1", "Solid", "Metallic", "Hexagonal", "Silvery", 1961, "Albert Ghiorso", true, "Man-made", "Highly toxic", "Scientific research", "Lr-262", "Man-made", 3, 2, 266, 163]

rutherfordium = [104, "Rf", "Rutherfordium", 267, "Transition metal", 4, 7, "d", "Solid", 23.2, 2400, 5800, 1.3, 150, "–", 157, 580, 66.6, "+4", "[Rn] 5f14 6d2 7s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1969, "Albert Ghiorso", true, "Man-made", "Highly toxic", "Research", "Rf-267", "Man-made", 4, 1, 267, 163]

dubnium = [105, "Db", "Dubnium", 270, "Transition metal", 5, 7, "d", "Solid", "–", 2430, "–", 1.3, 149, "–", 153, 664, 33.96, "+5", "[Rn] 5f14 6d3 7s2", "Solid", "Metallic", "Body-centered cubic", "Silvery", 1967, "Joint Institute for Nuclear Research", true, "Man-made", "Highly toxic", "Scientific research", "Db-268", "Man-made", 5, 2, 270, 165]

seaborgium = [106, "Sg", "Seaborgium", 271, "Transition metal", 6, 7, "d", "Solid", "–", 2830, "–", 1.3, 143, "–", 150, 757, 35, "+6", "[Rn] 5f14 6d4 7s2", "Solid", "Metallic", "Body-centered cubic", "Silvery", 1974, "Albert Ghiorso", true, "Man-made", "Highly toxic", "Scientific research", "Sg-271", "Man-made", 6, 2, 271, 165]

bohrium = [107, "Bh", "Bohrium", 270, "Transition metal", 7, 7, "d", "Solid", "–", 2650, "–", 1.3, 141, "–", 147, 740, 36, "+7", "[Rn] 5f14 6d5 7s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1981, "Peter Armbruster, Gottfried Münzenberg", true, "Man-made", "Highly toxic", "Scientific research", "Bh-270", "Man-made", 7, 2, 270, 163]

hassium = [108, "Hs", "Hassium", 277, "Transition metal", 8, 7, "d", "Solid", 27.0, 1260, "–", 1.3, 134, "–", 143, 733, 41, "+8", "[Rn] 5f14 6d6 7s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1984, "Peter Armbruster, Gottfried Münzenberg", true, "Man-made", "Highly toxic", "Scientific research", "Hs-277", "Man-made", 8, 2, 277, 169]

meitnerium = [109, "Mt", "Meitnerium", 278, "Transition metal", 9, 7, "d", "Solid", "–", 1100, "–", 1.3, 129, "–", 140, 800, 36.4, "+9", "[Rn] 5f14 6d7 7s2", "Solid", "Metallic", "Hexagonal", "Silvery", 1982, "Gesellschaft für Schwerionenforschung", true, "Man-made", "Highly toxic", "Scientific research", "Mt-278", "Man-made", 9, 2, 278, 169]

darmstadtium = [110, "Ds", "Darmstadtium", 281, "Transition metal", 10, 7, "d", "Solid", "–", 1100, "–", 1.3, 128, "–", 137, 800, 36.4, "+6, +8", "[Rn] 5f14 6d9 7s1", "Solid", "Metallic", "Hexagonal", "Silvery", 1994, "Gesellschaft für Schwerionenforschung", true, "Man-made", "Highly toxic", "Scientific research", "Ds-281", "Man-made", 8, 2, 281, 171]

darmstadtium = [110, "Ds", "Darmstadtium", 281, "Transition Metal", 10, 7, "d", "Solid (predicted)", "–", "–", "–", "–", "–", "–", "–", "–", "–", "+8,+6,+4,+2,0", "[Rn] 5f14 6d8 7s2", "Predicted Solid", "Metallic", "Body-Centered Cubic", "Unknown", 1994, "GSI Helmholtz Centre", false, "Synthetic", "Extremely High", "Scientific research", 9, "Synthetic", 0, 1, 281, 77]

roentgenium = [111, "Rg", "Roentgenium", 282, "Transition Metal", 11, 7, "d", "Solid (predicted)", "–", "–", "–", "–", "–", "–", "–", "–", "–", "+5,+3,+1", "[Rn] 5f14 6d9 7s2", "Predicted Solid", "Metallic", "Body-Centered Cubic", "Unknown", 1994, "GSI Helmholtz Centre", false, "Synthetic", "Extremely High", "Scientific research", 9, "Synthetic", 0, 1, 282, 77]

copernicium = [112, "Cn", "Copernicium", 285, "Transition Metal", 12, 7, "d", "Gas (predicted)", "–", "–", "–", "–", "–", "–", "–", "–", "–", "+4,+2,0", "[Rn] 5f14 6d10 7s2", "Predicted Gas", "Unknown", "Hexagonal Close-Packed", "Colorless (predicted)", 1996, "GSI Helmholtz Centre", false, "Synthetic", "Extremely High", "Scientific research", 9, "Synthetic", 0, 1, 285, 77]

nihonium = [113, "Nh", "Nihonium", 286, "Post-Transition Metal", 13, 7, "p", "Solid (predicted)", "–", "–", "–", "–", "–", "–", "–", "–", "–", "+3,+1", "[Rn] 5f14 6d10 7s2 7p1", "Predicted Solid", "Metallic", "Hexagonal", "Unknown", 2003, "RIKEN, Japan", false, "Synthetic", "Extremely High", "Scientific research", 9, "Synthetic", 0, 1, 286, 77]

flerovium = [114, "Fl", "Flerovium", 289, "Post-Transition Metal", 14, 7, "p", "Solid (predicted)", "–", "–", "–", "–", "–", "–", "–", "–", "–", "+4,+2", "[Rn] 5f14 6d10 7s2 7p2", "Predicted Solid", "Metallic", "Face-Centered Cubic", "Unknown", 1998, "Joint Institute for Nuclear Research", false, "Synthetic", "Extremely High", "Scientific research", 9, "Synthetic", 0, 1, 289, 77]

moscovium = [115, "Mc", "Moscovium", 290, "Post-Transition Metal", 15, 7, "p", "Solid (predicted)", "–", "–", "–", "–", "–", "–", "–", "–", "–", "+3,+1", "[Rn] 5f14 6d10 7s2 7p3", "Predicted Solid", "Metallic", "Simple Cubic", "Unknown", 2003, "Joint Institute for Nuclear Research", false, "Synthetic", "Extremely High", "Scientific research", 9, "Synthetic", 0, 1, 290, 77]

livermorium = [116, "Lv", "Livermorium", 293, "Post-Transition Metal", 16, 7, "p", "Solid (predicted)", "–", "–", "–", "–", "–", "–", "–", "–", "–", "+4,+2", "[Rn] 5f14 6d10 7s2 7p4", "Predicted Solid", "Metallic", "Simple Cubic", "Unknown", 2000, "Joint Institute for Nuclear Research", false, "Synthetic", "Extremely High", "Scientific research", 9, "Synthetic", 0, 1, 293, 77]

tennessine = [117, "Ts", "Tennessine", 294, "Halogen", 17, 7, "p", "Solid (predicted)", "–", "–", "–", "–", "–", "–", "–", "–", "–", "−1,+1,+3,+5,+7", "[Rn] 5f14 6d10 7s2 7p5", "Predicted Solid", "Nonmetallic", "Orthorhombic", "Unknown", 2010, "Joint Institute for Nuclear Research", false, "Synthetic", "Extremely High", "Scientific research", 9, "Synthetic", 0, 1, 294, 77]

oganesson = [118, "Og", "Oganesson", 294, "Noble Gas", 18, 7, "p", "Gas (predicted)", "–", "–", "–", "–", "–", "–", "–", "–", "–", "0", "[Rn] 5f14 6d10 7s2 7p6", "Predicted Gas", "Van der Waals", "Cubic", "Unknown", 2002, "Joint Institute for Nuclear Research", false, "Synthetic", "Extremely High", "Scientific research", 9, "Synthetic", 0, 1, 294, 77]

ununennium = [
    119, "Uue", "Ununennium", 315, "Alkali Metal",
    1, 8, "s", "Solid (predicted)", "–",
    "–", "–", "–", "–",
    "–", "–", "–", "–",
    "+1", "[Og] 8s1", "Predicted Solid", "Metallic",
    "Body-Centered Cubic", "Unknown", "Not yet synthesized", "Predicted",
    "Synthetic", "Extremely High", "Theoretical element", "Theoretical research",
    "Synthetic", 0, 1, 1,
    315, 196
]

unbinilium = [
    120, "Ubn", "Unbinilium", 320, "Alkaline Earth Metal",
    2, 8, "s", "Solid (predicted)", "–",
    "–", "–", "–", "–",
    "–", "–", "–", "–",
    "+2", "[Og] 8s2", "Predicted Solid", "Metallic",
    "Body-Centered Cubic", "Unknown", "Not yet synthesized", "Predicted",
    "Synthetic", "Extremely High", "Theoretical element", "Theoretical research",
    "Synthetic", 0, 2, 1,
    320, 200
]


"""The information above may or may not be accurate. So, verify before using."""



# Add more elements as arrays here...

# Combine into dictionaries
elements = []
for values in [hydrogen, helium, lithium, beryllium, boron, carbon, nitrogen, oxygen, fluorine, neon, sodium, magnesium, aluminium, silicon, phosphorus, sulfur, chlorine, argon, potassium, calcium, scandium, titanium, vanadium, chromium, manganese, iron, cobalt, nickel, copper, zinc, gallium, germanium, arsenic, selenium, bromine, krypton, rubidium, strontium, yttrium, zirconium, niobium, molybdenum, technetium, ruthenium, rhodium, palladium, silver, cadmium, indium, tin, antimony, tellurium, iodine, xenon, cesium, barium, lanthanum, cerium, praseodymium, neodymium, promethium, samarium, europium, gadolinium, terbium, dysprosium, holmium, erbium, thulium, ytterbium, lutetium, hafnium, tantalum, tungsten, rhenium, osmium, iridium, platinum, gold, mercury, thallium, lead, bismuth, polonium, astatine, radon, francium, radium, actinium, thorium, protactinium, uranium, neptunium, plutonium, americium, curium, berkelium, californium, einsteinium, fermium, mendelevium, nobelium, lawrencium, rutherfordium, dubnium, seaborgium, bohrium, hassium, meitnerium, darmstadtium, roentgenium, copernicium, nihonium, flerovium, moscovium, livermorium, tennessine, oganesson, ununennium, unbinilium]:
    element = dict(zip(keys, values))
    elements.append(element)

# Export to JSON
with open("elements.json", "w") as f:
    json.dump(elements, f, indent=2)

print("elements.json generated with", len(elements), "elements")


