import tkinter as tk
from tkinter import END
from functools import partial
from info_parameters import *
from function_parameters import *

import json


main_window = tk.Tk()
main_window.title("pyHiM parameters")
main_window.minsize(width=1000, height=700)


entries_dic = {}
user_values_dic = {}

# ---------------------------------------------Functions------------------------------------------------


def display_help(param):
    message = help_dic[param]
    help_label.config(text=message)


def restoreSetting():
    dapi_ch.set(default_Entry_dic["dapi_ch"])
    dapiFid_ch.set(default_Entry_dic["dapiFid_ch"])
    barcode_ch.set(default_Entry_dic["barcode_ch"])
    barcodeFid_ch.set(default_Entry_dic["barcodeFid_ch"])
    mask_ch.set(default_Entry_dic["mask_ch"])
    maskFid_ch.set(default_Entry_dic["maskFid_ch"])
    rna_ch.set(default_Entry_dic["rna_ch"])
    #rnaFid_ch.set(default_Entry_dic["rnaFid_ch"])
    for key, list_values in entries_dic.items():
        if list_values[0].get() != "ch00" and list_values[0].get() != "ch01":
            list_values[0].delete(first=0, last=END)
            list_values[0].insert(0, string=list_values[1])


def save_setting(entries_dic, user_values_dic):
    if check_settings(entries_dic):
        # Save getted values in Json file:
        for key, list_values in entries_dic.items():
            entered_value = list_values[0].get()
            user_values_dic[key] = entered_value
        User_parameters_dic = create_user_parameters_dic(user_values_dic)
        with open("./infoList_user.json", mode='w') as file:
            json.dump(User_parameters_dic, file, indent=4)
        messagebox.showinfo("Info Message", "The settings have been saved.")


# ----------------Save and restaure button----------------------------

# Restore button
restore_button = tk.Button(main_window, text='Restore default settings', command=restoreSetting)
restore_button.grid(row=27, column=0, columnspan=3, pady=5, padx=5)

# Save button
save_button = tk.Button(main_window, text='Save settings', command=partial(save_setting, entries_dic, user_values_dic))
save_button.grid(row=27, column=2, columnspan=3, pady=5, padx=5)

# -------------------------Label Frame--------------------------------
# label frame (box) for Acquisition parameters
acquisition_labelFrame = tk.LabelFrame(main_window, text="1. Acquisition parameters")
acquisition_labelFrame.grid(row=0, column=0, columnspan=6, pady=5, padx=5)

# label frame (box) for quick help box
help_LabelFrame = tk.LabelFrame(main_window, text="Quick Help")
help_LabelFrame.grid(row=0, column=7, pady=5, padx=5)

# label frame (box) for AlignImages parameters
alignImages_LabelFrame = tk.LabelFrame(main_window, text="2. AlignImages parameters")
alignImages_LabelFrame.grid(row=9, column=0, columnspan=6, pady=5, padx=5, sticky='WE')

# label frame (box) for BuildsPWDmatrix parameters
buildsPWDmatrix_LabelFrame = tk.LabelFrame(main_window, text="3. BuildsPWDmatrix parameters")
buildsPWDmatrix_LabelFrame.grid(row=11, column=0, columnspan=6, pady=5, padx=5, sticky='WE')

# label frame (box) for SegmentedObjects parameters
segmentedObjects_LabelFrame = tk.LabelFrame(main_window, text="4. SegmentedObjects parameters")
segmentedObjects_LabelFrame.grid(row=17, column=0, columnspan=6, pady=5, padx=5, sticky='WE')

# label frame (box) for Labels parameters
labels_LabelFrame = tk.LabelFrame(main_window, text="5. Labels parameters")
labels_LabelFrame.grid(row=19, column=0, columnspan=6, pady=5, padx=5, sticky='WE')

# ---------------------------Help Box-----------------------------------
help_label = tk.Label(help_LabelFrame,
                      text="Help will come to those who ask for it",
                      height=20,
                      width=50,
                      justify='center',
                      wraplength=350)
help_label.grid()

# -----------------------------------------Help Button--------------------------------------------
# Dapi Channel Help Button:
dapi_ch_HelpButton = tk.Button(acquisition_labelFrame, text="?", command=partial(display_help, "DAPI_channel"))
dapi_ch_HelpButton.grid(row=0, column=0)

