<a id="readme-top"></a>   

<div align="center">

  <img src="kuro.png" alt="Logo" width="80" height="80">

  <h3 align="center">Kuro-CLI : Voice-Controlled Terminal Assistant</h3>

  <p align="center">
    <a href="https://github.com/Sukumarsawant/Kuro-CLI-"><strong>Explore the Code »</strong></a>
    <br/>
    <br/>
    <a href="#usage">View Usage</a>
    ·
    <a href="#issues">Report Bug</a>
    ·
    <a href="#contributing">Request Feature</a>
  </p>

</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details> <br><br>
<!-- ABOUT THE PROJECT -->
About The Project:  <br><br>
Kuro is a command line interface powered by AI that listens to your commands and uses Google's Gemini AI to execute them.
<ul>
  <li>Convert speech to text </li> <br>
  <li>Use Gemini AI to perform coding related tasks</li> <br>
  <li>Generate and execute the appropriate terminal command</li> <br>
</ul> 
<p align="right">(<a href="#readme-top">back to top</a>)</p>
Built With: 
<ul>
  <li>Python</li> <br>
  <li>Google Generative AI (Gemini)</li><br>
  <li>SpeechRecognition</li> <br>
  <li>Python-dotenv</li><br>
</ul>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- GETTING STARTED -->
Getting Started:  <br><br>
To run Kuro locally.
<br><br>
Prerequisites:  
<br>
<ul>
  <li>Python 3.8+</li> <br>
  <li>Microphone</li><br>
  <li>Google Gemini API Key</li> <br>
</ul> <br> 
Installation: 
<br>
<br>
1. Clone the repo
<br><br>
git clone https://github.com/Sukumarsawant/Kuro-CLI-.git  
cd Kuro-CLI-
<br>
<br>
2. Create a .env file and add your Gemini API key:
<br>
<br>
GEMINI_API_KEY=your_api_key_here
<br>
<br>
3. Run the assistant:
<br><br>
python main.py
<br><br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- USAGE --> <br> 
Usage: 
<br> <br>
Once it starts running, speak commands like:
<br><br>
"- Open Notepad" 
<br><br>
"- Open Visual Studio Code"
<br><br>
"- Open Chrome & search for Python" 
<br><br>
To stop Kuro, say:
<br><br>
"- exit"
<br><br>
"- quit"
<br><br>
"-  stop"
<br><br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- CONTRIBUTING -->
Contributing: 
<br><br>
Contributions are welcome! Fork the repo and submit a PR.
<br><br>
1. Fork the Project
<br><br>
2. Create a new branch (git checkout -b feature/YourFeature)
<br><br>
3. Commit changes (git commit -m 'Add YourFeature')
<br><br>
4. Push to the branch (git push origin feature/YourFeature)
<br><br>
5. Open a Pull Request
<br><br>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- ACKNOWLEDGMENTS -->
Acknowledgments: 
<br>
<ul>
  <li>SpeechRecognition Docs </li> <br>
  <li>Google Gemini AI</li> <br>
  <li>Best README Template</li> <br>
  <li>Python-dotenv</li> <br>
</ul>