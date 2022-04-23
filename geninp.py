import dhutil

def parse_xc_s(xc):
    xc_s = dhutil.XC_DH_MAP[xc][0]
    if ',' not in xc_s:
        raise NotImplementedError(''' ''') 

    exch, corr = xc_s.split(',')
    if '+' in corr:
        raise NotImplementedError('''Correlation functional contains more than 1 component, 
                                   which is not supported yet''')
    corr_scal, corr_fnal = corr.split('*')
    corr_scal = float(corr_scal.strip())
    corr_fnal = corr_fnal.strip()
    exchs = exch.split('+')
    if len(exchs)>2:
        raise NotImplementedError('''Exchange functional contains more than 1 component 
                                   other than HF, which is not supported yet''')
    for item in exchs:
        if 'HF' not in item:
            exch_scal, exch_fnal = item.split('*')
    exch_scal = float(exch_scal.strip())
    hf_exch = 1 - exch_scal
    exch_fnal = exch_fnal.strip()
    return exch_fnal, corr_fnal, hf_exch, corr_scal

p2g = {
    'B88':'B'
}

def tostr(floatnum, len=5):
    scal = 10**(len-1)
    gauint = int(round(floatnum*scal,0))
    gaustr = '%09d'%gauint
    return gaustr[-len:]

def dump_fnal(params):
    exch_fnal, corr_fnal, hf_exch, corr_scal = params
    if exch_fnal in p2g:
        exch_fnal = p2g[exch_fnal]
    if corr_fnal in p2g:
        corr_fnal = p2g[corr_fnal]
    fnal_g = exch_fnal + corr_fnal
    exch_scal = 1 - hf_exch
    scal = '# iop(3/76=10000%s, 3/77=%s%s, 3/78=%s%s) '% (tostr(hf_exch),
           tostr(exch_scal), tostr(exch_scal), tostr(corr_scal), tostr(corr_scal))
    return fnal_g, scal

def parse_xc_d3(xc):
    params = dhutil.XC_DH_ADD_MAP[xc]["D3"]
    if params[1] == 3:
        raise NotImplementedError('''Zero-damping not implemented''')
    return params

def dump_d3(params):
    params_dump = []
    for item in params[0]:
        if item == 0:
            params_dump.append('-1')
        else:
            params_dump.append(tostr(item, 7))
    s6, a1, s8, a2, sr6 = params_dump
    dump = 'iop(3/174=%s,3/175=%s,3/176=0,3/177=%s,3/178=%s)' % (s6, s8, a1, a2)
    return dump

def gau_scf(xc):
    params = parse_xc_s(xc.lower())
    templ, scal = dump_fnal(params)
    print('#p ' + templ)
    print('# ' + scal)
    if 'd3' in xc.lower():
        d3_params = parse_xc_d3(xc.lower())
        print('# ' + dump_d3(d3_params))

def parse_xc_pt(xc):
    c_pt, os, ss = dhutil.XC_DH_MAP[xc][2:]
    return c_pt, os, ss

def dump_pt(params):
    c_pt, os, ss = params
    os *= c_pt
    ss *= c_pt
    os = tostr(os)
    ss = tostr(ss)
    dump = 'iop(3/125=%s%s)' %(ss,os)
    return dump

def gau_dh(xc):
    params = parse_xc_s(xc.lower())
    templ, scal = dump_fnal(params)
    params_pt = parse_xc_pt(xc.lower())
    pt_scal = dump_pt(params_pt)
    print('#p ' + templ)
    print('# ' + scal)
    print('# ' + pt_scal)
    if 'd3' in xc.lower():
        d3_params = parse_xc_d3(xc.lower())
        print('# ' + dump_d3(d3_params))

    
