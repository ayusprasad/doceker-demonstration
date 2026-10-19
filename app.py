from __future__ import annotations

from flask import Flask, render_template_string, request

app = Flask(__name__)


PAGE = """
<!doctype html>
<html lang="en">
  <head><meta charset="utf-8"><title>Docker Greeting</title></head>
  <body>
    <main>
      <h1>Docker Greeting</h1>
      <form action="/greet" method="post">
        <label for="username">Your name</label>
        <input id="username" name="username" required maxlength="80">
        <button type="submit">Greet me</button>
      </form>
      {% if message %}<p role="status">{{ message }}</p>{% endif %}
    </main>
  </body>
</html>
"""


@app.get("/")
def index():
    return render_template_string(PAGE, message="")


@app.post("/greet")
def greet():
    username = request.form.get("username", "").strip()
    if not username:
        return render_template_string(PAGE, message="Please enter your name."), 400
    if len(username) > 80:
        return render_template_string(PAGE, message="Name must be 80 characters or fewer."), 400
    return render_template_string(PAGE, message=f"Hello {username}, welcome to the Docker demo!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
