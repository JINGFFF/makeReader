#!/usr/bin/python

import sys
import time
import os
import ROOT
from ROOT import gROOT, THStack, TH1D, TList, TFile, TH2D, TObjArray, TTree, TBranch
from math import fabs, sqrt

reader_name = sys.argv[1]

file1 = TFile.Open(sys.argv[2]);
dir1 = file1.Get("treeDumper");
tree1 =dir1.Get("PKUCandidates");

outfile_h = open(reader_name+'.h', 'w')
outfile_c = open(reader_name+'.C', 'w')

outfile_c.write('#include <TROOT.h> \n')
outfile_c.write('#include <TChain.h>\n')
outfile_c.write('#include <TCanvas.h>\n')
outfile_c.write('#include <TFile.h>\n')
outfile_c.write('#include <TCanvas.h>\n')
outfile_c.write('#include <TLorentzVector.h>\n')
outfile_c.write('#include <fstream>\n')
outfile_c.write('#include <iomanip>\n')
outfile_c.write('#include <TH1D.h>\n')
outfile_c.write('#include "TTreeReader.h"\n')
outfile_c.write('#include <TTreeReaderArray.h>\n')
outfile_c.write('#include <TH2.h>\n')
outfile_c.write('#include <algorithm>\n')
outfile_c.write('#include <cmath>\n')
outfile_c.write('#include <ctime>\n')
outfile_c.write('#include <map>\n')
outfile_c.write('#include <sstream>\n')
outfile_c.write('#include <string>\n')
outfile_c.write('#include <vector>\n')
outfile_c.write('#include "tree.h"\n\n')
outfile_c.write('using namespace std;\n\n')

outfile_c.write('void tree_read(){\n')
#outfile_c.write('   TString infilename = "/data/pku/home/pengj/testvbs/data/for_analysis/2018_tight_for_analysis_single_muon_A.root";\n')
outfile_c.write('   TFile *file1 =new TFile(infilename);\n')
outfile_c.write('   TDirectory * dir = (TDirectory*)file1->Get("treeDumper");\n')

outfile_c.write('   TTreeReader fReader ;\n')
outfile_c.write('   fReader.SetTree("PKUCandidates", dir);\n')


bA = tree1.GetListOfBranches()
for i in range(bA.GetEntries()):
    b2 = bA.At(i)
    print(b2.GetTitle())

    data_type, data_array_or_not = '', ''
    if '[' in b2.GetTitle():
        data_array_or_not = 'Array'
    else:
        data_array_or_not = 'Value'
    
    dp = b2.GetTitle().split('/')[1]

    if dp == 'I':
        data_type = 'Int_t'
    if dp == 'D':
        data_type = 'Double_t'
    if dp == 'O':
        data_type = 'Bool_t'
    if dp == 'F':
        data_type = 'Float_t'

    branch_name = b2.GetName()
    outfile_h.write(data_type + ' m_' + b2.GetTitle().split('/')[0] + ';\n')
    outfile_c.write('   TTreeReader'+data_array_or_not+'<'+data_type+'>    '+branch_name+'  = {fReader, "'+branch_name+'"};'  +'\n')

outfile_c.write('   Long64_t maxEntries = fReader.GetEntries(false);\n\n')
outfile_c.write('   int n = 0; \n')
outfile_c.write('   while (fReader.Next()) {\n\n\n')
#outfile_c.write('      cout<<"event num : "<< n<<" "<<*nevent<<"   "<<*run<<"   "<<*ls<<endl;\n')
outfile_c.write('      n++;\n\n\n')
outfile_c.write('   }\n\n')

outfile_c.write('}\n')
