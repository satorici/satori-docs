import datetime
import os

url = "https://docs.satori.ci/#"
file_path = "./sitemap.xml"
exclude_files = ["coverpage", "navbar", "README", "_sidebar"]


def create_sitemap() -> None:
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for path, dirs, files in os.walk("./satori_help/docs"):
        for file in files:
            if not file.endswith(".md"):
                continue
            try:
                if not path.endswith("/"):
                    path += "/"
                new_path = (path.replace("\\", "/") + file)[2:-3]
                new_path = new_path.replace("satori_help/docs/", "")
                if new_path in exclude_files:
                    continue
                print(new_path)
                xml += "  <url>\n"
                xml += f"    <loc>{url}/{new_path}</loc>\n"
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

    with open(file_path, "w", encoding="utf-8") as sitemap:
        sitemap.write(xml)


if __name__ == "__main__":
    create_sitemap()
