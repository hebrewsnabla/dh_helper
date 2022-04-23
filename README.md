# dh_helper

## Features
### Generate Gaussian iops for doubly hybrid functionals
* full functional (include SCF and PT2)
```
> python3 gau_dh revDSDPBEP86D3
#p DSDPBEP86
# iop(3/76=1000006900, 3/77=0310003100, 3/78=0429604296)
# iop(3/125=0079905785)
# em=gd3bj iop(3/174=0437700,3/175=-1,3/176=0,3/177=-1,3/178=5500000)
```
* SCF only (useful for stable=opt)
```
> python3 gau_scf revDSDPBEP86D3
#p PBEP86
# iop(3/76=1000006900, 3/77=0310003100, 3/78=0429604296)
# em=gd3bj iop(3/174=0437700,3/175=-1,3/176=0,3/177=-1,3/178=5500000)
```

