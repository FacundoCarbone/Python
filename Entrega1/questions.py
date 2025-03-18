import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    ("// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario"),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Unir las preguntas, respuestas y respuestas correctas en un solo iterable
question_data = list(zip(questions, answers, correct_answers_index))

# Elegir 3 preguntas aleatorias sin repetición
questions_to_ask = random.sample(question_data, k=3)

puntaje = 0.0

# El usuario deberá contestar 3 preguntas
for question, possible_answers, correct_index in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(possible_answers):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        try:
            user_answer = int(input("Respuesta: ")) - 1
            if user_answer < 0 or user_answer >= len(possible_answers):
                print('Respuesta no válida')
                sys.exit(1)
            # Se verifica si la respuesta es correcta
            if user_answer == correct_index:
                print("¡Correcto!")
                puntaje += 1
                break
        except ValueError:
            print('Respuesta no válida')
            sys.exit(1)
        else:
            puntaje -= 0.5

    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(possible_answers[correct_index])

    # Se imprime un blanco al final de la pregunta
    print()

# Se imprime el puntaje final de manera más clara
print(f"¡Juego terminado! Su puntuación final es: {puntaje}")