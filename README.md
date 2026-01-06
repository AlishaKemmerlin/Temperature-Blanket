# 🧶 Crochet Temperature Blanket App
A cozy blend of code, color, and creativity.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Project-Learning_Project-purple)
![Category](https://img.shields.io/badge/Type-Creative_Coding-pink)
![Last Commit](https://img.shields.io/github/last-commit/AlishaKemmerlin/Temperature-Blanket)
![Crochet Project](https://img.shields.io/badge/Crochet_Project-%F0%9F%A7%B6-pink)

---

## ✨ Overview
This project is the first step in a larger vision. Right now, it’s a Python‑based application that tracks daily temperatures and maps them to yarn colors, helping users create a year‑long crochet weather blanket. It’s part data collection, part creative expression, and entirely born from the thought, *“I want to code something more interesting than a basic stitch counter.”*

For now, the app runs in the terminal and guides users through selecting dates, fetching or entering temperatures, mapping colors, saving entries, and viewing summaries — all backed by **JSON** data storage.

---

## 🛠️ Features
A quick look at what the app can do:

- Select and validate dates  
- Fetch or manually enter daily temperatures  
- Map temperatures to color ranges  
- Map colors to yarn selections  
- Save daily entries using a centralized JSON helper
- View summaries for any saved day  
- Prevent duplicate entries
- Allow users to update and delete entries
- Offer to create an entry for past dates with no saved data  
- Display a simple, hard‑coded granny square pattern  
- Navigate through a clean, simple home menu  

---

## 🧠 Technical Skills Demonstrated

### **Data validation & error handling**  
Ensuring user input is clean, safe, and predictable — from date formats to temperature ranges — with graceful fallbacks when things go sideways.

### **JSON data persistence**  
Loading, updating, and storing daily entries using a centralized save_data() helper for clean consistant JSON persistence. 

### **Mapping logic**  
Converting temperatures → colors → yarn selections using Python ranges and dictionaries to create a clean, extensible mapping system.

---

## 🧩 How It Works
The app follows a simple workflow. It was meticulously designed to keep things organized and reliable, but I wanted it to still be fun to use:

When the app starts, it checks your JSON file -- the little storage box where all your weather-blanket memories live. If the file is missing or messy, it doesn't panic: it simply starts fresh, like pulling out a new skein when the old one gets tangled.  

You begin at the Home Menu, a simple hub where you can **Record Today's Temperature**, *Look Into the Past*, **Read the Instructions** (for the 80th time, because you didn't remember for the last 79 times), *Open the Edit Menu*, or peek at the **Granny Square Pattern**. Everything branches out from here.   

Choosing a date kicks off a quick reality check — no future dates, no duplicates, no weird formats. (No, this app cannot read Klingon.) The app keeps everything neat and tidy so your blanket stays accurate. 

If the date is new, the app helps you create an entry. At this time, it has you type in the high temperature in your area (future update will allow the app to fetch it all on its own). It then translates that number into a color based on a built-in range. That color becomes a yarn shade -- the part that makes this whole project feel real and tactile. The app takes the guesswork out of what color to use. 

Once everything is mapped, the entry is saved using a centralized **<code>save_data()</code>** helper. This keeps your JSON file consistent and your code base clean.

You can revisit any saved day to see its details, or head into the **Edit Menu** to update or delete entries when life happens and things need adjusting. And whenever you want a quick creative nudge, the granny square pattern is right there -- simple, familiar, and ready to use. 

The whole flow is structured, friendly and a bit whimsical -- the kind of cozy order that makes a long term craft project feel doable. 

---

## 🧶 Optional Extras
These features aren’t the core workflow, but they add personality and flexibility to the app — and they support the long‑term vision of turning this into a fully visual, calendar‑based project.

---

### **Create Entries for Past Dates**  
If a user selects a past date that doesn’t have an entry yet, the app offers to create one on the spot. This keeps the experience smooth and makes it easy to fill in missed days without breaking the flow.

### **Simple Granny Square Pattern (Hard‑Coded for Now)**  
For users who want a quick reference, the app can display a basic granny square pattern. It’s intentionally simple and hard‑coded for now, but it lays the groundwork for future pattern customization.

### **Future Calendar Visualization**  
The long‑term goal is a color‑coded calendar that fills in as each day is completed. The current JSON structure already supports this, making it easy to build a visual layer later — whether in the terminal, a GUI, or a web interface.

---

## 📁 Project Structure

I was going to keep the project simple, but it kept growing and growing, so I had to add new files:

```
📂temperature_blanket/
│
├── 🐍 main.py                # Main program: menus, flow, features
├── 📝 edit_menu.py           # Editing features (delete, update, etc.)
├── 🧩 helpers.py             # Shared helper functions (dates, saving, mapping)
├── 🗃️ my_blanket_data.json   # Saved temperature entries
└── 📘 README.md              # Project documentation

```

I will continue to expand the structure as the project grows.
Future versions will include folders like:

```
📂 data/       # for JSON storage
📂 src/        # for modular Python logic
📂 assets/     # for images or visual references
```

…but those will be added naturally as the project reaches those stages.

---

## 🚀 Future Enhancements
- 💡 Add real weather API integration  
- 💡 Build a desktop GUI (Tkinter or PyQt)  
- 💡 Create a web version  
- 💡 Add color charts and pattern suggestions  
- 💡 Generate a visual calendar view  
- 💡 Export summaries or yearly reports  

---

## 💬 Final Thoughts
This project started as a simple idea:  
*“How can I blend crochet and code in a way that feels meaningful and creative?”*

That sparked the flame that grew into the wildfire now known as **The Weather Blanket App** — blending logic, design, and craft — and it’s still growing.

I hope you enjoy exploring it as much as I building it
