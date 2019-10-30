def autofill_form(entry, which_form):
    #print(entry['JournalID'])
    #print(which_form)
    data = {}
    print(entry)
    if which_form == 0:
        data.update({'Name_of_brew': entry['JournalID']['Name_of_brew']})
        data.update({'Overall_notes': entry['JournalID']['Overall_notes']})
        print(data)
        return data

    elif which_form == 1:
        data.update({'Step_Mash_1_temp': entry['JournalID']['Step_Mash_1_temp']})
        data.update({'Step_Mash_1_time': entry['JournalID']['Step_Mash_1_time']})

        data.update({'Step_Mash_2_temp': entry['JournalID']['Step_Mash_2_temp']})
        data.update({'Step_Mash_2_time': entry['JournalID']['Step_Mash_2_time']})

        data.update({'Step_Mash_3_temp': entry['JournalID']['Step_Mash_3_temp']})
        data.update({'Step_Mash_3_time': entry['JournalID']['Step_Mash_3_time']})

        data.update({'Step_Mash_4_temp': entry['JournalID']['Step_Mash_4_temp']})
        data.update({'Step_Mash_4_time': entry['JournalID']['Step_Mash_4_time']})

        data.update({'Step_Mash_5_temp': entry['JournalID']['Step_Mash_5_temp']})
        data.update({'Step_Mash_5_time': entry['JournalID']['Step_Mash_5_time']})

        data.update({'Mash_out': entry['JournalID']['Mash_out']})
        data.update({'Sparge_temp': entry['JournalID']['Sparge_temp']})
        data.update({'Sparge_time': entry['JournalID']['Sparge_time']})
        data.update({'Recirc_time': entry['JournalID']['Recirc_time']})
        data.update({'Mash_notes': entry['JournalID']['Mash_notes']})
        print(data)
        return data
    
    elif which_form == 2:
        data.update({'Start_vol': entry['JournalID']['Start_vol']})
        data.update({'End_vol': entry['JournalID']['End_vol']})

        data.update({'hop_name_1': entry['JournalID']['hop_name_1']})
        data.update({'hop_amount_1': entry['JournalID']['hop_amount_1']})
        data.update({'hop_alpha_acid_1': entry['JournalID']['hop_alpha_acid_1']})
        data.update({'hop_time_1': entry['JournalID']['hop_time_1']})

        data.update({'hop_name_2': entry['JournalID']['hop_name_2']})
        data.update({'hop_amount_2': entry['JournalID']['hop_amount_2']})
        data.update({'hop_alpha_acid_2': entry['JournalID']['hop_alpha_acid_2']})
        data.update({'hop_time_2': entry['JournalID']['hop_time_2']})

        data.update({'hop_name_3': entry['JournalID']['hop_name_3']})
        data.update({'hop_amount_3': entry['JournalID']['hop_amount_3']})
        data.update({'hop_alpha_acid_3': entry['JournalID']['hop_alpha_acid_3']})
        data.update({'hop_time_3': entry['JournalID']['hop_time_3']})

        data.update({'Whirlfloc': entry['JournalID']['Whirlfloc']})
        data.update({'Whirlpool_time': entry['JournalID']['Whirlpool_time']})
        data.update({'Boil_notes': entry['JournalID']['Boil_notes']})
    
    elif which_form == 3:
        data.update({'Yeast_name': entry['JournalID']['Yeast_name']})
        data.update({'Yeast_amount': entry['JournalID']['Yeast_amount']})
        data.update({'Start_gravity': entry['JournalID']['Start_gravity']})

        data.update({'temp_1': entry['JournalID']['temp_1']})
        data.update({'time_1': entry['JournalID']['time_1']})
        data.update({'End_gravity_1': entry['JournalID']['End_gravity_1']})

        data.update({'temp_2': entry['JournalID']['temp_2']})
        data.update({'time_2': entry['JournalID']['time_2']})
        data.update({'End_gravity_2': entry['JournalID']['End_gravity_2']})

        data.update({'temp_3': entry['JournalID']['temp_3']})
        data.update({'time_3': entry['JournalID']['time_3']})
        data.update({'End_gravity_3': entry['JournalID']['End_gravity_3']})

        data.update({'ABV': entry['JournalID']['ABV']})
        data.update({'Lager_temp': entry['JournalID']['Lager_temp']})
        data.update({'Lager_time': entry['JournalID']['Lager_time']})
        data.update({'Fermentation_notes': entry['JournalID']['Fermentation_notes']})

