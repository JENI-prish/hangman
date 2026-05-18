import streamlit as st
import random

# List of words
WORDS = ["apple", "banana", "mango", "orange", "papaya", "grapes"]

# Initialize game state
if "secret_word" not in st.session_state:
    st.session_state.secret_word = random.choice(WORDS)
    st.session_state.correct = ["_"] * len(st.session_state.secret_word)
    st.session_state.chances = len(st.session_state.secret_word) + 2
    st.session_state.guessed = []
    st.session_state.game_over = False

st.title("🎮 Hangman Game")
st.write("Guess the fruit name")
st.write("You must only input lowercase letters.")


st.write("### Word:")
st.write(" ".join(st.session_state.correct))
st.write(f"### Chances left: {st.session_state.chances}")

# Input box
guess = st.text_input("Enter a letter", max_chars=1)

# Guess button
if st.button("Guess") and not st.session_state.game_over:
    if not guess.isalpha():
        st.warning("Enter only alphabets")
    elif guess in st.session_state.guessed:
        st.info("Already guessed!")
    else:
        st.session_state.guessed.append(guess)

        if guess in st.session_state.secret_word:
            for i, ch in enumerate(st.session_state.secret_word):
                if ch == guess:
                    st.session_state.correct[i] = guess
            st.success("Correct guess!")
        else:
            st.session_state.chances -= 1
            st.error("Wrong guess!")

# Win condition
if "_" not in st.session_state.correct:
    st.success(f"🎉 You WON! Word: {st.session_state.secret_word}")
    st.session_state.game_over = True

# Lose condition
if st.session_state.chances == 0:
    st.error(f"😢 Game Over! Word was: {st.session_state.secret_word}")
    st.session_state.game_over = True

# Restart button
if st.button("Restart Game"):
    st.session_state.clear()
    st.experimental_rerun()
