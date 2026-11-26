"""Builds privacy.html, terms.html and cloud-data.html from one layout.

Run from the site root:  python3 tools/build_legal.py
To reuse for another console, change STUDIO, EMAIL, PLAY_DEV, UPDATED and APPS.
"""
import html
import re

STUDIO = "OBanaf Apps Studio"
EMAIL = "info@pandezlabsltd.site"
PLAY_DEV = "https://play.google.com/store/apps/dev?id=5410437552612865577"
UPDATED = "November 26, 2026"

APPS = [
    ("com.ethiopian.calender.converter", "Ethiopian Calendar (ቀን መቁጠሪያ)"),
    ("com.nepalipatro.nepalicalendar", "Nepali Patro – Nepali Calendar"),
    ("com.persian.calendar", "Persian Calendar تقویم فارسی"),
    ("com.ob.aimathsolver.scan.solve", "AI Math Solver With Solution"),
    ("com.ts.smart.printer.scanner.mobile.printshare", "Smart Printer App: Mobile Print"),
    ("com.hd.camera.photo.android", "HD Camera Beauty And Filter"),
    ("com.ob.pose.camera.photo.guide", "Pose Camera Photo Guide"),
    ("com.ob.dress.ai.tryon.fashion", "Dress AI : AI Try On"),
    ("com.ob.aigiftfinder.wishlist", "AI Gift Finder"),
]

MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
APP_LIST = '<ul class="app-list">' + "".join(
    f'<li><img src="assets/img/apps/{pid}/icon.webp" alt="" width="28" height="28" loading="lazy">{html.escape(name)}</li>'
    for pid, name in APPS) + "</ul>"

PAGES = [
    ("privacy.html", "Privacy Policy"),
    ("terms.html", "Terms & Conditions"),
    ("cloud-data.html", "Cloud & Google Data"),
]

