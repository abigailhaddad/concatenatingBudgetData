# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:28:36 2019
analyzing budget data
@author: admin
"""

import pandas as pd
import os
import numpy as np

newDir=r'C:\Users\admin\Documents\Python Scripts\budget'
os.chdir(newDir)

allBudgetData=pd.read_csv("allBudgetData.csv", low_memory=False)
"""
fourthEstateOrgs=['TJS',
 'DAU',
 'DCAA',
 'DCMA',
 'DHRA',
 'DLA',
 'DMACT',
 'DPAA',
 'DSCA',
 'DTSA',
 'DTRA',
 'DODEA',
 'MDA',
 'WHS',
 'IG',
 'DARPA',
 'DTIC',
 'DIA',
 'DFAS']

absentOrgs=["TCMA"
"DMEA",
"NDU",
"PFPA"
"TRMC"
]

fourthEstateData=allBudgetData.loc[allBudgetData['Organization'].isin(fourthEstateOrgs)]
"""
data2017=allBudgetData.loc[allBudgetData['tabName'].str.contains("2017")]


#if we look just at 2017 data we lose orgs

#missingOrgs=[i for i in fourthEstateData['Organization'].unique() if i not in data2017['Organization'].unique()]

keepFiles=[ 'rf1', 'r1', 'o1', 'p1', 'c1']

#keepFiles=[ 'rf1', 'r1', 'o1', 'p1']

data2017keep=data2017.loc[data2017['fileName'].isin(keepFiles)]

keepColumns=[i for i in data2017keep.columns if "2018" not in i and "2019" not in i]

cutDownColumns=data2017keep[keepColumns].dropna(axis='columns',how='all')

#As a note: the C1 (that's milcon) spending is just specified as being 2017, it doesn't say Base+ OCO, it says 'toa', which is Total Obligation Authority


dictOfNumColumns={"FY 2017 Base and OCO": ['FY 2017 (Base + OCO)', 'FY 2017 (Base + OCO) Amount', 'FY 2017 (Base + OCO) Quantity'
                                           ,'TOA Amount'
                            ]
               }

dictOfTextColumns={"Line Title": ['Line Item Title', 'Program Element / Budget Line Item (BLI) Title', 'SAG / Budget Line Item (BLI) Title']}

for key in dictOfNumColumns.keys():
    cutDownColumns[key]=cutDownColumns[dictOfNumColumns[key]].sum(axis=1)
    cutDownColumns=cutDownColumns.drop(dictOfNumColumns[key], axis=1)
    
for key in dictOfTextColumns.keys():
    cutDownColumns[key]=cutDownColumns[dictOfTextColumns[key]].astype(str).sum(1).str.replace("nan","")
    cutDownColumns=cutDownColumns.drop(dictOfTextColumns[key], axis=1)
    
    

cutDownColumns.groupby(['fileName'])["FY 2017 Base and OCO"].sum()
#cutDownColumns.to_excel("2017ExcludingMilcon.xlsx")