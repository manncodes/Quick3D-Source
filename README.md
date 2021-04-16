# Quick3D

## Installation
1. Clone this repository
    ```bash
    git clone https://github.com/manncodes/Quick3D-Source.git
    cd Quick3D-Source
    ```
    
2. Downloading Pretrained Models

    ```bash
    git clone https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch.git 
    cd lightweight-human-pose-estimation.pytorch 
    wget https://download.01.org/opencv/openvino_training_extensions/models/human_pose_estimation/checkpoint_iter_370000.pth
    cd ../src/scripts
    sh download_trained_model.sh
    ```

3. Reach out to me for the configuration files of firebase project if needed! ;)

4. Setup your own paths where needed.

5. Run Server

    ```bash
    python server.py
    ```
