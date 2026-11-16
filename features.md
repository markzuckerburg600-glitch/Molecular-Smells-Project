| Node (Atom properties)                                                                                                                                                                                                                             | Edge (Bond properties)                            | Global (Molecule properties)                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Atomic Mass (Normalized)                                                                                                                                                                                                                           | Bond type (single, double triple, aromatic (1.5)) | \# of single bond                                                                                               |
| Degree (# of atoms it’s bonded to)                                                                                                                                                                                                                 | Is in ring                                        | \# of double bond                                                                                               |
| Radical?                                                                                                                                                                                                                                           | Is in resonance                   | \# of triple bond                                                                                               |
| Electronegativity                                                                                                                                                                                                                                  | Is conjugated (delocalized pi system)             | Morgan fingerprints                                                                                             |
| Atomic volume                                                                                                                                                                                                                                      | 3D Distance                                       | Molecular volume                                                                                                |
| Formal charge                                                                                                                                                                                                                                      | Cis                                               | Log p value (Higher value more lipophillic, measures ratio of [D] in octanol vs water) normalized between -3-7  |
| Electron affinity                                                                                                                                                                                                                                  | Trans                                             | 3D structural information (VSEPR)                                                                               |
| R                                                                                                                                                                                                                                                  | E                                                 | Molar Mass/400 or 500                                                                                           |
| S                                                                                                                                                                                                                                                  | Z                                                 | TPSA (Surface area)                                                                                             |
| \# of atoms it’s bonded to (not including hydrogen)                                                                                                                                                                                                |                                                   | Vapor pressure/boiling point (Some sense of how easy it is for it to turn into a gas. Might need normalization) |
| Number of atoms it’s bonded to (including hydrogen/total degree)                                                                                                                                                                                   |                                                   | LabuteASA

20-200                                                                                               |
| Hybridization (One hot encoding) 

<br>

Values -> (sp, sp2, sp3, sp3d, sp3d2)                                                                                                                                                                     |                                                   | MolMR                                                                                                           |
| Is in ring                                                                                                                                                                                                                                         |                                                   | Num rotateable bonds                                                                                            |
| Ring Size                                                                                                                                                                                                                                          |                                                   |                                                                                                                 |
| Is in resonance                                                                                                                                                                                                                                    |                                                   |                                                                                                                 |
| Is aromatic                                                                                                                                                                                                                                        |                                                   |                                                                                                                 |
| H-bond donor                                                                                                                                                                                                                                       |                                                   |                                                                                                                 |
| H-bond acceptor                                                                                                                                                                                                                                    |                                                   |                                                                                                                 |
| Gasteiger Partial Charge (electron distribution)                                                                                                                                                                                                   |                                                   |                                                                                                                 |
| One hot encoding for the type of atom from this list

['C',

 'O',

 'N',

 'S',

 'Cl',

 'K',

 'Ca',

 'Na',

 'P',

 'Br',

 'Si',

 'Mg',

 'Fe',

 'Zn',

 'V',

 'Cu',

 'He',

 'I',

 'Co',

 'Al',

 'Ti',

 'Cr',

 'B',

 'Bi',

 'F'] |                                                   |                                                                                                                 |




### Normalization 

Molar mass (Molecule) -> 30-400 

#### (Atomic Features) 

Electronegative -> 0.8-4 

Atomic Volume -> 4-46 

Electron Affinity -> -70-350

Atomic Mass -> (4.0026, 208.98) he/bi