# ---------------------------------------------------------------- privacy
PRIVACY = [
("scope", "Who we are & scope", f"""
<p>{STUDIO} (“we”, “us”, “our”) publishes the Android applications listed below on Google Play. This Privacy Policy explains what information our apps collect, how it is used and shared, and the choices you have. It applies to every app published under our <a href="{PLAY_DEV}" target="_blank" rel="noopener">Google Play developer account</a>, including:</p>
{APP_LIST}
<p>By installing or using our apps you agree to this policy. If you do not agree, please uninstall the app.</p>"""),
("collect", "Information we collect", """
<h3>Information collected automatically</h3>
<ul>
<li><strong>Device information</strong> — device model, operating system version, language, country/region and screen size.</li>
<li><strong>App usage & diagnostics</strong> — screens viewed, features used, session length, crash logs and performance data.</li>
<li><strong>Device identifiers</strong> — the Android Advertising ID and Firebase installation IDs, used for analytics and advertising.</li>
</ul>
<h3>Information you choose to provide</h3>
<ul>
<li><strong>Photos and camera images</strong> — when you take or select a photo to scan, edit, solve, apply a filter or try on an outfit.</li>
<li><strong>Text you enter</strong> — math questions, gift-finder answers, calendar events, reminders and notes.</li>
<li><strong>Files and documents</strong> — documents, PDFs and images you choose to print or scan.</li>
<li><strong>Contact details</strong> — your email address and message, only if you contact us for support.</li>
</ul>
<p>We do <strong>not</strong> ask for your name, postal address or phone number, and we do not create user accounts on our own servers.</p>"""),
("use", "How we use information", """
<ul>
<li>To provide app features you request, such as converting dates, solving a problem, generating a try-on image or printing a document.</li>
<li>To keep apps stable and secure: diagnosing crashes, fixing bugs and preventing abuse.</li>
<li>To understand which features are used so we can improve them.</li>
<li>To show advertising that keeps our apps free, and to measure how ads perform.</li>
<li>To process in-app purchases and subscriptions through Google Play.</li>
<li>To reply to you when you contact support.</li>
</ul>
<p>We do <strong>not sell</strong> your personal information, and we do not use it for any purpose that is unrelated to our apps.</p>"""),
("ai", "AI features & your photos", """
<p>Some apps offer AI features — <strong>AI Math Solver</strong>, <strong>Dress AI</strong>, <strong>AI Gift Finder</strong> and AI effects in our camera apps. When you use one of these features:</p>
<ul>
<li>The photo or text you submit is sent over an encrypted (HTTPS/TLS) connection to an AI processing service solely to produce your result.</li>
<li>Submitted content is processed temporarily and is <strong>not</strong> used to build a profile of you, sold, or shared for advertising.</li>
<li>We do not keep your uploaded photos after the result has been generated, except where the app explicitly lets you save results to your own device.</li>
</ul>
<p>Photos, videos and files that you do not submit to an AI feature stay on your device.</p>"""),
("permissions", "Device permissions", """
<p>Our apps request a permission only when a feature needs it, and you can deny or revoke it at any time in Android <em>Settings → Apps → Permissions</em>. Denying a permission only disables the related feature.</p>
<div class="table-wrap"><table>
<tr><th>Permission</th><th>Why it is used</th></tr>
<tr><td>Camera</td><td>Scanning math problems and documents, taking photos, live pose guides and beauty filters.</td></tr>
<tr><td>Photos, media & files</td><td>Selecting an image to edit, solve, try on or print, and saving your results.</td></tr>
<tr><td>Notifications</td><td>Calendar reminders, holiday alerts and event notifications.</td></tr>
<tr><td>Alarms & reminders</td><td>Delivering calendar reminders at the exact time you set.</td></tr>
<tr><td>Location (approximate)</td><td>Showing local prayer, sunrise and sunset times in calendar apps. Location is used on-device and is never shared with advertisers.</td></tr>
<tr><td>Nearby devices / Bluetooth / Wi-Fi</td><td>Finding and connecting to printers.</td></tr>
<tr><td>Internet & network state</td><td>Loading content, currency and gold rates, AI features and ads.</td></tr>
</table></div>"""),
("third-parties", "Third-party services", """
<p>Our apps use trusted third-party services that may collect information as described in their own privacy policies:</p>
<div class="table-wrap"><table>
<tr><th>Service</th><th>Purpose</th><th>Policy</th></tr>
<tr><td>Google Play Services</td><td>App delivery, updates and core Android functions</td><td><a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Link</a></td></tr>
<tr><td>Google AdMob</td><td>Advertising</td><td><a href="https://support.google.com/admob/answer/6128543" target="_blank" rel="noopener">Link</a></td></tr>
<tr><td>Google Analytics for Firebase</td><td>Usage analytics</td><td><a href="https://firebase.google.com/support/privacy" target="_blank" rel="noopener">Link</a></td></tr>
<tr><td>Firebase Crashlytics</td><td>Crash reporting</td><td><a href="https://firebase.google.com/support/privacy" target="_blank" rel="noopener">Link</a></td></tr>
<tr><td>Google Play Billing</td><td>In-app purchases & subscriptions</td><td><a href="https://payments.google.com/payments/apis-secure/get_legal_document?ldo=0&ldt=privacynotice" target="_blank" rel="noopener">Link</a></td></tr>
<tr><td>Google Sign-In, Drive & Calendar APIs</td><td>Optional backup, restore and calendar sync</td><td><a href="cloud-data.html">Our declaration</a></td></tr>
</table></div>"""),
("ads", "Advertising & consent", """
<p>Free versions of our apps show ads served by Google AdMob. AdMob may use your device’s Advertising ID and similar technologies to show ads and measure their performance.</p>
<ul>
<li>Users in the EEA, UK and Switzerland are asked for consent through Google’s consent message before personalised ads are shown.</li>
<li>You can reset or delete your Advertising ID, or opt out of personalised ads, in Android <em>Settings → Google → Ads</em>.</li>
<li>Purchasing an ad-free option, where available, removes ads from that app.</li>
</ul>"""),
("google-data", "Google user data", """
<p>Some apps let you <strong>optionally</strong> sign in with Google to back up your data to Google Drive or sync events with Google Calendar. This data is accessed only after you grant permission, is used only to provide that feature, and is stored in <strong>your own</strong> Google account — not on our servers.</p>
<p>Full details of the scopes we request, how the data is stored and how to revoke access are in our <a href="cloud-data.html">Cloud Storage & Google User Data Declaration</a>.</p>"""),
("security", "Data security", """
<ul>
<li>All data in transit is encrypted with HTTPS/TLS.</li>
<li>We follow data-minimisation: we collect only what a feature needs and process it on-device whenever possible.</li>
<li>Access to analytics and crash dashboards is restricted to our team.</li>
</ul>
<p>No method of storage or transmission is 100% secure, but we work to protect your information using industry-standard safeguards.</p>"""),
("retention", "Retention & deletion", """
<ul>
<li><strong>On-device data</strong> (events, reminders, settings, saved results) stays on your device and is removed when you clear app data or uninstall the app.</li>
<li><strong>AI submissions</strong> are deleted after your result is generated.</li>
<li><strong>Analytics & crash data</strong> are kept for up to 14 months by Firebase, then deleted automatically.</li>
<li><strong>Cloud backups</strong> live in your Google Drive and can be deleted by you at any time.</li>
<li><strong>Support emails</strong> are kept only as long as needed to resolve your request.</li>
</ul>
<p>To ask us to delete any data associated with you, follow the steps in <a href="cloud-data.html#delete">Request data deletion</a>.</p>"""),
("rights", "Your rights & choices", """
<p>Depending on where you live (for example under the GDPR, UK GDPR or CCPA/CPRA), you may have the right to access, correct, delete or export your personal information, to object to or restrict processing, and to withdraw consent at any time. We do not sell or “share” personal information as defined by the CCPA.</p>
<p>To exercise any right, email us — we respond within 30 days. You can also manage permissions and ad settings on your device at any time.</p>"""),
("children", "Children’s privacy", """
<p>Our apps are intended for a general audience and are not directed at children under 13 (or the minimum age in your country). We do not knowingly collect personal information from children. If you believe a child has provided us with information, contact us and we will delete it promptly.</p>"""),
("changes", "Changes to this policy", """
<p>We may update this policy as our apps change. The “Last updated” date at the top will show when it was last revised, and significant changes will be announced in the app or on this page.</p>"""),
("contact", "Contact us", f"""
<p>Questions, requests or concerns about privacy:</p>
<div class="callout"><p><strong>{STUDIO}</strong><br>Email: {MAIL}</p></div>"""),
]

