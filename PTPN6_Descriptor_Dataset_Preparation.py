import pandas as pd

#Load bioactivity data
df3 = pd.read_csv('/Users/mrinalmishra/Documents/drug_discovery/PTPN6_bioactivity_data_3class_pIC50.csv')

selection = ['canonical_smiles','molecule_chembl_id']
df3_selection = df3[selection]
df3_selection.to_csv('molecule.smi', sep='\t', index=False, header=False)

#Calculate fingerprint descriptors
#Calculate PaDEL descriptors
#Download padel.zip from ""https://raw.githubusercontent.com/dataprofessor/bioinformatics/master/padel.sh"
#Unzip padel.zip and add molecule.smi file in the unzipped folder
#Run padel with command: java -jar PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv
#Copy the output in folder "/Users/mrinalmishra/Documents/drug_discovery/"


#Preparing the X and Y Data Matrices
#X data matrix
df3_X = pd.read_csv('/Users/mrinalmishra/Documents/drug_discovery/descriptors_output.csv')
df3_X = df3_X.drop(columns=['Name'])

#Y variable
#Convert IC50 to pIC50

df3_Y = df3['pIC50']
df3_Y


#Combining X and Y variable

dataset3 = pd.concat([df3_X,df3_Y], axis=1)
dataset3

dataset3.to_csv('/Users/mrinalmishra/Documents/drug_discovery/PTPN6_bioactivity_data_3class_pIC50_pubchem_fp.csv', index=False)
