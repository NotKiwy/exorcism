<p align="center">
  <img src="https://raw.githubusercontent.com/notkiwy/exorcism/main/assets/exorcism.png" alt="Screen" width="900"/>
</p>

# 🖤 EXORCISM PACKAGE

A powerful Python package for terminal text manipulation, including gradients, animations, tables, and number system converter.

## ⚡ Quick Installation

```
pip install exorcism
```

## 🚀 Features

### 🌈 Gradient Text
```
from exorcism import color

# Horizontal gradient
color("Hello World!", "red", "blue", "h")

# Vertical gradient
color("Multi\nLine\nText", "green", "yellow", "v")
```

### 🔄 Function Renaming
```
from exorcism import system

# Create short aliases for built-in functions
system("print", "p")
p("Hello!")  # Now works as print()
```

### ✨ Animated Text
```
from exorcism import animate

animate("Loading...", "typing")  # Typing effect
animate("Warning!", "fade")  # Fade effect
```

### 📦 Framed Text
```
from exorcism import frame

frame("Important message!")  # Single frame
frame("Special message", "double")  # Double frame
frame("Simple note", "dots")  # Dotted frame
```

### 🎯 Centered Text
```
from exorcism import center

center("Centered text")
center("""Multiple\nLines\nOf Text")
```

### 📊 Tables
```
from exorcism import table

data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Alice", "age": 25, "city": "London"}
]
table(data)
```

### ⏳ Progress Bar
```
from exorcism import progress

for i in range(101):
    progress(i, 100)
```

### 🔢 Number System Converter
```
from exorcism import convert

convert(42, '10', '2')     # 42₁₀ = 101010₂
convert('1A', '16', '10')  # 1A₁₆ = 26₁₀
convert(1010, '2', '16')   # 1010₂ = A₁₆
```

## 🎨 Available Colors for Gradients
| Color Name | Description |
|------------|-------------|
| 🔴 red | Red color |
| 💚 green | Green color |
| 💙 blue | Blue color |
| 💛 yellow | Yellow color |
| 🔷 cyan | Cyan color |
| 💜 magenta | Magenta color |
| ⚪ white | White color |
| ⚫ black | Black color |
| 🟧 orange | Orange color |
| 🟣 purple | Purple color |
| 🎀 pink | Pink color |
| ⚪ gray | Gray color |

## 🛠️ Requirements
- Python 3.6+
- Windows/Linux/MacOS

## 📝 License
MIT License

## 👨‍💻 Author
notkiwy

## 🌟 Star Us on GitHub!
If you find this package useful, please consider giving it a star on GitHub!

## 🤝 Contributing
We welcome contributions! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📫 Contact
- GitHub: @NotKiwy
- Email: notkiwy@yahoo.com

## 🙏 Acknowledgments
Special thanks to all contributors who helped make this package awesome!