# Dapi Fiducial Channel Help Button:
dapiFid_ch_HelpButton = tk.Button(acquisition_labelFrame, text="?", command=partial(display_help, "fiducialDAPI_channel"))
dapiFid_ch_HelpButton.grid(row=0, column=3)

# Barcode Channel Help Button:
barcode_ch_HelpButton = tk.Button(acquisition_labelFrame, text="?", command=partial(display_help, "barcode_channel"))
barcode_ch_HelpButton.grid(row=3, column=0)

# Barcode Fiducial Channel Help Button:
barcodeFid_ch_HelpButton = tk.Button(acquisition_labelFrame, text="?", command=partial(display_help, "fiducialBarcode_channel"))
barcodeFid_ch_HelpButton.grid(row=3, column=3)

# Mask Channel Help Button:
mask_ch_HelpButton = tk.Button(acquisition_labelFrame, text="?", command=partial(display_help, "mask_channel"))
mask_ch_HelpButton.grid(row=5, column=0)

# Barcode Fiducial Channel Help Button:
maskFid_ch_HelpButton = tk.Button(acquisition_labelFrame, text="?", command=partial(display_help, "fiducialMask_channel"))
maskFid_ch_HelpButton.grid(row=5, column=3)

# RNA Channel Help Button:
rna_ch_HelpButton = tk.Button(acquisition_labelFrame, text="?", command=partial(display_help, "RNA_channel"))
rna_ch_HelpButton.grid(row=7, column=0)

# # RNA Fiducial Channel Help Button:
# rnaFid_ch_HelpButton = tk.Button(acquisition_labelFrame, text="?", command=partial(display_help, "fiducialRNA_channel"))
# rnaFid_ch_HelpButton.grid(row=6, column=3)

# pixelSizeXY Help Button:
pixelSizeXY_HelpButton = tk.Button(acquisition_labelFrame, text="?", command=partial(display_help, "pixelSizeXY"))
pixelSizeXY_HelpButton.grid(row=10, column=0)

# pixelSizeZ Help Button:
pixelSizeZ_HelpButton = tk.Button(acquisition_labelFrame, text="?", command=partial(display_help, "pixelSizeZ"))
pixelSizeZ_HelpButton.grid(row=10, column=3)

# BlockSize Help Button:
blockSize_HelpButton = tk.Button(alignImages_LabelFrame, text="?", command=partial(display_help, "blockSize"))
blockSize_HelpButton.grid(row=11, column=0)

# ReferenceFiducial Help Button:
referenceFiducial_HelpButton = tk.Button(alignImages_LabelFrame, text="?", command=partial(display_help, "referenceFiducial"))
referenceFiducial_HelpButton.grid(row=12, column=0)

# flux_min Help Button:
flux_min_HelpButton = tk.Button(buildsPWDmatrix_LabelFrame, text="?", command=partial(display_help, "flux_min"))
flux_min_HelpButton.grid(row=13, column=0)

#flux_min_3D Help Button:
flux_min_3D_HelpButton = tk.Button(buildsPWDmatrix_LabelFrame, text="?", command=partial(display_help, "flux_min_3D"))
flux_min_3D_HelpButton.grid(row=13, column=3)

# toleranceDrift Help Button:
toleranceDrift_HelpButton = tk.Button(buildsPWDmatrix_LabelFrame, text="?", command=partial(display_help, "toleranceDrift"))
toleranceDrift_HelpButton.grid(row=14, column=0)

# mask_expansion Help Button:
mask_expansion_HelpButton = tk.Button(buildsPWDmatrix_LabelFrame, text="?", command=partial(display_help, "mask_expansion"))
mask_expansion_HelpButton.grid(row=14, column=3)

# folder Help Button:
mask_expansion_HelpButton = tk.Button(buildsPWDmatrix_LabelFrame, text="?", command=partial(display_help, "folder"))
mask_expansion_HelpButton.grid(row=15, column=0)

# masks2process Help Button:
masks2process_HelpButton = tk.Button(buildsPWDmatrix_LabelFrame, text="?", command=partial(display_help, "masks2process"))
masks2process_HelpButton.grid(row=16, column=0)

