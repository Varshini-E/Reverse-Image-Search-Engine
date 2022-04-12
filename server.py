import numpy as np
from PIL import Image
import import_ipynb
from feature_extractor import FeatureExtractorResnet
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path
import csv

app = Flask(__name__)

fe = FeatureExtractorResnet()
features = []
img_paths = []
img_id = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
    img_id.append(feature_path.stem)
features = np.array(features)


from sklearn.neighbors import NearestNeighbors
knn = NearestNeighbors(metric="euclidean",algorithm="ball_tree")
knn.fit(features)
N=5


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img']
        N = request.form.get('number_images',None)
        print(N)
        N = int(N)
        # Save query image
        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)

        # Run search
        feature = fe.extract(img)
        query = np.array(feature).flatten().reshape(1,-1)
        res = knn.kneighbors(query,return_distance=True,n_neighbors=N) 
        scores = []
        links = []
        imagename = []
        for i in range(len(res[0][0])):
            scores.append([res[0][0][i],img_paths[res[1][0][i]]])
            imagename.append(img_id[res[1][0][i]])
            print(uploaded_img_path)
        for i in range(N):
            with open("amazon_data.csv") as f:
                reader = csv.reader(f)
                query = imagename[i]
                print(scores[i][1])
                for row in reader:                    
                    if(row[1]==query):
                        links.append(row[3])
                        print(row[0])
                        print(row[3])
                        break
        print(links)
        results = []
        for i in range (len(scores)):
            results.append([scores[i][0],scores[i][1],links[i]])
        return render_template('index.html',
                               query_path=uploaded_img_path,
                               results= results)
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run("0.0.0.0")