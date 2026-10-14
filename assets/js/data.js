/* Site content. To reuse this theme for another Play Console account,
   edit SITE and APPS here and the color tokens at the top of assets/css/style.css. */
window.SITE = {
  name: "OBanaf Apps Studio",
  short: "OBanaf",
  email: "info@pandezlabsltd.site",
  playDevUrl: "https://play.google.com/store/apps/dev?id=5410437552612865577",
  stats: [
    { value: 9, suffix: "", label: "Apps published", note: "Live on Google Play across six categories." },
    { value: 120, suffix: "K+", label: "Downloads", note: "People installing our apps every single day." },
    { value: 4.8, suffix: "★", decimals: 1, label: "Average rating", note: "Weighted across 900+ public reviews." },
    { value: 5, suffix: "+", label: "Languages & scripts", note: "Amharic, Nepali, Farsi, Dari and English." }
  ]
};

window.APPS = [
  {
    id: "com.ethiopian.calender.converter",
    title: "Ethiopian Calendar",
    native: "ቀን መቁጠሪያ",
    category: "Productivity",
    tagline: "Ethiopian ↔ Gregorian date converter with holidays, reminders and Ge’ez numbers.",
    features: ["Meskerem to Pagume month views", "Two-way date converter", "Orthodox holidays & fasting days", "Reminders and Ge’ez numerals"],
    rating: 5.0, reviews: 709, downloads: "100K+", shots: 8, featured: true, hue: "#2bb673"
  },
  {
    id: "com.ob.aimathsolver.scan.solve",
    title: "AI Math Solver",
    native: "With Solution",
    category: "Education",
    tagline: "Scan any printed or handwritten problem and get step-by-step solutions from an AI tutor.",
    features: ["Camera scan & solve", "Step-by-step explanations", "Algebra to calculus", "Type or snap word problems"],
    rating: 3.4, reviews: 115, downloads: "10K+", shots: 8, featured: true, hue: "#7c5cff"
  },
  {
    id: "com.nepalipatro.nepalicalendar",
    title: "Nepali Patro",
    native: "नेपाली पात्रो",
    category: "Productivity",
    tagline: "Bikram Sambat calendar 2083 with festivals, holidays, Rashifal, Panchang and widgets.",
    features: ["BS ↔ AD calendar views", "Daily Rashifal & Panchang", "Festivals and public holidays", "Home screen widgets"],
    rating: 5.0, reviews: 37, downloads: "5K+", shots: 6, featured: true, hue: "#e5484d"
  },
  {
    id: "com.persian.calendar",
    title: "Persian Calendar",
    native: "تقویم فارسی",
    category: "Productivity",
    tagline: "Solar Hijri calendar with date converter, currency and gold rates — in Farsi & Dari.",
    features: ["All 12 Shamsi months", "Nowruz, Yalda & Afghan holidays", "Shamsi ↔ Gregorian ↔ Hijri", "Currency & gold rate converter"],
    rating: 5.0, reviews: 49, downloads: "5K+", shots: 5, hue: "#f5a524"
  },
  {
    id: "com.ts.smart.printer.scanner.mobile.printshare",
    title: "Smart Printer App",
    native: "Mobile Print",
    category: "Tools",
    tagline: "Print and scan from your phone — documents, PDFs and photos, over Wi-Fi or Bluetooth.",
    features: ["Wireless printing, no drivers", "Document scanner to PDF", "Photos, emails & web pages", "Works with most printers"],
    downloads: "500+", shots: 6, hue: "#0ea5e9"
  },
  {
    id: "com.hd.camera.photo.android",
    title: "HD Camera Beauty",
    native: "& Filter",
    category: "Photography",
    tagline: "A 4K beauty camera with AI filters, one-tap retouching and a full photo editor.",
    features: ["HD photo & video capture", "AI beauty & skin smoothing", "Filters, stickers and frames", "Collage maker"],
    downloads: "100+", shots: 6, hue: "#ec4899"
  },
  {
    id: "com.ob.pose.camera.photo.guide",
    title: "Pose Camera",
    native: "Photo Guide",
    category: "Photography",
    tagline: "Real-time pose suggestions on your camera, so every photo looks natural and confident.",
    features: ["Live pose overlays", "Solo, couple & group ideas", "Travel, party & fashion poses", "Simple for beginners"],
    downloads: "100+", shots: 5, hue: "#f97316"
  },
  {
    id: "com.ob.dress.ai.tryon.fashion",
    title: "Dress AI",
    native: "AI Try On",
    category: "Lifestyle",
    tagline: "Upload a photo and try on new outfits instantly with an AI virtual fitting room.",
    features: ["Realistic virtual try-on", "AI outfit generator", "Try colors & styles before you buy", "Works from a single photo"],
    downloads: "10+", shots: 5, hue: "#a855f7"
  },
  {
    id: "com.ob.aigiftfinder.wishlist",
    title: "AI Gift Finder",
    native: "Wishlist",
    category: "Shopping",
    tagline: "Answer a few questions and get personalised gift ideas for any person, budget and occasion.",
    features: ["Personalised AI suggestions", "Birthdays, holidays & anniversaries", "Budget-aware picks", "Save ideas to a wishlist"],
    downloads: "1+", shots: 5, hue: "#14b8a6"
  }
];
