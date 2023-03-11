# LARSOFT_OPDET_ANALYSIS
Repository used to analyse raw and deco optical wvfs from larsoft.

Currently the notebook expects raw data (output of the digitizer module) and deconvolved data (output of the deconvolution module):
 - The raw data should be a file named opdetraw_hist.root and contain the folders opdigi and opdigiana.
 - The deco data should be two files named deconv_*_hist.root and contain the folder opdecoana. Remember to change name and label in the import section of the notebook accordingly.