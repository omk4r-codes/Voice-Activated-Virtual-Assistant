# ai-desktop-assistant
<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="VoiceActivated_Virtual_Assistant_0"></a>Voice-Activated Virtual Assistant</h1>
<h5 class="code-line" data-line-start=1 data-line-end=2 ><a id="_Ong_its_the_simplest_one__1"></a><em>Ong it’s the simplest one!</em></h5>
<p class="has-line-data" data-line-start="4" data-line-end="5">This Python script creates a voice-activated virtual assistant that can perform various tasks such as opening websites, playing songs, providing the current time, and even generating responses using OpenAI’s GPT-3 language model.</p>
<h2 class="code-line" data-line-start=7 data-line-end=8 ><a id="Features_7"></a>Features</h2>
<ul>
<li class="has-line-data" data-line-start="9" data-line-end="10"><strong>Voice Recognition</strong>: The assistant uses the SpeechRecognition library to recognize spoken commands.</li>
<li class="has-line-data" data-line-start="10" data-line-end="11"><strong>Text-to-Speech</strong>: It utilizes the pyttsx3 library to provide spoken responses in a customizable voice.</li>
<li class="has-line-data" data-line-start="11" data-line-end="13"><strong>Web and App Control</strong>: You can command the assistant to open specific websites or applications.<br>
<em>*by specific I mean those stored in the nameofsites python file</em></li>
<li class="has-line-data" data-line-start="13" data-line-end="15"><strong>Music &amp; Video Playback</strong>: You can instruct the assistant to play songs/videos from a predefined list.<br>
<em>*Audio/video files should be downloaded on the system. Then add the name and path of the file to be played to the list in namesofsites file.</em></li>
<li class="has-line-data" data-line-start="15" data-line-end="16"><strong>Time Display</strong>: Ask the assistant for the current time, and it will respond with the current time.</li>
<li class="has-line-data" data-line-start="16" data-line-end="18"><strong>AI-Powered Responses</strong>: By saying “using AI” followed by a prompt, the assistant can generate responses using OpenAI’s GPT-3 text generation model.</li>
</ul>
<h2 class="code-line" data-line-start=18 data-line-end=19 ><a id="Prerequisites_18"></a>Prerequisites</h2>
<h5 class="code-line" data-line-start=19 data-line-end=20 ><a id="Before_running_the_script_ensure_you_have_the_following_19"></a>Before running the script, ensure you have the following:</h5>
<ul>
<li class="has-line-data" data-line-start="21" data-line-end="22">Python 3 installed on your system.</li>
<li class="has-line-data" data-line-start="22" data-line-end="23">pyAudio should be installed. (install it from <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/">https://www.lfd.uci.edu/~gohlke/pythonlibs/</a>)</li>
<li class="has-line-data" data-line-start="23" data-line-end="24">Required Python libraries, including <strong>speech_recognition</strong>, <strong>pyttsx3</strong>, <strong>webbrowser</strong>, <strong>os</strong>, and <strong>openai</strong>.</li>
<li class="has-line-data" data-line-start="24" data-line-end="25">Access to an <strong>OpenAI API key</strong> for generating AI-powered responses.</li>
<li class="has-line-data" data-line-start="25" data-line-end="27">Though you need to pay for openAI’s responses as per the guidlines of the company.</li>
</ul>
<h2 class="code-line" data-line-start=27 data-line-end=28 ><a id="Usage_27"></a>Usage</h2>
<ol>
<li class="has-line-data" data-line-start="28" data-line-end="29">Run the python file using any compiler.</li>
<li class="has-line-data" data-line-start="29" data-line-end="30">The assistant will greet you and wait for your voice command.</li>
<li class="has-line-data" data-line-start="30" data-line-end="31">Speak your command clearly, and the assistant will process it accordingly.</li>
<li class="has-line-data" data-line-start="31" data-line-end="32">To exit the program, say “no” when asked if you want any other help.</li>
<li class="has-line-data" data-line-start="32" data-line-end="33">For now the number of commands is limited.</li>
<li class="has-line-data" data-line-start="33" data-line-end="39">some of the common commands are:
<ul>
<li class="has-line-data" data-line-start="34" data-line-end="35">“what’s the time now?”</li>
<li class="has-line-data" data-line-start="35" data-line-end="36">“tell me a joke”</li>
<li class="has-line-data" data-line-start="36" data-line-end="37">“open {file/app/website name}”</li>
<li class="has-line-data" data-line-start="37" data-line-end="38">“play {video/audio name}”</li>
<li class="has-line-data" data-line-start="38" data-line-end="39">“using AI, {prompt for openAI}”</li>
</ul>
</li>
<li class="has-line-data" data-line-start="39" data-line-end="40">“using AI, …” is the most flexible command as it returns the query from openAI servers.</li>
<li class="has-line-data" data-line-start="40" data-line-end="41">For any audio/video playing, take the another file, i.e., <em>namesofsites</em> and add the name and its address in the <em>“songs_or_videos”</em> list.</li>
<li class="has-line-data" data-line-start="41" data-line-end="42">For website/app opening, add the name of the website/app and its url/local address in the <em>“sites_or_apps”</em> list.</li>
<li class="has-line-data" data-line-start="42" data-line-end="49">If the <em>zira_id</em> doesn’t work for you or you want to change the voice, find the compatible voice ID’s in your pc using:<pre><code class="has-line-data" data-line-start="44" data-line-end="48" class="language-py">voices = pyttsx3.init().getProperty(<span class="hljs-string">'voices'</span>)
<span class="hljs-keyword">for</span> voice <span class="hljs-keyword">in</span> voices:
    print(f<span class="hljs-string">"Voice ID: {voice.id}, Name: {voice.name}"</span>)
</code></pre>
</li>
</ol>
<h2 class="code-line" data-line-start=49 data-line-end=50 ><a id="Customization_49"></a>Customization</h2>
<ul>
<li class="has-line-data" data-line-start="50" data-line-end="51">You can customize the voice accent used by modifying the <em>zira_id</em> variable.</li>
<li class="has-line-data" data-line-start="51" data-line-end="52">Careful with changing the voice ID; change as mentioned.</li>
<li class="has-line-data" data-line-start="52" data-line-end="54">Add or remove websites and songs in the <em>“sites_or_apps”</em> and <em>“songs_or_videos”</em> lists, respectively, to expand or modify the assistant’s capabilities.</li>
</ul>
<h2 class="code-line" data-line-start=54 data-line-end=55 ><a id="Note_54"></a>Note</h2>
<ul>
<li class="has-line-data" data-line-start="55" data-line-end="56">Be cautious with your OpenAI API key usage to avoid rate limit errors.</li>
<li class="has-line-data" data-line-start="56" data-line-end="58">Ensure that you have the necessary voices and language packs installed for text-to-speech functionality.</li>
</ul>
<h2 class="code-line" data-line-start=58 data-line-end=59 ><a id="Acknowledgments_58"></a>Acknowledgments</h2>
<ul>
<li class="has-line-data" data-line-start="59" data-line-end="60">The project uses the SpeechRecognition, pyttsx3, and OpenAI libraries.</li>
<li class="has-line-data" data-line-start="60" data-line-end="61">Voice responses are generated using OpenAI’s GPT-3.</li>
<li class="has-line-data" data-line-start="61" data-line-end="63">You can take the help of <a href="https://www.youtube.com/watch?v=s_8b5iq4Rvk&amp;t=2437s">CodeWithHarry’s Video</a> in the initial developement, thanks to him I was able to solve some queries!</li>
</ul>
<p class="has-line-data" data-line-start="63" data-line-end="64">Feel free to customize and expand upon this code to create your own voice-activated virtual assistant!</p>
