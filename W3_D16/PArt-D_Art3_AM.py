"""
Day 16 · AM Session · Take-Home Assignment
Part D — AI-Augmented Task
"""

# 1. Prompt AI: 
# 'Explain Type I and Type II errors in the context of a fraud detection system. 
#  What are the real-world consequences of each, and how do you balance them?'

# 2. Document prompt and output.

"""
--- AI PROMPT ---
'Explain Type I and Type II errors in the context of a fraud detection system. 
What are the real-world consequences of each, and how do you balance them?'

--- AI OUTPUT ---
In fraud detection, Type I and Type II errors represent the two ways a system can get it wrong:

1. Type I Error (False Positive): The system flags a legitimate transaction as fraudulent.
   - Real-world Consequences: Legitimate customers are inconvenienced (declined cards, locked accounts). This leads to customer frustration, loss of trust, and increased operational costs for customer support.
   
2. Type II Error (False Negative): The system fails to flag a truly fraudulent transaction as fraud.
   - Real-world Consequences: The business suffers direct financial loss (chargebacks, stolen funds). If frequent, it can lead to regulatory penalties and a reputation for being 'easy to exploit.'

Balancing them:
This is a classic precision-recall tradeoff. By lowering the detection threshold, you catch more fraud (fewer Type II errors) but annoy more customers (more Type I errors). Banks usually tune this threshold based on the 'cost of the error.' A $10,000 transaction might have a lower threshold for flagging than a $5 cup of coffee.
"""

# 3. Evaluate: Does the AI correctly explain the precision-recall tradeoff as the Type I/II error tradeoff?

"""
--- Evaluation ---
The AI correctly identifies the relationship between statistical errors and the precision-recall tradeoff. 

- Type I errors (False Positives) directly affect Precision: As Type I errors increase, Precision decreases (Precision = TP / (TP + FP)).
- Type II errors (False Negatives) directly affect Recall: As Type II errors increase, Recall decreases (Recall = TP / (TP + FN)).

The AI’s explanation of balancing the errors via thresholds is spot on for a business context. It accurately describes how a fraud system must decide which error is more "expensive" and adjust accordingly. The example of the $10,000 transaction vs. a $5 transaction perfectly illustrates the real-world application of cost-benefit analysis in statistical decision-making.
"""
