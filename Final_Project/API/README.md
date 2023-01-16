<h1><center>FINAL PROJECT CS114.M11</center></h1>
<h2><center>Sign Traffic Detection</center></h2>

Chúng em sử dụng Flask để deploy model thành API.

## Môi trường team chạy thực nghiệm
    OS: ubuntu 20.04
    Python: 3.8

## Cách cài đặt và sử dụng

B1: Tải source code

    git clone https://github.com/lynguyenminh/CS114.M11.Vietnam-traffic-sign-detection.git
    cd CS114.M11.Vietnam-traffic-sign-detection.git/Final_Project/API

    # Tai file weights
    gdown --id 1pux_7RPKlZiqQhRILtU0e6GVxS_7iw_R

B2: Cài môi trường

    pip install -r requirements.txt --no-cache-dir

B3: Start API

    python app.py