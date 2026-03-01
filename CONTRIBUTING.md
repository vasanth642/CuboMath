# Contributing to CuboMath

Welcome, Math Wizard!  
Thank you for your interest in contributing to **CuboMath**.

CuboMath is a community-driven Python library where contributors share
**clever, fun, and educational mathematical functions**.  
This is a place where math ideas turn into clean, readable code — and where
learners and builders grow together.

Whether you are a student, developer, or math enthusiast, **your magic is welcome here**.

---

##  What Can You Contribute?

You can contribute in many ways:

- New mathematical functions or tricks
- Optimized or more elegant implementations
- Documentation improvements
- Tests for existing functions
- Bug fixes
- Creative math ideas explained through code

If it feels **interesting, clever, or educational**, it belongs here.

---

## Contribution Philosophy

CuboMath values:

- **Clarity over cleverness**
- **Readability over complexity**
- **Learning over showing off**

Every contribution should feel like a small lesson — something another
developer or student can learn from.

---

##  Getting Started

### 1. Fork the Repository
Click the **Fork** button on GitHub to create your own copy of the repository.

### 2. Clone Your Fork
```bash
git clone https://github.com/your-username/CuboMath.git
cd CuboMath
```

### 3. Create a New Branch
```bash
git checkout -b feature/your-math-magic
```

### 4.Adding a New Mathematical Function

When adding a new function:

- Place it in the appropriate module
- Use clear and meaningful variable names
- Keep the implementation simple and readable
- Avoid unnecessary dependencies

Function Requirements:

- Every function should include:
- A proper docstring
- A short explanation of the idea or formula
- Example usage if helpful

### Writing Tests

Test are mandatory for any function that is created.
- Add tests inside the tests/ directory
- Use clear and simple test cases
- Focus on correctness

Steps to write test and run locally:
- Create a seperate  test file for each function and place it in the directory: CUBOMATH/tests/.
- write  tests using the unittest library from python since it has been used as a standard testing tool for CuboMath.
- in the terminal install the library locally in editable  mode using the comand:
```bash
pip install -e .
```
- run the tests using the following command:
```bash
python -m unittest discover -s tests
```
this command will run all the test files .
- If you want to test your specific test file, use the command:
```bash
python tests/your_testfile.py
```

### Code Style Guidelines

- Follow PEP 8
- Prefer readability over short tricks
- Avoid deeply nested logic
- Keep each function focused on one idea
- Readable code is more valuable than clever code.

### Submitting Your Contribution

1.Stage your changes:
```bash
git add .
```

2.Commit your changes:
```bash
git commit -m "Add: new math function for XYZ"
```

3.Push your Branch:
```bash
git push origin feature/your-math-magic
```

4.Open a pull request from github to the upstream.

### Pull Request Guidelines:
In your pull request, describe:
- What you added or changed
- Why it is useful or interesting
- Any math concept involved (briefly)

### Community Rules:
- Be respectful
- Help others learn
- No plagiarism
- Feedback should focus on code, not people
