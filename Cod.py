from sklearn import ensemble, metrics
import numpy as np

date =np.zeros((100, 9))
j = 0
etichete = ['']*100

with open('fertility_Diagnosis.txt','r') as f:
    for j in range(100):
        line = f.readline()
        line = line.split(",", 9)
        
        for i in range(9):
            line[i] = float(line[i])
            
        etichete[j] = line[9]
        etichete[j] = etichete[j].strip()
        date[j] = line[0:9]
        
f.close()

date_train = date[0:75, :]
etichete_train = etichete[0:75]
date_test = date[75:, :]
etichete_test = etichete[75:]

clf = ensemble.RandomForestClassifier(n_estimators = 10, criterion = 'gini', max_samples = 0.25, max_features = 0.10)

clf.fit(date_train, etichete_train)

predictii = clf.predict(date_test)

acuratete = metrics.accuracy_score(y_true = etichete_test, y_pred = predictii)
print('Acuratete test = ', acuratete)