# tracing_method Help Button:
tracing_method_HelpButton = tk.Button(buildsPWDmatrix_LabelFrame, text="?", command=partial(display_help, "tracing_method"))
tracing_method_HelpButton.grid(row=17, column=0)

# KDtree_distance_threshold_mum Help Button:
tracing_method_HelpButton = tk.Button(buildsPWDmatrix_LabelFrame, text="?", command=partial(display_help, "KDtree_distance_threshold_mum"))
tracing_method_HelpButton.grid(row=18, column=0)

# stardist_basename Help Button
stardist_HelpButton = tk.Button(segmentedObjects_LabelFrame, text="?", command=partial(display_help, "Stardist_basename"))
stardist_HelpButton.grid(row=19, column=0)

# brightest Help Button
brightest_HelpButton = tk.Button(segmentedObjects_LabelFrame, text="?", command=partial(display_help, "brightest"))
brightest_HelpButton.grid(row=20, column=0)

# segmentObject_Labels_aeramax Help Button
segmentObject_Labels_aeraMax_HelpButton = tk.Button(labels_LabelFrame, text="?", command=partial(display_help, "segmentObject_Labels_aeraMax"))
segmentObject_Labels_aeraMax_HelpButton.grid(row=22, column=0)
# segmentObject_Labels_aeramin Help Button
segmentObject_Labels_aeraMin_HelpButton = tk.Button(labels_LabelFrame, text="?", command=partial(display_help, "segmentObject_Labels_aeraMin"))
segmentObject_Labels_aeraMin_HelpButton.grid(row=23, column=0)

# ZProject_dapi_zmax Help Button
zProject_zmax_HelpButton = tk.Button(labels_LabelFrame, text="?", command=partial(display_help, "zProject_dapi_zmax"))
zProject_zmax_HelpButton.grid(row=22, column=4)
# ZProject_dapi_zmin Help Button
zProject_zmin_HelpButton = tk.Button(labels_LabelFrame, text="?", command=partial(display_help, "zProject_dapi_zmin"))
zProject_zmin_HelpButton.grid(row=23, column=4)

# ZProject_Bcd_zmax Help Button
zProject_Bcd_zmax_HelpButton = tk.Button(labels_LabelFrame, text="?", command=partial(display_help, "zProject_Bcd_zmax"))
zProject_Bcd_zmax_HelpButton.grid(row=25, column=0)
# ZProject_Bcd_zmin Help Button
zProject_Bcd_zmin_HelpButton = tk.Button(labels_LabelFrame, text="?", command=partial(display_help, "zProject_Bcd_zmin"))
zProject_Bcd_zmin_HelpButton.grid(row=26, column=0)

# ZProject_Mask_zmax Help Button
zProject_Mask_zmax_HelpButton = tk.Button(labels_LabelFrame, text="?", command=partial(display_help, "zProject_Mask_zmax"))
zProject_Mask_zmax_HelpButton.grid(row=25, column=4)
# ZProject_Mask_zmin Help Button
zProject_Mask_zmin_HelpButton = tk.Button(labels_LabelFrame, text="?", command=partial(display_help, "zProject_Mask_zmin"))
zProject_Mask_zmin_HelpButton.grid(row=26, column=4)


