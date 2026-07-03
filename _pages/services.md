---
title: "Work With Me"
layout: splash
permalink: /services/
description: "Hire an experienced iOS & macOS developer — new apps from idea to App Store, UIKit to SwiftUI modernization, App Store launch help, and 1:1 advisory."
keywords: "freelance iOS developer, hire SwiftUI developer, macOS app developer, UIKit to SwiftUI migration, App Store launch help, iOS consultant, iOS mentor"
og_title: "Work With Me — iOS & macOS App Development | Ravi Shankar"
og_description: "New apps from idea to App Store, SwiftUI modernization, App Store launch help, and 1:1 iOS advisory. 10 apps shipped, building with Swift since 2014."
og_type: "website"
twitter_card: "summary_large_image"
twitter_title: "Work With Me — iOS & macOS App Development"
twitter_description: "New apps from idea to App Store, SwiftUI modernization, App Store launch help, and 1:1 iOS advisory."
header:
  overlay_color: "#0d1b2a"
  overlay_filter: "0.2"
  actions:
    - label: "Start a project"
      url: "#contact"
excerpt: "I take iOS, macOS, and watchOS apps from idea to the App Store — and help teams rescue, modernize, and launch the ones they already have."
---

<div class="landing">

  <!-- Services -->
  <section class="lp-section">
    <h2 class="lp-h2">What I can help you with</h2>
    <p class="lp-sub">10 apps shipped across iPhone, iPad, Mac, and Apple Watch. Building with Swift since 2014 — now AI-accelerated, so projects move faster without cutting corners.</p>

    <div class="services-grid">
      <div class="service-card">
        <div class="service-icon">🚀</div>
        <h3>New app — idea to App Store</h3>
        <p>Product thinking, native SwiftUI development, and App Store submission for iOS, macOS, and watchOS. You bring the idea; I handle everything from architecture to the "Ready for Sale" email.</p>
      </div>
      <div class="service-card">
        <div class="service-icon">🔧</div>
        <h3>Modernization &amp; rescue</h3>
        <p>UIKit → SwiftUI migration, performance fixes, latest-OS support, and stuck or inherited projects brought back on track — with code quality that keeps future development easy.</p>
      </div>
      <div class="service-card">
        <div class="service-icon">📦</div>
        <h3>App Store &amp; launch help</h3>
        <p>Submission, metadata and screenshots, App Review rejections worked to resolution, and launch strategy. I've been through review many times with my own apps.</p>
      </div>
      <div class="service-card">
        <div class="service-icon">🎓</div>
        <h3>Advisory &amp; mentorship</h3>
        <p>1:1 sessions on architecture, code review, debugging, and AI-assisted development workflows for iOS. I've trained 11,000+ students and mentored developers through Upwork.</p>
      </div>
    </div>
  </section>

  <!-- How we'll work -->
  <section class="lp-section">
    <h2 class="lp-h2">How we'll work</h2>
    <ol class="process-steps">
      <li><strong>Tell me about your project.</strong> A few lines by email or the form below is enough to start.</li>
      <li><strong>Short scoping call.</strong> We clarify goals, constraints, and what "done" looks like. No charge, no obligation.</li>
      <li><strong>Fixed quote.</strong> You get a clear scope, timeline, and price — fixed-scope for defined projects, retainer for ongoing work, or a single session for advisory.</li>
      <li><strong>Build, with visibility.</strong> Regular updates and working builds via TestFlight — you see progress, not just promises.</li>
      <li><strong>Launch and handover.</strong> App Store submission, clean documented code, and everything you need to continue without me.</li>
    </ol>
  </section>

  <!-- Testimonials -->
  <section class="lp-section">
    <h2 class="lp-h2">What clients say</h2>
    <p class="lp-sub">From verified Upwork contracts and LinkedIn recommendations.</p>
    <div class="testimonials-grid">
      {% for t in site.data.testimonials %}
      <figure class="testimonial-card">
        <blockquote>&ldquo;{{ t.quote }}&rdquo;</blockquote>
        {% if t.endorsements and t.endorsements.size > 0 %}
        <div class="testimonial-tags">
          {% for e in t.endorsements %}<span class="testimonial-tag">{{ e }}</span>{% endfor %}
        </div>
        {% endif %}
        <figcaption>{{ t.source }}</figcaption>
      </figure>
      {% endfor %}
    </div>
  </section>

  <!-- FAQ -->
  <section class="lp-section">
    <h2 class="lp-h2">Common questions</h2>
    <div class="faq-list">
      <details class="faq-item">
        <summary>Where are you based, and do you work remotely?</summary>
        <p>I'm based in Chennai, India, and work remotely with clients worldwide. I've delivered projects for clients across time zones — async updates plus scheduled calls keep everything moving.</p>
      </details>
      <details class="faq-item">
        <summary>What technologies do you use?</summary>
        <p>Native Apple development: Swift and SwiftUI first, with deep UIKit experience for existing codebases. I use AI-assisted workflows (I build open-source Claude Code tooling for Apple developers) to move faster — but every line that ships is reviewed, tested, and maintainable.</p>
      </details>
      <details class="faq-item">
        <summary>Who owns the code?</summary>
        <p>You do — full rights to all code and assets on final payment. NDAs are fine.</p>
      </details>
      <details class="faq-item">
        <summary>What does it cost?</summary>
        <p>Every project gets a fixed quote after a short scoping call, so there are no surprises. Advisory sessions are a simple flat rate.</p>
      </details>
      <details class="faq-item">
        <summary>Can you take over an existing app?</summary>
        <p>Yes — inherited codebases, half-finished projects, and apps whose original developer moved on are a specialty. I'll audit first, then give you an honest assessment before we commit.</p>
      </details>
    </div>
  </section>

  <!-- Contact -->
  <section id="contact" class="lp-section">
    <h2 class="lp-h2">Start a project</h2>
    <p class="lp-sub">Tell me what you're building. I take on a small number of projects at a time and reply personally, usually within a day.</p>

    <form class="contact-form" id="project-form">
      <div class="cf-row">
        <label for="cf-name">Your name</label>
        <input type="text" id="cf-name" name="name" required>
      </div>
      <div class="cf-row">
        <label for="cf-type">What do you need?</label>
        <select id="cf-type" name="type">
          <option>New app — idea to App Store</option>
          <option>Modernization or rescue of an existing app</option>
          <option>App Store / launch help</option>
          <option>Advisory or mentorship session</option>
          <option>Something else</option>
        </select>
      </div>
      <div class="cf-row">
        <label for="cf-desc">Tell me about the project</label>
        <textarea id="cf-desc" name="description" rows="5" placeholder="What are you building? What's the current state? What does success look like?" required></textarea>
      </div>
      <div class="cf-row cf-row--split">
        <div>
          <label for="cf-timeline">Timeline</label>
          <select id="cf-timeline" name="timeline">
            <option>Flexible</option>
            <option>Within 1 month</option>
            <option>1–3 months</option>
            <option>ASAP</option>
          </select>
        </div>
        <div>
          <label for="cf-budget">Budget (optional)</label>
          <select id="cf-budget" name="budget">
            <option>Not sure yet</option>
            <option>Under $1,000</option>
            <option>$1,000–5,000</option>
            <option>$5,000–15,000</option>
            <option>$15,000+</option>
          </select>
        </div>
      </div>
      <button type="submit" class="btn btn--primary btn--large">Send inquiry →</button>
      <p class="cf-note">This opens a pre-filled email in your mail app — nothing is stored on this site. Prefer to write directly? <a href="mailto:ravi@rshankar.com?subject=Project%20inquiry%20from%20rshankar.com">ravi@rshankar.com</a></p>
    </form>
  </section>

</div>

<script>
document.getElementById('project-form').addEventListener('submit', function (e) {
  e.preventDefault();
  var v = function (id) { return document.getElementById(id).value; };
  var subject = 'Project inquiry — ' + v('cf-type');
  var body = 'Name: ' + v('cf-name') + '\n'
    + 'Project type: ' + v('cf-type') + '\n'
    + 'Timeline: ' + v('cf-timeline') + '\n'
    + 'Budget: ' + v('cf-budget') + '\n\n'
    + v('cf-desc');
  window.location.href = 'mailto:ravi@rshankar.com?subject='
    + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
});
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "iOS and macOS app development",
  "name": "iOS & macOS App Development Services",
  "description": "Native app development for Apple platforms — new apps from idea to App Store, UIKit to SwiftUI modernization, App Store launch help, and 1:1 advisory.",
  "provider": {
    "@type": "Person",
    "name": "Ravi Shankar",
    "url": "https://www.rshankar.com/about/"
  },
  "areaServed": "Worldwide",
  "url": "https://www.rshankar.com/services/"
}
</script>
