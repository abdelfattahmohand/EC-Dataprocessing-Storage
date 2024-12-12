# EC-Dataprocessing-Storage
ESEP Extra Credit assignment

## Here is the output of the main function tests from fig.2 of the assignment insturctions:
<img width="800" alt="Screen Shot 2024-12-11 at 8 59 15 PM" src="https://github.com/user-attachments/assets/6ca70469-1527-41d8-b0cb-821fa15e2d99" />

This output demonstrates code functionality as it closely follows the expected behavior presented in fig.2.

## How to run the code:
To run the code simply fork and clone the repository to your local machine, then open the project in the IDE of your choice or navigate to it via the command line. Once the project is opened simply click the run button in the IDE environment, or if you are using the terminal, run this command in the terminal:
```
python db.py
```
Upon running, you will see a similiar output as displayed above because of the function tests written in the main function.

## How this assignment should be modified to become an official assignment:
To make this assignment more official, we can make it more challaenging by requiring funcionality of multiple users and multiple transactions at once (1 transaction per user), introducing the complexity of making sure the transactions dont collide and corrupt one another. Also, we can explore requiring functionality that makes the database save its contents when a session ends, we can easily do this by making the database write its contents to a file upon close, and reading the file again when the databse starts back up. Finally, consider requiring students to come up with at least 5 unit tests that cover all the functionality of the database, giving them unit testing experience that is very important in industry. This are some ideas to make this assignment match the difficulty of the other assignments while also letting students practice valuable skills like testing. If I had to pick one out of the 3 ideas to implement, I would definitely pick the unit testing idea because it is an actual useful skill to learn to come up with comprehensive tests.
