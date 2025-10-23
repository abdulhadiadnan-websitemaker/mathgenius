from sympy import symbols, Eq, solve, simplify, factor, expand

print("👋 Hi! I'm MathHelper AI. Ask me any simple math questions or linear equations!")

x, y, z = symbols('x y z')

while True:
    question = input("\nEnter your math problem (or 'exit' to quit): ")

    if question.lower() == "exit":
        print("Goodbye! 👋")
        break

    try:
        # Try to simplify or solve equations
        if "=" in question:
            left, right = question.split("=")
            eq = Eq(simplify(left), simplify(right))
            steps = f"Simplify both sides:\n→ {simplify(left)} = {simplify(right)}"
            solution = solve(eq)
            print(steps)
            print("Solve for variable:")
            print("→ Solution:", solution)
        else:
            result = simplify(question)
            print("Simplify the expression:")
            print("→", result)

    except Exception as e:
        print("Sorry, I couldn’t understand that. Try a simple equation like:")
        print("Example: 2x + 5 = 15 or (x+2)*(x+3)")
history = []

while True:
    question = input("Question: ")

    if question.lower() == "exit":
        break

    # ... solve question ...
    answer = "Your answer here"

    # save to memory
    history.append((question, answer))

    print("AI:", answer)
    print("\n📘 Memory so far:")
    for q, a in history:
        print(f"- {q} → {a}")
with open("memory.txt", "a") as file:
    file.write(f"Q: {question}\nA: {answer}\n\n")
    with open("memory.txt", "r") as file:int(file.read())

    from sympy import symbols, Eq, solve, simplify, expand, factor
import re

# Define common variables
x, y, z = symbols('x y z')

# Memory to store past questions & answers
memory = []

print("👋 Hi! I'm SmartMath AI — I can solve 1–7 grade math problems step by step!")
print("Type 'history' to see past questions, or 'exit' to quit.\n")

while True:
    question = input("🧮 Enter your math problem: ").strip()

    if question.lower() == "exit":
        print("Goodbye! 👋")
        break

    if question.lower() == "history":
        print("\n📘 Your previous questions:")
        if not memory:
            print("No history yet.")
        else:
            for q, a in memory[-10:]:
                print(f"→ {q} = {a}")
        print()
        continue

    try:
        # Clean input a bit
        question = question.replace("^", "**")  # allow ^ for powers

        # Detect equation vs expression
        if "=" in question:
            left, right = question.split("=")
            eq = Eq(simplify(left), simplify(right))
            solution = solve(eq)

            print("🔹 Step 1: Simplify both sides.")
            print(f"     {simplify(left)} = {simplify(right)}")
            print("🔹 Step 2: Solve for the variable.")
            print("     Solution:", solution)
            memory.append((question, solution))

        else:
            # For plain expressions
            simple = simplify(question)
            expanded = expand(simple)
            factored = factor(expanded)

            print("🔹 Step 1: Simplify expression.")
            print("     =", simple)
            if expanded != simple:
                print("🔹 Step 2: Expand it.")
                print("     =", expanded)
            if factored != expanded:
                print("🔹 Step 3: Factorize if possible.")
                print("     =", factored)

            memory.append((question, simple))

    except Exception as e:
        print("⚠️ Sorry, I couldn’t understand that.")
        print("Try examples like:")
        print("   2x + 5 = 15")
        print("   (x+2)*(x+3)")
        print("   3 + 4 * 2\n")
   # Save each question & answer to a file
with open("math_memory.txt", "a", encoding="utf-8") as f:
    f.write(f"Q: {question}\nA: {solution if '=' in question else simple}\n\n")
    from sympy import symbols, Eq, simplify, solve
from sympy.solvers.solveset import linear_eq_to_matrix

x, y, z = symbols('x y z')

def explain_linear_equation(eq_str):
    """Return detailed working for a one-variable linear equation."""
    eq_str = eq_str.replace("^", "**")
    left, right = eq_str.split("=")
    eq = Eq(simplify(left), simplify(right))
    print("🔹 Step 1 – Simplify both sides:")
    print("     ", eq)

    # bring everything to one side (ax + b = 0)
    simplified = Eq(eq.lhs - eq.rhs, 0)
    print("🔹 Step 2 – Move all terms to one side:")
    print("     ", simplified)

    # find a, b for ax + b = 0
    A, b = linear_eq_to_matrix([simplified], [x])
    a_val = A[0]
    b_val = b[0]
    print(f"🔹 Step 3 – Identify coefficients: a = {a_val}, b = {b_val}")

    # solving
    sol = solve(simplified, x)[0]
    print("🔹 Step 4 – Solve:")
    print(f"     x = −b/a = −({b_val}) / ({a_val})")
    print(f"     x = {sol}")
    return sol


print("👋 Hi, I’m EquationMaster AI – I show each step clearly!\n")
while True:
    q = input("Enter an equation (or exit): ").strip()
    if q.lower() == "exit":
        break
    try:
        explain_linear_equation(q)
    except Exception as e:
        print("⚠️ Try a simple linear equation like 2x + 5 = 15\n")
        