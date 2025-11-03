import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
from typing import Dict, List
import threading

# Try to import openai
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

COLORS = {
    'bg_primary': '#1a1a2e',
    'bg_secondary': '#16213e',
    'accent': '#00d4ff',
    'text_primary': '#eaeaea'
}

# Tools Database
TOOLS_DB = {
    "Code Editor": {
        "keywords": ["edit", "code", "write", "ide", "programming", "syntax", "text editor"],
        "description": "Full-featured code editor with syntax highlighting, autocomplete, multi-language support",
        "download": "Available as app_ctk.py in your workspace",
        "website": "Built with CustomTkinter - https://github.com/TomSchimansky/CustomTkinter",
        "use_cases": ["Write Python/JavaScript/Java/C++ code", "Syntax highlighting", "Auto-complete"],
        "tutorial": """**CODE EDITOR TUTORIAL**

1. LAUNCH
   Run: python app_ctk.py

2. CREATE/OPEN FILES
   - File → New (Ctrl+N)
   - File → Open (Ctrl+O)
   - Use file explorer on left

3. WRITE CODE
   - Auto-indent (press Enter after : or {)
   - Auto-close brackets
   - Line numbers displayed

4. AUTOCOMPLETE
   - Type 2+ characters
   - Press Ctrl+Space for suggestions

5. RUN CODE
   - Press F5 or click Run button
   - Output appears in bottom panel

6. FEATURES
   - Syntax highlighting for multiple languages
   - Integrated terminal
   - File management
   - VS Code-style theme"""
    },
    
    "Web Scraper": {
        "keywords": ["scrape", "web", "extract", "data", "crawl", "html", "parse", "website"],
        "description": "Extract data from websites using BeautifulSoup and requests",
        "download": "pip install beautifulsoup4 requests lxml",
        "website": "https://www.crummy.com/software/BeautifulSoup/",
        "use_cases": ["Extract website data", "Parse HTML content", "Collect information"],
        "tutorial": """**WEB SCRAPER TUTORIAL**

1. INSTALLATION
   pip install beautifulsoup4 requests

2. BASIC SCRAPING
   import requests
   from bs4 import BeautifulSoup
   
   url = 'https://example.com'
   response = requests.get(url)
   soup = BeautifulSoup(response.content, 'html.parser')
   
   # Extract all headings
   headings = soup.find_all('h1')
   for h in headings:
       print(h.text)

3. KEY METHODS
   - soup.find('tag') → First element
   - soup.find_all('tag') → All elements
   - soup.select('.class') → CSS selectors
   - soup.find(id='name') → By ID

4. EXTRACT LINKS
   links = soup.find_all('a')
   for link in links:
       print(link.get('href'))

5. BEST PRACTICES
   - Add User-Agent header
   - Respect robots.txt
   - Add delays between requests
   - Handle exceptions"""
    },
    
    "GUI Builder": {
        "keywords": ["gui", "interface", "window", "tkinter", "customtkinter", "ui", "app", "desktop"],
        "description": "Build beautiful desktop applications with CustomTkinter",
        "download": "pip install customtkinter",
        "website": "https://github.com/TomSchimansky/CustomTkinter",
        "use_cases": ["Desktop applications", "User interfaces", "Dashboards"],
        "tutorial": """**GUI BUILDER TUTORIAL**

1. INSTALLATION
   pip install customtkinter

2. BASIC WINDOW
   import customtkinter as ctk
   
   app = ctk.CTk()
   app.geometry(\"800x600\")
   app.title(\"My App\")
   
   ctk.set_appearance_mode(\"dark\")
   app.mainloop()

3. ADD WIDGETS
   # Button
   btn = ctk.CTkButton(app, text=\"Click\", command=on_click)
   btn.pack(pady=20)
   
   # Entry
   entry = ctk.CTkEntry(app, placeholder_text=\"Text\")
   entry.pack(pady=10)
   
   # Label
   label = ctk.CTkLabel(app, text=\"Hello\")
   label.pack()

4. LAYOUT
   - pack() → Simple stacking
   - grid() → Table layout
   - place() → Absolute positioning

5. FRAMES
   frame = ctk.CTkFrame(app)
   frame.pack(pady=20, fill=\"both\", expand=True)
   
   # Add widgets to frame
   label = ctk.CTkLabel(frame, text=\"In Frame\")
   label.pack()"""
    },
    
    "AI Assistant": {
        "keywords": ["ai", "assistant", "help", "chatgpt", "copilot", "completion", "smart"],
        "description": "AI-powered coding assistant using OpenAI API",
        "download": "pip install openai",
        "website": "https://platform.openai.com/",
        "use_cases": ["Code completion", "Bug fixes", "Code explanations", "Documentation"],
        "tutorial": """**AI ASSISTANT TUTORIAL**

1. INSTALLATION
   pip install openai

2. GET API KEY
   - Visit platform.openai.com
   - Create account
   - Go to API Keys section
   - Create new key

3. BASIC USAGE
   import openai
   
   openai.api_key = \"your-key-here\"
   
   response = openai.ChatCompletion.create(
       model=\"gpt-3.5-turbo\",
       messages=[
           {\"role\": \"user\", \"content\": \"Explain this code\"}
       ]
   )
   print(response.choices[0].message.content)

4. SECURITY
   # Use environment variables
   import os
   openai.api_key = os.getenv('OPENAI_API_KEY')

5. USE CASES
   - Code review and suggestions
   - Explain complex code
   - Generate documentation
   - Debug errors
   - Refactor code"""
    },
    
    "Git Version Control": {
        "keywords": ["git", "version", "control", "github", "commit", "push", "pull", "repository"],
        "description": "Track and manage code changes with Git",
        "download": "https://git-scm.com/downloads",
        "website": "https://github.com | https://git-scm.com",
        "use_cases": ["Version control", "Collaboration", "Branch management", "Code backup"],
        "tutorial": """**GIT VERSION CONTROL TUTORIAL**

1. INSTALLATION
   Download from: https://git-scm.com/downloads
   Verify: git --version

2. SETUP
   git config --global user.name \"Your Name\"
   git config --global user.email \"email@example.com\"

3. CREATE REPOSITORY
   git init                    # New project
   git clone https://github.com/user/repo.git  # Existing

4. BASIC WORKFLOW
   git status                  # Check status
   git add file.py             # Stage file
   git add .                   # Stage all
   git commit -m \"message\"     # Commit
   git push origin main        # Push to remote

5. BRANCHING
   git branch feature-name     # Create branch
   git checkout feature-name   # Switch branch
   git merge feature-name      # Merge branch

6. GITHUB
   git remote add origin https://github.com/user/repo.git
   git push -u origin main"""
    },
    
    "Package Manager": {
        "keywords": ["pip", "package", "install", "library", "dependency", "module", "requirements"],
        "description": "Manage Python packages with pip",
        "download": "Included with Python",
        "website": "https://pip.pypa.io/ | https://pypi.org/",
        "use_cases": ["Install libraries", "Manage dependencies", "Virtual environments"],
        "tutorial": """**PIP PACKAGE MANAGER TUTORIAL**

1. BASIC INSTALLATION
   pip install package-name
   pip install requests beautifulsoup4 pandas

2. REQUIREMENTS FILE
   pip freeze > requirements.txt
   pip install -r requirements.txt

3. VIRTUAL ENVIRONMENTS
   python -m venv venv
   venv\\Scripts\\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   pip install package-name

4. PACKAGE MANAGEMENT
   pip list                    # List all
   pip show package-name       # Info
   pip uninstall package-name  # Remove
   pip install --upgrade pip   # Update pip

5. EXAMPLE requirements.txt
   customtkinter>=5.0.0
   requests==2.31.0
   beautifulsoup4==4.12.0"""
    },
    
    "API Tester": {
        "keywords": ["api", "rest", "http", "request", "postman", "test", "endpoint"],
        "description": "Test and debug REST APIs with requests library",
        "download": "pip install requests",
        "website": "https://requests.readthedocs.io/",
        "use_cases": ["Test APIs", "HTTP requests", "Debug endpoints", "API development"],
        "tutorial": """**API TESTER TUTORIAL**

1. INSTALLATION
   pip install requests

2. GET REQUEST
   import requests
   
   response = requests.get('https://api.example.com/data')
   data = response.json()
   print(data)

3. POST REQUEST
   data = {'key': 'value'}
   response = requests.post('https://api.example.com/create', json=data)

4. HEADERS & AUTH
   headers = {'Authorization': 'Bearer token'}
   response = requests.get(url, headers=headers)

5. ERROR HANDLING
   try:
       response = requests.get(url, timeout=5)
       response.raise_for_status()
   except requests.exceptions.HTTPError as e:
       print(f\"Error: {e}\")

6. HTTP METHODS
   requests.get()      # Retrieve
   requests.post()     # Create
   requests.put()      # Update
   requests.delete()   # Delete"""
    },
    
    "Database Manager": {
        "keywords": ["database", "sql", "sqlite", "data", "query", "table", "crud"],
        "description": "Manage databases with SQLite and SQLAlchemy",
        "download": "Built into Python (SQLite) | pip install sqlalchemy",
        "website": "https://www.sqlite.org/ | https://www.sqlalchemy.org/",
        "use_cases": ["Store data", "Query databases", "CRUD operations", "Data persistence"],
        "tutorial": """**DATABASE MANAGER TUTORIAL**

1. SQLITE BASICS
   import sqlite3
   
   conn = sqlite3.connect('database.db')
   cursor = conn.cursor()
   
   # Create table
   cursor.execute('''
       CREATE TABLE users (
           id INTEGER PRIMARY KEY,
           name TEXT,
           email TEXT
       )
   ''')
   
   # Insert
   cursor.execute(\"INSERT INTO users VALUES (?, ?, ?)\",
                  (1, \"John\", \"john@email.com\"))
   
   # Query
   cursor.execute(\"SELECT * FROM users\")
   rows = cursor.fetchall()
   
   conn.commit()
   conn.close()

2. CRUD OPERATIONS
   CREATE → INSERT
   READ → SELECT
   UPDATE → UPDATE
   DELETE → DELETE

3. BEST PRACTICES
   - Use parameterized queries
   - Close connections
   - Handle exceptions
   - Regular backups"""
    }
}


