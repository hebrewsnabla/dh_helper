
# Doubly hybrid functionals xc code in detail
XC_DH_MAP = {   # [xc_s, xc_n, cc, c_os, c_ss]
    "mp2": ("HF", None, 1, 1, 1),
    "xyg3": ("B3LYPg", "0.8033*HF - 0.0140*LDA + 0.2107*B88, 0.6789*LYP", 0.3211, 1, 1),
    "xygjos": ("B3LYPg", "0.7731*HF + 0.2269*LDA, 0.2309*VWN3 + 0.2754*LYP", 0.4364, 1, 0),
    "xdhpbe0": ("PBE0", "0.8335*HF + 0.1665*PBE, 0.5292*PBE", 0.5428, 1, 0),
    "b2plyp": ("0.53*HF + 0.47*B88, 0.73*LYP", None, 0.27, 1, 1),
    "mpw2plyp": ("0.55*HF + 0.45*mPW91, 0.75*LYP", None, 0.25, 1, 1),
    "pbe0dh": ("0.5*HF + 0.5*PBE, 0.875*PBE", None, 0.125, 1, 1),
    "pbeqidh": ("0.693361*HF + 0.306639*PBE, 0.666667*PBE", None, 0.333333, 1, 1),
    "pbe02": ("0.793701*HF + 0.206299*PBE, 0.5*PBE", None, 0.5, 1, 1),
    "revxyg3": ("B3LYPg", "0.9196*HF - 0.0222*LDA + 0.1026*B88, 0.6059*LYP", 0.3941, 1, 1),
    "xyg5": ("B3LYPg", "0.9150*HF + 0.0612*LDA + 0.0238*B88, 0.4957*LYP", 1, 0.4548, 0.2764),
    "xyg6": ("B3LYPg", "0.9105*HF + 0.1576*LDA - 0.0681*B88, 0.1800*VWN3 + 0.2244*LYP", 1, 0.4695, 0.2426),
    "xyg7": ("B3LYPg", "0.8971*HF + 0.2055*LDA - 0.1408*B88, 0.4056*VWN3 + 0.1159*LYP", 1, 0.4052, 0.2589),
    "revxygjos": ("B3LYPg", "0.8877*HF + 0.1123*LDA, -0.0697*VWN3 + 0.6167*LYP", 0.5485, 1, 0),
    "xygjos5": ("B3LYPg", "0.8928*HF + 0.3393*LDA - 0.2321*B88, 0.3268*VWN3 - 0.0635*LYP", 0.5574, 1, 0),
    "b2gpplyp": ("0.65*HF + 0.35*B88, 0.64*LYP", None, 0.36, 1, 1),
    "ls1dhpbe": ("0.75*HF + 0.25*PBE, 0.578125*PBE", None, 0.421875, 1, 1),
    "dsdpbep86d3": ("0.69*HF + 0.31*PBE, 0.44*P86", None, 1, 0.52, 0.22),
    "dsdpbepbed3": ("0.68*HF + 0.32*PBE, 0.49*PBE", None, 1, 0.55, 0.13),
    "dsdblypd3": ("0.71*HF + 0.29*B88, 0.54*LYP", None, 1, 0.47, 0.40),
    "dsdpbeb95d3": ("0.66*HF + 0.34*PBE, 0.55*B95", None, 0.46, 0.09),
    "b2plypd3": ("0.53*HF + 0.47*B88, 0.73*LYP", None, 0.27, 1, 1),
    "hfb3lyp": ("HF", "B3LYP", 0, 0, 0),
    "hfpbe0": ("HF", "PBE0", 0, 0, 0),
}
# Additional parameters for doubly hybrids (mostly dftd3)
XC_DH_ADD_MAP = {
    "dsdpbep86d3": {"D3": ([0.48, 0, 0, 5.6, 0], 4)},
    "dsdpbepbed3": {"D3": ([0.78, 0, 0, 6.1, 0], 4)},
    "dsdblypd3": {"D3": ([0.57, 0, 0, 5.4, 0], 4)},
    "dsdpbeb95d3": {"D3": ([0.61, 0, 0, 6.2, 0], 4)},
    "b2plypd3": {"D3": ([0.64, 0.9147, 0.3065, 5.0570, 0], 4)},
}

