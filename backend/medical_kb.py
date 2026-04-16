class MedicalKnowledgeBase:
    def __init__(self):
        # Initialize the medical knowledge base with symptom-disease-medication mappings
        self.mapping = {
            'fever': {
                'disease': 'Flu',
                'medication': 'Acetaminophen'
            },
            'cough': {
                'disease': 'Cold',
                'medication': 'Cough Syrup'
            },
            'headache': {
                'disease': 'Migraine',
                'medication': 'Ibuprofen'
            }
            # Add more symptom mappings as needed
        }

    def get_disease(self, symptom):
        return self.mapping.get(symptom, {}).get('disease', 'Unknown Disease')

    def get_medication(self, symptom):
        return self.mapping.get(symptom, {}).get('medication', 'No Medication Found')

    def add_mapping(self, symptom, disease, medication):
        self.mapping[symptom] = {'disease': disease, 'medication': medication}

    def remove_mapping(self, symptom):
        if symptom in self.mapping:
            del self.mapping[symptom]