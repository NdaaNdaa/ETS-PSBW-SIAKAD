
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = "kunci-siakad-untuk-prototipe"

mahasiswa_list = [
    {
        "nim": "240001",
        "nama": "Yudi Knalpot",
        "prodi": "Sistem Teknologi dan Informasi",
        "semester": 3
    },
    {
        "nim": "240002",
        "nama": "Dimas Ukin",
        "prodi": "Sistem Teknologi dan Informasi",
        "semester": 3
    },
    {
        "nim": "240003",
        "nama": "Bayu Stop Kontak",
        "prodi": "Sistem Teknologi dan Informasi",
        "semester": 3
    }
]

@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/mahasiswa")
def mahasiswa():
    return render_template(
        "mahasiswa.html",
        mahasiswa_list=mahasiswa_list
    )


@app.route("/mahasiswa/tambah", methods=["GET", "POST"])
def tambah_mahasiswa():
    if request.method == "POST":
        nim = request.form.get("nim", "").strip()
        nama = request.form.get("nama", "").strip()
        prodi = request.form.get("prodi", "").strip()
        semester = request.form.get("semester", "")

        if not nim or not nama or not prodi or not semester:
            flash("Semua kolom wajib diisi.", "danger")
            return redirect(url_for("tambah_mahasiswa"))

        if any(m["nim"] == nim for m in mahasiswa_list):
            flash("NIM tersebut sudah terdaftar.", "danger")
            return redirect(url_for("tambah_mahasiswa"))

        mahasiswa_list.append({
            "nim": nim,
            "nama": nama,
            "prodi": prodi,
            "semester": int(semester)
        })

        flash("Mahasiswa berhasil ditambahkan!", "success")
        return redirect(url_for("mahasiswa"))

    return render_template(
        "simple_page.html",
        page_title="Tambah Mahasiswa",
        page_description="Formulir penambahan data mahasiswa."
    )


@app.route("/matakuliah")
def matakuliah():
    return render_template(
        "simple_page.html",
        page_title="Mata Kuliah",
        page_description="Halaman informasi dan daftar mata kuliah."
    )


@app.route("/profil")
def profil():
    return render_template(
        "simple_page.html",
        page_title="Profil",
        page_description="Informasi profil pengguna SIAKAD."
    )


@app.route("/bantuan")
def bantuan():
    return render_template(
        "simple_page.html",
        page_title="Bantuan",
        page_description="Panduan penggunaan Sistem Informasi Akademik."
    )


if __name__ == "__main__":
    app.run(debug=True)