# --------------------------Label of different channels for acquisition_labelFrame---------------------
# Dapi Channel Label:
dapi_ch_label = tk.Label(acquisition_labelFrame, text="DAPI Channel :")
dapi_ch_label.grid(row=0, column=1)
# Dapi Fiducial Channel Label:
dapiFid_ch_label = tk.Label(acquisition_labelFrame, text="DAPI Fiducial Channel :")
dapiFid_ch_label.grid(row=0, column=4)
# Barcode Channel Label:
barcode_ch_label = tk.Label(acquisition_labelFrame, text="Barcode/RT Channel :")
barcode_ch_label.grid(row=3, column=1)
# Barcode Fiducial Channel Label:
barcodeFid_ch_label = tk.Label(acquisition_labelFrame, text="Barcode/RT Fiducial Channel :")
barcodeFid_ch_label.grid(row=3, column=4)
# Mask Channel Label:
mask_ch_label = tk.Label(acquisition_labelFrame, text="Mask Channel :")
mask_ch_label.grid(row=5, column=1)
# Barcode Fiducial Channel Label:
maskFid_ch_label = tk.Label(acquisition_labelFrame, text="Mask Fiducial Channel :")
maskFid_ch_label.grid(row=5, column=4)
# RNA Channel Label:
rna_ch_label = tk.Label(acquisition_labelFrame, text="RNA Channel :")
rna_ch_label.grid(row=7, column=1)
# # RNA Fiducial Channel Label:
# rnaFid_ch_label = tk.Label(acquisition_labelFrame, text="RNA Fiducial Channel :")
# rnaFid_ch_label.grid(row=6, column=4)
# pixelSizeXY Label:
pixelSizeXY_label = tk.Label(acquisition_labelFrame, text="Pixel size (XY) :")
pixelSizeXY_label.grid(row=10, column=1)
# pixelSizeZ Label:
pixelSizeZ_label = tk.Label(acquisition_labelFrame, text="Pixel size (Z) :")
pixelSizeZ_label.grid(row=10, column=4)
# --------------------------Entry for acquisition_labelFrame---------------------
# pixelSizeXY Entry
pixelSizeXY_Entry = tk.Entry(acquisition_labelFrame)
value = default_Entry_dic["pixelSizeXY_Entry"]
pixelSizeXY_Entry.insert(0, string=value)
entries_dic["pixelSizeXY_Entry"] = [pixelSizeXY_Entry, value, type(value)]
pixelSizeXY_Entry.grid(row=10, column=2)

# pixelSizeZ Entry
pixelSizeZ_Entry = tk.Entry(acquisition_labelFrame)
value = default_Entry_dic["pixelSizeZ_Entry"]
pixelSizeZ_Entry.insert(0, string=value)
entries_dic["pixelSizeZ_Entry"] = [pixelSizeZ_Entry, value, type(value)]
pixelSizeZ_Entry.grid(row=10, column=5)

# --------------------------Radiobutton of different channels for acquisition_labelFrame---------------------
# Dapi Channel Radiobutton:
dapi_ch = tk.StringVar()
value = default_Entry_dic["dapi_ch"]
dapi_ch.set(value)
entries_dic["dapi_ch"] = [dapi_ch, value, type(value)]
dapi_ch_Radiobutton1 = tk.Radiobutton(acquisition_labelFrame, text="Ch00", value="ch00", variable=dapi_ch)
dapi_ch_Radiobutton1.grid(row=0, column=2)
dapi_ch_Radiobutton2 = tk.Radiobutton(acquisition_labelFrame, text="Ch01", value="ch01", variable=dapi_ch)
dapi_ch_Radiobutton2.grid(row=1, column=2)
dapi_ch_Radiobutton3 = tk.Radiobutton(acquisition_labelFrame, text="Ch02", value="ch02", variable=dapi_ch)
dapi_ch_Radiobutton3.grid(row=2, column=2)

# Dapi Fiducial Channel Radiobutton:
dapiFid_ch = tk.StringVar()
value = default_Entry_dic["dapiFid_ch"]
dapiFid_ch.set(value)
entries_dic["dapiFid_ch"] = [dapiFid_ch, value, type(value)]
dapiFid_ch_Radiobutton1 = tk.Radiobutton(acquisition_labelFrame, text="Ch00", value="ch00", variable=dapiFid_ch)
dapiFid_ch_Radiobutton1.grid(row=0, column=5)
dapiFid_ch_Radiobutton2 = tk.Radiobutton(acquisition_labelFrame, text="Ch01", value="ch01", variable=dapiFid_ch)
dapiFid_ch_Radiobutton2.grid(row=1, column=5)
dapiFid_ch_Radiobutton3 = tk.Radiobutton(acquisition_labelFrame, text="Ch02", value="ch02", variable=dapiFid_ch)
dapiFid_ch_Radiobutton3.grid(row=2, column=5)

# Barcode Channel Radiobutton:
barcode_ch = tk.StringVar()
value = default_Entry_dic["barcode_ch"]
barcode_ch.set(value)
entries_dic["barcode_ch"] = [barcode_ch, value, type(value)]
barcode_ch_Radiobutton1 = tk.Radiobutton(acquisition_labelFrame, text="Ch00", value="ch00", variable=barcode_ch)
barcode_ch_Radiobutton1.grid(row=3, column=2)
barcode_ch_Radiobutton2 = tk.Radiobutton(acquisition_labelFrame, text="Ch01", value="ch01", variable=barcode_ch)
barcode_ch_Radiobutton2.grid(row=4, column=2)

