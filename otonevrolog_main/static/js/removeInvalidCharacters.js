
  function removeInvalidCharacters(input) {
    // Разрешаваме само букви и интервали
    input.value = input.value.replace(/[^a-zA-Zа-яА-Я\s]/g, '');
  }
