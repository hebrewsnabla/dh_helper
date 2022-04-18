import dhutil

def parse_xc_s(xc):
    exch, corr = xc.split(',')
    if '+' in corr:
        raise NotImplementedError('''Correlation functional contains more than 1 component, 
                                   which is not supported yet''')
    corr_scal, corr_fnal = corr.split('*')
    corr_scal = float(corr_scal.strip())
    exchs = exch.split('+')
    if len(exchs)>2:
        raise NotImplementedError('''Exchange functional contains more than 1 component 
                                   other than HF, which is not supported yet''')
    for item in exchs:
        if 'HF' not in item:
            exch_scal, exch_fnal = exch.split('*')
