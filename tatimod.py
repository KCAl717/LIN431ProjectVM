################################
#                              #
# Tati Verb Machine Beep Boop  #
#                              #
################################

modality = 0
aspect = 0
polarity = 0
valency = 0
voice = 0
agreement = 0
paralist = []

#To-Do:
##Vowel Harmony

def verb_parameters():
    
    print("Choose modality:")
    print("1.Indicative, 2.Subjunctive, 3.Imperative")

    mod_input = input()

    while mod_input not in ["1", "2", "3"]:
        print("Please choose a number value from 1 to 3")
        mod_input = input()

    global modality
        
    if mod_input == "1":
            modality = "IND"

    elif mod_input == "2":
            modality = "SUBJ"

    elif mod_input == "3":
            modality = "IMP"

                 
            
    print("Choose aspect:")
    print("1.Neutral, 2.Imperfective")

    asp_input = input()

    while (asp_input == "2" and modality != "IND") or asp_input not in ["1", "2"]:
        
        if asp_input == "2" and modality != "IND":
            print("IPFV aspect is not compatible with SUBJ/IMP modality.")
            print("Please make another selection.")
            asp_input = input()

        elif asp_input not in ["1", "2"]:
            print("Please choose a number value from 1 to 2")
            asp_input = input()

    global aspect
    
    if asp_input == "1":
            aspect = "NEU"

    elif asp_input == "2":
            aspect = "IMPV"
        

    print("Choose polarity:")
    print("1.Affirmative, 2.Negative")

    pol_input = input()

    while pol_input not in ["1", "2"]:
        print("Please choose a number value from 1 to 2")
        pol_input = input()

    global polarity
    
    if pol_input == "1":
            polarity = "AFF"

    elif pol_input == "2":
            polarity = "NEG"
            
    print("Choose valency:")
    print("1.Non-causative, 2.causative")

    valency_input = input()

    while valency_input not in ["1", "2"]:
        print("Please choose a number value from 1 to 2")
        valency_input = input()

    global valency
    
    if valency_input == "1":
        valency = "NCAUS"

    elif valency_input == "2":
        valency = "CAUS"
            
        
    print("Choose voice:")
    print("1.Active, 2.Passive")

    voice_input = input()

    while voice_input not in ["1", "2"]:
        print("Please choose a number value from 1 to 2")
        voice_input = input()

    while voice_input == "2" and modality == "IMP":
        print("PASS voice is incompatible with IMP modality.")
        print("Please make another selection.")
        voice_input = input()
    

    global voice
        
    if voice_input == "1":
        voice = "ACT"

    elif voice_input == "2":       
        voice = "PASS"

    print("Choose person:")
    print("1.First-person, 2.Second-person, 3.Third-person")

    pers_input = input()

    while pers_input not in ["1", "2", "3"]:
        print("Please choose a number value from 1 to 3")
        pers_input = input()

    while modality == "IMP" and pers_input != "2":
        print("IMP modality is only compatible with the second-person.")
        print("Please make another selection.")
        pers_input = input()

    global AGR

    if pers_input == "1":
        print("Choose plurality:")
        print("1.Singular, 2.Plural")
        
            
        plur_input = input()
            
        while plur_input not in ["1", "2"]:
            print("Please choose a number value from 1 to 2")
            plur_input = input()
                
        if plur_input == "1":
                AGR = "1SG"

        elif plur_input == "2":
                AGR = "1PL"                            

    elif pers_input == "2":
        print("Choose plurality:")
        print("1.Singular, 2.Plural")

        plur_input = input()
            
        while plur_input not in ["1", "2"]:
            print("Please choose a number value from 1 to 2")
            plur_input = input()
            
        if plur_input == "1":
                    AGR = "2SG"

        elif plur_input == "2":
                    AGR = "2PL"

    elif pers_input == "3":
        print("Choose plurality:")
        print("1.Singular, 2.Plural")

        plur_input = input()

        while plur_input not in ["1", "2"]:
            print("Please choose a number value from 1 to 2")
            plur_input = input()
                
        if plur_input == "1":
            print("Choose gender:")
            print("1.Masculine, 2.Feminine")

            gend_input = input()

            while gend_input not in ["1", "2"]:
                print("Please choose a number value from 1 to 2")
                gend_input = input()
                    
            if gend_input == "1":
                AGR = "M.3SG"

            elif gend_input == "2":
                AGR = "F.3SG"
                        
        elif plur_input == "2":
            AGR = "3PL"
    
            
    global paralist
    paralist = []
    
    paralist.extend([modality, aspect, polarity, valency, voice, AGR])

    return 
    

def conjugate(preverb, stem):

    verb_parameters()


    ##P-3
    
    if preverb == "be":
        if polarity == "NEG" or aspect == "IMPV":
            Pm3 = ""
        
        else:
            Pm3 = preverb
            
    else:
        Pm3 = preverb

    ##P-2

    if aspect == "IMPV":
        
        if preverb in ["a", "e", "i", "o", "u", "æ", "ʌ", "ɛ", "ø"]:
            if polarity == "NEG":
                Pm2 = "m"
            else:
                Pm2 = "n"
        else:
            Pm2 = "me"

    else:
        Pm2 = ""
            
    ##P-1

    if polarity == "NEG":
        if modality == "IMP":
            Pm1 = "ma"
        else:
            Pm1 = "ne"

    else:
        Pm1 = ""
    
    ##P0
        
    if stem[-1] == "d":
        P0 = stem[:-1]

    else:
        P0 = stem
    

    ##P+1

    if valency == "CAUS":
        Pp1 = "den"

    else:
        Pp1 = ""

    ##P+2

    if voice == "PASS":
        
        Pp2 = "i"

    else:
        Pp2 = ""

    ##P+3

    if modality == "IMP":

        if AGR == "2SG":
            Pp3 = "ø"

        elif AGR == "2PL":
            Pp3 = "ʌ"

    else:
        
        if AGR == "1SG":
            Pp3 = "em"  

        elif AGR == "1PL":
            Pp3 = "om"

        elif AGR == "2SG":
            Pp3 = "i"

        elif AGR == "2PL":
            Pp3 = "ʌ"

        elif AGR == "3PL":
            Pp3 = "endɛ"

        elif AGR == "M.3SG":
            Pp3 = "e"
             
        elif AGR == "F.3SG":
            Pp3 = "iɛ"

    ##Ps
    stress = "ˈ"
    
    if polarity == "AFF":
        if modality == "IND":
            UR = Pm3 + Pm2 + Pm1 + P0 + Pp1 + Pp2 + stress + Pp3
            
        else:
            UR = stress + Pm3 + Pm2 + Pm1 + P0 + Pp1 + Pp2 + Pp3

    elif polarity == "NEG":
       UR = Pm3 + Pm2 + stress + Pm1 + P0 + Pp1 + Pp2 + Pp3 


    print("Selected features:")
    print(paralist)
    
    print("Conjugated verb:")
    return print(UR)
    
