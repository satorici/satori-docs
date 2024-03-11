import datetime
import os

URL = "https://docs.satori.ci/#"
EXCLUDE_FILES = ["coverpage", "navbar", "README", "_sidebar"]
OUTPUT_FOLDER = "./satori_help/docs"
FILE_PATH = OUTPUT_FOLDER + "/sitemap.xml"

def create_sitemap() -> None:
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for path, dirs, files in os.walk(OUTPUT_FOLDER):
        for file in files:
            if not file.endswith(".md"):
                continue
            try:
                if not path.endswith("/"):
                    path += "/"
                new_path = (path.replace("\\", "/") + file)[2:-3]
                new_path = new_path.replace("satori_help/docs/", "")
                if new_path in EXCLUDE_FILES:
                    continue
                print(new_path)
                xml += "  <url>\n"
                xml += f"    <loc>{URL}/{new_path}</loc>\n"
                lastmod = datetime.datetime.utcfromtimestamp(
                    os.path.getmtime(path + file)
                ).strftime("%Y-%m-%d")
                xml += f"    <lastmod>{lastmod}</lastmod>\n"
                xml += "    <changefreq>monthly</changefreq>\n"
                xml += "    <priority>0.5</priority>\n"
                xml += "  </url>\n"
            except Exception as e:
                print(path, file, e)
                break
    xml += "</urlset>\n"

    with open(FILE_PATH, "w", encoding="utf-8") as sitemap:
        sitemap.write(xml)


if __name__ == "__main__":
    create_sitemap()
