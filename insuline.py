with open('preproinsulin-seq.txt') as preproinsulinFile:
    result = []
    for line in preproinsulinFile:
        line = line.replace("\n", "")
        line = line.replace("ORIGIN", "")
        line = line.replace("61", "")
        line = line.replace("1", "")
        line = line.replace("//", "")
        line = line.strip()
        result.append(line)
    finalResult = "".join(result)
    finalResult = finalResult.replace(" ", "")
    with open('preproinsulin_seq_clean.txt', 'w') as preproinsulinCleanFile:
        preproinsulinCleanFile.write(finalResult)

with open('preproinsulin_seq_clean.txt') as preproinsulinCleanFile:
    content = preproinsulinCleanFile.read()
    if (len(content) == 110):
        print("The sequence is the correct length.")

        # Si le nombre de caracteres correspond au resultat attendu,
        # On passe a la suite, recuperer les 24 premiers acides amines 
        # de la sequence et les ecrire dans un nouveau fichier
        firstValues = content[0:24]
        print("The first 24 amino acids are: " + firstValues)
        with open('lsinsulin-seq-clean.txt', 'w+') as preproinsulinLsFile:
            preproinsulinLsFile.write(firstValues)
            # Verifier si le fichier contient bien 24 caracteres
            content2 = preproinsulinLsFile.read()
            if (len(content2) == 24):
                print("The sequence is the correct length.")
            else:
                print("The sequence is the incorrect length.")
    else:
        print("The sequence is the incorrect length.")