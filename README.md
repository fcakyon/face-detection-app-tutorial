# Flask Face Detection

<a href="https://github.com/fcakyon/face-detection-app-tutorial/actions/workflows/ci.yml"><img src="https://github.com/fcakyon/face-detection-app-tutorial/actions/workflows/ci.yml/badge.svg" alt="CI Tests"></a>

A face detection web app powered by SSD face detector using Flask, OpenCV, Heroku 

Live demo: https://face-detection-api-flask.herokuapp.com/

[Tutorial notebook](/tutorial/tutorial.ipynb) | [Tutorial presentation](/presentation/FaceDetectionWebAppTutorial.pdf)

![DemoScreen](/images/webappscreen.jpg)

# App Usage
Run face detection app:

```console
git clone https://github.com/fcakyon/face-detection-app-tutorial.git
cd face-detection-app-tutorial
python app.py
```

(Adjust detection threshold in [config.py](config.py) if needed)

# Deploy
One-click deploy build on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)