# Barcode Fiducial Channel Radiobutton:
barcodeFid_ch = tk.StringVar()
value = default_Entry_dic["barcodeFid_ch"]
barcodeFid_ch.set(value)
entries_dic["barcodeFid_ch"] = [barcodeFid_ch, value, type(value)]
barcodeFid_ch_Radiobutton1 = tk.Radiobutton(acquisition_labelFrame, text="Ch00", value="ch00", variable=barcodeFid_ch)
barcodeFid_ch_Radiobutton1.grid(row=3, column=5)
barcodeFid_ch_Radiobutton2 = tk.Radiobutton(acquisition_labelFrame, text="Ch01", value="ch01", variable=barcodeFid_ch)
barcodeFid_ch_Radiobutton2.grid(row=4, column=5)

# Mask Channel Radiobutton:
mask_ch = tk.StringVar()
value = default_Entry_dic["mask_ch"]
mask_ch.set(value)
entries_dic["mask_ch"] = [mask_ch, value, type(value)]
mask_ch_Radiobutton1 = tk.Radiobutton(acquisition_labelFrame, text="Ch00", value="ch00", variable=mask_ch)
mask_ch_Radiobutton1.grid(row=5, column=2)
mask_ch_Radiobutton2 = tk.Radiobutton(acquisition_labelFrame, text="Ch01", value="ch01", variable=mask_ch)
mask_ch_Radiobutton2.grid(row=6, column=2)

# # Barcode Fiducial Channel Radiobutton:
maskFid_ch = tk.StringVar()
value = default_Entry_dic["maskFid_ch"]
maskFid_ch.set(value)
entries_dic["maskFid_ch"] = [maskFid_ch, value, type(value)]
maskFid_ch_Radiobutton1 = tk.Radiobutton(acquisition_labelFrame, text="Ch00", value="ch00", variable=maskFid_ch)
maskFid_ch_Radiobutton1.grid(row=5, column=5)
maskFid_ch_Radiobutton2 = tk.Radiobutton(acquisition_labelFrame, text="Ch01", value="ch01", variable=maskFid_ch)
maskFid_ch_Radiobutton2.grid(row=6, column=5)

# # RNA Channel Radiobutton:
# rna_ch_Radiobutton
rna_ch = tk.StringVar()
value = default_Entry_dic["rna_ch"]
rna_ch.set(value)
entries_dic["rna_ch"] = [rna_ch, value, type(value)]
rna_ch_Radiobutton1 = tk.Radiobutton(acquisition_labelFrame, text="Ch00", value="ch00", variable=rna_ch)
rna_ch_Radiobutton1.grid(row=7, column=2)
rna_ch_Radiobutton2 = tk.Radiobutton(acquisition_labelFrame, text="Ch01", value="ch01", variable=rna_ch)
rna_ch_Radiobutton2.grid(row=8, column=2)
rna_ch_Radiobutton3 = tk.Radiobutton(acquisition_labelFrame, text="Ch01", value="ch02", variable=rna_ch)
rna_ch_Radiobutton3.grid(row=9, column=2)

# RNA Fiducial Channel Radiobutton:
# rnaFid_ch = tk.StringVar()
# value = default_Entry_dic["rnaFid_ch"]
# rnaFid_ch.set(value)
# entries_dic["rnaFid_ch"] = [rnaFid_ch, value, type(value)]
# rnaFid_ch_Radiobutton1 = tk.Radiobutton(acquisition_labelFrame, text="Ch00", value="ch00", variable=rnaFid_ch)
# rnaFid_ch_Radiobutton1.grid(row=6, column=5)
# rnaFid_ch_Radiobutton2 = tk.Radiobutton(acquisition_labelFrame, text="Ch01", value="ch01", variable=rnaFid_ch)
# rnaFid_ch_Radiobutton2.grid(row=7, column=5)


# --------------------------------alignImages parameters-------------------------------
# BlockSize Label
blockSize_label = tk.Label(alignImages_LabelFrame, text="Block Size :")
blockSize_label.grid(row=11, column=1)