# ---------------------------------------------------------------- terms
TERMS = [
("acceptance", "Acceptance of terms", f"""
<p>These Terms & Conditions (“Terms”) govern your use of every Android app published by {STUDIO} (“we”, “us”) on Google Play (the “Apps”). By downloading or using an App you agree to these Terms and to our <a href="privacy.html">Privacy Policy</a>. If you do not agree, do not use the Apps.</p>
{APP_LIST}"""),
("license", "License to use the apps", """
<p>We grant you a personal, non-exclusive, non-transferable, revocable license to install and use the Apps on Android devices you own or control, for personal and non-commercial use, in line with these Terms and the Google Play Terms of Service.</p>
<p>You may not copy, modify, reverse-engineer, decompile, resell, rent or redistribute the Apps or any part of them, except where the law expressly allows it.</p>"""),
("use", "Acceptable use", """
<p>You agree not to use the Apps to:</p>
<ul>
<li>upload photos of other people without their permission, or create content that is unlawful, harassing, sexual, hateful or deceptive;</li>
<li>impersonate anyone or create misleading “deepfake” images of real people;</li>
<li>violate copyright, privacy or any other rights of others;</li>
<li>interfere with, overload or attempt to gain unauthorised access to the Apps or their services;</li>
<li>use bots, scrapers or automated means to access AI features.</li>
</ul>"""),
("content", "Your content", """
<p>You keep ownership of the photos, text and files you use in the Apps (“Your Content”). You give us a limited permission to process Your Content only to provide the feature you requested, as described in our Privacy Policy. You are responsible for having the rights to any content you submit.</p>"""),
("ai", "AI-generated results", """
<p>AI features — including math solutions, virtual try-on images, gift suggestions and beauty effects — are generated automatically and may be inaccurate, incomplete or unrealistic.</p>
<ul>
<li>Math solutions are a <strong>learning aid</strong>; check important answers and follow your school’s academic-integrity rules.</li>
<li>Try-on images are a <strong>visual preview</strong> and may not reflect real fit, size, colour or appearance.</li>
<li>Gift suggestions are ideas only; we are not responsible for third-party products, prices or sellers.</li>
</ul>"""),
("info", "Calendars, dates & rates", """
<p>Calendar dates, holidays, fasting days, festivals, Rashifal, Panchang, prayer and sunrise/sunset times, currency rates and gold prices are provided <strong>for general information only</strong>. They are prepared carefully but may differ by region, authority or method of calculation, and live rates may be delayed. Please confirm with official or religious authorities before relying on them for important decisions.</p>"""),
("printing", "Printing & scanning", """
<p>Printer compatibility depends on your printer model, firmware and network. We do not guarantee that every printer is supported and are not responsible for print quality, paper, ink or damage to devices.</p>"""),
("purchases", "Purchases & subscriptions", """
<ul>
<li>Some Apps offer optional in-app purchases or subscriptions, processed entirely by <strong>Google Play</strong>. Prices are shown before you buy.</li>
<li>Subscriptions renew automatically unless cancelled at least 24 hours before the end of the current period. Manage or cancel them in <em>Google Play → Payments & subscriptions</em>.</li>
<li>Free trials convert to paid subscriptions unless cancelled before the trial ends.</li>
<li>Refunds are handled under <a href="https://support.google.com/googleplay/answer/2479637" target="_blank" rel="noopener">Google Play’s refund policy</a>.</li>
</ul>"""),
("ads", "Advertising & third-party services", """
<p>Free Apps display ads and rely on third-party services such as Google AdMob and Firebase. Your use of those services is also subject to their terms. We are not responsible for the content of third-party ads, websites or products.</p>"""),
("ip", "Intellectual property", f"""
<p>The Apps, including their design, code, graphics, logos and text, are owned by {STUDIO} or its licensors and are protected by copyright and trademark laws. Google Play and the Google Play logo are trademarks of Google LLC.</p>"""),
("disclaimer", "Disclaimer of warranties", """
<p>The Apps are provided <strong>“as is” and “as available”</strong>, without warranties of any kind, express or implied, including fitness for a particular purpose, accuracy or uninterrupted availability. We may change, suspend or discontinue any feature at any time.</p>"""),
("liability", "Limitation of liability", f"""
<p>To the maximum extent permitted by law, {STUDIO} will not be liable for any indirect, incidental, special or consequential damages, or for loss of data, profits or goodwill, arising from your use of the Apps. Our total liability for any claim is limited to the amount you paid us for the App in the 12 months before the claim, if any.</p>
<p>Nothing in these Terms limits rights that cannot be limited under the consumer laws of your country.</p>"""),
("termination", "Termination", """
<p>You can stop using the Apps at any time by uninstalling them. We may suspend or end your access if you breach these Terms. Sections that by their nature should survive (such as intellectual property, disclaimers and limitation of liability) continue after termination.</p>"""),
("changes", "Changes to these terms", """
<p>We may update these Terms from time to time. The “Last updated” date shows the latest version. Continuing to use the Apps after a change means you accept the updated Terms.</p>"""),
("contact", "Contact us", f"""
<div class="callout"><p><strong>{STUDIO}</strong><br>Email: {MAIL}</p></div>"""),
]

