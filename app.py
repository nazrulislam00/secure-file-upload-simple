from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            return "No file uploaded"

        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return "File uploaded successfully"

    return """
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