# ReferenceFiducial Label
referenceFiducial_label = tk.Label(alignImages_LabelFrame, text="Reference Fiducial :")
referenceFiducial_label.grid(row=12, column=1)

# BlockSize Entry
blockSize_Entry = tk.Entry(alignImages_LabelFrame)
value = default_Entry_dic["blockSize_Entry"]
blockSize_Entry.insert(0, string=value)
entries_dic["blockSize_Entry"]=[blockSize_Entry, value, type(value)]
blockSize_Entry.grid(row=11, column=2)

# ReferenceFiducial Entry
referenceFiducial_Entry = tk.Entry(alignImages_LabelFrame)
value = default_Entry_dic["referenceFiducial_Entry"]
referenceFiducial_Entry.insert(0, string=value)
entries_dic["referenceFiducial_Entry"]=[referenceFiducial_Entry, value, type(value)]
referenceFiducial_Entry.grid(row=12, column=2)

# -----------------------------buildsPWDmatrix parameters-------------------------------

# flux_min Label
flux_min_label = tk.Label(buildsPWDmatrix_LabelFrame, text="flux_min :")
flux_min_label.grid(row=13, column=1)

# flux_min_3D label
flux_min_3D_label = tk.Label(buildsPWDmatrix_LabelFrame, text="flux_min_3D :")
flux_min_3D_label.grid(row=13, column=4)

# toleranceDrift label
toleranceDrift_label = tk.Label(buildsPWDmatrix_LabelFrame, text="toleranceDrift :")
toleranceDrift_label.grid(row=14, column=1)

# mask_expansion label
mask_expansion_label = tk.Label(buildsPWDmatrix_LabelFrame, text="mask_expansion :")
mask_expansion_label.grid(row=14, column=4)

# folder label
folder_label = tk.Label(buildsPWDmatrix_LabelFrame, text="folder :")
folder_label.grid(row=15, column=1)

# masks2process label
masks2process_label = tk.Label(buildsPWDmatrix_LabelFrame, text="masks2process :")
masks2process_label.grid(row=16, column=1)

# tracing_method label
tracing_method_label = tk.Label(buildsPWDmatrix_LabelFrame, text="tracing_method :")
tracing_method_label.grid(row=17, column=1)

# KDtree_distance_threshold_mum label
KDtree_distance_threshold_mum_label = tk.Label(buildsPWDmatrix_LabelFrame, text="KDtree_distance_threshold_mum :")
KDtree_distance_threshold_mum_label.grid(row=18, column=1)

# flux_min Entry
flux_min_Entry = tk.Entry(buildsPWDmatrix_LabelFrame, width=25)
value = default_Entry_dic["flux_min_Entry"]
flux_min_Entry.insert(0, string=value)
entries_dic["flux_min_Entry"] = [flux_min_Entry, value, type(value)]
flux_min_Entry.grid(row=13, column=2)

# flux_min_3D Entry
flux_min_3D_Entry = tk.Entry(buildsPWDmatrix_LabelFrame, width=10)
value = default_Entry_dic["flux_min_3D_Entry"]
flux_min_3D_Entry.insert(0, string=value)
entries_dic["flux_min_3D_Entry"] = [flux_min_3D_Entry, value, type(value)]
flux_min_3D_Entry.grid(row=13, column=5)

# toleranceDrift Entry
toleranceDrift_Entry = tk.Entry(buildsPWDmatrix_LabelFrame, width=25)
value = default_Entry_dic["toleranceDrift_Entry"]
toleranceDrift_Entry.insert(0, string=value)
entries_dic["toleranceDrift_Entry"] = [toleranceDrift_Entry, value, type(value)]
toleranceDrift_Entry.grid(row=14, column=2)


# mask_expansion Entry
mask_expansion_Entry = tk.Entry(buildsPWDmatrix_LabelFrame, width=10)
value = default_Entry_dic["mask_expansion_Entry"]
mask_expansion_Entry.insert(0, string=value)
entries_dic["mask_expansion_Entry"] = [mask_expansion_Entry, value, type(value)]
mask_expansion_Entry.grid(row=14, column=5)

# folder Entry
folder_Entry = tk.Entry(buildsPWDmatrix_LabelFrame, width=25)
value = default_Entry_dic["folder_Entry"]
folder_Entry.insert(0, string=value)
entries_dic["folder_Entry"] = [folder_Entry, value, type(value)]
folder_Entry.grid(row=15, column=2)

