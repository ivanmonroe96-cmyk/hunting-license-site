---
title: "Contact & Inquiry"
description: "Send us an inquiry — we check your documents and register you with a hunting school."
slug: "contact"
date: 2025-10-15
lastmod: 2025-10-15
languages: ["en"]
---

<form action="https://formsubmit.co/YOUR_EMAIL" method="POST">
  <input type="hidden" name="_subject" value="New Hunting License Inquiry">
  <input type="hidden" name="_captcha" value="false">

  <label>Full Name <input type="text" name="name" required></label>
  <label>Email <input type="email" name="email" required></label>
  <label>Country <select name="country">
    <option value="DE">Germany</option>
    <option value="PL">Poland</option>
    <option value="AT">Austria</option>
    <option value="Other">Other</option>
  </select></label>
  <label>Preferred Start Date <input type="date" name="start_date"></label>
  <label>I want full service <input type="checkbox" name="full_service" value="yes" checked></label>
  <label>I agree to the privacy policy <input type="checkbox" name="gdpr" required></label>
  <textarea name="notes" placeholder="Additional info (e.g., physical limitations, language preferences)"></textarea>
  <button type="submit">Send Inquiry</button>
</form>

**Email Templates:**

- **Automatic Customer Confirmation (sendImmediately)**
  Subject: "We received your inquiry — Hunting License Registration"
  Body: "Hello {{name}}, we received your inquiry and are reviewing your documents. We usually respond within 48 hours."

- **Customer Follow-up (after docs check)**
  Subject: "Missing documents for your hunting license registration"
  Body: "Hello {{name}}, please send us: [list of missing docs]. Once we have everything, we'll register you."

- **School registration email (internal template)**
  To: [school contact]
  Subject: "Registration: {{candidate_name}} — Hunting License Course"
  Body: "Dear Sir or Madam, we would like to register the following candidate: [name, birthdate, documents attached]. Please confirm course / exam dates."
