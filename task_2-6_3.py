
patient_blood = input("\n\tВведите фенотип группы крови пациента (I, II, III, IV): ").strip().upper()
donor_blood = input("\n\tВведите фенотип группы крови донора (I, II, III, IV): ").strip().upper()

if patient_blood == "I":
    if donor_blood == "I":
        print("\nГруппы совместимы, переливание возможно")
    else:
        print("\nГруппы несовместимы, переливание невозможно\n Подойдут группы: I(0)")
elif patient_blood == "II":
    if donor_blood == "I" or donor_blood == "II":
        print("\nГруппы совместимы, переливание возможно")
    else:
        print("\nГруппы несовместимы, переливание невозможно\n Подойдут группы: I(0), II(А)")
elif patient_blood == "III":
    if donor_blood == "I" or donor_blood == "III":
        print("\nГруппы совместимы, переливание возможно")
    else:
        print("\nГруппы несовместимы, переливание невозможно\n Подойдут группы: I(0), III(В)")
elif patient_blood == "IV":
    if donor_blood == "I" or donor_blood == "II" or donor_blood == "III" or donor_blood == "IV":
        print("\nГруппы совместимы, переливание возможно")
else:
    print("\nВведите корректные группы крови (I, II, III, IV)")


