from flask import Flask, request, jsonify
import swisseph as swe

app = Flask(__name__)

# trỏ đến thư mục ephemeris (chứa sepl_18.se1)
swe.set_ephe_path("./ephe")

@app.route("/chart", methods=["GET"])
def chart():
    # Lấy tham số từ URL
    year = int(request.args.get("year"))
    month = int(request.args.get("month"))
    day = int(request.args.get("day"))
    hour = float(request.args.get("hour", 0))  # giờ có thể kèm phút, ví dụ 14.5 = 14:30

    jd = swe.julday(year, month, day, hour)

    planets = {
        "Sun": swe.SUN,
        "Moon": swe.MOON,
        "Mercury": swe.MERCURY,
        "Venus": swe.VENUS,
        "Mars": swe.MARS,
        "Jupiter": swe.JUPITER,
        "Saturn": swe.SATURN,
        "Uranus": swe.URANUS,
        "Neptune": swe.NEPTUNE,
        "Pluto": swe.PLUTO,
    }

    results = {}
    for name, code in planets.items():
        pos, _ = swe.calc_ut(jd, code)
        results[name] = pos[0]  # chỉ lấy kinh độ (0–360°)

    return jsonify(results)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

