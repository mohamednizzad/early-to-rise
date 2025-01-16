# GitHub Copilot Instructions

## Introduction
This document provides custom instructions for using GitHub Copilot effectively in the Early-To-Rise project.

## Instructions

1. **Code Completion**: 
    - Use GitHub Copilot to autocomplete code snippets by starting to type a function or variable name.
    - Press `Tab` to accept the suggestion.

2. **Documentation**:
    - Generate documentation comments by typing `/**` above a function or class.
    - Use Copilot to suggest descriptions and parameter details.

3. **Code Generation**:
    - Write a comment describing the functionality you need.
    - Let Copilot generate the corresponding code.

4. **Refactoring**:
    - Highlight a block of code and describe the desired refactor in a comment.
    - Use Copilot's suggestions to refactor the code.

5. **Testing**:
    - Write test cases by describing the test scenario in a comment.
    - Allow Copilot to generate the test code.

## Project-Specific Instructions

1. **Environment Variables**:
    - Ensure that sensitive information such as the OpenAI API key is stored in environment variables.
    - Use the `dotenv` package to load environment variables from a `.env` file.

2. **Styling**:
    - Use Bootstrap for styling the Streamlit app.
    - Add custom CSS for additional styling needs.

3. **Image Handling**:
    - Use the `PIL` library to create and manipulate images.
    - Ensure that images are saved to a bytes buffer before being used in the app.

4. **File Downloads**:
    - Implement features to download content as `.txt` and `.png` files.
    - Ensure that download buttons are styled and placed appropriately in the layout.

## Best Practices

- **Review Suggestions**: Always review Copilot's suggestions to ensure they meet your requirements and coding standards.
- **Security**: Be cautious of security implications in the generated code.
- **Customization**: Customize Copilot's behavior through the settings to better fit your workflow.

## Conclusion
By following these instructions, you can leverage GitHub Copilot to enhance your coding efficiency and productivity in the Early-To-Rise project.
