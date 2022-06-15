import re
from tkinter import messagebox
import json


def is_integer(num):
    """Return True if num is an integer, else return False"""
    try:
        convert_num = float(num)
    except:
        return False
    else:
        if convert_num % 1 == 0:
            return True
        else:
            return False


def is_float(num):
    """Return True if num is an integer or float, else return False if string"""
    try:
        float(num)
    except:
        return False
    return True


def check_blocksize(entry_value):
    """Return True if entry_value is a number power of 2, else return False."""
# to check if a given positive integer is a power of two
    return entry_value > 0 and (entry_value & (entry_value - 1)) == 0


def match_name(reg_expression, string_name):
    """Test string_name with regular expression, return True if the string_name is in the form 'RT+integer'"""
    regex = re.fullmatch(reg_expression, string_name)
    if regex == None :
        return False
    else:
        return True


def check_brightest(entry_value):
    """Convert string in integer, and return the integer, else return the string 'None'
    (=no limit in the number of spot detection)"""
    try:
        output = int(entry_value)
    except:
       output = 'None'
    return output


def convert_string_to_dictionnary(string: str) -> dict:
    """Convert a string to a dictionary"""
    dictionnary = {}
    temp = string.replace(" ","").split(",")
    for item in temp:
        list_temp = item.split(":")
        dictionnary[list_temp[0]] = list_temp[1]
    return dictionnary


def check_dict(string: str):
    """Check if the string correspond to a dictionary, return True if is the case, else return False."""
    try :
        convert_string_to_dictionnary(string)
        return True
    except:
        return False


def update_infoList(user_values_dic):
    dic_comm_acqui ={
        "DAPI_channel": user_values_dic['dapi_ch'],
        "RNA_channel": user_values_dic['rna_ch'],
        "barcode_channel": user_values_dic['barcode_ch'],
        "mask_channel": user_values_dic['mask_ch'],
        "fiducialBarcode_channel": user_values_dic['barcodeFid_ch'],
        "fiducialMask_channel": user_values_dic['maskFid_ch'],
        "fiducialDAPI_channel": user_values_dic['dapiFid_ch'],
        "pixelSizeXY": float(user_values_dic['pixelSizeXY_Entry']),
        "pixelSizeZ": float(user_values_dic['pixelSizeZ_Entry'])
    }
    dic_comm_aligimg = {
        "blockSize": int(user_values_dic['blockSize_Entry']),
        "referenceFiducial": user_values_dic['referenceFiducial_Entry']
    }
    dic_comm_buildmatrix = {
        "tracing_method": user_values_dic['tracing_method_Entry'].replace(' ','').split(","),
        "mask_expansion": int(user_values_dic['mask_expansion_Entry']),
        "flux_min": int(user_values_dic['flux_min_Entry']),
        "flux_min_3D": int(user_values_dic['flux_min_3D_Entry']),
        "KDtree_distance_threshold_mum": int(user_values_dic['KDtree_distance_threshold_mum_Entry']),
        "folder": str(user_values_dic['folder_Entry']),
        "masks2process": convert_string_to_dictionnary(user_values_dic['masks2process_Entry']),
        "toleranceDrift": int(user_values_dic['toleranceDrift_Entry'])
    }
    dic_comm_segmObj = {
        "stardist_basename": str(user_values_dic['stardist_Entry']),
        "brightest": check_brightest(user_values_dic['brightest_Entry'])
    }
    dic_labels_dapi_segmObj = {
        "area_max": int(user_values_dic['aeraMax_dapi_SegOblt_Entry']),
        "area_min": int(user_values_dic['aeraMin_dapi_SegOblt_Entry'])
    }
    
   
    dic_labels_dapi_zpro = {
        "zmax": int(user_values_dic['zProject_Dapi_zmax_Entry']),
        "zmin": int(user_values_dic['zProject_Dapi_zmin_Entry'])
    }
    dic_labels_bcd_zpro = {
        "zmax": int(user_values_dic['zProject_Bcd_zmax_Entry']),
        "zmin": int(user_values_dic['zProject_Bcd_zmin_Entry'])
    }
    
    dic_labels_mask_zpro = {
         "zmax": int(user_values_dic['zProject_Mask_zmax_Entry']),
         "zmin": int(user_values_dic['zProject_Mask_zmin_Entry'])
     }
    with open("./infoList.json", mode='r') as file:
        infoList = json.load(file)
    infoList["common"]["acquisition"].update(dic_comm_acqui)
    infoList["common"]["alignImages"].update(dic_comm_aligimg)
    infoList["common"]["buildsPWDmatrix"].update(dic_comm_buildmatrix)
    infoList["common"]["segmentedObjects"].update(dic_comm_segmObj)
    infoList["labels"]["DAPI"]["segmentedObjects"].update(dic_labels_dapi_segmObj)
    infoList["labels"]["DAPI"]["zProject"].update(dic_labels_dapi_zpro)
    infoList["labels"]["barcode"]["zProject"].update(dic_labels_bcd_zpro)
    infoList["labels"]["mask"]["zProject"].update(dic_labels_mask_zpro)
    with open("./infoList_user.json", mode='w') as file:
        json.dump(infoList, file, indent=4)

