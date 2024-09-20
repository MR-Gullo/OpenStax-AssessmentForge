# 🚀 Automated Assessment Workflow

## 📚 OpenStax to LMS: Streamlined Content Creation

This project automates the creation of LMS-ready assessments from OpenStax textbooks using r/exams, Claude AI, Mathpix, and LaTeX.

### 🛠️ Tools Used

- R/exams
- Claude AI (3.5 Sonnet)
- Mathpix
- LaTeX

## 🔄 Detailed Workflow

1. **Prepare OpenStax Content:**
   - Obtain the OpenStax solution manual for your textbook
   - Use Mathpix to convert the manual to Markdown format

2. **AI-Powered Question Conversion:**
   - Use Claude 3.5 Sonnet with the "OpenStax Question Parser" project
   - Convert questions to r/exams format
   - Output: Text file with formatted questions

3. **Question Processing:**
   - Run question_parser.py
   - Input: Text file from step 2
   - Output: Individual .rmd files in "01exercises" folder

4. **Test Generation:**
   - Modify testGen.Rmd (update chapter_num and course_code)
   - Run testGen.Rmd
   - Output: Quiz and test files (HTML and QTI 2.1 zip)

## 🎯 Key Features

- Converts OpenStax questions:
  - All even-numbered questions (solutions not accessible to students)
  - One-third of odd-numbered questions (solutions accessible to students)
- Generates distractors based on common misconceptions
- Supports single-choice and multiple-choice questions
- Includes multi-part questions with randomized correct answers
- Produces LMS-ready assessments in QTI 2.1 format

## 🚧 Current Limitations

- Supports multiple-choice questions only (proof of concept)
- Multi-part questions need appropriate weighting in LMS
- Does not support images, graphs, or plots in questions
- Limited to text-based questions and answers

## 📋 Usage Instructions

1. Place Markdown solutions manual in project folder
2. Run question_parser.py:
   - Creates individual .rmd files in "01exercises" folder
3. Modify testGen.Rmd:
   - Update chapter_num and course_code variables
4. Run testGen.Rmd:
   - Generates quiz and test files
   - Creates directory structure based on chapter and course

### 📂 Output Structure

```
~/NANMO-2024/Courses/Test Generator/
└── CH[chapter_num]_[course_code]/
    ├── CH[chapter_num]_[course_code]_quiz.zip
    ├── CH[chapter_num]_[course_code]_test.zip
    └── html/
        ├── CH[chapter_num]_[course_code]_quiz1.html
        └── CH[chapter_num]_[course_code]_test1.html
```

## 🔧 Customization

- Modify the question selection criteria in question_parser.py
- Adjust quiz and test lengths in testGen.Rmd
- Customize output formats in testGen.Rmd (currently HTML and QTI 2.1)

## 🤝 Contributing

We welcome contributions. Submit issues or pull requests.

## 🙏 Acknowledgements

- OpenStax
- R/exams project
- Anthropic
- Mathpix

Happy assessment creation! 📝✨

## 📜 Attribution

This project uses content from OpenStax textbooks, which are licensed under the Creative Commons Attribution License v4.0 (CC BY 4.0).

Attribution:
© 2023 Texas Education Agency (TEA). This work is derived from "College Physics 2e" and "Physics" by OpenStax and is licensed under Creative Commons Attribution License v4.0 (CC BY 4.0).

To view a copy of this license, visit: https://creativecommons.org/licenses/by/4.0/

Changes to the original work: Content and questions from the original works have been modified for assessment creation purposes. This includes reformatting, rewording, and generating new questions based on the original content.

OpenStax, OpenStax CNX, and OpenStax Design are trademarks of Rice University. © 1999-2023, Rice University. Except where otherwise noted, textbooks on OpenStax.org are licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0).

Original textbooks can be found at:
- College Physics 2e: https://openstax.org/details/books/college-physics-2e
- Physics: https://openstax.org/details/books/physics