class RecommendationEngine:
    """AI-powered tool recommendation"""
    
    def __init__(self):
        self.tools = TOOLS_DB
    
    def recommend(self, user_input: str) -> List[Dict]:
        """Recommend tools based on user input"""
        user_input = user_input.lower()
        scores = {}
        
        for tool_name, tool_data in self.tools.items():
            score = 0
            matches = []
            
            # Check keyword matches
            for keyword in tool_data['keywords']:
                if keyword in user_input:
                    score += 10
                    matches.append(keyword)
            
            # Check description match
            if any(word in tool_data['description'].lower() for word in user_input.split()):
                score += 5
            
            if score > 0:
                scores[tool_name] = {
                    'score': score,
                    'matches': matches,
                    'data': tool_data
                }
        
        # Sort by score
        sorted_tools = sorted(scores.items(), key=lambda x: x[1]['score'], reverse=True)
        return [(name, data['data']) for name, data in sorted_tools[:3]]


class VibcoderAssistant(ctk.CTk):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        
        self.title("Vibecoder AI Assistant")
        self.geometry("1200x800")
        
        self.engine = RecommendationEngine()
        self.chat_history = []
        self.openai_key = ""
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        
        # Header
        header = ctk.CTkFrame(self, fg_color=COLORS['bg_secondary'], height=80)
        header.pack(fill="x", padx=0, pady=0)
        header.pack_propagate(False)
        
        title = ctk.CTkLabel(
            header,
            text="🚀 Vibecoder AI Tool Assistant",
            font=("Helvetica", 28, "bold"),
            text_color=COLORS['accent']
        )
        title.pack(pady=20)
        
        # Main container
        main_container = ctk.CTkFrame(self, fg_color=COLORS['bg_primary'])
        main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Left panel - Input and recommendations
        left_panel = ctk.CTkFrame(main_container, fg_color=COLORS['bg_secondary'])
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 5))
        
        # Input section
        input_label = ctk.CTkLabel(
            left_panel,
            text="What do you want to do?",
            font=("Helvetica", 16, "bold")
        )
        input_label.pack(pady=(20, 10), padx=20)
        
        self.input_entry = ctk.CTkTextbox(
            left_panel,
            height=100,
            font=("Helvetica", 14),
            fg_color=COLORS['bg_primary']
        )
        self.input_entry.pack(pady=10, padx=20, fill="x")
        
        # Button frame
        btn_frame = ctk.CTkFrame(left_panel, fg_color="transparent")
        btn_frame.pack(pady=10)
        
        recommend_btn = ctk.CTkButton(
            btn_frame,
            text="🔍 Find Tool",
            command=self.find_tool,
            font=("Helvetica", 14, "bold"),
            height=40,
            width=150,
            fg_color=COLORS['accent'],
            hover_color=COLORS['accent']
        )
        recommend_btn.pack(side="left", padx=5)
        
        clear_btn = ctk.CTkButton(
            btn_frame,
            text="Clear",
            command=self.clear_all,
            font=("Helvetica", 14),
            height=40,
            width=100
        )
        clear_btn.pack(side="left", padx=5)
        
        # Results area
        results_label = ctk.CTkLabel(
            left_panel,
            text="Recommended Tools:",
            font=("Helvetica", 14, "bold")
        )
        results_label.pack(pady=(20, 10), padx=20)
        
        self.results_text = ctk.CTkTextbox(
            left_panel,
            font=("Consolas", 11),
            fg_color=COLORS['bg_primary']
        )
        self.results_text.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Right panel - Tutorial and chatbot
        right_panel = ctk.CTkFrame(main_container, fg_color=COLORS['bg_secondary'])
        right_panel.pack(side="right", fill="both", expand=True, padx=(5, 0))
        
        # Tutorial section
        tutorial_label = ctk.CTkLabel(
            right_panel,
            text="📚 Tutorial & Details",
            font=("Helvetica", 16, "bold")
        )
        tutorial_label.pack(pady=(20, 10), padx=20)
        
        self.tutorial_text = ctk.CTkTextbox(
            right_panel,
            font=("Consolas", 10),
            fg_color=COLORS['bg_primary']
        )
        self.tutorial_text.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Chatbot section
        chat_label = ctk.CTkLabel(
            right_panel,
            text="💬 Ask AI Assistant",
            font=("Helvetica", 14, "bold")
        )
        chat_label.pack(pady=(10, 5), padx=20)
        
        chat_frame = ctk.CTkFrame(right_panel, fg_color="transparent")
        chat_frame.pack(pady=5, padx=20, fill="x")
        
        self.chat_input = ctk.CTkEntry(
            chat_frame,
            placeholder_text="Ask a question about the tool...",
            font=("Helvetica", 12),
            height=35
        )
        self.chat_input.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.chat_input.bind("<Return>", lambda e: self.ask_chatbot())
        
        chat_btn = ctk.CTkButton(
            chat_frame,
            text="Send",
            command=self.ask_chatbot,
            width=80,
            height=35
        )
        chat_btn.pack(side="right")
        
        self.chat_display = ctk.CTkTextbox(
            right_panel,
            height=150,
            font=("Helvetica", 10),
            fg_color=COLORS['bg_primary']
        )
        self.chat_display.pack(pady=10, padx=20, fill="x")
        
        # OpenAI status
        if OPENAI_AVAILABLE:
            api_frame = ctk.CTkFrame(right_panel, fg_color="transparent")
            api_frame.pack(pady=5, padx=20, fill="x")
            
            api_label = ctk.CTkLabel(
                api_frame,
                text="OpenAI API Key:",
                font=("Helvetica", 10)
            )
            api_label.pack(side="left", padx=(0, 5))
            
            self.api_entry = ctk.CTkEntry(
                api_frame,
                placeholder_text="Optional: Enter API key for AI chat",
                show="*",
                font=("Helvetica", 9),
                height=25
            )
            self.api_entry.pack(side="left", fill="x", expand=True)
        else:
            status_label = ctk.CTkLabel(
                right_panel,
                text="⚠️ OpenAI not installed. Install with: pip install openai",
                font=("Helvetica", 9),
                text_color="orange"
            )
            status_label.pack(pady=5, padx=20)
    
    def find_tool(self):
        """Find and display tool recommendations"""
        user_input = self.input_entry.get("1.0", "end-1c").strip()
        
        if not user_input:
            messagebox.showwarning("Input Required", "Please describe what you want to do!")
            return
        
        # Get recommendations
        recommendations = self.engine.recommend(user_input)
        
        # Display results
        self.results_text.delete("1.0", "end")
        
        if not recommendations:
            self.results_text.insert("end", "❌ No matching tools found.\n\n")
            self.results_text.insert("end", "Try describing your task differently, e.g.:\n")
            self.results_text.insert("end", "- 'I want to build a desktop app'\n")
            self.results_text.insert("end", "- 'I need to scrape website data'\n")
            self.results_text.insert("end", "- 'I want to manage code versions'\n")
            return
        
        self.results_text.insert("end", f"✅ Found {len(recommendations)} tool(s) for you!\n\n")
        self.results_text.insert("end", "=" * 60 + "\n\n")
        
        for i, (tool_name, tool_data) in enumerate(recommendations, 1):
            self.results_text.insert("end", f"🔧 {i}. {tool_name}\n", "title")
            self.results_text.insert("end", "-" * 60 + "\n")
            self.results_text.insert("end", f"\n📝 Description:\n{tool_data['description']}\n\n")
            self.results_text.insert("end", f"📥 Download/Install:\n{tool_data['download']}\n\n")
            self.results_text.insert("end", f"🌐 Website:\n{tool_data['website']}\n\n")
            self.results_text.insert("end", f"💡 Use Cases:\n")
            for use_case in tool_data['use_cases']:
                self.results_text.insert("end", f"   • {use_case}\n")
            self.results_text.insert("end", "\n" + "=" * 60 + "\n\n")
            
            # Show tutorial for first recommendation
            if i == 1:
                self.show_tutorial(tool_name, tool_data)
        
        self.results_text.tag_config("title", foreground=COLORS['accent'], font=("Helvetica", 14, "bold"))
    
    def show_tutorial(self, tool_name: str, tool_data: Dict):
        """Display tutorial in the tutorial panel"""
        self.tutorial_text.delete("1.0", "end")
        self.tutorial_text.insert("end", f"📚 {tool_name} - Complete Tutorial\n\n", "title")
        self.tutorial_text.insert("end", "=" * 70 + "\n\n")
        self.tutorial_text.insert("end", tool_data['tutorial'])
        self.tutorial_text.insert("end", "\n\n" + "=" * 70 + "\n")
        self.tutorial_text.insert("end", "\n💬 Have questions? Ask the AI assistant below!")
        
        self.tutorial_text.tag_config("title", foreground=COLORS['accent'], font=("Helvetica", 14, "bold"))
        
        # Store current tool for chatbot context
        self.current_tool = tool_name
    
    def ask_chatbot(self):
        """Handle chatbot questions"""
        question = self.chat_input.get().strip()
        
        if not question:
            return
        
        # Display user question
        self.chat_display.insert("end", f"You: {question}\n\n", "user")
        self.chat_input.delete(0, "end")
        
        # Check if OpenAI is available and configured
        if OPENAI_AVAILABLE and hasattr(self, 'api_entry'):
            api_key = self.api_entry.get().strip()
            if api_key:
                self.get_ai_response(question, api_key)
                return
        
        # Fallback: Rule-based responses
        self.get_rule_based_response(question)
        
        self.chat_display.tag_config("user", foreground=COLORS['accent'])
        self.chat_display.tag_config("bot", foreground="#00ff88")
    
    def get_ai_response(self, question: str, api_key: str):
        """Get response from OpenAI API"""
        def api_call():
            try:
                openai.api_key = api_key
                
                context = ""
                if hasattr(self, 'current_tool'):
                    tool_data = TOOLS_DB.get(self.current_tool, {})
                    context = f"Current tool: {self.current_tool}. {tool_data.get('description', '')}"
                
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": f"You are a helpful coding tool assistant. {context}"},
                        {"role": "user", "content": question}
                    ],
                    max_tokens=300
                )
                
                answer = response.choices[0].message.content
                self.after(0, lambda: self.display_bot_response(answer))
                
            except Exception as e:
                self.after(0, lambda: self.display_bot_response(f"Error: {str(e)}\\nFalling back to basic responses."))
                self.after(100, lambda: self.get_rule_based_response(question))
        
        # Run in thread to avoid blocking UI
        threading.Thread(target=api_call, daemon=True).start()
        self.chat_display.insert("end", "AI: Thinking...\n\n", "bot")
    
    def get_rule_based_response(self, question: str):
        """Fallback rule-based responses"""
        question_lower = question.lower()
        
        responses = {
            "how": "Check the tutorial above for step-by-step instructions!",
            "install": "See the 'Download/Install' section in the recommendation results.",
            "where": "Look at the 'Website' field in the tool details above.",
            "what": "The description explains what the tool does. Check the recommendation results!",
            "example": "The tutorial includes code examples. Scroll through the tutorial panel above.",
            "error": "Make sure you've installed all dependencies. Check the installation section.",
            "help": "I can help with tool recommendations. Describe what you want to build!",
            "tutorial": "The full tutorial is displayed in the panel above. Let me know if you need specific clarification.",
        }
        
        response = "I'm a basic assistant without OpenAI API. "
        for keyword, answer in responses.items():
            if keyword in question_lower:
                response = answer
                break
        else:
            response += "Please refer to the tutorial above, or add an OpenAI API key for advanced AI chat!"
        
        self.display_bot_response(response)
    
    def display_bot_response(self, response: str):
        """Display chatbot response"""
        # Remove "Thinking..." message if present
        content = self.chat_display.get("1.0", "end")
        if "Thinking..." in content:
            lines = content.split("\n")
            self.chat_display.delete("1.0", "end")
            for line in lines:
                if "Thinking..." not in line:
                    self.chat_display.insert("end", line + "\n")
        
        self.chat_display.insert("end", f"AI: {response}\n\n", "bot")
        self.chat_display.see("end")
    
    def clear_all(self):
        """Clear all text fields"""
        self.input_entry.delete("1.0", "end")
        self.results_text.delete("1.0", "end")
        self.tutorial_text.delete("1.0", "end")
        self.chat_display.delete("1.0", "end")
        self.chat_input.delete(0, "end")


def main():
    """Main entry point"""
    app = VibcoderAssistant()
    app.mainloop()


if __name__ == "__main__":
    main()
