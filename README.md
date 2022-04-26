# dh_helper

## Features
### Generate Gaussian iops for doubly hybrid functionals
* full functional (include SCF and PT2)
```
> python3 dhhelper -t dh -f revDSDPBEP86D3
#p DSDPBEP86
# iop(3/76=1000006900, 3/77=0310003100, 3/78=0429604296)
# iop(3/125=0079905785)
# em=gd3bj iop(3/174=0437700,3/175=-1,3/176=0,3/177=-1,3/178=5500000)
```
* SCF only (useful for stable=opt)
```
> python3 dhhelper -t scf -f revDSDPBEP86D3
#p PBEP86
# iop(3/76=1000006900, 3/77=0310003100, 3/78=0429604296)
# em=gd3bj iop(3/174=0437700,3/175=-1,3/176=0,3/177=-1,3/178=5500000)
```
* functionals supported

| bDH | bDH-D3 |
| :---: | :---: |
| B2PLYP | B2PLYPD3 |
| mPW2PLYP | |
| B2GPPLYP | |
| PBE0DH | |
| PBE02 | |
| PBEQIDH | |
| LS1DHPBE | |
| DSDPBEP86 | DSDPBEP86D3 |
| | revDSDPBEP86D3 |
| | DSDPBEPBED3 |
| | DSDBLYPD3 |
| | DSDPBEB95D3 |

Note: all hyphens are removed due to compatibility with [ajz34/dh](https://github.com/ajz34/dh). DSDPBEP86 here is equivalent to the 2013 one (renamed by Martin) but not the original one (DSDPBEP86 in ORCA).
