<div align="center">
  <h1>🚀 Supercharge your <a href="https://lmstudio.ai/">LM Studio</a> with a Vector Database!  Now with Vision Models!</h1>
  <h3>Ask questions about your documents and get an answer from LM Studio!<br>(https://www.youtube.com/watch?v=KXYH8zqN8c8)</h3>
</div>
<div align="center">
  <h4>⚡GPU Acceleration for Database⚡</h4>
  <table>
    <thead>
      <tr>
        <th>GPU</th>
        <th>Windows</th>
        <th>Linux</th>
        <th>Requirements</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Nvidia</td>
        <td>✅</td>
        <td>✅</td>
        <td>CUDA 11.8</td>
      </tr>
      <tr>
        <td>AMD</td>
        <td>❌</td>
        <td>✅</td>
        <td>ROCm 5.6 (5.7 untested)</td>
      </tr>
      <tr>
        <td>Apple/Metal</td>
        <td colspan="3" align="center"> ✅ </td>
      </tr>
    </tbody>
  </table>
</div>

<div align="center"> <h2><u>REQUIREMENTS</h2></div>
You <b>MUST</b> install these before installing my program:<p>

1) 🐍[Python 3.10](https://www.python.org/downloads/release/python-31011/) or [Python 3.11](https://www.python.org/downloads/release/python-3117/) (PyTorch is NOT compatible with 3.12, at least as of 12/19/2023).
2) [Git](https://git-scm.com/downloads)
3) [Git Large File Storage](https://git-lfs.com/).
4) [Pandoc](https://github.com/jgm/pandoc).
5) [Microsoft Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) (🔥 Unconfirmed 🔥)
   > Some WINDOWS users have reported installation errors mentioning ```hnswlib```, ```numpy``` or other libraries.  If you encounter this, you can try installing Microsoft Build Tools at the link above.  This may or may not require [Visual Studio](https://visualstudio.microsoft.com/).  Moreover, when installing Build Tools you must check the box for "Desktop development with C++" extension.  If this still doesn't work, try installing again but additionally checking the four boxes on the right that state "SDK."

<details>
  <summary>EXAMPLE ON WINDOWS</summary>
<img src="https://github.com/BBC-Esq/ChromaDB-Plugin-for-LM-Studio/raw/main/build_tools.png">
</details>

<div align="center"> <h2>INSTALLATION</h2></div>

<details>
  <summary>🪟WINDOWS INSTRUCTIONS🪟</summary>
  
### Step 1
🟢 Nvidia GPU ➜ [Install CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)
> CUDA 12+ is currently NOT compatible since the faster-whisper library is only compatible up to CUDA 11.8, but it will hopefully be upgraded soon!<br>

🔴 AMD GPU - PyTorch currently pnly supports AMD gpu-acceleration on Linux, not Windows, and obly if ROCm is properly installed. There are several possible workarounds but I'm unable to verify since I don't have an AMD GPU nor use Linux.  You can look [HERE](https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html), [HERE](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview), [HERE](https://ubuntu.com/tutorials/enabling-gpu-acceleration-on-ubuntu-on-wsl2-with-the-nvidia-cuda-platform#1-overview), and possibly [HERE](https://user-images.githubusercontent.com/108230321/275660295-e2d6e097-38c5-4e38-9a1f-f28441ba8812.png).
### Step 2
Download the ZIP file from the latest "release" and extract the contents anywhere you want.  DO NOT simply clone this repository...there may be incremental changes to scripts that will be undone inbetween official releases.
### Step 3
Navigate to the ```src``` folder, open a command prompt, and create a virtual environment:
```
python -m venv .
```
### Step 4
Activate the virtual environment:
```
.\Scripts\activate
```
### Step 5
Run setup:
```
python setup.py
```

### Optional Step 6
Run this command if you want to doublecheck that you installed the Pytorch and gpu-acceleration software correctly:
```
python check_gpu.py
```
</details>

<details>
  <summary>🐧LINUX INSTRUCTIONS🐧</summary>

### Step 1
🟢 Nvidia GPUs ➜ Install [CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive)<br>
🔴 AMD GPUs ➜ Install [ROCm version 5.6](https://docs.amd.com/en/docs-5.6.0/deploy/windows/gui/index.html).
> [THIS REPO](https://github.com/nktice/AMD-AI) also has instructions.
> Also, although I'm unable to test on my system...[here are some "wheels"](https://github.com/jllllll/llama-cpp-python-cuBLAS-wheels/releases/tag/rocm) that I believe should work.  However, you'd have to search and find the right one for your system.

### Step 2
Download the ZIP file from the latest "release" and extract the contents anywhere you want.  DO NOT simply clone this repository...there may be incremental changes to scripts that will be undone inbetween official releases.
### Step 3
Navigate to the ```src``` folder, open a command prompt, and create a virtual environment:
```
python -m venv .
```
### Step 4
Activate the virtual environment:
```
source bin/activate
```
### Step 5
```
python -m pip install --upgrade pip
```
### Step 6
🟢 Nvidia GPU:
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
```
pip3 install -U xformers --index-url https://download.pytorch.org/whl/cu118
```
🔴 AMD GPU:
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.6
```
```
pip3 install -U xformers --index-url https://download.pytorch.org/whl/cu118
```
🔵 CPU only:
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```
### Step 7
```
sudo apt-get install portaudio19-dev
```
### Step 8
```
sudo apt-get install python3-dev
```
### Step 9
```
pip3 install -r requirements.txt
```
### Step 10
You must run:
```
python replace_pdf.py
```

### Step 11
```
sudo apt -y install libxcb-cursor0
```

### Optional Step 12
Run this script if you want to doublecheck wherher you installed the Pytorch and gpu-acceleration software correctly:
```
python check_gpu.py
```
</details>

<details>
  <summary>🍎APPLE INSTRUCTIONS🍎</summary>

### Step 1
All Macs with MacOS 12.3+ come with 🔘 MPS (aka "Metal"), which is basically a dedicated portion of Apple CPUs that act as a GPU and provide gpu-acceleration similiar to Nvidia/AMD.
### Step 2
Install [Xcode Command Line Tools](https://www.makeuseof.com/install-xcode-command-line-tools/).
### Step 3
Download the ZIP file from the latest "release" and extract the contents anywhere you want.  DO NOT simply clone this repository...there may be incremental changes to scripts that will be undone inbetween official releases.
### Step 4
Navigate to the ```src``` folder, open a command prompt, and create a virtual environment:
```
python -m venv .
```
### Step 5
Activate the virtual environment:
```
source bin/activate
```
### Step 6
```
python -m pip install --upgrade pip
```
### Step 7
```
pip3 install torch torchvision torchaudio
```
* If the above command fails for some reason or, when trying to create the vector database you get an error that mentions Pytorch and CUDA, you can try these commands instead:
```
pip uninstall torch torchvision torchaudio
```
The reinstall using this:
```
pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 -f https://download.pytorch.org/whl/cpu/torch_stable.html
```
### Step 8
```
brew install portaudio
```
* Homebrew can be installed with:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### Step 9
```
pip install -r requirements.txt
```
### Step 10
Upgrade PDF loader by running:
```
python replace_pdf.py
```
### Optional Step 11
Run this script if you want to doublecheck that you installed the Pytorch and gpu-acceleration software correctly:
```
python check_gpu.py
```
</details>

<div align="center"> <h2>USING THE PROGRAM</h2></div>
<details>
  <summary>🖥️INSTRUCTIONS🖥️</summary>

## Activate Virtual Environment
* You do not have to create a virtual environment except when first installing the program, but you must activate the virtual environment each time by opening a command prompt/terminal from within the ```src``` folder and running the appropriate command above for your platform.
## Start the Program
```
python gui.py
```
> Only systems with an Nvidia GPU will display gpu power, usage, and VRAM metrics.

# 🔥Important🔥
* Read the User Guide before sending me questions.

## Download Vector Model
* In the ```Vector Models``` tab, choose the embedding model you want to download.

## Set Vector Model
* In the ```Databases Tab```, choose the directory containing the vector model you want to use to create the database.  It can be any of the models you've already downloaded.
  > Do not choose the ```Embedding_Models``` folder itself.

## Set Chunk Size and Overlap
* Making sure to read the User Manual, set the chunk size and chunk overlap.  Remember, anytime you want to change these two settings or add/remove documents, you must re-create the database for the chages to take effect.

## Add Files to be Vectorized
* Click the ```Choose Documents or Images``` button to add files.
  * * Supported non-image extensions are: ```.pdf```, ```.docx```, ```.epub```, ```.txt```, ```.html```, ```.enex```, ```.eml```, ```.msg```, ```.csv```, ```.xls```, ```.xlsx```, ```.rtf```, ```.odt```.
  * * Supported image extensions are: ```.png```, ```.jpg```, ```.jpeg```, ```.bmp```, ```.gif```, ```.tif```, ```.tiff```
* In the ```Tools Tab```, you can also transcribe one or more audio files into ```.txt``` files to be put into the vector databse.
    > Also, in the Tools Tab, don't forget to test the vision model you want to use before processing a large number of images.

## Removing Files
* In the ```Databases Tab```, select one or more files, right click, and delete.  Re-create the database.

## Creating the Databaase
* Click the ```Create Vector Database``` button.  Wait until the command prompt says "persisted" before proceeding to the next step.

## Connecting to LM Studio
* Start LM Studio and load a model.

## Choosing a Prompt Format
The LLM within LM Studio works best with an appropriate "prompt format."  In the ```Settings Tab``` in my program, choose the prompt format from the pulldown menu or enter one manually.  In order for prompt formatting to work, however, you must disable the "automatic prompt formatting" setting in the "Server" portion of LM Studio.
  > You do not need to do this if you're using ```LM Studio v0.2.9``` or earlier.
Morever, there is a bug specific to ```LM Studio v0.2.10``` preventing LM Studio from respecting the prompt format you choose.  However, you can fix this by going to the Server settings (far right side) and:
* ⚠️ Delete any/all text within the ```User Message Prefix``` box; and
* ⚠️ Delete any/all text within the ```User Message Suffix``` box.

## Start the LM Studio Server
* In the Server tab,  click ```Start Server.```

## Search Database
* Type (or speak) your question and click ```Submit Questions.```

## Test Chunks
* If you wish to test the quality of the chunk settings, check the ```Chunks Only``` checkbox.  This means the program will not connect to LM Studio and will instead simply provide you with the chunks retrieved from the vector database.

## Text to Voice
* This program uses "Bark" models to convert the response from LM Studio into audio.  You must wait until the ENTIRE response is received, however, before clicking the ```Bark Response``` button.

## Voice to Text
* Both the voice recorder and audio file transcriber use the ```faster-whisper``` library, and GPU acceleration is as follows:

  > Note, ```faster-whisper``` only supports CUDA 11.8 currently, but CUDA 12+ support is coming in the near future.

<div align="center">
  <h4>⚡Acceleration for Transcription⚡</h4>
  <table>
    <tbody>
      <tr>
        <td>Intel CPU</td>
        <td>✅</td>
        <td></td>
      </tr>
      <tr>
        <td>AMD CPU</td>
        <td>✅</td>
        <td></td>
      </tr>
      <tr>
        <td>Nvidia GPU</td>
        <td>✅</td>
        <td>Requires CUDA 11.8 (not 12.1)</td>
      </tr>
      <tr>
        <td>AMD GPU</td>
        <td>❌</td>
        <td>Will default to CPU</td>
      </tr>
      <tr>
        <td>Apple CPU</td>
        <td>✅</td>
        <td></td>
      </tr>
      <tr>
        <td>Apple Metal/MPS</td>
        <td>❌</td>
        <td>Will default to CPU</td>
      </tr>
    </tbody>
  </table>
</div>

</details>

## NEW and Exciting Vision Models
As of release 3.0 the program includes Vision Models that will generate summaries of what each picture depicts, which are then added to the vector database.

<div align="center"><h2>CONTACT</h2></div>

All suggestions (positive and negative) are welcome.  "bbc@chintellalaw.com" or feel free to message me on the [LM Studio Discord Server](https://discord.gg/aPQfnNkxGC).

<div align="center">
  <img src="https://github.com/BBC-Esq/ChromaDB-Plugin-for-LM-Studio/raw/main/example.png" alt="Example Image">
</div>
