import markdown

with open("Business Change.md", 'r', encoding='UTF-8') as md_file:
	file=md_file.read()

content=markdown.markdown(file)
print(content)


# ============= To edit a file ============================
# with open("some_file.md", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
#     output_file.write(html)