# masks2process Entry
masks2process_Entry = tk.Entry(buildsPWDmatrix_LabelFrame, width=25)
value = default_Entry_dic["masks2process_Entry"]
masks2process_Entry.insert(0, string=value)
entries_dic["masks2process_Entry"] = [masks2process_Entry, value, type(value)]
masks2process_Entry.grid(row=16, column=2)

# tracing_method Entry
tracing_method_Entry = tk.Entry(buildsPWDmatrix_LabelFrame, width=25)
value = default_Entry_dic["tracing_method_Entry"]
tracing_method_Entry.insert(0, string=value)
entries_dic["tracing_method_Entry"] = [tracing_method_Entry, value, type(value)]
tracing_method_Entry.grid(row=17, column=2)

# KDtree_distance_threshold_mum Entry
KDtree_distance_threshold_mum_Entry = tk.Entry(buildsPWDmatrix_LabelFrame, width=25)
value = default_Entry_dic["KDtree_distance_threshold_mum_Entry"]
KDtree_distance_threshold_mum_Entry.insert(0, string=value)
entries_dic["KDtree_distance_threshold_mum_Entry"] = [KDtree_distance_threshold_mum_Entry, value, type(value)]
KDtree_distance_threshold_mum_Entry.grid(row=18, column=2)

# ----------------------SegmentedObjects parameters-----------------------------------
# stardist_basename Label
stardist_label = tk.Label(segmentedObjects_LabelFrame, text="Stardist_basename :")
stardist_label.grid(row=19, column=1)

# brightest Label
brightest_label = tk.Label(segmentedObjects_LabelFrame, text="Brightest :")
brightest_label.grid(row=20, column=1)

# stardist_basename Entry
stardist_Entry = tk.Entry(segmentedObjects_LabelFrame, width=65)
value = default_Entry_dic["stardist_Entry"]
stardist_Entry.insert(0, string=value)
entries_dic["stardist_Entry"] = [stardist_Entry, value, type(value)]
stardist_Entry.grid(row=19, column=2)

# brightest Entry
brightest_Entry = tk.Entry(segmentedObjects_LabelFrame, width=25)
value = default_Entry_dic["brightest_Entry"]
brightest_Entry.insert(0, string=value)
entries_dic["brightest_Entry"] = [brightest_Entry, value, type(value)]
brightest_Entry.grid(row=20, column=2)


# -----------------------------------Labels parameters-------------------------------------------

# segmentedObjects Aera Label
segmentedObjects_label = tk.Label(labels_LabelFrame, text="SegmentedObjects :")
segmentedObjects_label.grid(row=21, column=0)
#       Aera_max Label
aeraMaxSegOblt_label = tk.Label(labels_LabelFrame, text="Aera_max :")
aeraMaxSegOblt_label.grid(row=22, column=1)
#       Aera_min Label
aeraMinSegOblt_label = tk.Label(labels_LabelFrame, text="Aera_min :")
aeraMinSegOblt_label.grid(row=23, column=1)

# zProject for Dapi Label
zProjectDapi_label = tk.Label(labels_LabelFrame, text="zProject for Dapi :")
zProjectDapi_label.grid(row=21, column=4)
#       zmax Dapi Label
zmaxZProjct_dapi_label = tk.Label(labels_LabelFrame, text="zmax :")
zmaxZProjct_dapi_label.grid(row=22, column=5)
#       zmin Dapi Label
zminZProjct_dapi_label = tk.Label(labels_LabelFrame, text="zmin :")
zminZProjct_dapi_label.grid(row=23, column=5)

# zProject barcode Label
zProjectBcd_label = tk.Label(labels_LabelFrame, text="zProject for Barcode :")
zProjectBcd_label.grid(row=24, column=0)
#       zmax Label
zmaxZProjct_Bcd_label = tk.Label(labels_LabelFrame, text="zmax :")
zmaxZProjct_Bcd_label.grid(row=25, column=1)
#       zmin Label
zminZProjct_Bcd_label = tk.Label(labels_LabelFrame, text="zmin :")
zminZProjct_Bcd_label.grid(row=26, column=1)

