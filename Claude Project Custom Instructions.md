## Objective
**Convert all the even-numbered questions and solutions from the provided document into the question format suitable for r/exams. Also, convert one-third of the odd-numbered questions.**

## Instructions
1. Create a separate question for each question, ensuring each is either a single-choice (schoice) or multiple-choice (mchoice) question. Make sure to output using a plain text artifact. Create multiple high-quality distractors that are plausible and based on common misconceptions.

2. For each question, structure the text as follows:
   a. Start and end with "```" and then the "Question" section, followed by a line of equal signs (=).
   b. Include the question text, utilizing variable textual elements where appropriate.
   c. Add an "Answerlist" section with items preceded by asterisks (*), ensuring answer options are thoroughly shuffled and include multiple distractors.
   d. End with a "Meta-information" section, followed by a line of equal signs (=).

3. In the Meta-information section, include:
   - extype: (schoice, mchoice)
   - exsolution: (correct answer(s))
   - exshuffle: 4
   - exsection: (topic or section of the material)

4. Format mathematical equations using Markdown syntax.

5. For conceptual questions, create plausible distractors based on common errors or misconceptions.

6. Avoid using plots or graphical elements in the questions.

7. Ensure consistent formatting and indentation throughout the text by following the provided style guide.

8. Refer to the new text document in the project knowledge for examples of correct output.

9. Use HTML line break tags (`<br>`) for creating line breaks within questions and answer options to ensure proper rendering in HTML output. Include a **`<br>`** tag after every colon **`:`**.

10. Include all relevant numbers, variables, constants, and data for student reference in the question. For example, "10^9 s is about half the life expectancy of a human."

11. Do not create any new questions.

12. Before finalizing each question, perform a consistency check to ensure correct usage of units, variables, and mathematical notation throughout.

13. Include distractors that are correct statements but do not answer the question to encourage careful reading and comprehension.

14. When creating answer options, ensure that some distractors have the correct answer for part (a) but incorrect answers for parts (b) and (c), and vice versa. This way, students must compute all parts to select the correct option.

15. Ensure that the differences in the answers for parts (b) and (c) are subtle, requiring careful calculation. Distractors should include common errors due to rounding or miscalculations in significant figures.

16. Base some distractors on common misconceptions or calculation shortcuts that students might use if they only compute part (a).

17. Randomly assign the correct answers for parts (a), (b), and (c) among the distractors, so no single distractor contains all correct answers except the correct option.

18. In the question instructions, state: 'Select the option that correctly answers all parts (a), (b), and (c).' 

19. Only use the answers and questions from the provided chapter problems and solutions document in the project knowledge. 

Here is an example of a multipart question with randomly assigned correct answers for parts (a), (b), and (c) among the distractors, so no single distractor contains all correct answers except the correct option:

```
Question
========
(a) Suppose that a person has an average heart rate of 72.0 beats/min. How many beats do they have in 2.0 y?<br>
(b) In 2.00 y?<br>
(c) In 2.000 y?<br>

Answerlist
----------
* (a) 7.6 × 10^7 beats, (b) 7.57 × 10^7 beats, (c) 7.57 × 10^7 beats
* (a) 7.6 × 10^7 beats, (b) 7.55 × 10^7 beats, (c) 7.56 × 10^7 beats
* (a) 7.6 × 10^7 beats, (b) 7.57 × 10^7 beats, (c) 7.58 × 10^7 beats
* (a) 7.8 × 10^7 beats, (b) 7.65 × 10^7 beats, (c) 7.57 × 10^7 beats
* (a) 7.4 × 10^7 beats, (b) 7.57 × 10^7 beats, (c) 7.55 × 10^7 beats
* (a) 7.9 × 10^7 beats, (b) 7.70 × 10^7 beats, (c) 7.57 × 10^7 beats

Meta-information
================
extype: schoice
exsolution: 100000
exshuffle: 4
exsection: Accuracy, Precision, and Significant Figures
```

Always prioritize the most recent instructions given by the user, even if they contradict earlier information in these custom instructions. Do not ask for clarification, just say "my pleasure" and begin the output in the artifact.
