# 🧶 Crochet Temperature Blanket App
A cozy blend of code, color, and creativity.

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
- Save daily entries to JSON  
- View summaries for any saved day  
- Prevent duplicate entries  
- Offer to create an entry for past dates with no saved data  
- Display a simple, hard‑coded granny square pattern  
- Navigate through a clean, simple home menu  

---

## 🧠 Technical Skills Demonstrated

### **Data validation & error handling**  
Ensuring user input is clean, safe, and predictable — from date formats to temperature ranges — with graceful fallbacks when things go sideways.

### **JSON data persistence**  
Loading, updating, and storing daily entries in a structured, human‑readable format that keeps the project organized and future‑proof.

### **Mapping logic**  
Converting temperatures → colors → yarn selections using Python ranges and dictionaries to create a clean, extensible mapping system.

---

## 🧩 How It Works
The app follows a simple workflow. It was meticulously designed to keep things organized and reliable, but I wanted it to still be fun to use:

1. When the app starts, it loads your existing JSON data (or creates a fresh file if you’re new here).  
2. You begin on a small home menu where you can pick a date, view a saved day, see a granny square pattern, or exit.  
3. Choosing a date kicks off a quick validation check — no future dates, no duplicates, no weird formats.  
4. If the date doesn’t have an entry yet, the app offers to create one right then and there.  
5. The app then grabs the day’s temperature (or lets you type it in yourself).  
6. That temperature gets translated into a color based on predefined ranges.  
7. The color then maps to a yarn shade, giving the data a real‑world crafting connection.  
8. Once everything looks good, the app saves the entry to JSON.  
9. You can also pull up any saved day to see its full summary.  
10. And if you’re feeling crafty, you can view a simple, hard‑coded granny square pattern for inspiration.  

---

## 🧶 Optional Extras
These features aren’t the core workflow, but they add personality and flexibility to the app — and they support the long‑term vision of turning this into a fully visual, calendar‑based project.

---

### **Create Entries for Past Dates**  
If a user selects a past date that doesn’t have an entry yet, the app offers to create one on the spot. This keeps the experience smooth and makes it easy to fill in missed days without breaking the flow.

---

### **Simple Granny Square Pattern (Hard‑Coded for Now)**  
For users who want a quick reference, the app can display a basic granny square pattern. It’s intentionally simple and hard‑coded for now, but it lays the groundwork for future pattern customization.

---

### **Future Calendar Visualization**  
The long‑term goal is a color‑coded calendar that fills in as each day is completed. The current JSON structure already supports this, making it easy to build a visual layer later — whether in the terminal, a GUI, or a web interface.

---

## 📁 Project Structure (planned)
Right now, the project is intentionally simple:

```
app.py
README.md
```

I’ll be expanding the structure as the project grows. Future versions will include folders like:

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