# zProject mask Label
zProjectMask_label = tk.Label(labels_LabelFrame, text="zProject for Mask :")
zProjectMask_label.grid(row=24, column=4)
#       zmax Label
zmaxZProjct_Mask_label = tk.Label(labels_LabelFrame, text="zmax :")
zmaxZProjct_Mask_label.grid(row=25, column=5)
#       zmin Label
zminZProjct_Mask_label = tk.Label(labels_LabelFrame, text="zmin :")
zminZProjct_Mask_label.grid(row=26, column=5)

# segmentedObjects Aera_max Entry
aeraMaxSegObjt_Entry = tk.Entry(labels_LabelFrame, width=10)
value = default_Entry_dic["aeraMaxSegObjt_Entry"]
aeraMaxSegObjt_Entry.insert(0, string=value)
entries_dic["aeraMaxSegObjt_Entry"] = [aeraMaxSegObjt_Entry, value, type(value)]
aeraMaxSegObjt_Entry.grid(row=22, column=2)
# segmentedObjects Aera_min Entry
aeraMinSegObjt_Entry = tk.Entry(labels_LabelFrame, width=10)
value = default_Entry_dic["aeraMinSegObjt_Entry"]
aeraMinSegObjt_Entry.insert(0, string=value)
entries_dic["aeraMinSegObjt_Entry"] = [aeraMinSegObjt_Entry, value, type(value)]
aeraMinSegObjt_Entry.grid(row=23, column=2)

# zProject zmax Entry
zProject_Dapi_zmax_Entry = tk.Entry(labels_LabelFrame, width=10)
value = default_Entry_dic["zProject_Dapi_zmax_Entry"]
zProject_Dapi_zmax_Entry.insert(0, string=value)
entries_dic["zProject_Dapi_zmax_Entry"] = [zProject_Dapi_zmax_Entry, value, type(value)]
zProject_Dapi_zmax_Entry.grid(row=22, column=6)

# zProject zmin Entry
zProject_Dapi_zmin_Entry = tk.Entry(labels_LabelFrame, width=10)
value = default_Entry_dic["zProject_Dapi_zmin_Entry"]
zProject_Dapi_zmin_Entry.insert(0, string=value)
entries_dic["zProject_Dapi_zmin_Entry"] = [zProject_Dapi_zmin_Entry, value, type(value)]
zProject_Dapi_zmin_Entry.grid(row=23, column=6)


# zProject barcode zmax Entry
zmaxZProjct_Bcd_Entry = tk.Entry(labels_LabelFrame, width=10)
value = default_Entry_dic["zmaxZProjct_Bcd_Entry"]
zmaxZProjct_Bcd_Entry.insert(0, string=value)
entries_dic["zmaxZProjct_Bcd_Entry"] = [zmaxZProjct_Bcd_Entry, value, type(value)]
zmaxZProjct_Bcd_Entry.grid(row=25, column=2)
# zProject barcode zmin Entry
zminZProjct_Bcd_Entry = tk.Entry(labels_LabelFrame, width=10)
value = default_Entry_dic["zminZProjct_Bcd_Entry"]
zminZProjct_Bcd_Entry.insert(0, string=value)
entries_dic["zminZProjct_Bcd_Entry"] = [zminZProjct_Bcd_Entry, value, type(value)]
zminZProjct_Bcd_Entry.grid(row=26, column=2)

# zProject mask zmax Entry
zmaxZProjct_Mask_Entry = tk.Entry(labels_LabelFrame, width=10)
value = default_Entry_dic["zmaxZProjct_Mask_Entry"]
zmaxZProjct_Mask_Entry.insert(0, string=value)
entries_dic["zmaxZProjct_Mask_Entry"] = [zmaxZProjct_Mask_Entry, value, type(value)]
zmaxZProjct_Mask_Entry.grid(row=25, column=6)
# zProject mask zmin Entry
zminZProjct_Mask_Entry = tk.Entry(labels_LabelFrame, width=10)
value = default_Entry_dic["zminZProjct_Mask_Entry"]
zminZProjct_Mask_Entry.insert(0, string=value)
entries_dic["zminZProjct_Mask_Entry"] = [zminZProjct_Mask_Entry, value, type(value)]
zminZProjct_Mask_Entry.grid(row=26, column=6)

main_window.mainloop()