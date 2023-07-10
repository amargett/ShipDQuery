# ShipD Dataset Data Query

credit for ShipD dataset goes to Noah Bagazinski and MIT Decode Lab


run getData file
you will be prompted to enter an integer "boatInt". This represents the index of the boat within the ShipD dataset you 
would like to access. This will then output the data associated with this boat in the following order: 
This file will take in a boat index and return a list of the data for that boat
the indices of the data are as follows:
0: Boat Number
1: Boat Area WP
2: Boat Area WS
3: Boat Curvature
4: Boat Ixx
5: Boat Iyy
6: Boat LCB
7: Boat LCF
8: Boat VCB
9: Boat Volume
10: Boat WL_Length
11: Boat z
12: list of boat input vectors, in this order : LOA,Lb,Ls,Bd,Dd,Bs,WL,Bc,Beta,Rc,Rk,Abow,Bbow,BK_z,Kappa_bow,Adel bow,Bdel bow,Adrft,Bdrft,Cdrft,bit_EP_S,bit_EP_T,Atrans,SK_z,Kappa_stern,Adel stern,Bdel stern,Beta trans,Bc trans,Rc Trans,Rk trans,bit_BB,bit_SB,Lbb,Hbb,Bbb,Lbbm,Rbb,Kappa_SB,Lsb,HSBOA,Hsb,Bsb,Lsbm,Rsb
13: filename of profile image

description of parameters at index 12 are in HullParameterizationOverview.pdf
