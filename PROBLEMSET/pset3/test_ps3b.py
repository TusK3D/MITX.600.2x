from ps3b import *
# from ps3b_precompiled_39 import *
durgDict = {"drug1":True, "drug2":True}
"""
virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
patient = TreatedPatient([virus1, virus2, virus3], 100)
print(patient.getResistPop(['drug1']))
print(patient.getResistPop(['drug2']))
print(patient.getResistPop(['drug1','drug2']))
print(patient.getResistPop(['drug3']))
print(patient.getResistPop(['drug1', 'drug3']))
print(patient.getResistPop(['drug1','drug2', 'drug3']))


virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
patient = TreatedPatient([virus1, virus2], 1000000)
patient.addPrescription("drug1")
for i in range(5):
     patient.update()
print(patient.getResistPop(['drug1']))
print(patient.getTotalPop())

def test_TreatedPatient_class():
     patient = TreatedPatient([(ResistantVirus(random.random(), random.random(),
                                               {"guttagonol":False,
                                                "srinol":False},
                                               0.1)) for i in range(10)], 50)
     for i in range(20):
         print(patient.update())
# test_TreatedPatient_class()
"""

simulationWithDrug(100, 1000, 0.1, 0.05, {"guttagonol":False},.005, 100)
simulationWithDrug(100, 1000, 0.1, 0.05, {"guttagonol":False},.005, 10)
simulationWithDrug(10, 100, 0.1, 0.05, {"guttagonol":False},.005, 100)
