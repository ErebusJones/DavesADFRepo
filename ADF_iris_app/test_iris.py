from calc import predict_species


def test_iris_vc():
    # Arrange
    sepal_length = 7.0
    sepal_width = 3.2
    petal_length = 4.7
    petal_width = 1.4
    expected_species = "versicolor"

    # Act
    species_measurements = predict_species(sepal_length, sepal_width, petal_length, petal_width)
    
    # Assert
    assert species_measurements == expected_species


def test_iris_s():
    # Arrange
    sepal_length = 5.1
    sepal_width = 3.5
    petal_length = 1.4
    petal_width = 0.2
    expected_species = "setosa"

    # Act
    species_measurements = predict_species(sepal_length, sepal_width, petal_length, petal_width)
    
    # Assert
    assert species_measurements == expected_species


def test_iris_v():
    # Arrange
    sepal_length = 5.9
    sepal_width = 3.0
    petal_length = 5.1
    petal_width = 1.8
    expected_species = "virginica"

    # Act
    species_measurements = predict_species(sepal_length, sepal_width, petal_length, petal_width)
    
    # Assert
    assert species_measurements == expected_species