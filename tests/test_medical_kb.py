import unittest
from backend.medical_kb import MedicalKnowledgeBase

class TestMedicalKnowledgeBase(unittest.TestCase):
    def setUp(self):
        self.kb = MedicalKnowledgeBase()

    def test_get_disease(self):
        disease = self.kb.get_disease('fever')
        self.assertEqual(disease, 'Flu')

    def test_get_medication(self):
        medication = self.kb.get_medication('cough')
        self.assertEqual(medication, 'Cough Syrup')

    def test_add_mapping(self):
        self.kb.add_mapping('dizziness', 'Vertigo', 'Antihistamine')
        disease = self.kb.get_disease('dizziness')
        self.assertEqual(disease, 'Vertigo')

    def test_remove_mapping(self):
        self.kb.remove_mapping('fever')
        disease = self.kb.get_disease('fever')
        self.assertEqual(disease, 'Unknown Disease')

if __name__ == '__main__':
    unittest.main()