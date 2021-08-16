# Pong
Pong game created using python tkinter

# Paddle
Both the paddles are a single block of 'square shaped turtle' stretched vertically. Even though this gives an appearance of a rectangular block it is effectively a square block and the collision between the ball and the 'square block' is checked, when the distance between them both is less than a certain value the ball changes its direction.

# Paddle movement
Both paddles can be controlled in 2 directions (upwards or downwards) using the UP and DOWN arrow keys for 1 player and W and S keys for the other player .

# Ball
The ball is a 'circle shaped turtle'. The ball moves around the screen and checks for collision with walls and paddles. When the ball is collided with the top and bottom walls of the screen or either one of the paddle, it deflects about 90 degree and move in the new direction until a collision occurs

# Score
If the ball misses a paddle and moves past the right or left wall of the screen, the opponent's score gets incremented by 1. Effectively the ball just detects collision with right or left wall of the screen and resets to the ball's original position, the coordinates (0, 0), which is the centre of the screen.