# def create_user_parameters_dic(user_values_dic):
#     user_parameters_dic= {
#             "common": {
#                 "acquisition": {
#                     "DAPI_channel": user_values_dic['dapi_ch'],
#                     "RNA_channel": user_values_dic['rna_ch'],
#                     "barcode_channel": user_values_dic['barcode_ch'],
#                     "mask_channel": user_values_dic['mask_ch'],
#                     "fiducialBarcode_channel": user_values_dic['barcodeFid_ch'],
#                     "fiducialMask_channel": user_values_dic['maskFid_ch'],
#                     "fiducialDAPI_channel": user_values_dic['dapiFid_ch'],
#                     "pixelSizeXY": float(user_values_dic['pixelSizeXY_Entry']),
#                     "pixelSizeZ": float(user_values_dic['pixelSizeZ_Entry'])
#                 },
#                 "alignImages": {
#                     "blockSize": int(user_values_dic['blockSize_Entry']),
#                     "referenceFiducial": user_values_dic['referenceFiducial_Entry']
#                 },
#                 "buildsPWDmatrix": {
#                     "tracing_method": user_values_dic['tracing_method_Entry'].replace(' ','').split(","),
#                     "mask_expansion": int(user_values_dic['mask_expansion_Entry']),
#                     "flux_min": int(user_values_dic['flux_min_Entry']),
#                     "flux_min_3D": int(user_values_dic['flux_min_3D_Entry']),
#                     "KDtree_distance_threshold_mum": int(user_values_dic['KDtree_distance_threshold_mum_Entry']),
#                     "folder": str(user_values_dic['folder_Entry']),
#                     "masks2process": convert_string_to_dictionnary(user_values_dic['masks2process_Entry']),
#                     "toleranceDrift": int(user_values_dic['toleranceDrift_Entry'])
#                 },
#                 "segmentedObjects": {
#                     "stardist_basename": str(user_values_dic['stardist_Entry']),
#                     "brightest": check_brightest(user_values_dic['brightest_Entry'])
#                 }
#             },
#             "labels": {
#                 "DAPI": {
#                     "segmentedObjects": {
#                         "area_max": int(user_values_dic['aeraMax_dapi_SegOblt_Entry']),
#                         "area_min": int(user_values_dic['aeraMin_dapi_SegOblt_Entry'])
#                     },
#                     "zProject": {
#                         "zmax": int(user_values_dic['zProject_Dapi_zmax_Entry']),
#                         "zmin": int(user_values_dic['zProject_Dapi_zmin_Entry'])
#                     }
#                 },
#                 "barcode": {
#                     "zProject": {
#                         "zmax": int(user_values_dic['zProject_Bcd_zmax_Entry']),
#                         "zmin": int(user_values_dic['zProject_Bcd_zmin_Entry'])
#                     }
#                 },
#                 "mask": {
#                     "zProject": {
#                         "zmax": int(user_values_dic['zProject_Mask_zmax_Entry']),
#                         "zmin": int(user_values_dic['zProject_Mask_zmin_Entry'])
#                     }
#                 }
#             }
#         }
#     return user_parameters_dic

def check_settings(entries_dic):
    """Return True if all parameters have good type expected, else return False with a pop-up error window"""
    is_ok = True
    # checks if the inputs correspond to what is expected, else show error window
    for key, list_values in entries_dic.items():
        entered_value = list_values[0].get()
# test for values that would be normally integer (not string or float)
        if key == 'brightest_Entry':
            if entered_value != 'None' and not is_integer(entered_value):
                messagebox.showerror("Input Error", f'The type of {key} input is not correct.\nPlease enter integer '
                                                    f'value or None.')
                is_ok = False
# test if masks2process_Entry is a string that can be converted in a dictionary
        elif key == 'masks2process_Entry':
            if not check_dict(entered_value):
                messagebox.showerror("Input Error", f'The type of {key} input is not correct.\nPlease enter string in '
                                                    f'the form "key1:value1, key2:value2".')
                is_ok = False
# test if number is an integer and a power of 2
        elif key == 'blockSize_Entry':
            entered_value = float(entered_value)
            if not check_blocksize(int(entered_value)) or not is_integer(entered_value):
                messagebox.showerror("Input Error", f'The type of {key} input is not correct.\nPlease enter an interger that is a power of 2.')
                is_ok = False
# test if name of RT/Barcode is in the form 'RT' + integer
        elif key == 'referenceFiducial_Entry':
            if not match_name('^RT[0-9][0-9]*', entered_value):
                messagebox.showerror("Input Error", f'The name of Reference Fiducial is not correct.\nPlease enter a name starting with "RT" and followed only by numbers.')
                is_ok = False
        elif list_values[2] is int:
            if not is_integer(entered_value):
                messagebox.showerror("Input Error", f'The type of {key} input is not correct.\nPlease enter interger value.')
                is_ok = False
# test for values that would be normally float (not string)
        elif list_values[2] is float:
            if not is_float(entered_value):
                messagebox.showerror("Input Error", f'The type of {key} input is not correct.\nPlease enter float value.')
                is_ok = False
    return is_ok

