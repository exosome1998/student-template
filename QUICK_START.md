# QUICK START GUIDE - STUDENT PORTAL ASSESSMENT

## For Students

### Step 1: Fork the Repository
1. Go to the GitHub repository (provided by your teacher)
2. Click "Fork" button (top right)
3. This creates your own copy

### Step 2: Create Codespace
1. In YOUR forked repository, click "Code" button
2. Click "Codespaces" tab
3. Click "Create codespace on main"
4. Wait 2-3 minutes for setup

### Step 3: Install Dependencies
In the terminal:
```bash
pip3 install -r requirements.txt
```

### Step 4: Run the Application
```bash
python3 app.py
```

### Step 5: Open in Browser
- Click "Open in Browser" when popup appears
- Or click the link in terminal

### Step 6: Start Testing!
**Test Accounts:**
- Student ID: `S12345`, Password: `password123`
- Student ID: `S12346`, Password: `qwerty`

---

## For Teachers

### Setting Up the Assessment

1. **Create a GitHub Repository:**
   ```bash
   cd Student_Portal_Assessment
   git init
   git add .
   git commit -m "Initial commit: Student Portal Assessment"
   git branch -M main
   git remote add origin [your-repo-url]
   git push -u origin main
   ```

2. **IMPORTANT:** Remove `TEACHER_ANSWER_KEY.md` before students access:
   ```bash
   git rm TEACHER_ANSWER_KEY.md
   git commit -m "Remove teacher answer key"
   git push
   ```

3. **Share Repository Link** with students

4. **Set Deadline** in README.md

---

## Vulnerabilities Summary (For Teachers)

**10 Total Vulnerabilities:**
1. SQL Injection in Login
2. SQL Injection in Grade Lookup
3. SQL Injection in Assignment Submission
4. SQL Injection in Profile Update
5. SQL Injection in Comments
6. Stored XSS in Comments Display
7. Open Redirect
8. Insecure Direct Object Reference (IDOR)
9. Plain Text Password Storage
10. Missing Input Validation

---

## Testing the Vulnerabilities

### Test SQL Injection in Login:
- Student ID: `S12345' OR '1'='1' --`
- Password: `anything`
- Should log in without valid password

### Test IDOR:
- Log in as S12345
- Change URL to: `/dashboard.html?id=S12346`
- Should see another student's grades

### Test XSS:
- Log in
- Go to Announcements
- Post comment: `<script>alert('XSS')</script>`
- Should execute JavaScript

### Test Open Redirect:
- Go to: `/?redirect=http://google.com`
- Should redirect to external site

---

## Marking Checklist

For each student submission:
- [ ] Check Git commit history (multiple commits?)
- [ ] Test each fix (do attacks still work?)
- [ ] Read security report (do they understand?)
- [ ] Check code quality (clean, commented?)
- [ ] Verify all 10 vulnerabilities addressed
- [ ] Check for plagiarism

---

## Common Issues

**"The app won't start"**
- Check: `pip3 install -r requirements.txt`
- Check: Python 3.x is installed

**"Database error"**
- Delete `student_portal.db` file
- Restart the app (it will recreate)

**"Can't access in browser"**
- Check the popup in bottom right
- Or click the link in terminal

---

## Assessment Timeline Suggestion

- **Week 1:** Students audit and document vulnerabilities
- **Week 2:** Students fix vulnerabilities and test
- **Week 3:** Students write report
- **Week 4:** Submission and marking

---

## Support

Students should:
- Review their lesson notes
- Use the hints in the application
- Ask questions during class time
- NOT share code with other students

---

Good luck! 🎓
