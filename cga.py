
from flask import Flask, flash, request, redirect, url_for, render_template

import os
import shutil

from pypdf import PdfReader
from uploads import *

import google.generativeai as genai

genai.configure(api_key="AIzaSyAWbQt8Cas9sQehjforPTvMcaz0582DBFM")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

convo.send_message("you will summarize the text I will provide you will not output anything else. do not summerize until I say '**text done**' and at that point you will summerize the text")
print(convo.last.text)


app = Flask(__name__)
upload_folder = 'uploads'

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'pdf' in request.files:
            # Delete all previous uploads
            if os.path.exists(upload_folder):
                shutil.rmtree(upload_folder)
            os.makedirs(upload_folder)

            # Save the new file
            f = request.files['pdf']
            f.save(os.path.join(upload_folder, f.filename))
            pdf = os.listdir("./uploads")[0]
            reader = PdfReader(f'./uploads/{pdf}')
    for page in reader.pages:
        print(page.extract_text)
        convo.send_message(str(page.extract_text))
    convo.send_message("**text done**")
    return render_template('index.html', text=convo.last.text)

if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)