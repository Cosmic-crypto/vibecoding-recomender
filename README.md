# 🚀 Vibecoder AI Tool Assistant

An AI-powered desktop application that recommends the best Vibecoder tools based on your needs, provides comprehensive tutorials, and includes an intelligent chatbot for questions.

## ✨ Features

- **🔍 Smart Tool Recommendation**: Describe what you want to do, and the AI recommends the perfect tool
- **📚 Complete Tutorials**: Step-by-step guides for each recommended tool
- **💬 AI Chatbot**: Ask questions about the tools and get instant answers
- **🎨 Modern UI**: Beautiful dark-themed interface built with CustomTkinter
- **🛠️ 8 Essential Tools**: Code Editor, Web Scraper, GUI Builder, AI Assistant, Git, Package Manager, API Tester, Database Manager

## 📋 Requirements

```bash
Python 3.7+
customtkinter>=5.0.0
openai>=0.27.0 (optional for AI chat)
```

## 🚀 Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python vibecoder_assistant.py
   ```

## 📖 How to Use

### 1. Find the Right Tool

1. In the **"What do you want to do?"** text box, describe your task:
   - "I want to build a desktop app"
   - "I need to scrape website data"
   - "I want to manage code versions"
   - "I need to test APIs"

2. Click **🔍 Find Tool**

3. View recommended tools with:
   - Description
   - Download/Installation instructions
   - Website links
   - Use cases

### 2. Read the Tutorial

- The **Tutorial & Details** panel shows a complete step-by-step guide
- Includes code examples
- Installation instructions
- Best practices

### 3. Ask Questions

- Use the **💬 Ask AI Assistant** chatbot for follow-up questions
- Works with or without OpenAI API
- **With OpenAI API**: Advanced AI responses
- **Without API**: Rule-based helpful responses

### 4. Optional: Enable Advanced AI Chat

1. Get an OpenAI API key from [platform.openai.com](https://platform.openai.com/)
2. Enter your API key in the field at the bottom
3. Now the chatbot uses GPT-3.5 for intelligent responses!

## 🛠️ Available Tools

| Tool | Description | Keywords |
|------|-------------|----------|
| **Code Editor** | Full-featured IDE with syntax highlighting | edit, code, ide, programming |
| **Web Scraper** | Extract data from websites | scrape, web, data, html |
| **GUI Builder** | Build desktop applications | gui, interface, tkinter, app |
| **AI Assistant** | OpenAI-powered coding help | ai, chatgpt, copilot |
| **Git Version Control** | Manage code changes | git, github, version, commit |
| **Package Manager** | Manage Python packages | pip, install, library |
| **API Tester** | Test REST APIs | api, rest, http, request |
| **Database Manager** | SQLite database management | database, sql, data |

## 💡 Example Queries

Try these in the input box:

- "How do I create a GUI application?"
- "I want to extract data from websites"
- "Help me test my REST API"
- "I need to track my code changes"
- "I want to build a code editor"
- "How do I manage Python packages?"

## 🎯 Features Breakdown

### Smart Recommendation Engine
- Keyword matching algorithm
- Scores tools based on relevance
- Returns top 3 matches

### Comprehensive Tutorials
- Installation guides
- Code examples
- Best practices
- Common use cases

### Intelligent Chatbot
- Context-aware responses
- OpenAI integration (optional)
- Rule-based fallback
- Helpful suggestions

## 🔧 Technical Details

- **Framework**: CustomTkinter
- **Python Version**: 3.7+
- **AI Integration**: OpenAI GPT-3.5-turbo (optional)
- **Architecture**: Event-driven GUI with threaded API calls

## 🎨 Screenshots

The application features:
- Left panel: Input and tool recommendations
- Right panel: Tutorials and chatbot
- Color-coded responses
- Clean, modern interface

## 🤝 Contributing

This tool includes a curated database of Vibecoder tools. To add more tools, edit the `TOOLS_DB` dictionary in `vibecoder_assistant.py`.

## 📝 Notes

- OpenAI API is **optional** - the app works without it
- Rule-based chatbot provides basic responses without API
- API key is never stored permanently (enter each session)
- All tools and tutorials are included in the database

## 🐛 Troubleshooting

**Issue**: OpenAI error
- **Solution**: Check your API key is valid and has credits

**Issue**: Can't find tools
- **Solution**: Try different keywords or be more specific

**Issue**: GUI doesn't display properly
- **Solution**: Make sure customtkinter is installed: `pip install customtkinter`

## 📄 License

Free to use and modify for personal and educational purposes.

## 🎉 Enjoy!

Start finding the perfect tools for your coding projects!
