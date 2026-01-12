# TEACHER ANSWER KEY - STUDENT PORTAL ASSESSMENT

## ⚠️ CONFIDENTIAL - FOR TEACHERS ONLY

This document contains all vulnerabilities and their solutions for marking purposes.

---

## VULNERABILITIES CHECKLIST (Total: 10 vulnerabilities)

### 1. SQL Injection in Login (database.py, line 20)
**Location:** `database.py` - `checkLogin()` function, line 20
**Vulnerable Code:**
```python
query = f"SELECT * FROM users WHERE student_id = '{student_id}' AND password = '{password}'"
```

**Attack Example:**
- Student ID: `S12345' OR '1'='1' --`
- Password: `anything`

**Fix:**
```python
cur.execute("SELECT * FROM users WHERE student_id = ? AND password = ?", (student_id, password))
```

**Marks:** 5 marks (2 for identification, 3 for correct fix)

---

### 2. SQL Injection in Grade Lookup (database.py, line 32)
**Location:** `database.py` - `getGrades()` function, line 32
**Vulnerable Code:**
```python
query = f"SELECT * FROM grades WHERE student_id = '{student_id}'"
```

**Attack Example:**
- URL: `/dashboard.html?id=S12345' OR '1'='1`
- Result: See all students' grades

**Fix:**
```python
cur.execute("SELECT * FROM grades WHERE student_id = ?", (student_id,))
```

**Marks:** 5 marks

---

### 3. SQL Injection in Assignment Submission (database.py, line 45)
**Location:** `database.py` - `submitAssignment()` function, line 45
**Vulnerable Code:**
```python
query = f"INSERT INTO assignments (student_id, assignment_name, link) VALUES ('{student_id}', '{assignment_name}', '{link}')"
```

**Attack Example:**
- Assignment name: `test'); DROP TABLE assignments; --`

**Fix:**
```python
cur.execute("INSERT INTO assignments (student_id, assignment_name, link) VALUES (?, ?, ?)",
            (student_id, assignment_name, link))
```

**Marks:** 5 marks

---

### 4. SQL Injection in Profile Update (database.py, line 56)
**Location:** `database.py` - `updateProfile()` function, line 56
**Vulnerable Code:**
```python
query = f"UPDATE users SET email = '{email}', phone = '{phone}' WHERE student_id = '{student_id}'"
```

**Attack Example:**
- Email: `test@test.com', phone='1234' WHERE student_id='S12346' --`
- Result: Update another student's profile

**Fix:**
```python
cur.execute("UPDATE users SET email = ?, phone = ? WHERE student_id = ?",
            (email, phone, student_id))
```

**Marks:** 5 marks

---

### 5. SQL Injection in Comments (database.py, line 85)
**Location:** `database.py` - `addComment()` function, line 85
**Vulnerable Code:**
```python
query = f"INSERT INTO comments (student_id, comment, date) VALUES ('{student_id}', '{comment}', '{date}')"
```

**Attack Example:**
- Comment: `test'); DELETE FROM comments; --`

**Fix:**
```python
cur.execute("INSERT INTO comments (student_id, comment, date) VALUES (?, ?, ?)",
            (student_id, comment, date))
```

**Marks:** 5 marks

---

### 6. Stored XSS in Comments (templates/announcements.html, line 28)
**Location:** `templates/announcements.html` - line 28
**Vulnerable Code:**
```html
<div>{{ comment.comment|safe }}</div>
```

**Attack Example:**
- Comment: `<script>alert('XSS')</script>`
- Result: JavaScript executes for all users viewing comments

**Fix:**
```html
<div>{{ comment.comment }}</div>
```
OR in database.py:
```python
import html
# In getComments(), escape the comment
```

**Marks:** 5 marks

---

### 7. Open Redirect Vulnerability (app.py, lines 18-20)
**Location:** `app.py` - `index()` function, lines 18-20
**Vulnerable Code:**
```python
if request.method == "GET" and request.args.get("redirect"):
    redirect_url = request.args.get("redirect")
    return redirect(redirect_url)
```

**Attack Example:**
- URL: `/?redirect=http://evil.com`
- Result: User redirected to malicious site

**Fix:**
```python
# Whitelist allowed redirects
ALLOWED_REDIRECTS = ['/dashboard.html', '/profile.html', '/announcements.html']
if request.method == "GET" and request.args.get("redirect"):
    redirect_url = request.args.get("redirect")
    if redirect_url in ALLOWED_REDIRECTS:
        return redirect(redirect_url)
    else:
        return redirect("/")
```

**Marks:** 5 marks

---

