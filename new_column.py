import csv

# abra o arquivo CSV de entrada e crie um objeto csv.reader
with open('rebec.csv', 'r', newline='', encoding="utf-16") as input_file:
    csv_reader = csv.reader(input_file, delimiter=';')
    
    # abra o arquivo CSV de saída e crie um objeto csv.writer
    with open('novo_arquivo.csv', 'w', encoding="utf-16", newline='') as output_file:
        csv_writer = csv.writer(output_file, delimiter=';')
        
        for row in csv_reader:
            try:
                # Remove espaços em branco do começo e final de todas as strings em cada linha
                row = [item.strip() for item in row]

                col4 = row[4]
                col5 = row[5]
                nova_coluna = ''

                padroes_texto = ['\n', '\t', 'XVI - ', 'XVII - ', 'XVIII - ', 'XIX - ', 'XX - ', 'XXI - ', 'XXII - ', 'XXIII - ', 'II - ', 'III - ', 'IV - ', 'V - ', 'VI - ', 'VII - ', 'VIII - ', 'IX - ', 'X - ', 'XI - ', 'XII - ', 'XIII - ', 'XIV - ', 'XV - ', 'I - ']
                for padrao in padroes_texto:
                    if padrao in col5:
                        nova_coluna = col5.replace(padrao, "")
                        break
                    elif 'pain' in col4.lower() or 'pain' in col5.lower():
                        nova_coluna = 'Pain'
                    elif 'covid' in col4.lower() or 'covid' in col5.lower() or 'coronavirus' in col4.lower() or 'coronavirus' in col5.lower() or 'SARS' in col5.lower():
                        nova_coluna = 'Coronavirus infections'
                    elif 'obesity' in col4.lower() or 'Metabolic' in col5.lower() or 'Diabetes' in col5.lower() or 'pancrea' in col5.lower() or 'endocrine' in col5.lower():
                        nova_coluna = 'Endocrine, nutritional and metabolic diseases'
                    elif 'stress' in col5.lower() or 'anxiety' in col5.lower() or 'psyco' in col5.lower() or 'compulsive' in col5.lower() or 'autism' in col5.lower() or 'mental' in col5.lower() or 'dissociative' in col5.lower() or 'intelectual' in col5.lower() or 'behav' in col5.lower():
                        nova_coluna = 'Mental, Behavioral and Neurodevelopmental disorders'
                    elif 'joint' in col5.lower() or 'arthriti' in col5.lower() or 'myalg' in col5.lower() or 'musculo' in col5.lower() or 'muscles' in col5.lower() or 'osteo' in col5.lower() or 'tendon' in col5.lower():
                        nova_coluna = 'Diseases of the musculoskeletal system and connective tissue'
                    elif 'cardiac' in col5.lower() or 'cardiovascular' in col5.lower():
                        nova_coluna = 'Cardiovascular Diseases'
                    elif 'vascular' in col5.lower() or 'venous' in col5.lower() or 'heart' in col5.lower() or 'pulm' in col5.lower() or 'arter' in col5.lower() or 'lymph' in col5.lower() or 'circulatory' in col5.lower():
                        nova_coluna = 'Diseases of the circulatory system'
                    elif 'virus' in col5.lower() or 'viruses' in col5.lower() or 'bacteria' in col5.lower() or 'sepsis' in col5.lower() or 'septicemia' in col5.lower():
                        nova_coluna = 'Certain infectious and parasitic diseases'
                    elif 'Renal' in col5.lower() or 'urinary' in col5.lower() or 'genital' in col5.lower() or 'pelvic' in col5.lower() or 'kidney' in col5.lower() or 'renal' in col5.lower():
                        nova_coluna = 'Diseases of the genitourinary system'
                    elif 'Tooth' in col5.lower() or 'molar' in col5.lower() or 'periodont' in col5.lower() or 'periapical' in col5.lower() or 'dentis' in col5.lower() or 'teeth' in col5.lower():
                        nova_coluna = 'Tooth diseases'
                    elif 'tongue' in col5.lower() or 'intestine' in col5.lower() or 'oral' in col5.lower() or 'digestive' in col5.lower() or 'stoma' in col5.lower() or 'esopha' in col5.lower() or 'gingiva' in col5.lower():
                        nova_coluna = 'Diseases of the digestive system'
                    elif 'Urticaria' in col5.lower() or 'erythema' in col5.lower() or 'eczema' in col5.lower() or 'acne' in col5.lower() or 'Dermatitis' in col5.lower() or 'skin' in col5.lower():
                        nova_coluna = 'Diseases of the skin and subcutaneous tissue'
                    elif 'health services' in col5.lower() or 'nurs' in col5.lower():
                        nova_coluna = 'Factors influencing health status and contact with health services'
                    elif 'sleep' in col5.lower():
                        nova_coluna = 'Sleep disorders'
                    elif 'ear' in col5.lower() or 'mastoid' in col5.lower():
                        nova_coluna = 'Diseases of the ear and mastoid process'
                    elif 'respiratory' in col5.lower() or 'Influenza' in col5.lower() or 'Influenza' in col5.lower() or 'pneumonia' in col5.lower() or 'Lung' in col5.lower() or 'asma' in col5.lower() or 'asthma' in col5.lower():
                        nova_coluna = 'Diseases of the respiratory system'
                    elif 'Pregnancy' in col5.lower() or 'obstetric' in col5.lower() or 'childbirth' in col5.lower() or 'puerperium' in col5.lower() or 'labor' in col5.lower() or 'delivery' in col5.lower() or 'gestac' in col5.lower():
                        nova_coluna = 'Pregnancy, childbirth and the puerperium'
                    elif 'anemias' in col5.lower() or 'marrow' in col5.lower() or 'Coagulation' in col5.lower() or 'hemorrha' in col5.lower():
                        nova_coluna = 'Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism'
                    elif 'care' in col5.lower() or 'safety' in col5.lower():
                        nova_coluna = 'Patient care related studies'
                    elif 'parkins' in col5.lower():
                        nova_coluna = 'Parkinsons disease'
                    elif 'eye' in col5.lower() or 'conjunct' in col5.lower() or 'cornea' in col5.lower() or 'iris' in col5.lower() or 'retina' in col5.lower() or 'optic' in col5.lower() or 'ocular' in col5.lower() or 'ophtha' in col5.lower():
                        nova_coluna = 'Diseases of the eye and adnexa'
                    elif 'nerv' in col5.lower() or 'neural' in col5.lower():
                        nova_coluna = 'Diseases of the nervous system'
                    elif 'physical' in col5.lower() or 'pilates' in col5.lower() or 'sport' in col5.lower():
                        nova_coluna = 'Physical-related studies'
                    else:
                        nova_coluna = col5
            except IndexError:
                print("A linha não tem elementos suficientes")        
            row.append(nova_coluna)
            csv_writer.writerow(row)
