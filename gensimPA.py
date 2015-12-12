import csv
import gensim
model = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

with open('validation_set.tsv', 'r') as tsvin, open ('new.csv', 'w') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    #csvout = csv.writer(csvout)
    #For each question in the psread sheet.
    for row in tsvin:
        # Average for question
        avgQ = 0
        for word in row[1].split():
            if word not in model: continue
            avgQ = avgQ + model[word]
        avgQ = avgQ/len(row[1].split())
        #Averages for answers 
        avgA = 0
        for word in row[2].split():
            if word not in model: continue
            avgA = avgA + model[word]
        avgA = avgA/len(row[2].split())
        
        avgB = 0
        for word in row[3].split():
            if word not in model: continue
            avgB = avgB + model[word]
        avgB = avgB/len(row[3].split())
        
        avgC = 0
        for word in row[4].split():
            if word not in model: continue
            avgC = avgC + model[word]
        avgC = avgC/len(row[4].split())
        
        avgD = 0
        for word in row[5].split():
            if word not in model: continue
            avgD = avgD + model[word]
        avgD = avgD/len(row[5].split())
        
        distA = abs(avgQ - avgA)
        distB = abs(avgQ - avgB)
        distC = abs(avgQ - avgC)
        distD = abs(avgQ - avgD)
        #print min(distA, distB, distC, distD)
        csvout.write( row[0] + ',' + min(distA, distB, distC, distD)+'\n')
