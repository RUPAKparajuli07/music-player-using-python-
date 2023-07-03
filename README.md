<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">

</head>
<body>
  <h1>Music Player</h1>

  <h2>Overview</h2>
  <p>
    This is a simple music player application implemented in Python using the Tkinter and Pygame libraries.
    It allows you to play and control the playback of MP3 music files.
  </p>

  <h2>Features</h2>
  <ul>
    <li>Load and play MP3 music files from a specified directory or manually select a file.</li>
    <li>Control the playback with buttons for previous, play/pause, and next track.</li>
    <li>Display the current track name, duration, and current playing time.</li>
    <li>Automatically update the current playing time every second.</li>
  </ul>

  <h2>Prerequisites</h2>
  <ul>
    <li>Python 3.x installed on your system.</li>
    <li>The following Python libraries need to be installed:</li>
  </ul>
  <pre><code>pip install tkinter pygame mutagen</code></pre>

  <h2>Installation</h2>
  <ol>
    <li>Clone the repository or download the source code files.</li>
    <pre><code>git clone https://github.com/RUPAKparajuli07/music-player-using-python-</code></pre>
    <li>Make sure you have the required libraries installed.</li>
    <pre><code>pip install pygame </code></pre>
    <pre><code>pip install mutagen</code></pre>
    <pre><code>pip install tkinter </code></pre>
  </ol>

  <h2>Usage</h2>
  <ol>
    <li>Open a terminal or command prompt and navigate to the project directory.</li>
    <pre><code>cd path/to/project</code></pre>
    <li>Run the <code>music_player.py</code> file.</li>
    <pre><code>python music_player.py</code></pre>
    <li>The music player window will appear.</li>
    <li>The music player will automatically load MP3 files from the default directory specified in the code (<code>C:/Users/paraj/Music</code>). You can change this directory by modifying the <code>directory</code> variable in the <code>load_tracks()</code> method.</li>
    <li>The current track, duration, and time labels will display the initial values.</li>
    <li>Use the following buttons to control the playback:
      <ul>
        <li><strong>Previous</strong>: Plays the previous track in the track list.</li>
        <li><strong>Play</strong>: Plays or pauses the current track.</li>
        <li><strong>Next</strong>: Plays the next track in the track list.</li>
      </ul>
    </li>
    <li>You can also manually select an MP3 file to play by clicking the <strong>Play</strong> button and selecting a file from the file dialog.</li>
    <li>The current track, duration, and time labels will update accordingly.</li>
    <li>To exit the music player, close the window or press <code>Ctrl + C</code> in the terminal or command prompt.</li>
  </ol>

  <h2>Customization</h2>
  <p>
    You can customize the music player by modifying the code as per your requirements. Here are a few suggestions:
  </p>
  <ul>
    <li>Change the appearance of the UI components by modifying the attributes of the tkinter widgets (e.g., font, color, background).</li>
    <li>Add more buttons or controls to enhance the functionality (e.g., volume control).</li>
    <li>Implement a playlist feature to manage multiple tracks.</li>
    <li>Improve the user interface with additional information or visual elements.</li>
  </ul>
  <p>
    Feel free to experiment and make changes to suit your needs.
  </p>

  <h2>License</h2>
  <p>
    This project is licensed under the <a href="LICENSE">MIT License</a>.
  </p>
</body>
</html>