### 8. Insecure Direct Object Reference (IDOR) in Dashboard (app.py, line 42)
**Location:** `app.py` - `dashboard()` function, line 42
**Vulnerable Code:**
```python
student_id = request.args.get("id", session['student_id'])
grades = db.getGrades(student_id)
```

**Attack Example:**
- URL: `/dashboard.html?id=S12346`
- Result: View another student's grades

**Fix:**
```python
# Only allow viewing own grades
student_id = session['student_id']  # Don't accept from URL parameter
grades = db.getGrades(student_id)
```

**Marks:** 5 marks

---

### 9. Plain Text Password Storage (database.py, lines 44-46)
**Location:** `database.py` - `init_db()` function, sample data insertion
**Vulnerable Code:**
```python
cur.execute("INSERT INTO users VALUES ('S12345', 'Alice Johnson', 'password123', ...)")
```

**Issue:** Passwords stored in plain text in database

**Fix:**
```python
import hashlib

# In insertUser (if it existed):
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# In checkLogin:
hashed_input = hashlib.sha256(password.encode()).hexdigest()
# Then compare hashed values
```

**Marks:** 5 marks

---

### 10. Missing Input Validation (Multiple locations)
**Location:** All forms lack proper validation
**Issues:**
- No email format validation
- No phone number format validation
- No length limits on inputs
- No sanitization of special characters

**Fix:** Add validation in app.py:
```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    pattern = r'^\d{10}$'
    return re.match(pattern, phone) is not None

# Use in routes before database operations
```

**Marks:** 5 marks

---

## MARKING RUBRIC

**Total Marks: 100**

### Part 1: Security Audit (40 marks)
- Found 9-10 vulnerabilities: 40 marks
- Found 7-8 vulnerabilities: 32 marks
- Found 5-6 vulnerabilities: 24 marks
- Found 3-4 vulnerabilities: 16 marks
- Found 1-2 vulnerabilities: 8 marks

### Part 2: Fixes (40 marks)
- All fixes correct and secure: 40 marks
- Most fixes correct (7-8): 32 marks
- Several fixes correct (5-6): 24 marks
- Some fixes correct (3-4): 16 marks
- Few fixes correct (1-2): 8 marks

### Part 3: Testing (10 marks)
- Comprehensive testing with evidence: 10 marks
- Good testing: 8 marks
- Basic testing: 6 marks
- Minimal testing: 4 marks

### Part 4: Report (10 marks)
- Professional, comprehensive report: 10 marks
- Clear, well-structured report: 8 marks
- Adequate report: 6 marks
- Basic report: 4 marks

---

## EXPECTED STUDENT WORKFLOW

1. **Fork repository** to their GitHub account
2. **Create Codespace** and run the app
3. **Test each feature** with normal and malicious input
4. **Document vulnerabilities** as they find them
5. **Fix each vulnerability** one at a time
6. **Commit after each fix** with clear messages
7. **Test fixes** to ensure they work
8. **Write report** documenting findings

---

## COMMON STUDENT MISTAKES

1. **Fixing only SQL Injection in login** but missing other forms
2. **Removing `|safe` filter** but not understanding why
3. **Not testing their fixes** properly
4. **Poor commit messages** like "fixed bug"
5. **Not documenting** the impact of vulnerabilities
6. **Copying code** without understanding it

---

## ASSESSMENT TIPS FOR TEACHERS

1. **Check Git history** - should see multiple commits, one per fix
2. **Test their fixes** - try the attacks yourself
3. **Read their report** - do they understand the vulnerabilities?
4. **Check for plagiarism** - compare with other students
5. **Look for understanding** - not just copy-paste fixes

---

## EXTENSION TASKS (For Advanced Students)

1. Implement CSRF protection
2. Add Content Security Policy headers
3. Implement rate limiting on login
4. Add session timeout
5. Implement two-factor authentication
6. Add logging for security events
7. Implement password strength requirements
8. Add CAPTCHA to prevent brute force

---

## SAMPLE STUDENT REPORT STRUCTURE

**Executive Summary**
- Brief overview of findings
- Number of vulnerabilities found
- Overall risk assessment

**Vulnerabilities Found**
For each vulnerability:
- Name and type
- Location (file and line)
- Description
- How to exploit
- Potential impact
- Risk rating (Critical/High/Medium/Low)

**Fixes Implemented**
For each fix:
- What was changed
- Why this fixes the vulnerability
- Code before and after

**Testing Results**
- Test cases performed
- Results of each test
- Evidence (screenshots)

**Recommendations**
- Additional security measures
- Best practices for future development
- Security training recommendations

---

**END OF TEACHER ANSWER KEY**