# ---------------------------------------------------------------- cloud data
CLOUD = [
("summary", "Summary", f"""
<p>This page declares how apps published by {STUDIO} access, use, store and share <strong>Google user data</strong> and <strong>cloud-stored data</strong>. It supplements our <a href="privacy.html">Privacy Policy</a>.</p>
<div class="callout"><p>{STUDIO}’s use and transfer of information received from Google APIs to any other app will adhere to the <a href="https://developers.google.com/terms/api-services-user-data-policy" target="_blank" rel="noopener">Google API Services User Data Policy</a>, including the Limited Use requirements.</p></div>
<ul>
<li>Google sign-in, Drive backup and Calendar sync are <strong>optional</strong>. Every app works without them.</li>
<li>Your backups are stored in <strong>your own Google Drive</strong> — never on our servers.</li>
<li>We never sell Google user data, use it for advertising, or let humans read it.</li>
</ul>"""),
("scopes", "Data we access & why", """
<p>We request only the narrowest scope needed for each feature, and only when you turn that feature on:</p>
<div class="table-wrap"><table>
<tr><th>Google API & scope</th><th>Data accessed</th><th>Purpose</th></tr>
<tr><td>Google Sign-In<br><code>openid</code> <code>email</code> <code>profile</code></td><td>Name, email address, profile picture</td><td>Identify which Google account to back up to and show it in settings.</td></tr>
<tr><td>Google Drive<br><code>drive.appdata</code></td><td>Only the hidden app-data folder that our app creates in your Drive</td><td>Back up and restore your events, reminders, notes, wishlists and settings. We cannot see any other file in your Drive.</td></tr>
<tr><td>Google Drive<br><code>drive.file</code></td><td>Only files you create or open with our app</td><td>Save scanned PDFs or results to Drive, or pick a file from Drive to print.</td></tr>
<tr><td>Google Calendar<br><code>calendar.events</code></td><td>Events on calendars you choose</td><td>Add holidays and reminders to your Google Calendar and keep them in sync.</td></tr>
</table></div>"""),
("storage", "Where cloud data is stored", """
<ul>
<li><strong>Drive backups</strong> are stored in your Google Drive account, encrypted by Google, and count toward your own Drive storage.</li>
<li><strong>Calendar events</strong> are stored in your Google Calendar.</li>
<li><strong>Access tokens</strong> are kept on your device in Android’s secure storage and are never sent to our servers.</li>
<li>All transfers between the app and Google use HTTPS/TLS encryption.</li>
</ul>"""),
("sharing", "Sharing & Limited Use", """
<p>Google user data obtained through our apps:</p>
<ul>
<li>is used <strong>only</strong> to provide or improve the user-facing backup, restore and sync features described above;</li>
<li>is <strong>not</strong> transferred to third parties, except as needed to provide those features, to comply with law, or as part of a merger or acquisition with your notice;</li>
<li>is <strong>not</strong> used for serving advertisements, including retargeting, personalised or interest-based ads;</li>
<li>is <strong>not</strong> sold, and is not used to determine credit-worthiness or for lending;</li>
<li>is <strong>not</strong> read by humans, unless you give explicit permission for specific data (for example, a support request), it is needed for security or abuse investigation, or required by law;</li>
<li>is <strong>not</strong> used to develop, improve or train generalised AI or machine-learning models.</li>
</ul>"""),
("revoke", "Revoking access", """
<ol>
<li>In the app, open <strong>Settings → Backup & Sync</strong> and tap <strong>Sign out / Disconnect</strong>.</li>
<li>Or visit <a href="https://myaccount.google.com/connections" target="_blank" rel="noopener">myaccount.google.com/connections</a>, select the app, and choose <strong>Delete all connections</strong>.</li>
</ol>
<p>Revoking access stops all future access immediately. Existing backups remain in your Drive until you delete them.</p>"""),
("delete", "Request data deletion", f"""
<p>You can delete your data at any time, with or without contacting us:</p>
<h3>Delete it yourself</h3>
<ul>
<li><strong>Drive backups</strong> — in Google Drive on the web, open <em>Settings → Manage apps</em>, find the app and choose <strong>Delete hidden app data</strong>.</li>
<li><strong>On-device data</strong> — in Android <em>Settings → Apps → [app] → Storage</em>, tap <strong>Clear data</strong>, or uninstall the app.</li>
<li><strong>Advertising ID</strong> — in Android <em>Settings → Google → Ads</em>, tap <strong>Delete advertising ID</strong>.</li>
</ul>
<h3>Ask us to delete it</h3>
<p>Email {MAIL} with the subject <strong>“Data deletion request”</strong>, the app name, and (if you used Google sign-in) the Google account email. We will delete any data associated with you — including analytics records linked to your installation and any support correspondence — within <strong>30 days</strong> and confirm by email.</p>
<p>We do not keep any data after deletion, except where the law requires us to keep limited records (for example, purchase records handled by Google Play).</p>"""),
("contact", "Contact", f"""
<div class="callout"><p><strong>{STUDIO}</strong><br>Email: {MAIL}<br>Developer page: <a href="{PLAY_DEV}" target="_blank" rel="noopener">Google Play</a></p></div>"""),
]

