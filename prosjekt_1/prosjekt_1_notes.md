# Number Guessing Game

### Main Tasks

1. Generate int between that's >1 and <100
2. Guess input in 5 attempts
3. After fail, tell if it's above or below
4. Display remaining attempts
5. If fails in 5 attempts, display message 
`Sorry! You did not manage to guess the number. You have reached the guessing limit.`
6. If guessed correct, display message
`Congratulations! You guessed the number in ** attempt(s)."`
7. Ask if they want to play again. if yes, start new game. Generate new number and start again.

### Prototype plan

*Variables*
- Define variable 5 LIVES
- Define variable >1 and <100 RANDOM-NUMBER

1. Start main loop
2. Explain game rules, request input.
    1. If input is yes, proceed with game, start next loop.
    2. If input is no, stop the game
3. Start loop. Check if LIVES = 0
    1. If lives = >0, continue
    2. If lives = 0, print lose message.
4. Ask for user input. 
    1. If INPUT = RANDOM-NUMBER, exit loop, print win message
    2. If INPUT =/ RANDOM-NUMBER, LIVES - 1, return.

*Potantial things to add*
- "Want to try again?" message on loss
