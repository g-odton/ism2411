# self-assessment qs
# 1. forgot to answer these, my bad - the first bug i spotted was that one of the loops didn't have a colon, meaning it'd not work, and i found that because of a red squiggle under it. the second one was that sales had a variable that was out of range, which the traceback output thing in the terminal pointed out. since those were the only errors, what this tells me about my debugging is that i rely too much on vscode's shortcuts to actually do things.
# 2. apply_discount assigns 2 parameters (price, tier) to a pair of arguments, and then applies a discount based on the "tier" argument. its inputs are price and tier, and it returns discounted values. a colleague could probably use it without reading the body, provided they know what the tiers' discounts are.
# 3. AI was used to auto-fill in a lot of the code. it shortcut my understanding since, instead of letting me figure things out, i just got handed the answers.

# exercise 1
#define calculate tax function
def calculate_tax(price, rate): 
    return price * rate
# calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}")
print()

# exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85      
    elif tier == "silver":
        return price * 0.90      
    elif tier == "bronze":
        return price * 0.95
    else:
        return price     

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")
print()

# exercise 3

# write out manually first, then refactor into function
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

# refactor
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    total = calculate_tax(discounted, tax_rate)
    return discounted + tax
print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")
print()

# exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")
print()

# exercise 5
# bug 1: SyntaxError: expected ':' -- basically a grammar error in programming language; forgot the : so the code was like a run-off sentence and not 2 separate ones
# bug 2: IndexError: list index out of range -- attempted to access an index that isn't in i
# bug 3: n/a?? no error given when running anymore

def double_it():
    global x
    # x = 999  - local, another appl 
    return x * 2

print(x)           # what prints here? 100, because that's the original variable's value unaffected by double_it
print(double_it()) # what prints here? 1998, because x was used in double_it
print(x)           # has x changed? no because of scope
# scope is a variable/change existing only locally or in a function. the effect of a function on a variable is not universal unless coded otherwise, maybe