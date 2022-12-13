from src.logic.classification import Classification

classification = Classification()

classification.generate_initial_points()
classification.generate_new_points()

classification.perform_classification()