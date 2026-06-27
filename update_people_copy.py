import re

with open('apps/people/index.html', 'r') as f:
    content = f.read()

# 1. Hero Section
content = content.replace(
    '<h1>Your staff, scheduled and paid</h1>',
    '<h1>End-to-End HR & Payroll for Healthcare</h1>'
)
content = content.replace(
    '<p style="font-size:1.1rem;color:#555;margin-bottom:2rem;max-width:500px;">Rosters, attendance, leave, PF, ESI and payslips - everything HR for doctors, nurses and every staff member in your hospital, in one place.</p>',
    '<p style="font-size:1.1rem;color:#555;margin-bottom:2rem;max-width:500px;">Manage the entire employee lifecycle—from onboarding and duty rostering to complex payroll and compliance—specifically designed for hospitals and clinics.</p>'
)

# 2. Feature 1 (Currently "Duty roster & shift scheduling", change to "Hospital HR Management & Onboarding")
feat1_old = """<h2>Duty roster & shift scheduling</h2>
        <p>Build weekly rosters for every department in minutes. ZenoHosp People flags understaffed shifts, prevents consecutive night-shift overloads, and lets staff view their schedule from their phone - no more WhatsApp roster photos.</p>
        <ul class="feature-list">
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Department-wise manpower allocation</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Auto-alerts for understaffed or double-booked shifts</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Swap requests with manager approval workflow</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> SMS / WhatsApp notifications on roster publish</li>
        </ul>"""

feat1_new = """<h2>Hospital HR Management & Onboarding</h2>
        <p>Maintain centralized digital records for your entire workforce. Track doctor licenses, nurse certifications, and employee contracts easily. Oversee the complete lifecycle from recruitment and onboarding to annual appraisals.</p>
        <ul class="feature-list">
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Digital document vault for licenses & degrees</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Auto-reminders for certification renewals</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Custom recruitment & onboarding workflows</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Streamlined performance & appraisal tracking</li>
        </ul>"""

content = content.replace(feat1_old, feat1_new)

# 3. Feature 2 (Currently "Attendance & leave management", change to "Smart Rostering & Attendance Tracking")
feat2_old = """<h2>Attendance & leave management</h2>
        <p>Biometric and RFID punches flow directly into the attendance register. Late arrivals, early exits, and absences are flagged automatically. Leave requests are routed to the right approver without a single paper form.</p>
        <ul class="feature-list">
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Biometric / RFID / mobile punch-in support</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Multi-level leave approval workflows</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Comp-off, LOP, and leave encashment tracking</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Automated late and absent SMS alerts to manager</li>
        </ul>"""

feat2_new = """<h2>Smart Duty Rostering & Attendance</h2>
        <p>Prevent understaffed wards with intelligent shift scheduling that flags consecutive night shifts and double-bookings. Biometric and RFID punches flow directly into the attendance register, making real-time absentee tracking effortless.</p>
        <ul class="feature-list">
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Drag-and-drop department shift scheduling</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Biometric / RFID integration with late arrival flags</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Swap requests with manager approval workflows</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Centralized multi-level leave approval system</li>
        </ul>"""

content = content.replace(feat2_old, feat2_new)

# 4. Feature 3 (Currently "One-click payroll with statutory compliance built in", leave title similar but update copy)
# Wait, Feature 3 is fine as it represents the Payroll pillar perfectly, but I'll update the title to be "Automated Payroll & Statutory Compliance" for better structure.
feat3_old = """<h2>One-click payroll with statutory compliance built in</h2>
        <p>Attendance feeds directly into payroll. ZenoHosp People calculates gross pay, deductions, PF, ESI, and PT automatically - then generates payslips and statutory challans in a single run. No spreadsheets, no manual errors.</p>"""

feat3_new = """<h2>Automated Payroll & Statutory Compliance</h2>
        <p>Seamlessly convert attendance and leaves into accurate salary payouts. ZenoHosp People calculates gross pay, overtime, and automatically handles complex statutory deductions (PF, ESI, PT, TDS) to keep you fully compliant without manual spreadsheets.</p>"""

content = content.replace(feat3_old, feat3_new)

# 5. Feature 4 (Currently "Employee self-service portal", update to highlight Loans/Advances + ESS)
feat4_old = """<h2>Employee self-service portal</h2>
        <p>Give every staff member their own portal to view payslips, check leave balances, apply for leave, and see their upcoming roster - reducing repetitive HR queries and putting information directly in their hands.</p>
        <ul class="feature-list">
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Digital payslip download (PDF)</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Leave application & balance view</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Upcoming shift and duty schedule</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Loan & advance application tracking</li>
        </ul>"""

feat4_new = """<h2>Advances, Deductions & Self-Service</h2>
        <p>Eliminate repetitive HR queries with a self-service portal for staff. Employees can view payslips, check leave balances, and apply for loans or salary advances. The system automatically handles EMI deductions from future payouts.</p>
        <ul class="feature-list">
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Automated loan & advance EMI recovery via payroll</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Staff portal for digital payslip downloads (PDF)</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Mobile access to upcoming shift rosters & duty schedules</li>
          <li><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="10" fill="#E8F5F2"/><path d="M6 10L9 13L14 7" stroke="#2D8A6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg> Real-time leave balance viewing and requests</li>
        </ul>"""

content = content.replace(feat4_old, feat4_new)

with open('apps/people/index.html', 'w') as f:
    f.write(content)

print("Content successfully updated.")