INTRO = {
    "privacy.html": ("Privacy Policy", "How our apps collect, use and protect your information — one policy for every app we publish on Google Play."),
    "terms.html": ("Terms & Conditions", "The rules for using our apps, AI features, purchases and subscriptions."),
    "cloud-data.html": ("Cloud & Google Data Declaration", "Exactly which Google user data our apps can access, where cloud data is stored, and how to revoke access or delete it."),
}


CURRENT = ' aria-current="page"'


def page(fname, sections):
    title, lead = INTRO[fname]
    tabs = "".join(
        f'<a href="{f}"{CURRENT if f == fname else ""}>{t}</a>' for f, t in PAGES)
    toc = "".join(f'<a href="#{sid}">{html.escape(h)}</a>' for sid, h, _ in sections)
    body = "".join(f'<section id="{sid}"><h2>{html.escape(h)}</h2>{c.strip()}</section>' for sid, h, c in sections)
    desc = re.sub(r"\s+", " ", lead)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title} — {STUDIO}</title>
  <meta name="description" content="{html.escape(desc)}">
  <meta name="theme-color" content="#07080d">
  <link rel="icon" type="image/webp" href="assets/img/logo.webp">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>
  <div class="grain" aria-hidden="true"></div>
  <header class="nav scrolled" id="nav">
    <a href="./" class="brand" aria-label="{STUDIO} home">
      <img src="assets/img/logo.webp" alt="" width="36" height="36">
      <span>OBanaf<em>Apps Studio</em></span>
    </a>
    <nav class="nav-links" aria-label="Primary">
      <a href="./#apps">Apps</a>
      <a href="privacy.html"{' class="active"' if fname == 'privacy.html' else ''}>Privacy</a>
      <a href="terms.html"{' class="active"' if fname == 'terms.html' else ''}>Terms</a>
      <a href="cloud-data.html"{' class="active"' if fname == 'cloud-data.html' else ''}>Cloud data</a>
    </nav>
    <a class="btn btn-sm btn-light" href="{PLAY_DEV}" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M3.6 1.8 13.8 12 3.6 22.2a1.6 1.6 0 0 1-.6-1.3V3.1c0-.5.2-1 .6-1.3Zm11.3 11.3 2.6 2.6-11.9 6.8 9.3-9.4Zm3.9-3.9 3.2 1.8c.9.5.9 1.6 0 2.1l-3.2 1.8-2.8-2.9 2.8-2.8ZM5.6 1.5l11.9 6.8-2.6 2.6-9.3-9.4Z"/></svg>
      <span>Google Play</span>
    </a>
    <button class="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span></button>
  </header>

  <main id="content">
    <section class="legal-hero">
      <div class="orb orb-a" aria-hidden="true"></div>
      <div class="wrap">
        <p class="kicker">Legal</p>
        <h1>{title}</h1>
        <p class="lead">{lead}</p>
        <div class="legal-meta"><span>Last updated · {UPDATED}</span><span>Applies to all {len(APPS)} apps</span></div>
        <nav class="legal-tabs" aria-label="Legal documents">{tabs}</nav>
      </div>
    </section>
    <div class="wrap legal">
      <nav class="toc" aria-label="On this page"><p>On this page</p>{toc}</nav>
      <article class="prose">{body}</article>
    </div>
  </main>

  <footer class="footer">
    <div class="wrap footer-inner">
      <div class="brand"><img src="assets/img/logo.webp" alt="" width="32" height="32" loading="lazy"><span>OBanaf<em>Apps Studio</em></span></div>
      <nav aria-label="Footer">
        <a href="./#apps">Apps</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="cloud-data.html">Cloud data</a><a href="cloud-data.html#delete">Delete my data</a><a href="mailto:{EMAIL}">Contact</a>
      </nav>
      <p class="copy">© <span id="year">2026</span> {STUDIO}. Google Play and the Google Play logo are trademarks of Google LLC.</p>
    </div>
  </footer>
  <script src="assets/js/legal.js" defer></script>
</body>
</html>
"""


for fname, sections in [("privacy.html", PRIVACY), ("terms.html", TERMS), ("cloud-data.html", CLOUD)]:
    with open(fname, "w", encoding="utf-8") as f:
        f.write(page(fname, sections))
    print("wrote", fname)
