# THE STUDENT PORTAL - SECURITY ASSESSMENT

## ⚠️ ASSESSMENT TASK

This is a **security assessment** for HSC Software Engineering students.

Your task is to:
1. Find ALL security vulnerabilities in this application
2. Fix each vulnerability using secure coding practices
3. Test that your fixes work
4. Document your findings in a report

## THE SCENARIO

You have been hired as a security consultant for "The Student Portal" - a web application used by a school to manage student information.

The previous developer has left, and the school is concerned about security. They want you to:
- Audit the application for vulnerabilities
- Fix all security issues
- Provide a professional security report

## THE APPLICATION

**The Student Portal** allows:
- Students to log in with their student ID and password
- Students to view their grades
- Students to submit assignment links
- Students to update their profile information
- Teachers to post announcements

## KNOWN ISSUES

The school has reported:
- Some students claim they can see other students' grades
- Strange comments have appeared in the announcements
- The previous developer used "quick and dirty" code
- No security testing has been done

## YOUR TASK

### Part 1: Security Audit (40 marks)

Find and document ALL vulnerabilities in:
- `app.py` (main application file)
- `database.py` (database functions)
- `templates/*.html` (HTML templates)

For each vulnerability, document:
- What the vulnerability is
- Where it is (file and line number)
- How it could be exploited
- The potential impact

### Part 2: Fix the Vulnerabilities (40 marks)

Fix each vulnerability using secure coding practices:
- Use parameterized queries for SQL
- Implement proper input validation
- Use output encoding for XSS prevention
- Fix any authentication issues
- Fix any redirect vulnerabilities

### Part 3: Testing (10 marks)

Test that:
- Your fixes prevent the attacks
- Normal functionality still works
- Document your testing process

### Part 4: Security Report (10 marks)

Write a professional report including:
- Executive summary
- List of vulnerabilities found
- Risk assessment for each
- Fixes implemented
- Testing results
- Recommendations

## SUBMISSION REQUIREMENTS

1. **Code**: Push all fixes to your GitHub repository
2. **Commits**: Use clear commit messages for each fix
3. **Report**: Submit as PDF (max 10 pages)
4. **Testing Evidence**: Screenshots or test results

## ASSESSMENT CRITERIA

**High Distinction (85-100%):**
- Found ALL vulnerabilities (8+)
- Fixed all correctly
- Comprehensive testing
- Professional report

**Distinction (75-84%):**
- Found most vulnerabilities (6-7)
- Fixed most correctly
- Good testing
- Clear report

**Credit (65-74%):**
- Found several vulnerabilities (4-5)
- Fixed most correctly
- Basic testing
- Adequate report

**Pass (50-64%):**
- Found some vulnerabilities (2-3)
- Fixed some correctly
- Minimal testing
- Basic report

## GETTING STARTED

1. Fork this repository
2. Create a Codespace
3. Install dependencies: `pip3 install flask flask-cors`
4. Run the app: `python3 app.py`
5. Start your security audit!

## HINTS

- Review your lessons on SQL Injection, XSS, CSRF, etc.
- Test with malicious input
- Check ALL forms and input fields
- Look for f-strings in SQL queries
- Check for `|safe` filters in templates
- Look for unvalidated redirects

## RULES

- This is an **individual assessment**
- You may use your lesson notes
- You may use online resources
- You must write your own code
- You must write your own report
- Plagiarism will result in zero marks

## DEADLINE

[To be announced by your teacher]

## QUESTIONS?

Ask your teacher during class time.

Good luck! 🎓
