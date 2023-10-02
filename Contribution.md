# Contribution Guidelines for Project-Wizard

Thank you for considering contributing to Project-Wizard! We welcome contributions from engineering graduates and enthusiasts interested in adding open-source projects to our repository. Please follow these guidelines to make your contributions as smooth as possible.

## Getting Started

Before you start contributing, make sure you have Git installed on your system and have created a GitHub account. Here are the basic steps to contribute:

1. Fork the Project-Wizard repository to your GitHub account.
2. Clone your forked repository to your local machine using `git clone`.
3. Create a new branch for your contribution using `git checkout -b your-branch-name`.

## Project and Game Structure

The repository has two main folders: `Projects` and `Games`. When adding a new project or game, follow these guidelines:

1. **Folder Structure:**

   - For projects, create a new folder in the `Projects` directory.
   - For games, create a new folder in the `Games` directory.

   Example: `Projects/MyProject` or `Games/MyGame`

2. **Content Files:**

   - Place all the content files for your project or game within the respective folder.
   
   Example: If your game is called "Snake Game," place the game's content files inside `games/SnakeGame`.

3. **Main Program File:**

   - Ensure that your project or game includes a main program file named `main.__` (e.g., `main.py` for Python projects).
   
   Example: `Games/SnakeGame/main.py`

4. **Additional Files:**

   - Include any other necessary files, such as data files or assets, within the folder.

5. **Executable and Compatibility:**

   - Ensure that your project or game is executable on various systems. If specific versions or dependencies are required, mention them in your project's README.

6. **Documentation:**

   - Provide clear and concise documentation within your project's folder, including instructions on how to run and use your project or game.

7. **Requirements.txt:**

   - For Python projects, create a `requirements.txt` file if your project depends on specific Python modules or packages.

## Contribution Process

To contribute to Project-Wizard, follow these steps using Git or GitHub Desktop:

#### Using Git:

1. Fork the Project-Wizard repository to your GitHub account.

2. Clone your forked repository to your local machine:
   ```shell
   git clone https://github.com/pralinkhaira/Project-Wizard.git
   ```

3. Create a new branch for your project or game:
   ```shell
   git checkout -b feature/your-project-name
   ```

4. Add your project or game files to the appropriate folder as described above.

5. Commit your changes:
   ```shell
   git add .
   git commit -m "Add your project/game: Snake Game"
   ```

6. Push your changes to your forked repository:
   ```shell
   git push origin feature/your-project-name
   ```

7. Create a pull request from your forked repository to the main Project-Wizard repository on GitHub.

8. Once your pull request is reviewed and approved, it will be merged into the main repository.

#### Using GitHub Desktop:

1. Open GitHub Desktop and sign in to your GitHub account.

2. Clone the Project-Wizard repository to your local machine using GitHub Desktop.

3. Create a new branch for your project or game using GitHub Desktop.

4. Add your project or game files to the appropriate folder as described above.

5. Commit your changes using GitHub Desktop.

6. Push your changes to your forked repository using GitHub Desktop.

7. Create a pull request from your forked repository to the main Project-Wizard repository on GitHub.

8. Once your pull request is reviewed and approved, it will be merged into the main repository.

## Submitting Your Contribution

Once you have added your project or game, follow these steps to submit your contribution:

1. Commit your changes to your branch using `git commit`.

2. Push your changes to your forked repository on GitHub using `git push`.

3. Create a Pull Request (PR) from your forked repository to the main Project-Wizard repository. Ensure that you provide a clear title and description for your PR.

4. Our team will review your contribution, and if it meets our guidelines and is valuable to the community, we will merge it.

5. Congratulations! You have successfully contributed to Project-Wizard.

## Note

- Fake or invalid contributions will not be accepted.

- If your project includes bugs, we may ask you to update or fix them before merging.

- We do not accept contributions that only update the README.md.

Thank you for your contribution to Project-Wizard. Your efforts help create a valuable resource for engineering graduates and enthusiasts. Happy coding!
